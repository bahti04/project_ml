from flask import Flask, request, jsonify
import mlflow
import os

app = Flask(__name__)

mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI", "http://mlflow:5002"))

@app.route('/')
def home():
    return "Flask API для MLflow успешно запущен!"

@app.route('/run-experiment', methods=['POST'])
def run_experiment():
    data = request.json
    experiment_name = data.get('experiment_name', 'Default')
    with mlflow.start_run(experiment_id=mlflow.get_experiment_by_name(experiment_name).experiment_id):
        param = data.get('param', 1)
        mlflow.log_param("param", param)

        metric = data.get('metric', 0.5)
        mlflow.log_metric("metric", metric)
        
        return jsonify({"message": "Эксперимент успешно запущен", "run_id": mlflow.active_run().info.run_id}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)