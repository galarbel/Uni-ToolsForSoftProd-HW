int gcd(int x, int y) 
{
  int i, gcd;
  for(i=1; i < x && i < y; ++i)
  {
	if(x%i==0 && y%i==0){y
          gcd = i;
	}
  }

  return gcd;

}
