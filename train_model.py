import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import numpy as np

def create_labels(df):
    # Label = 1 if any sensor goes beyond threshold, else 0
    
    df["label"] = ((df["temperature"] > 80) | (df["vibration"] > 40) | (df["pressure"] > 160)).astype(int)
    return df

def train_model():
    df = pd.read_csv("sensor_data.csv")
    df = create_labels(df)

    X = df[["temperature", "vibration", "pressure"]]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

    joblib.dump(model, "predictive_model.pkl")
    print(" Model saved as predictive_model.pkl")

if __name__ == "__main__":
    train_model()
