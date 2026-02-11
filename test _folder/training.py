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

print("creating 11x5 array of gloatingpoint numbers")
num_py_random_data= np.random.rand(11,5)

num_py_random_data_to_Pd_df = pd.DataFrame(num_py_random_data,columns={'0':"col0",'1':"col1","2":"col2","3":"col3","4":"col4"})
num_py_random_data_to_Pd_df.columns=['cols0','cols1','cols2','cols3','cols4']
print(f"{num_py_random_data_to_Pd_df}")

df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
# View the first few rows
df.head()
print(f"got here2")

# print a one-dimensional array as a series of integers in pandas
array=[1, 'two',3,4, 'five']
df1 =pd.Series(array)
#print a two-dimensional array as a data frame in pandas
# get the data from a csv which contains cities, countries, and country codes
print("get the data from a csv which contains cities, countries, and country codes")
cities_countries_codes=pd.read_csv("datatf.csv")
print("changing cities_countries_codes to dataFrame")
cities_countries_codes_df= pd.DataFrame(cities_countries_codes)
print("displaying cities_countries_codes_df")

data1 = {
    'City': ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai'],
    'Country': ['Japan', 'India', 'China', 'Brazil', 'India'],
    'Population_Millions': [37.3, 32.0, 28.5, 22.4, 20.4]
}
print("all done csv read")
data2 = {
    'City': ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai'],
    'Country': ['Japan', 'India', 'China', 'Brazil', 'India'],
    'Population_Millions': df1
}

df2 = pd.DataFrame(data1)
df3 = pd.DataFrame(data2)
print(f"got here3")
X = df.drop('target', axis=1) # Features
y = df['target']              # Labels (what we want to predict)
print(f"got here4")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)
print(f"got here5")

import torch
import math

# Check for and use GPU if available, otherwise use CPU
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("Using GPU:", torch.cuda.get_device_name(0))
else:
    device = torch.device("cpu")
    print("Using CPU")

# Create a PyTorch Tensor
# Tensors are the fundamental data structure in PyTorch, similar to NumPy arrays
x = torch.randn(3, 4, device=device)
y = torch.randn(3, 4, device=device)

print("\nTensor x:")
print(x)
print("Shape of x:", x.shape)
print("Device of x:", x.device)

# Perform basic operations
z = x + y
print("\nAddition operation (x + y):")
print(z)

# In-place addition (modifies y)
y.add_(x)
print("\nIn-place addition (y.add_(x)):")
print(y)

# Autograd example: Tensors can track computations for gradient calculation (essential for neural networks)
a = torch.randn(1, requires_grad=True, device=device)
b = torch.randn(1, requires_grad=True, device=device)

# A simple operation
c = a * b
# Compute gradients
c.backward()

print("\nAutograd example:")
print("Gradient of a with respect to c:", a.grad)
print("Gradient of b with respect to c:", b.grad)
