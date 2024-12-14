import pandas as pd


@data_loader
def load_data(*args, **kwargs):
    df = pd.read_parquet('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet')

    return df