import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_demand(csv_file="inventory.csv", product_name="Apple"):
    df = pd.read_csv(csv_file)
    df = df[df['name'] == product_name]

    df['day'] = range(len(df))
    X = df[['day']]
    y = df['quantity']

    model = LinearRegression()
    model.fit(X, y)

    next_day = [[len(df)]]
    predicted = model.predict(next_day)
    return int(predicted[0])
