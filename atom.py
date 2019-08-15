l=[]
m=[]
n=[]
num=int(input("enter the no of elements:"))
for i in range(0,num):
    x=int(input("enter the elements to be inserted:"))
    l.append(x)
print("list l=",l)
for j in range(0,num):
    y=int(input("enter the elements to be inserted:"))
    m.append(y)
print("list 2=",m)
for k in range(0,num):
    z=l[k]+m[k]
    n.append(z)
print("THE FINAL LIST AFTER ADDITION\n")
print("list n=",n)
