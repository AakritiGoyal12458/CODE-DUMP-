#include<stdio.h>
#include<string.h>
int main( )
{
char name [10 ],name2[10] ;
printf("Enter your name");
gets( name);//akku\
printf("Name is :");
puts(name);
printf("Character at index 0 is %c\n", name[0]);
printf("ASCII value of character at index 0 is %d\n", name[0]);
i=0;
while(name[i]!='\0')
{
name2[i]=name[i];//akku
i++;
}
// append ‘\0’ at the end of t
name[i]='\0';
return 0;
}











int main()

{

char s[20], t[40];

printf("Enter string1");

gets(s);

printf("Enter string2");

gets(t);
//iterate till end of string s
int i = 0; \\s=TOM t=LEE
while(s[i]!='\0')  
{
i++;//3 
}
//Append t at the end of s
int j = 0;
while(t[j]!='\0')           s=T_ O_ M_ L_ E_ E_
{
s[i]=t[j];s[4]=t[1]
i++;
j++;
}
// append ‘\0’ at the end of s
s[i]='\0';
puts(s);
}
