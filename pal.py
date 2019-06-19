n=int(input())
sum=0
temp=n
while(n>0):
    dig=n%10
    sum=sum*10+dig
    n=n//10
if(temp==sum):
    print("palindrome")
else:
    print("not palindrome")
