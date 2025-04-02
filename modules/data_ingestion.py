# modules/data_ingestion.py

import pandas as pd

def load_and_clean_data(filepath):
    """
    Loads data from a CSV file and performs cleaning operations.

    Parameters:
        filepath (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The cleaned data.
    """
    try:
        # Load data
        data = pd.read_csv(filepath)
        print("Data loaded successfully from {}.".format(filepath))
        
        # Clean data
        initial_shape = data.shape
        data.dropna(inplace=True)
        final_shape = data.shape
        print("Dropped {} rows with missing values.".format(initial_shape[0] - final_shape[0]))
        
        # Additional cleaning steps (if any)
        # For example, convert categorical variables to numerical
        data['defaulted'] = data['defaulted'].map({'No': 0, 'Yes': 1})
        
        return data
    except Exception as e:
        print("An error occurred during data ingestion: {}".format(e))
        return None

