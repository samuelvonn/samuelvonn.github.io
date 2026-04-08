#libraries
import pandas as pd
import numpy as np
from lets_plot import *
LetsPlot.setup_html(isolated_frame=True)
df = pd.read_json("https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json")
# Count records where month is missing (NaN, "N/A", or empty string)
num_missing_month = df['month'].isna().sum() + (df['month'] == 'N/A').sum() + (df['month'] == '').sum()
print(f"Number of records with missing month: {num_missing_month}")
