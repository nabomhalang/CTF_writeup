#include <stdio.h>
#define TRUE 1

int main() {
    int v1 = 0;
    int v3 = 8;
    do
    {
        printf("%d\n", v3);
        --v3;
    }
    while ( v3 );
    return 0;
}