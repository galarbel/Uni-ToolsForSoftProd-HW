int add_numbers(int x, int y) 
{
  int sumOfTwoNumbers, firstNumber, secondNumber;
  firstNumber = x;
  secondNumber = y;

	//handling overflow and underflow
	if((firstNumber > 0 && secondNumber > 2147483647 - firstNumber) || (firstNumber < 0 && secondNumber < -2147483648 - firstNumber)){
		return;
	}
	else{
	  sumOfTwoNumbers = firstNumber + secondNumber;
	  return sumOfTwoNumbers;
	}

}
