import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    # Drop identifiers
    df = df.drop(columns=["UDI", "Product ID", "Failure Type"])

    return df