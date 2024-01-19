fh=open('/home/btech/22/snehanshu.pal22b/AILab/2/text.txt','r')
x=fh.readlines()
fh2=open('/home/btech/22/snehanshu.pal22b/AILab/2/text2.txt','w')
for i in x:
    fh2.write(i)
fh.close()
fh2.close()


