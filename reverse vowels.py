n=input()
n1=""
for i in n:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        pass
    else:
        n1=n1+i
n=n1
ans=n[::-1]
print(ans)
