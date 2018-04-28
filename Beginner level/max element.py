j=[]
x=int(input("enter the no of elements:"))
for i in range (1,x+1):
    d=int(input("enter elemenmt:"))
    j.append(d)
    j.sort()
print("largest element is:",j[x-1])
