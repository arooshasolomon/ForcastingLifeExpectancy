import pandas as pd
import os


# define file paths
DATA_DIR = "data"
OUTPUT_FILE = os.path.join(DATA_DIR, "merged_data.csv")


# load raw CSV files
caloric_supply = pd.read_csv(os.path.join(DATA_DIR, 'daily-per-capita-caloric-supply.csv'))
gdp_per_capita = pd.read_csv(os.path.join(DATA_DIR, 'gdp-per-capita-worldbank.csv'))
healthcare_expenditure = pd.read_csv(os.path.join(DATA_DIR, 'total-healthcare-expenditure-gdp.csv'))
life_expectancy = pd.read_csv(os.path.join(DATA_DIR, 'life-expectancy.csv'))


# helper function to filter for United States data only
def filter_us_data(df):
    return df[df["Entity"] == "United States"]

caloric_supply = filter_us_data(caloric_supply)
gdp_per_capita = filter_us_data(gdp_per_capita)
healthcare_expenditure = filter_us_data(healthcare_expenditure)
life_expectancy = filter_us_data(life_expectancy)


# helper function to drop unnecessary columns
def drop_columns(df):
    return df.drop(columns=["Entity", "Code"])

caloric_supply = drop_columns(caloric_supply)
gdp_per_capita = drop_columns(gdp_per_capita)
healthcare_expenditure = drop_columns(healthcare_expenditure)
life_expectancy = drop_columns(life_expectancy)


# merge the dataframes on 'Year'
merged_df = caloric_supply.merge(gdp_per_capita, on="Year", how="inner")
merged_df = merged_df.merge(healthcare_expenditure, on="Year", how="inner")
merged_df = merged_df.merge(life_expectancy, on="Year", how="inner")


# clean up columns names
merged_df.rename(columns={"Daily calorie supply per person": "Daily calorie supply",
                          "GDP per capita, PPP (constant 2021 international $)":"GDP per capita",
                          "Current health expenditure (CHE) as percentage of gross domestic product (GDP) (%)":"Health expenditure as percentage of GDP",
                          "Period life expectancy at birth - Sex: total - Age: 0":"Life expectancy"}, 
                          inplace=True)


# save the processed dataset to a CSV file in the data folder
os.makedirs(DATA_DIR, exist_ok=True)
merged_df.to_csv(OUTPUT_FILE, index=False)

print("Processed data saved to data folder.")
