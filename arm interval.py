l,u=map(int,input().split())
for n in range(l,u+1):
     rev=0
     temp=n
while(n>0):
    dig=n%10
    rev=rev+(dig*dig*dig)
    n=n//10
if(temp==rev):
    print(n)
