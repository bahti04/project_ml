from sklearn.preprocessing import StandardScaler
import pandas as pd

@transformer
def normalize_data(df, *args, **kwargs):
    numerical_features = ['passenger_count', 'trip_distance', 'fare_amount', 'tip_amount', 'total_amount']
    
    scaler = StandardScaler()
    df[numerical_features] = scaler.fit_transform(df[numerical_features])
    
    return df