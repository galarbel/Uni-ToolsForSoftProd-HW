method Product (m: nat, n: nat) returns (res:nat)
  ensures res == m * n;
{
  var m1: nat := m; res := 0;
  while (m1 != 0) 
  invariant m1 >= 0
  invariant res == m*n - m1*n
  {
     var n1: nat := n;
     while (n1 != 0) 
	 invariant n1 >= 0
	 invariant res == (m-m1+1)*n - n1 {
       res := res + 1;
       n1 := n1 - 1;
     }
     m1 := m1 - 1;
  }
}
