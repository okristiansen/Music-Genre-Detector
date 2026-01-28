import pandas as pd
from pathlib import Path
from data.raw import genres_original

#Gjør file path portabel
DATA_DIR = Path(__file__).parent.parent / "data" / "raw"
features_30_sec = DATA_DIR / "features_30_sec.csv"
features_3_sec = DATA_DIR / "features_3_sec.csv"

def load_features30sec():
    return pd.read_csv(features_30_sec)

def load_features3sec():
    return pd.read_csv(features_3_sec)