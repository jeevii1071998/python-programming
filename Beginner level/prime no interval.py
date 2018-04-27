x,y=int(input())
x=int(x)
y=int(y)
for num in range(1,y+1):
    if num>1:
           for i in range(2,num):
               if(num%i)==0:
                   break
               else:
                   print ("num")
