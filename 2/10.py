import numpy as np


a_zero = np.zeros(10)
print(a_zero)
a_one = np.ones(10)

print(a_one)
a_five = np.tile(5, 10)


print(a_five)


array_even = np.arange(10, 51, 2)
print("\n even integer 10 to 50:")
print(array_even)

random_no = np.random.rand()
print("\n Random number between 0 and 1:")
print(random_no)

matrix = np.arange(1, 21).reshape(4, 5)


np.savetxt('matrix.txt', matrix)
print("\niv. Original Matrix:")
print(matrix)

loaded_matrix = np.loadtxt('matrix.txt')
print("\nMatrix loaded from file:")
print(loaded_matrix)














