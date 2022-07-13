#include <stdio.h>
#include <unistd.h>

int main() {
    int x = 0x12345678;
    int y = 0xdeadbeef;
    char buf[100];

    read(0, buf, sizeof(buf) -1);
    printf(buf);
    return 0;
}