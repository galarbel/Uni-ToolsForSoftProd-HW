_Bool nondet_bool();
_Bool LOCK = 0;

_Bool lock() {
  if(nondet_bool()) {
    LOCK=1;
    return 1; }

  return 0;
}

void unlock() {
  LOCK=0;
}

int main() {
  unsigned got_lock = 0;
  int times;

  while(times > 0) {
    if(lock()) {
      got_lock++;
      /* critical section */
    }

    if(got_lock!=0)
      unlock();

    got_lock--;
    times--;
} }
