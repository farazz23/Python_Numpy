import numpy as np


# ? Removing elements from 1D array:
arr = np.array([10, 20, 30, 40, 50, 60, 70])
new_arr = np.delete(arr, 5)
print(new_arr)

# ? Removing elements from 2D array:
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
new_arr_2d = np.delete(arr_2d, 0, axis=0)
print(new_arr_2d)
