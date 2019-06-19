l,u=map(int,input().split())
for n in range(l,u+1):
    if(n>0):
        for i in range(1,n):
            if(n%2!=0):
                print(n)
                break
