method find(a : array<int>, key : int) returns (index : int)
  requires a != null;
  ensures 0 <= index <= a.Length;
  ensures index < a.Length ==> a[index] == key;
{
  index := 0;
  while (index < a.Length && a[index] != key)
  invariant 0 <= index <= a.Length
  invariant forall k :: 0 <= k < index ==> a[k] != key
  {
    index := index + 1;
  }
}
