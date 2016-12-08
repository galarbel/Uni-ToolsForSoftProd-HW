#include <float.h>
#include <stdio.h>
#include <limits.h>

int gcd(int x, int y) 
{
  int gcd;
  
  while(x!=y)
  {
    if(x > y && ((y <= 0 && INT_MAX + y  >= x) || (y>0 && INT_MIN + y < x))){
	      	x -= y;
	}
    else if((x <= 0 && INT_MAX + x  >= y) || (x>0 && INT_MIN + x < y)){
 	    	y -= x;
  	}
  }

  return gcd;

}
