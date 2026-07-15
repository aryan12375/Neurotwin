import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "dataset.csv"

def load_data():
    df = pd.read_csv(DATA_PATH)
    df.rename(columns={'Temp': 'load'}, inplace=True)

    data = df['load'].values.reshape(-1, 1)

    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(data)

    return data_scaled, scaler

def create_sequences(data, seq_length):
    X, y = [], []

    for i in range(len(data) - seq_length):
        X.append(data[i:i+seq_length])
        y.append(data[i+seq_length])

    return np.array(X), np.array(y)
