import sys

a = int(sys.argv[1])
b= int(sys.argv[2])
oddlist=[]
evenlist=[]
for x in range(a,b):
    if(x%2!=0):
        oddlist.append(x)
    else:
        evenlist.append(x)
print("odd list", oddlist)            
print("even list",evenlist) 