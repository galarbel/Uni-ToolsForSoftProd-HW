int putd(double x, double y) { }

void swap(double x, double y) 
{
  double x, y;

  x = x - y;
  y = x + y;
  x = y - x;

  putd(x, y);
}
