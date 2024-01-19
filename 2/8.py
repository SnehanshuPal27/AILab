import numpy as np
import random
a = np.zeros((3,4))
b = np.zeros((3,4))
for i in range(0,3):
    for j in range(0,4):
        a[i][j]=random.randrange(100)
for i in range(0,3):
    for j in range(0,4):
        b[i][j]=random.randrange(100)        

print("orignal array a:",a)
print("orignal array b:",b)
concatted=np.concatenate((a, b))
print(concatted)

print("Sorted first array:",np.sort(a))
print("Sorted second array:",np.sort(b))

added=a+b
print("added array is:",added)

subtracted=a-b
print("subtracted array is:",subtracted)

multiplied=a*b
print("multiplied array is:",multiplied)

divided = np.divide(a, np.where(b != 0, b, 1), dtype=float)
print("\nDivided array:")
print(divided)