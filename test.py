import pandas as pd

df = pd.read_csv('breast_cancer.csv')
print(df.head())
X = df.iloc[:, 1:-1].values
y = df.iloc[:, -1].values


print(X)
print(y)