#include <stdio.h>

int gcd(int a,int b)
{
    if(a==0)
    return b;
    if(b==0)
    return a;
    if(a==b)
    return a;
    if(a>b)
    return gcd(a-b,b);
    return gcd(a,b-a);
}
int main()
{
    int n1,n2,c;
    printf("enter the number");
    scanf("%d%d",&n1,&n2);
    c=gcd(n1,n2);
    printf("%d",c);
}
