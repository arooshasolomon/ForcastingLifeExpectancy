import os

# define directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "../data")
OUTPUT_DIR = os.path.join(BASE_DIR, "../outputs")

# ensure directories exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# file paths
RAW_FILES = {
    "caloric_supply": os.path.join(DATA_DIR, "daily-per-capita-caloric-supply.csv"),
    "gdp_per_capita": os.path.join(DATA_DIR, "gdp-per-capita-worldbank.csv"),
    "healthcare_expenditure": os.path.join(DATA_DIR, "total-healthcare-expenditure-gdp.csv"),
    "life_expectancy": os.path.join(DATA_DIR, "life-expectancy.csv"),
}

MERGED_DATA_FILE = os.path.join(DATA_DIR, "merged_data.csv")

# ARIMA model parameters (see arima_tuning.ipynb)
ARIMA_ORDER = (3, 2, 3)

# prophet configuration
PROPHET_REGRESSORS = ["Daily calorie supply", "GDP per capita", "Health expenditure as percentage of GDP"]

# train/test split (for facebook prophet models)
TRAIN_START_YEAR = 2000
TRAIN_END_YEAR = 2016
TEST_START_YEAR = 2017
TEST_END_YEAR = 2021
