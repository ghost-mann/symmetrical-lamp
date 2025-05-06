import requests
import pandas as pd

# extract data from csv file
class Extractor:
    @staticmethod
    def from_csv(file_path: str):
        # loads data from csv into df
        return pd.read_csv(file_path)

# stores resulting dataframe into variable df 
# staticmethod - didnt need to create object - class instance
df = Extractor.from_csv('spotify.csv')

# data cleaning, aggregation, formatting
class Transformer:
    

