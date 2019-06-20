n='hello.123?23@lav'
num=0
for i in n:
        if(i=='.' or i=='@' or i=='$' or i=='&' or i=='?'):
                num=num+1
print(num)
