fh=open("/home/btech/22/snehanshu.pal22b/AILab/2/example.txt","a+")
fh.seek(0)

print "The current line of file:\n",fh.read()

string=input("Enter text to be appended:")

fh.write(string)
fh.close()
fh=open("/home/btech/22/snehanshu.pal22b/AILab/2/example.txt","r")
print "file after append operation:\n" ,fh.read()    

