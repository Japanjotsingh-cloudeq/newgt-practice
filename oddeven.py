import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

for x in range(a,b):
    if(x%2!=0):
        print("even",x)
    else:
        print("odd")
           
