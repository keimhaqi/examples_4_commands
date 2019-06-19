import numpy as np
import pandas as pd

dates = pd.date_range('20130101', periods=6)

# print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

# print(df)

# print(df.head())

# print(df.tail(3))

# print(df.index)

# print(df.columns)

# print(df.describe())

# print(df.T)

print(df)

print(df.sort_index(axis=1, ascending=False))