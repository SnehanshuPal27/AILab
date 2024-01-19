fh=open('/home/btech/22/snehanshu.pal22b/AILab/2/text.txt','r')
x=fh.readlines()
print "Now printing the lines starting with anything except T\n"
for i in x:
    if(i[0]!='T' and i[0]!='t'):
        print i

