print(f"got here not test folder")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

print(f"got here1")
# Load the dataset
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
# View the first few rows
df.head()
print(f"got here2")

# print a one-dimensional array as a series of integers in pandas
array=[1,2,3,4,5]
df1 =pd.Series(array)
#print a two-dimensional array as a data frame in pandas

data = {
    'City': ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai'],
    'Country': ['Japan', 'India', 'China', 'Brazil', 'India'],
    'Population_Millions': [37.3, 32.0, 28.5, 22.4, 20.4]
}
data2 = {
    'City': ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai'],
    'Country': ['Japan', 'India', 'China', 'Brazil', 'India'],
    'Population_Millions': [1,2,3,4,5]
}

df2 = pd.DataFrame(data )
df3 = pd.DataFrame(data2)
print(f"got here3")
X = df.drop('target', axis=1) # Features
y = df['target']              # Labels (what we want to predict)
print(f"got here4")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)
print(f"got here5")