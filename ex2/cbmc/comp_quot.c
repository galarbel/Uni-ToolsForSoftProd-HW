int compute_quotient(int x, int y) 
{
  int quotient;
	
  if(y!=0 && (x != -2147483648 || y != -1)){
		quotient = x / y;
		return quotient;
	}else{
		printf("can't divide by zero");
  		return;
	}
}
