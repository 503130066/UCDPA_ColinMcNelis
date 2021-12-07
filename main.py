import pandas as pd
import numpy as np

# Reads Fleet Data CSV
df = pd.read_csv("fleet.csv", index_col=0, skipinitialspace=True)

# Take a look to understand data
print(df.head())
print(df.shape)

df = df.drop(['Lease To', 'Lease To Derived', 'Lease From', 'Engine Series'], axis=1)
# Outputs sum of missing values per column
print(df.isna().sum())

# Replaces missing values with 'NaN'
cleaned_df = df.fillna('NaN')
print(cleaned_df.isna().sum())

# Remove duplicates of Serial Number and Registration Number
cleaned_dup = df.drop_duplicates(subset=["Serial Number", "Tail/Registration Number"])
print(df.shape)

# Sorts Database by Lessor/Owner for Visualization
Lessor = df.sort_values(by=['Lessor/Owner', 'Operator Country/Territory', 'Age'])
print(Lessor.head())

# Using loc to create subset of Dataframe examining EasyJet Fleet
df1 = df.loc[["easyJet"],["Status", "Aircraft Variant"]]
print(df1.shape)

# Using loc to create subset of Dataframe examining Lessor Portfolio
df2 = df.loc[:,["Lessor/Owner", "Aircraft Variant", "Age"]]
print(df2.shape)

df3 = df.loc[["Wizz Air"],["Aircraft Variant", "Age"]]

df4 = df.iloc[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 10]]
print(df4)

print(df["Age"])

# The following code shows a looping function for a Pandas Dataframe
for lab, row in df3.iterrows() :
    df3.loc[lab, "Avg_age"]= np.mean(row["Age"])
print(df3)

print(df2[(df2["Age"] <= 4) & (df2['Aircraft Variant'] == "A320-200")])

# The following code merges Dataframes
frames = [df, df1]
result = pd.concat(frames)
print(df.shape)
print(result.shape)

cleaned_dup2 = result.drop_duplicates(subset=["Tail/Registration Number"])
print(cleaned_dup2.shape)

# This section examines using an aviation API
