method Divide(x : nat, y : nat) returns (q : nat, r : nat)
requires y > 0;
ensures q * y + r == x && r >= 0 && r < y;
{ 
  q := 0;
  r := x;
  while (r >= y) {
    r := r - y;
    q := q + 1;
  }
}
