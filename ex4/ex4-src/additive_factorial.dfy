function Factorial(n: nat): nat
{
  if n == 0 then 1 else n * Factorial(n-1)
}
 
method AdditiveFactorial(n: nat) returns (u: nat)
  ensures u == Factorial(n);
{
  u := 1;
  var r := 0;
  while (r < n) {
    var v := u;
    var s := 1;
    while (s <= r) {
      u := u + v;
      s := s + 1;
    }
    r := r + 1;
  }
}
