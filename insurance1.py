# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 07:53:19 2021

@author: Tanu Shree
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.api.types import is_string_dtype, is_numeric_dtype
df = pd.read_csv(r'C:\Users\Tanu Shree\Downloads\insurance.csv')
df.info()
num_list = []
cat_list = []
for column in df:
    plt.figure(column, figsize = (5,5))
    plt.title(column)
    if is_numeric_dtype(df[column]):
        df[column].plot(kind = 'hist')
        num_list.append(column)
    elif is_string_dtype(df[column]):
        df[column].value_counts()[:10].plot(kind = 'bar')
        cat_list.append(column)
sns.pairplot(df)
for i in range(0, len(cat_list)):
    hue_cat = cat_list[i]
    sns.pairplot(df, hue = hue_cat)
plt.figure(column, figsize = (10, 10))
correlation = df.corr()
sns.heatmap(correlation, cmap = "GnBu", annot = True)
