#include <float.h>
#include <stdio.h>
#include <limits.h>
#include <math.h>
int putd(double x, double y) { }

void swap(double x, double y) 
{
  double x, y;
  if((!(x == +INFINITY) || !(y == +INFINITY)) && (!(x == -INFINITY) || !(y == -INFINITY))){
	  if((y <= 0 && FLT_MAX + y  >= x) || (y>0 && -FLT_MAX + y < x)){
		x = x - y;
	  }
	  else {return ;}
  }
  else {return ;}
  if((y >= 0 && FLT_MAX - y >= x) || (y<0 && -FLT_MAX - y <= x)){	
  	y = x + y;
	}
  else {return ;}
  if((!(x == +INFINITY) || !(y == +INFINITY)) && (!(x == -INFINITY) || !(y == -INFINITY))){
	  if((x <= 0 && FLT_MAX + x  >= y) || (x>0 && -FLT_MAX + x < y)){
		x = y - x;
	  }
	  else {return ;}
  }
  else {return ;}
  putd(x, y);
}
