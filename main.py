import requests
import pandas as pd

# extract data from csv file
def from_csv(file_path: str):
    return pd.read_csv(file_path)


