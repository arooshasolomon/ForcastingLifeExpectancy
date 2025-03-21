# Life Expectancy Forecasting

## Overview

This repository contains a time series forecasting project focused on predicting life expectancy trends based on various economic and healthcare-related factors. It includes ARIMA as a baseline model, where ARIMA is used to predict life expectancy based on past life expectancy data. Additionally, the project employs Facebook Prophet models that incorporate external regressors alongside past life expectancy data to predict future trends.

## Contents of this Repository

life_expectancy_forecasting/
│── data/
│   ├── life_expectancy.csv
│   ├── gdp_per_capita.csv
│   ├── healthcare_spending.csv
│   ├── calories_supply.csv
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
- Project root ('/'):
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

## Acknowledgments

This project uses life expectancy data from Our World in Data and economic indicators to improve the forecasting of future trends.