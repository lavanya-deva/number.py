a=input()
c=len(a)
b=[]
d=[]
for i in range(0,c):
    if(i%2==0):
        print(i)
        b.append(a[i])
    else:
        d.append(a[i])
print("even",b)
print("odd",d)
a=""
for i in range(0,c//2):
    a=a+d[i]+b[i]
print("swap",a)
