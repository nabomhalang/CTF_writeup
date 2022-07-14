#include <stdio.h>

int main() {
  int x = 0;
  printf("AAAAA%nBBBB\n", &x);
  printf("x : %d\n", x);
  printf("$4096c%n\n", 'C', &x);
  printf("x : %d\n", x);
}
