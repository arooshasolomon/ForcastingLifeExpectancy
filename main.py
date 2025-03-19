'''
TO-DO:
- a script to run the full pipeline from start to finish (load data, preprocess, trains models, evaluates results)
'''

from scripts.data_preprocessing import main as preprocess_data

if __name__ == "__main__":
    preprocess_data()  
    # placeholder for calling modeling scripts
