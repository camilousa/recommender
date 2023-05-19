import pandas as pd
import numpy as np

def to_vector(df):
  m = np.ones((df.userID.max(), df.itemID.max())) * np.nan
  for index, row in df.iterrows():
    m[row.userID-1, row.itemID-1] = row.rating
  return m
