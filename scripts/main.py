from data_preprocessing import main as preprocess_data
from arima import main as arima
from facebook_prophet import main as facebook_prophet
from config import RAW_FILES, OUTPUT_DIR, ARIMA_ORDER, MERGED_DATA_FILE, PROPHET_REGRESSORS


if __name__ == "__main__":
    print("Starting life expectancy forecasting...")
    preprocess_data()  
    arima()
    facebook_prophet()
    print("Finished forecasting. Check the 'outputs' folder for results from ARIMA and Facebook Prophet.")