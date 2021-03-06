import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import seaborn as sns

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
df1 = df.loc[["easyJet"], ["Status", "Aircraft Variant"]]
print(df1.shape)
A2 =df.pivot_table(index="Operator", columns= "Aircraft Variant", values = "Age", aggfunc=np.mean)


# Using loc to create subset of Dataframe examining Lessor Portfolio
df2 = df.loc[:, ["Lessor/Owner", "Aircraft Variant", "Age"]]
print(df2.shape)
A1 =df2.pivot_table(index="Lessor/Owner", columns= "Aircraft Variant", values = "Age", aggfunc=np.mean)
print(A1.head(100))

df3 = df.loc[["Wizz Air"], ["Aircraft Variant", "Age"]]

df4 = df.iloc[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 10]]
print(df4)

print(df["Age"])

# The following code shows a looping function for a Pandas Dataframe
for lab, row in df3.iterrows():
    df3.loc[lab, "Avg_age"] = np.mean(row["Age"])
print(df3)

print(df2[(df2["Age"] <= 4) & (df2['Aircraft Variant'] == "A320-200")])

# The following code merges Dataframes
frames = [df, df1]
result = pd.concat(frames)
print(df.shape)
print(result.shape)

cleaned_dup2 = result.drop_duplicates(subset=["Tail/Registration Number"])
print(cleaned_dup2.shape)

# This section examines using an ISS Location API
# The ISS information API is a type 1 API
data = requests.get("http://api.open-notify.org/iss-now.json")
print(data.json())

data = data.json()
# The below print call outputs the ISS Position from the API
print(data["iss_position"])

# Define a custom function to create reusable code
# This function outputs a matrix of n size given n*n elements


def square_matrix(size, *elements):
    return np.array(elements).reshape(size,size)


a = square_matrix(3, 2, 9, 3, 10, 4, 15, 7, 1, 0)
b = square_matrix(3, 4, 3, 10, 9, 0, 0, 1, 0, 7)
print(a)
print(b)

# A numpy function can then be used to get the dot product of matrices
c = np.dot(a, b)
print(c)

# Creating a dictionary from lists
Airline = ["Wizz Air", "Ryanair", 'Delta Airlines', "Finnair", "Air France"]
AvgAge = [1.5, 9, 15.25, 11.6, 14]

Airline_Portfolio_Age = {'Wizz Air': 1.5, "Ryanair": 9, "Delta Airlines": 15.25, "Finnair": 11.6, "Air France": 14,
                         'EasyJet': 3}

# To manipulate the dictionary, a further key:value pair can be added
# The print command below indicates the key:value pair has been added to the dictionary
print(Airline_Portfolio_Age)


# Visualise: These plots use the data from the imported csv and subset dataframes
ax1 = sns.boxplot(x=df3['Aircraft Variant'].head(150), y=df3['Age'].head(150))
ax1.set_title('Wizz Air Aircraft Portfolio Age')
sns.set_style("whitegrid")
plt.show()

ax2 = sns.barplot(x=A1["A320-200"].head(20), y=A1.index[0:20], data=A1)
ax2.set(xlabel="Mean Age", ylabel="Lessor/Owner")
ax2.set_title('A320-200 Portfolio Age by Lessor')
sns.set_style("whitegrid")
plt.show()

ax3 = sns.barplot(x=A2["737-800"].head(25), y=A2.index[50:75], data=A2)
ax3.set(xlabel="Mean Age", ylabel="Operator")
ax3.set_title('737-800 Portfolio Age by Operator')
sns.set_style("whitegrid")
plt.show()

ax4 = sns.countplot(x="Aircraft Variant", data=df3, order=df3['Aircraft Variant'].value_counts(ascending=False).index)
ax4.set_title('Wizz Air Portfolio Count')
abs_values = df3['Aircraft Variant'].value_counts(ascending=False).values
ax4.bar_label(container=ax4.containers[0], labels=abs_values)
sns.set_style("whitegrid")
ax4.set(ylabel="# of Aircraft")
plt.show()
