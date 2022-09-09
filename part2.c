#include<stdio.h>

int main ()
{
   int height;
   printf("Please enter the height of the prymids between 2 and 5\n");
   scanf("%d",&height);
   
   while(height>5 || height<2)
   {
    printf("invaild option\nplease enter the height of the prymids between 2 and 5\n");
     scanf("%d",&height);
   }

   char pyramid[10][10];
   for(int i=0 ; i<height ; i++)
   {
     for(int j=0 ; j<height-i-1 ; j++)
        pyramid[i][j]=' ';

      for(int j=0 ; j<(i*2)+1 ; j++)
        pyramid[i][j+height-i-1]='*';
      
      for(int j=height+i ; j<(height*2)-1 ; j++)
        pyramid[i][j]=' ';
     
   }

   for(int i=0 ; i<height ; i++)
   {

   
      for(int j=0 ; j<height*2-1 ; j++)
         printf("%c",pyramid[i][j]);

    printf("\n");
   }




    return 0;
}