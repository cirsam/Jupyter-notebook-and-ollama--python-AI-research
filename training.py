#this shows simple examples of the fundamentals of numpy arrays transformed into pandas, DataFrame, and how they translate into tensors, and then are shown practically using matplotlib graphs
print(f"got here not test folder")
import pandas as pd
import numpy as np
import matplotlib.pyplot as ptl
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

print(f"got here1")
# Load the dataset
data = load_iris()

print("creating 11x5 array of gloatingpoint numbers\n")
num_py_random_data= np.random.rand(11,5)

num_py_random_data_to_Pd_df = pd.DataFrame(num_py_random_data,columns={'0':"col0",'1':"col1","2":"col2","3":"col3","4":"col4"})
num_py_random_data_to_Pd_df.columns=['cols0','cols1','cols2','cols3','cols4']
print(f"{num_py_random_data_to_Pd_df}")

df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
# View the first few rows
df.head()
print(f"got here2")

# print a one-dimensional array of integers and strings in pandas called a series. In numpy, they are called a vector
array=[1, 'two',3,4, 'five']
df1 =pd.Series(array)
#print a two-dimensional array of zeros and ones in numpy, called a matrix. In pandas, they are represented in tabular form, called a Frame
randomfnholder=np.random.default_rng(seed=50)
#now use randomfnholder to create different random number arrays. Below is a 4x3 shaped radom float array
random4by3 =randomfnholder.random((4,3))
print("2D numpy random number arrayrandom4by3\n",random4by3)
random_numbers =randomfnholder.integers(4,24,size=4)
print("print 1D numpy array of 4 random numbers between 1 and 20 random_numbers\n",random_numbers)
zeros=np.zeros((2,5),dtype=float)
print("2D numpy zeros array\n",zeros)
fig,xy=ptl.subplots()
x=np.array(random_numbers)
y=np.linspace(0,20,4).astype(int)
print(f"x is\n{x} y is\n {y}")

xy.plot(x,y)
xy.set(xlim=(0,20),ylim=(0,20))

ones=np.ones((2,5),dtype=int)
print("2D numpy ones array\n",ones)
array_data=[[1,2,3],[4,5,6],[7,8,9],[11,12,13]]
two_d_array=pd.DataFrame(array_data)

print("printing a hard coded numpy 2D array\n",two_d_array)
print("\ndisplay matplotlibplot for random_numbers\n")
xy.grid()#show the grid
ptl.show()
xy.set( xlabel="x Axis",ylabel="y Axis",title="plot of 4 random points on x axis and controlled y axis" )

print("printing the shape of the numpy 2D array\n",two_d_array.shape)
# get the data from a csv which contains cities, countries, and country codes
print("get the data from a csv which contains cities, countries, and country codes")
cities_countries_codes= pd.read_csv("data.csv")


print("\n changing cities_countries_codes to dataFrame \n")
cities_countries_codes_df= pd.DataFrame(cities_countries_codes)
print("\n displaying cities_countries_codes_df content \n")

print(cities_countries_codes_df)

data1 = {
    'City': ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai'],
    'Country': ['Japan', 'India', 'China', 'Brazil', 'India'],
    'Population_Millions': [37.3, 32.0, 28.5, 22.4, 20.4]
}
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

print("\n Tensor x:")
print(x)
print("\n Tensor y:")
print(y)
print("\n Shape of x:\n", x.shape)
print("\n Device of x:\n", x.device)
print("\n Shape of y:\n", y.shape)
print("\n Device of y:\n", y.device)
# Perform basic operations
z = x + y
print("\n Addition operation (x + y):\n",x+y)
print("\n print z \n",z)

# In-place addition (modifies y)
y.add_(x)
print("\n In-place addition (y.add_(x)\n",(y.add_(x)))
print("\n print y \n",y)

# Autograd example: Tensors can track computations for gradient calculation (essential for neural networks)
a = torch.randn(1, requires_grad=True, device=device)
b = torch.randn(1, requires_grad=True, device=device)

# A simple operation

c = a * b 
# Compute gradients
c.backward()

print("\n Autograd example:\n")
print("Gradient of a with respect to c:\n", a.grad)
print("Gradient of b with respect to c:\n", b.grad)

