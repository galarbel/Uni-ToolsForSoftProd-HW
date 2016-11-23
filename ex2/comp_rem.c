int compute_remainder(int x, int y) 
{
	int remainder;
	if(y!=0)
	{
		remainder = x % y;
		return remainder;
	}

	printf("can't divide by zero");
	return;
}
