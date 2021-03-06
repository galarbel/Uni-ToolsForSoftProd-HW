method Bitwise_add(a0 : int, b0 : int) returns (c : int)
requires a0 >= 0 && b0 >= 0;
ensures c == a0+b0;
{
  c := 0;  
  var a, b, g, m := a0, b0, 1, 0;
  while (a > 0 || b > 0) 
  decreases a
  decreases b
  invariant c == a0 + b0 - g*(a+b+m)
  {
    m := m + a % 2 + b % 2;
    a := a / 2;
    b := b / 2;
    c := c + g * (m % 2);
    g := 2 * g;
    m := m / 2;
  }
  c := c + g * m;
}
