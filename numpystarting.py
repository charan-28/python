import numpy as np
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
print(arr.astype())'''

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