#include <limits.h>
#include <float.h>
#include <math.h>


int putd(double x, double y) { return 1; }

void swap(double x, double y) 
{
  //double x, y;

if(isinf(x) || isinf(y) || x != x || y != y){
	return -1;
}

if(isinf(x) || isinf(y) || x<=DBL_MIN+y || y<=DBL_MIN+x || isinf(x-y)){
	return -1;
}else{
  x = x - y;
}

if(isinf(x) || isinf(y) || x>=DBL_MAX-y || y>=DBL_MAX-x || isinf(x+y)){
	return -1;
}else{
  y = x + y;
}

if(isinf(x) || isinf(y) || y<=DBL_MIN+x || x<=DBL_MIN+y || isinf(y-x)){
	return -1;
}else{
  x = y - x;
}

  putd(x, y);
}
