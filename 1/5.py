list1=[1,2,3]
list2=[4,5,6]
print "list1:"
for i in list1:
    print i
print "list2:"
for i in list2:
    print i
print "concatenated list:"
new_list=list1+list2
for i in new_list:
    print i

print "list after filtering:"

for i in new_list:
    if i%2==0:
        print i

