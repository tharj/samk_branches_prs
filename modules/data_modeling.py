# modules/data_modeling.py

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd

def model_data(data):
    """
    Trains a logistic regression model and evaluates its performance.

    Parameters:
        data (pd.DataFrame): The data to model.

    Returns:
        dict: A dictionary containing model metrics and results.
    """
    try:
        print("Preparing data for modeling...")
        # Features and target variable
        X = data[['age', 'income', 'credit_score']]
        y = data['defaulted']
        
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42)
        
        print("Training logistic regression model...")
        # Initialize and train the model
        model = LogisticRegression()
        model.fit(X_train, y_train)
        
        # Make predictions
        y_pred = model.predict(X_test)
        
        # Evaluate the model
        print("Evaluating model performance...")
        report = classification_report(y_test, y_pred, output_dict=True)
        confusion = confusion_matrix(y_test, y_pred)
        
        # Compile results
        model_results = {
            'classification_report': report,
            'confusion_matrix': confusion.tolist()
        }
        
        return model_results
    except Exception as e:
        print("An error occurred during data modeling: {}".format(e))
        return {}

