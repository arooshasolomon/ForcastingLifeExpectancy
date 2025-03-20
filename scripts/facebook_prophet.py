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
    predictions[reg] = results
    mae = mean_absolute_error(results["y"], results["yhat"])
    print(f"MAE ({reg}): {mae:.2f}")

    # plot
    plt.plot(results["ds"], results["y"], label="Actual")
    plt.plot(results["ds"], results["yhat"], linestyle="dashed", label=f"Predicted ({reg})")

plt.legend()
plt.title("Facebook Prophet - Life Expectancy Prediction")
plt.savefig(os.path.join(OUTPUT_DIR, "prophet_predictions.png"))
plt.show()
