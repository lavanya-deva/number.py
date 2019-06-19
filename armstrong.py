n=int(input())
rev=0
temp=n
while(n>0):
    dig=n%10
    rev=rev+(dig*dig*dig)
    n=n//10
if(temp==rev):
    print("armstrong")
else:
    print("not")
    
            
