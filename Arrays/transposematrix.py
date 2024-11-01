'''
---------- Test Case 1 ----------
[[1]]

---------- Test Case 2 ----------
[[1], [-1]]

---------- Test Case 3 ----------
[[1, 2, 3]]

---------- Test Case 4 ----------
[[1], [2], [3]]

---------- Test Case 5 ----------
[[1, 2, 3], [4, 5, 6]]

---------- Test Case 6 ----------
[[0, 0, 0], [1, 1, 1]]

---------- Test Case 7 ----------
[[0, 1], [0, 1], [0, 1]]

---------- Test Case 8 ----------
[[0, 0, 0], [0, 0, 0]]

---------- Test Case 9 ----------
[[1, 4], [2, 5], [3, 6]]

---------- Test Case 10 ----------
[[-7, -7], [100, 12], [-33, 17]]

---------- Test Case 11 ----------
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

---------- Test Case 12 ----------
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

---------- Test Case 13 ----------
[[5, 6, 3, -3, 12], [-3, 6, 5, 2, -1], [0, 0, 3, 12, 3]]

---------- Test Case 14 ----------
[[0, -1, -2, -3], [4, 5, 6, 7], [2, 3, -2, -3], [42, 100, 30, -42]]

---------- Test Case 15 ----------
[[1234, 6935, 4205], [-23459, 314159, 0], [100, 3, 987654]]

'''

def transposeMatrix(matrix):
    # Write your code here.
    return list(zip(*matrix))
