import numpy as np
import matplotlib.pyplot as plt
'''
arr=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9],[8,6,6]])
print("Original array:\n", arr)
print(arr.ndim)  # Number of dimensions
print(arr.shape)  # Shape of the array
print(arr.size)  # Total number of elements
print(arr.dtype)  # Data type of the elements
print()
arr1=np.array([[[1, 2, 3], [4, 5, 6]],[[7, 8, 9],[8,6,6]]])
print("Original array:\n", arr1)
print(arr1.ndim)  # Number of dimensions
print(arr1.shape)  # Shape of the array
print(arr1.size)  # Total number of elements
print(arr1.dtype)  # Data type of the elements
n_arr=arr1.reshape(2,3,2)
print("Reshaped array:\n", n_arr)

ap=np.array([[[1,2],[3,4]],    [[5,6],[7,8]]])
print("Original array:\n", ap)
print(ap.ndim)  # Number of dimensions
print(ap.shape)  # Shape of the array
n_arr=ap.reshape(2,4)
print("Reshaped array:\n", n_arr)
arr=np.array([10, 20, 30, 40, 50, 60])
print(arr[0])  # Accessing the first element
print(arr[-1])  # Accessing the last element
print(arr[2:5])  # Accessing elements from index 2 to 4
print(arr[::-1])
n_arr=arr.reshape(3,2)
print("Reshaped array:\n", n_arr)
print(n_arr[:,1])  # Accessing the second column
print(n_arr[0:2,:1])

arr=np.array([[1, 2, 3,3,5], [4, 5, 6,1,2], [7, 8, 9,5,4],[8,6,6,3,2]])
print("Original array:\n", arr)
print(arr.ndim)  # Number of dimensions
print(arr.shape)  # Shape of the array
print(arr[1:2,2:4])  # Accessing a subarray

arr=np.arange(1,13).reshape(2,6)
print(arr)

a=np.ones((3,4))
print(a)
b=np.zeros((2,3))
print(b)
c=np.random.random((2,3))
print(c)
print(np.linspace(-10,10,5)) 
print(np.logspace(-10,10,10))
print(np.eye(3))  # Identity matrix
print(np.identity(4))  # Identity matrix
print(c.itemsize)  # Size of each element in bytes
print(arr.astype(np.float32))  # Change the data type of the array
print(arr.astype())

arr1=np.arange(1,13).reshape(3,4)
arr2=np.arange(13,25).reshape(3,4)
print(arr1)
print(arr2)

#Scalar operations arthematic operations & Relational operations
# +,-,*,**,/,<,>,<=,>=,==
print(arr1 + 5)  # Adding a scalar to the array
print(arr2**3)  # Raising each element of the array to the power of 3
print(arr1/2)  # Dividing each element of the array by 2

print(arr1>3)  # Relational operation: greater than 3


#Vector operations arthematic operations & Relational operations

arr3=np.arange(0,12).reshape(4,3)
arr4=np.arange(12,24).reshape(4,3)
print(arr3>arr4)  # Relational operation: element-wise comparison 
print(arr3+arr4)
print(arr3)
#print(arr4)
print(np.max(arr3,axis=1))  # Maximum along the specified axis=1 for row-wise operation
print(np.min(arr3,axis=0))  # Minimum along the specified axis=0 for column-wise operation
print(arr1)
print(arr3)
print(np.dot(arr1,arr3))  # Dot product of two arrays 
print(arr1)
print(arr1[::2,1::2])
print(arr1[1,::3])
print(arr1[0:2,1:])

arr=np.arange(0,27).reshape(3,3,3)
print(arr)
print(arr[0::2,0:,0:])
print(arr[0,1:2])
print("1block middle coloumn",arr[1,:,1])
print(arr[2,1:,1:])
print(arr[0::2,0,0::2])

arr=np.random.randint(1,100,24).reshape(6,4)
print(arr)
print(arr>40)
print(arr[arr>35])
a = np.arange(24).reshape(6,4)
print(a)
#print(a[1:3,1:3])
print(a[[1,2],[0,2]])

arr=np.array([1,2,3,np.nan,5,6,np.nan])
print(arr)

print(arr[~np.isnan(arr)])

x=np.linspace(-10,10,100)
y=x**2
plt.plot(x,y)
plt.show()

a=np.linspace(1,10,20)
b=np.sin(a)
plt.plot(a,b)   
plt.title("Sine Wave")
plt.xlabel("X-axis")    
plt.ylabel("Y-axis")
plt.show()  

x=np.linspace(-10,10,100)
y=x*np.log(x)
print(y)
plt.plot(x,y)
plt.show()

arr=np.random.randint(1,100,24).reshape(6,4)
print(arr)
print(np.sort(arr,axis=0)[::-1])  # Sort along the specified axis=0 for column-wise operation
print(np.sort(arr,axis=1)[::-1])  # Sort along the specified axis=1 for row-wise operation

a=np.arange(1,25).reshape(4,6)
print(a)
a=np.append(a,np.array([25,26,27,28,29,30]).reshape(1,6),axis=0)   # Append a new row to the array
print("updated",np.sort(a))
a=np.append(a,np.random.randint(1,100,10).reshape(5,2),axis=1)   # Append a new column to the array
print("updated",np.sort(a))'''

a=np.array([1,2,3,2,6,5,6,7])
print(a)
np.cumsum(a)  # Cumulative sum of the array 
print(np.cumsum(a))