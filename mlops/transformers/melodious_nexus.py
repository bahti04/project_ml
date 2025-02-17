from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from mage_ai.data_preparation.decorators import transformer
import joblib
import mlflow
import mlflow.sklearn
import pandas as pd
import os

@transformer
def train_random_forest_model(df, *args, **kwargs):
    mlflow.set_tracking_uri('http://localhost:5002')
    mlflow.set_experiment('train')
    
    X = df[['passenger_count', 'trip_distance', 'fare_amount', 'total_amount']]
    y = df['tip_amount']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=(df['tip_amount'] > 0), random_state=42)
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    print(f"Mean Squared Error: {mse}")
    print(f"R^2 Score: {r2}")
    
    mlflow.log_metric("mse", mse)
    mlflow.log_metric("r2_score", r2)
    
    model_dir = "/mage/models"
    os.makedirs(model_dir, exist_ok=True)
    
    model_path = os.path.join(model_dir, "random_forest_model.joblib")
    joblib.dump(model, model_path)
    
    return model_path
