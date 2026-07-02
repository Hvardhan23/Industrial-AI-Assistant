import pandas as pd
import joblib

encoder = joblib.load("./models/type_encoder.pkl")


def engineer_features(df):
    df = df.copy()

    # Training dataset
    if "Process temperature [K]" in df.columns:
        process_temp = "Process temperature [K]"
        air_temp = "Air temperature [K]"
        rpm = "Rotational speed [rpm]"
        torque = "Torque [Nm]"

    # API input
    else:
        process_temp = "Process_temperature_K"
        air_temp = "Air_temperature_K"
        rpm = "Rotational_speed_rpm"
        torque = "Torque_Nm"

    
    df["Type"] = encoder.transform(df["Type"])

    # Temperature Difference
    df["Temp_Diff"] = df[process_temp] - df[air_temp]

    # Power Approximation
    df["Power"] = df[rpm] * df[torque]

    return df