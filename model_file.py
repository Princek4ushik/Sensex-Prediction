import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator
import joblib


WINDOW_LENGTH = 30
BATCH_SIZE = 32


def load_artifacts():
    """
    function to load data, scaler and sensex predictor
    """
    df = pd.read_csv("Data/main.csv", index_col='date')
    df = df.iloc[-WINDOW_LENGTH - 1: , :]
    scaler = joblib.load("scaler.gz")
    model = load_model("model.keras")
    return df, scaler, model


def preprocess_data(df_pred, scaler):
    """
    preprocessing function to preprocess data before prediction
    """
    df_pred_scaled = scaler.transform(df_pred)

    features = df_pred_scaled
    target = df_pred_scaled[: , -1]

    pred_gen = TimeseriesGenerator(
        features,
        target,
        length=WINDOW_LENGTH,
        sampling_rate=1,
        batch_size=BATCH_SIZE
    )

    return pred_gen, df_pred_scaled


def predict(df, scaler, model):
    """
    function to predict next day sensex points
    """
    data, df_pred_scaled = preprocess_data(df, scaler)
    pred = model.predict(data)
    prediction = pd.DataFrame(
        scaler.inverse_transform(
            np.concatenate(
                (df_pred_scaled[-1, :-1].reshape((1, 9)), pred),
                axis=1
            )
        )
    )
    prediction.columns = [
        'usinr', 'gdp', 'inflation', 'interest', 'leap',
        'election', 'dow_jones', 'gold', 'oil', 'points'
    ]
    return prediction


def get_next_month_data():
    """
    function to get next month predicted sensex data
    """
    df, scaler, model = load_artifacts()
    for _ in range(WINDOW_LENGTH):
        new_row_df = predict(df, scaler, model)
        df = pd.concat([df, new_row_df], ignore_index=True)
        df = df.iloc[1:, :].reset_index(drop=True)
    
    return df
