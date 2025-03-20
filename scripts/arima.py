import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error
import os
from config import RAW_FILES, OUTPUT_DIR, ARIMA_ORDER


def pull_data():
    '''load and preprocess the life expectancy dataset'''
    df = pd.read_csv(RAW_FILES["life_expectancy"])
    df = df[df['Code'] == 'USA'].reset_index(drop=True)
    df = df.iloc[2:].reset_index(drop=True)  # drop first two rows (1880, 1890)
    df.rename(columns={"Period life expectancy at birth - Sex: total - Age: 0": "Life Expectancy"}, inplace=True)
    df.drop(columns=["Entity", "Code"], inplace=True)
    return df


def train_arima(train_data):
    '''train the ARIMA model'''
    model = ARIMA(train_data["Life Expectancy"], order=ARIMA_ORDER)
    return model.fit()


def generate_forecast(model, test_years):
    '''generate forecasts for the test period'''
    forecast = model.forecast(steps=len(test_years))
    return pd.Series(forecast.values, index=test_years)


def evaluate_model(test_life, forecast):
    '''calculate and return Mean Absolute Error (MAE)'''
    return mean_absolute_error(test_life, forecast)


def plot_results(train, test, forecast):
    '''plot and save actual vs. predicted life expectancy'''
    plt.figure(figsize=(12, 6))
    plt.plot(train['Year'], train['Life Expectancy'], label='Train', color='blue')
    plt.plot(test['Year'], test['Life Expectancy'], label='Actual', color='green')
    plt.plot(forecast.index, forecast.values, label='Predicted', linestyle='dashed', color='orange')
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.title('Actual vs. Predicted Life Expectancy')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(OUTPUT_DIR, "arima_forecast_overview.png"))
    plt.close()

    plt.figure(figsize=(12, 6))
    plt.plot(test['Year'], test["Life Expectancy"], label='Actual', marker='o', linestyle='-', color='green')
    plt.plot(forecast.index, forecast.values, label='Predicted',  marker='o', linestyle='--', color='orange')
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.title('Actual vs. Predicted Life Expectancy')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(OUTPUT_DIR, "arima_forecast.png"))
    plt.close()


def save_results(test, forecast):
    '''save forecast results to a CSV file'''
    results_table = pd.DataFrame({
        'Year': forecast.index,
        'Predicted Life Expectancy': forecast.values,
        'Actual Life Expectancy': test.loc[test['Year'].isin(forecast.index), "Life Expectancy"].values,
        'Difference': forecast.values - test.loc[test['Year'].isin(forecast.index), "Life Expectancy"].values
    })
    results_table.to_csv(os.path.join(OUTPUT_DIR, "arima_predictions.csv"), index=False)
    print("ARIMA predictions saved to outputs/arima_predictions.csv")


def main():
    df = pull_data()
    train = df[df['Year'] <= 1999]
    test = df[df['Year'] >= 2000]
    
    best_model_fit = train_arima(train)
    forecast = generate_forecast(best_model_fit, test['Year'].values)
    
    mae = evaluate_model(test['Life Expectancy'].iloc[:len(forecast)], forecast)
    print(f"ARIMA Mean Absolute Error (MAE): {mae:.4f}")
        
    save_results(test, forecast)
    plot_results(train, test, forecast)


if __name__ == "__main__":
    main()
