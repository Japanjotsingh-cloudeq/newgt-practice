print("enter first number")
a=int(input())
print("enter last number")
b=int(input())
oddlist=[]
evenlist=[]
for x in range(a,b):
    if(x%2!=0):
        oddlist.append(x)
    else:
        evenlist.append(x)
print("odd list", oddlist)            
print("even list",evenlist) 