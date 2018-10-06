#define SIZE 50
#include<ctype.h>
#include<stdio.h>
int s[SIZE];
int top=-1;
void push(int ele)
{
 s[++top]=ele;
}
int pop()
{
return(s[top--]);
}  
void main()
{
char pofx[50],ch;
int i=0,op1,op2;
printf("\nEnter the postfix Exp.:");
scanf("%s",pofx);
while((ch=pofx[i++])!='\0')
{
if(isdigit(ch))push(ch-'O');
else
{
op2=pop();
op1=pop();
switch(ch)
{
case'+':push(op1+op2);break;
case'-':push(op1-op2);break;
case'*':push(op1*op2);break;
case'/':push(op1/op2);break;
  }
 }
}
printf("\n Given postfix Expn:%s",pofx);
printf("\n Result after Evaluation:%d",s[top]);
}
