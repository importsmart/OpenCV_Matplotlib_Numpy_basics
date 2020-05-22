import numpy as np

'''Inputting an array
array = np.array(list(map(int, input().split())))
print(array)
'''

#Best:
m,n = input().split()
arr1 = np.array(list(map(int, input().split())))
arr2 = np.array(list(map(int, input().split())))
matrix = np.array([arr1,arr2])
print(matrix)
print(np.transpose(matrix))
print(matrix.flatten())


'''Inputting all in one line and reshaping
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
print("Enter the entries in a single line (separated by space): ")
# User input of entries in a
# single line separated by space
entries = list(map(int, input().split()))
# For printing the matrix
matrix = np.array(entries).reshape(R, C)
print(matrix)
'''


''' Alternate array
arr1 = input().strip().split()
print(arr1)
arr2 = input().strip().split(' ')
matrix = numpy.array([arr1,arr2])
print(matrix)
'''