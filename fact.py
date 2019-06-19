def fct(n):
    if(n==1):
        return n
    else:
        return n*fct(n-1)
n=int(input())
if(n<0):
    print("not possible")
elif(n==0):
    print(1)
else:
    print(fct(n))
