print "enter the numbers to be in list write -1 to terminate:"
list1 = []
list2 = []

while True:
    x = input()
    if x!=-1:
        list1.append(int(x))
    else:
        break

for i in list1:
    count = 0
    for j in list1:
        if i == j:
            count += 1
    if count == 1:
        list2.append(i)

print "the list of unique elements is :", list2
