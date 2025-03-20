'''
TO-DO:
- a script to run the full pipeline from start to finish (load data, preprocess, trains models, evaluates results)
'''

from scripts.data_preprocessing import main as preprocess_data
from scripts.arima import main as arima
from scripts.facebook_prophet import main as facebook_prophet

if __name__ == "__main__":
    preprocess_data()  
    arima()
    facebook_prophet()
