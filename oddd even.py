m=input()
n=len(m)
a=[]
b=[]

for i in range(0,len(m)):
    if(i%2==0):
        print(i)
        a.append(m[i])
    else:
        b.append(m[i])
print("even",a)
print("odd",b)
s=""
for i in range(0,n//2):
    s=s+b[i]+a[i]
print(s)
        
