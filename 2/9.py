import numpy as np
import random
import sys
a=np.zeros((7,8))
print(a)
for i in range(0,7):
    for j in range(0,8):
        a[i][j]=random.randrange(100)
print(a)

for i in range(0,8):
    maxi=-1
    mini=111
    for j in range(0,7):
        maxi=max(maxi,a[j][i])
        mini=min(mini,a[j][i])
    print "MAX and min val for col",i," : are",maxi,"and",mini

