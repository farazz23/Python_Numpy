import numpy as np

# ? Check the data type of the following variable :
arr = np.array([10, 20, 30.7])
print(f"Type of the data inside the array is : {arr.dtype}")

arr2 = np.array(["abc", "def", "ghi", "jkl", "mno"])
print(f"Type of the data inside the array is : {arr2.dtype}")

arr3 = np.array([10, "abc", 10.7, True])
print(f"Type of the data inside the array is : {arr3.dtype}")


# ? Change the datatype of the following variable : \
arr_4 = np.array([1.3, 4.6, 8.2, 9.12])
print(f"Current data type of the following variable is : {arr_4.dtype}")
print(f"array list  before the type coresion: {arr_4}")
int_arr = arr_4.astype(int)
print(f"array list after the type conversion: {int_arr}")
print(f"and the data type of the following variable: {int_arr.dtype}")
