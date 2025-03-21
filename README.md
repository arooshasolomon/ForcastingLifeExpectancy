# Life Expectancy Forecasting

## Overview

This repository contains a time series forecasting project focused on predicting life expectancy trends based on various economic and healthcare-related factors. It includes ARIMA as a baseline model, where ARIMA is used to predict life expectancy based on past life expectancy data. Additionally, the project employs Facebook Prophet models that incorporate external regressors alongside past life expectancy data to predict future trends.

## Contents of this Repository

life_expectancy_forecasting/  
│── data/  
│   ├── life_expectancy.csv [[1]](#1)  
│   ├── gdp_per_capita.csv [[2]](#2)  
│   ├── healthcare_spending.csv [[3]](#3)  
│   ├── calories_supply.csv [[4]](#4)  
│   ├── merged_data.csv  
│  
│── scripts/  
│   ├── arima.py  
│   ├── config.py  
│   ├── data_preprocessing.py  
│   ├── facebook_prophet.py  
│   ├── main.py  
│   ├── notebooks/  
│   │   ├── EDA.ipynb  
│   │   ├── arima_tuning.ipynb  
│   │   ├── facebook_prophet.ipynb  
│   │   ├── data_appendix_scripts.ipynb
│  
│── requirements.txt  
│── README.md  
│── LICENSE  

## Software and Platform

- Programming language: Python
- Software: Jupyter Notebook (for exploratory analysis), Python scripts
- Platforms: Works on Windows, MacOS, and Linux
- Required Python libraries:
    - pandas
    - matplotlib
    - statsmodels
    - scikit-learn
    - prophet
- To install all required dependencies, run: `pip install -r requirements.txt`

## Map of Documentation

- Data folder (`data/`): contains the raw and processed datasets used for analysis
- Scripts folder (`scripts/`):
    - `arima.py`: implements ARIMA model for forecasting life expectancy
    - `facebook_prophet.py`: uses Facebook Prophet for forecasting
    - `data_preprocessing.py`: cleans and merges datasets
    - `config.py`: stores file paths and model parameters
    - `main.py`: runs the full pipeline from data preprocessing to model training
    - `notebooks/`: contains Jupyter notebooks for exploratory data analysis and model tuning
- Project root (`/`):
    - `requirements.txt`: lists dependencies for easy setup
    - `README.md`: provides project overview and instructions
    - `LICENSE`: license information

## Instructions for Reproducing Results

1. Clone the Repository

2. Install Dependencies

    `pip install -r requirements.txt`

3. Run the Pipeline

    Execute the main script to run data preprocessing, ARIMA forecasting, and Facebook Prophet forecasting

    `python scripts/main.py`

4. Check Outputs

    Forecasting results (graphs and tables) will be stored in the `outputs/` folder

## References

The data used in this project are sourced from Our World in Data.

<a id="1">[1]</a> UN WPP (2024); HMD (2024); Zijdeman et al. (2015); Riley (2005) – with minor processing by Our World in Data. “Life expectancy at birth – Various sources – period tables” [dataset]. Human Mortality Database, “Human Mortality Database”; United Nations, “World Population Prospects”; Zijdeman et al., “Life Expectancy at birth 2”; James C. Riley, “Estimates of Regional and Global Life Expectancy, 1800-2001” [original data]. Retrieved March 4, 2025 from https://ourworldindata.org/grapher/life-expectancy.

<a id="2">[2]</a> Data compiled from multiple sources by World Bank (2025) – with minor processing by Our World in Data. “GDP per capita – World Bank – In constant international-$” [dataset]. Data compiled from multiple sources by World Bank, “World Development Indicators” [original data]. Retrieved March 4, 2025 from https://ourworldindata.org/grapher/gdp-per-capita-worldbank.

<a id="3">[3]</a> World Health Organization - Global Health Observatory (2024) – processed by Our World in Data. “Total healthcare expenditure as a share of GDP” [dataset]. World Health Organization, “Global Health Observatory” [original data]. Retrieved March 4, 2025 from https://ourworldindata.org/grapher/total-healthcare-expenditure-gdp.

<a id="4">[4]</a> Food and Agriculture Organization of the United Nations (2023); Harris et al. (2015); Floud et al. (2011); Jonsson (1998); Grigg (1995); Fogel (2004); Food and Agriculture Organization of the United Nations (2000); Food and Agriculture Organization of the United Nations (1949); USDA Economic Research Service (ERS) (2015) – with major processing by Our World in Data. “Daily supply of calories per person” [dataset]. Food and Agriculture Organization of the United Nations, “Food Balances: Food Balances (-2013, old methodology and population)”; Food and Agriculture Organization of the United Nations, “Food Balances: Food Balances (2010-)”; Harris et al., “How Many Calories? Food Availability in England and Wales in the Eighteenth and Nineteenth Centuries”; Floud et al., “The Changing Body”; Jonsson, “Changes in food consumption in Iceland, 1770-1940”; Grigg, “The nutritional transition in Western Europe”; Fogel, “The Escape from Hunger and Premature Death”; Food and Agriculture Organization of the United Nations, “The State of Food and Agriculture 2000”; Food and Agriculture Organization of the United Nations, “The State of Food and Agriculture 1949”; USDA Economic Research Service (ERS), “U.S. food supply:  Nutrients and other food components, per capita per day” [original data]. Retrieved March 4, 2025 from https://ourworldindata.org/grapher/daily-per-capita-caloric-supply.