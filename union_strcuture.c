#include <stdio.h>
#include <stdlib.h>
struct item
{
    int stock_number;
    float price;
    int item_type;
    union
    {
        struct
        {
            char title[100];
            char author[100];
            int num_pages;
        } book;
        struct
        {
            char design[100];
        } mug;
        struct
        {
            char size;
            char color[20];
        } shirt;
    } item;
};
void main()
{
    int j;
    struct item x;
    printf("\nenter gift type \t 0: book \t 1: Mug \t 2:shirt\n");
    scanf("%d", &x.item_type);
    fflush(stdin);
    switch (x.item_type)
    {
    case 0:
        printf("\n enter book title ");
        gets(x.item.book.title);
        printf("\nthe title of the book is ");
        puts(x.item.book.title);
        break;
    case 1:
        printf("\n enter mug design ");
        scanf("%s", x.item.mug.design);
        printf("\ndesign of mug is ");
        puts(x.item.mug.design);
        break;
    case 2:
        printf("\nenter size and colour of shirt ");
        scanf("%c", &x.item.shirt.size);
        scanf("%s", x.item.shirt.color);
        printf("\nsize of shirt is %c and colour is%s", x.item.shirt.size, x.item.shirt.color);
        break;
    }
}
