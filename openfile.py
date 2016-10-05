f = open('../../files/tmp.txt')
#print f.read(4)
# print "-"*50+str(f.tell())
#f.seek(0)
# print f.read()
print f.readline(2)
lines=f.readlines()
f.close()
print lines[3]
#for line in f:
#	print line
#	print "-"*50

