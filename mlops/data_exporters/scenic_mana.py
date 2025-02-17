import mlflow
import joblib
from mage_ai.data_preparation.decorators import data_exporter

@data_exporter
def export_model_to_mlflow(model_path, *args, **kwargs):
    model = joblib.load(model_path)
    
    mlflow.set_tracking_uri("http://mlflow:5002")
    mlflow.set_experiment("taxi_trip_experiment")
    
    with mlflow.start_run():
        mlflow.sklearn.log_model(model, "random_forest_model")
        mlflow.log_param("n_estimators", model.n_estimators)
        mlflow.log_param("random_state", model.random_state)
    
    print("Модель успешно экспортирована в MLflow.")