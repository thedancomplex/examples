#include "example.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


double doMath(double x, double y)
{
  return x*y;
}
int doSum(double *z, double *x, double *y )
{
  for(int i = 0; i < 6; i ++)
  {
    z[i] = x[i]+y[i];
    printf("sum = %f\n",z[i]);
  }
  printf("addr z = %u\n", z);
  for(int i = 0; i < 6; i++)
  {
    printf("x = %f\n",x[i]);
    printf("y = %f\n",y[i]);
  }
  for(int i = 0; i < 20; i++)
  {
    printf("x then y = %f\n",x[i]);
  }

  return 0; 

}

int main()
{
  printf("example \n");
  printf("example %d \n", 42);
  printf("example %d \n", EXAMPLE_DEFINE);

  double x = 5;
  double y = 3;
  printf("math = %f * %f = %f\n", x,y, x*y);
  double z = doMath(x,y);
  printf("math = %f * %f = %f\n", x,y, z);
  double xx[] = {1,2,3,4,5,6};
  double zz[6]; 
  double yy[] = {11,22,33,44,55,66}; 
  printf("addr = %u\n", &xx);
  printf("addr = %u\n", &yy);
  if(doSum(&zz,&xx,&yy))
  {
    printf("***error****\n");
  }

  printf("addr zz = %u\n", &zz);
  for(int i = 0; i < 6; i++)
  {
    printf("zz = %f\n",zz[i]);
  }


  return 0;
}
