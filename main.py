import pandas as pd

# Reads Fleet Data CSV
df = pd.read_csv("fleet.csv", index_col=0)
df.columns.tolist()
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

df1 = df.iloc[0:100, 1:5]
print(df1.shape)
