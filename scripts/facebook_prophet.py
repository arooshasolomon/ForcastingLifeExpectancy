import pandas as pd
import os
from prophet import Prophet
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
from config import MERGED_DATA_FILE, PROPHET_REGRESSORS, OUTPUT_DIR

# load and prepare data
df = pd.read_csv(MERGED_DATA_FILE)
df.rename(columns={"Year": "ds", "Life expectancy": "y"}, inplace=True)
df["ds"] = pd.to_datetime(df["ds"], format="%Y")

# train-test split
train_df = df[df["ds"].dt.year <= 2016]
test_df = df[df["ds"].dt.year >= 2017]

# train and evaluate fb prophet models
predictions = {}

for reg in PROPHET_REGRESSORS:
    model = Prophet()
    model.add_regressor(reg)
    model.fit(train_df[["ds", "y", reg]])

    # forecast
    future = test_df[["ds", reg]]
    forecast = model.predict(future)

    # store results
    results = forecast[["ds", "yhat"]].merge(test_df[["ds", "y"]], on="ds")
    results["Diff"] = results["yhat"] - results["y"]
    predictions[reg] = results
    
    # save results to CSV
    results.to_csv(os.path.join(OUTPUT_DIR, f"prophet_results_{reg}.csv"), index=False)
    
    mae = mean_absolute_error(results["y"], results["yhat"])
    print(f"MAE ({reg}): {mae:.2f}")

    # plot
    plt.figure(figsize=(12, 6))
    plt.plot(test_df["ds"], test_df["y"], label="Actual", marker="o", linestyle="-")

    for reg, pred in predictions.items():
        plt.plot(pred["ds"], pred["yhat"], marker="o", linestyle="--", label=f"Predicted ({reg})")

plt.xlabel("Year")
plt.ylabel("Life Expectancy")
plt.legend()
plt.title("Facebook Prophet - Life Expectancy Prediction vs Actual")
plt.savefig(os.path.join(OUTPUT_DIR, "prophet_predictions.png"))
plt.show()