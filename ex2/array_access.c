#include <math.h>
int access(int x, int y) 
{

  int i, flag;
  int a[32];

  while (x < y)
  {
    flag = 0;

    for(i = 2; i <= x/2; ++i)
    {
      if(x % i == 0)
      {
        flag = 1;
        break;
      }
    }

    if (flag == 0) 
      break;

    ++x;
  }

  if(x<32 && x>=0){
  	return a[x];
  }else{
	return;
  } 
 
}
