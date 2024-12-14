FROM python:3.10-slim

RUN pip install mlflow==2.12.1

EXPOSE 5002

CMD ["mlflow", "server" \
    "--backend-store-uri", "postgresql://postgres:password@db:5432/magic" \
    "--host", "127.0.0.1" \
    "--port", "5002"]