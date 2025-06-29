import pytest
import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from ml.data import process_data
from ml.model import train_model, inference, compute_model_metrics
# TODO: add necessary import

project_path = os.getcwd()
data_path = os.path.join(project_path, "data", "census.csv")
data = pd.read_csv(data_path)

cat_features = [
    "workclass",
    "education",
    "marital_status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native_country",
]

train, test = train_test_split(data, test_size=0.2, random_state=42)
X_train, y_train, encoder, lb = process_data(
    train, categorical_features=cat_features, label="salary", training=True
)
X_test, y_test, _, _ = process_data(
    test, categorical_features=cat_features, label="salary",
    training=False, encoder=encoder, lb=lb
)
# TODO: implement the first test. Change the function name and input as needed
def test_model_returns_expected_type():
    """
    # Test if train_model returns a fitted model with predict method
    """
    model = train_model(X_train, y_train)
    assert hasattr(model, "predict"), "Model should have predict method"
    assert callable(model.predict), "Predict should be callable"
    


# TODO: implement the second test. Change the function name and input as needed
def test_compute_model_returns_floats():
    """
    # Test that precision, recall and fbeta are floats in range 0 - 1
    """
    model = train_model(X_train, y_train)
    preds = inference(model, X_test)
    precision, recall, fbeta = compute_model_metrics(y_test, preds)
    
    assert isinstance(precision, float)
    assert isinstance(recall, float)
    assert isinstance(fbeta, float)

    for metric in [precision, recall, fbeta]:
        assert 0.0 <= metric <= 1.0, f"Metric {metric} out of bounds"


# TODO: implement the third test. Change the function name and input as needed
def test_model_algo_type():
    """
    # Test that the trained model is a RandomForestClassifier
    """
    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier), "Model should be RandomForestClassifier"
