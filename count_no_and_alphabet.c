#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main()
{
char str1[50];//str1= Aa19 \0
gets(str1);      //   0123
int i =0, l=0, d=0;///i=indexing , l = count char //d = count digits 
while(str1[i]!='\0')//str1[4]=9
{
if((str1[i]>='A' && str1[i]<='Z')|| (str1[i]>='a' && str1[i]<='z'))//A TO Z or a to z //false or false =false
{l++;}//increase by 1 = 2  
else if((str1[i]>='0' && str1[i]<='9'))//
{d++;}
i++;
}
printf("The number of letters and digits in %s are: %d\t%d", str1, l, d);
return 0;
}













