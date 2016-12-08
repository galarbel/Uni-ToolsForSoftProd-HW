#include <stdio.h>
#include <limits.h>

int add_numbers(int firstNumber, int secondNumber) 
{
  int sumOfTwoNumbers;

  //handling overflow and underflow
  if((secondNumber >= 0 && INT_MAX - secondNumber >= firstNumber) || (secondNumber < 0 && INT_MIN - secondNumber <= firstNumber)){
  	sumOfTwoNumbers = firstNumber + secondNumber;
  	return sumOfTwoNumbers;
	}
  return ;
}


