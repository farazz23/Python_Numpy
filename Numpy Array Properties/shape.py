import numpy as np

arr_2D = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2D)

#! Shape of the array -> means how many rows and column is present
print(f"Shape of the array is: {arr_2D.shape}")

#! Size of the array -> how many elements is present inside the array
print(f"Size of the array is : {arr_2D.size}")

#! Dimension of the array :
print(f"Dimension of the array is: {arr_2D.ndim}")


arr_3D = np.array([[[1, 3, 5], [8, 9, 3]], [[6, 4, 8], [1, 7, 2]]])
print(f"Dimension of the array is : {arr_3D.ndim}")
