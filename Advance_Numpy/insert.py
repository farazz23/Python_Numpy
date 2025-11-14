"""
np.insert(array, index, value , asix=None)
array - original array
index -
value -
axis -
if axis= 0 -> row wise
if axis= 1 -> column wise
"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
new_arr = np.insert(
    arr, 3, 87
)  # NOTE : if you dont provide the axis value it will default be rows
print(new_arr)
print(arr)


#! insert in 2D array :
arr_2d = np.array([[1, 2], [3, 4]])
new_arr_2d = np.insert(arr_2d, 1, [5, 6], axis=0)
print(new_arr_2d)
new_arr_2d = np.insert(arr_2d, 1, [-1, -7], axis=1)
print(new_arr_2d)
