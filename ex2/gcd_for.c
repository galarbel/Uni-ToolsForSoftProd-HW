int gcd(int x, int y) 
{
  int gcd;
  
  while(x!=y)
  {
    if(x > y)
      x -= y;
    else
      y -= x;
  }

  return gcd;

}
