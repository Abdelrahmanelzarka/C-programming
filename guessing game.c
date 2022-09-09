#include<stdio.h>

int main ()
{
  int x=100,y,count=0;
  printf("guess a number between 1 and 1000\n");
  scanf("%d",&y);
  while(y!=x)
  {
    if(y>x)
      printf("lower number please\n");
    else if (y<x)
      printf("higher number please\n");

    count++;

  }
  printf("you guessed the number in %d attempts",count);



    return 0;
}