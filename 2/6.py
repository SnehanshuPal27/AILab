import numpy as np
n=input("enter n")
m=input("enter m")
mat=[]

for i in range(0,m):
    rows=[]
    for j in range(0,n):
        x=int(input(""))
        rows.append(x)
    mat.append(rows)
a=np.array(mat)
print(a)
print("\nThe transposed matrix:\n")
print(np.transpose(a))
a=np.transpose(a)
print("Flattened transpose output:")
print(a.flatten())
