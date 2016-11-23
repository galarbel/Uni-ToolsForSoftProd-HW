int compute_quotient(int x, int y) 
{
	int quotient;
	if(y!=0)
	{
		quotient = x / y;
		return quotient;
	}
	printf("can't divide by zero");
  	return;
}
