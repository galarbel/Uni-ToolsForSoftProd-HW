#include <stdio.h>
#include <limits.h>

int reverse(int x) 
{
	int reversedNumber = 0, remainder;

	while(x != 0)
	{
		remainder = x%10;
		if(reversedNumber >= 0 && INT_MAX/10 > reversedNumber){
			reversedNumber = reversedNumber*10 + remainder;
 		}
		if(reversedNumber < 0 && INT_MIN/10 < reversedNumber){
			reversedNumber = reversedNumber*10 + remainder;
 		}
		x /= 10;
	}

	return reversedNumber;

}
