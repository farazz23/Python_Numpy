import numpy as np


#! Appends the array
arr = np.array([10, 20, 30])
new_arr = np.append(arr, [40, 50, 60])
print(new_arr)

#! Concatinate :
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([50, 60, 70, 80])
new_concat_array = np.concat((arr1, arr2))
print(new_concat_array)
