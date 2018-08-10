#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Object Creation
# Create series
s = pd.Series([1,3,5,np.nan,6,8])

print(s)

# Create DataFrame
dates = pd.date_range('20130101', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df)

# Create DataFrame with dict
df2 = pd.DataFrame({
    'A':1.,
    'B':pd.Timestamp('20130102'),
    'C':pd.Series(1, index=list(range(4)), dtype='float32'),
    'D':np.array([3] * 4, dtype='int32'),
    'E':pd.Categorical(["text", "train", "test", "train"]),
    'F': 'foo'
})

print(df2)

print(df2.dtypes)

print(df2.A)

#Viewing Data

print(df.head())

print(df.tail(3))

print(df.index)

print(df.columns)
print(df.values)

# describe
print(df.describe())

# Transposing your data
print(df.T)


# Sort by an axis
print(df.sort_index(axis=1, ascending=False))


# Sort by values under specific column
print(df.sort_values(by='B'))

# Getting, select a single column, which yields s Series, equivalent to df.A:
print(df['A'])

# select via [], which slices the rows.
print(df[0:3])


print(df["20130102":"20130104"])

# selection by Label
print(df.loc[dates[0]])

# select on a multi-axis by label:
print(df.loc[:,["A", "B"]])

# Showing label slicing, both endpoints are included:
print(df.loc['20130102':'20130104', ['A','B']])

print(df.loc['20130102',['A','B']])

# 获取指定位置的值
print(df.loc[dates[0],'A'])


print(df.at[dates[0], 'A'])

# select by position
print(df.iloc[3])

print(df.iloc[3:5,0:2])

print(df.iloc[[1,2,4],[0,2]])

print(df.iloc[1:3,:])

print(df.iloc[:,1:3])

print(df.iloc[1,1])

print(df.iat[1,1])