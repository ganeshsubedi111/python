#pickle in python
import pickle
l=[10,20,30,40,50,60]
file=open("writedata.txt","wb")
pickle.dumb(l,file)
file.close()
