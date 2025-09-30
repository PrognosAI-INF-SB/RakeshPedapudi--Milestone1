import pandas as pd
import numpy as np

def generate_sensor_data(n=500):
    np.random.seed(42)
    time = pd.date_range(start="2025-01-01", periods=n, freq="h")
    temperature = 50 + np.random.normal(0, 5, n).cumsum()
    vibration = 20 + np.random.normal(0, 2, n).cumsum()
    pressure = 100 + np.random.normal(0, 3, n).cumsum()

    df = pd.DataFrame({"time": time, "temperature": temperature, "vibration": vibration, "pressure": pressure})
    df.to_csv("sensor_data.csv", index=False)
    print("✅ Sensor data saved to sensor_data.csv")

if __name__ == "__main__":
    generate_sensor_data()
