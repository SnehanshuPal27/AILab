a = 5
b= 6
print "Initial values of a:",a,"b:",b,"\n"

a=a^b
b=a^b
a=a^b

print "Final values of a:",a,"b:",b,"\n"

print "Now using temp variables \n"

temp=a
a=b
b=temp

print "Again swapping it a:",a,"b:",b
