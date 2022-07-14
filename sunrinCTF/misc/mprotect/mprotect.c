#include <stdio.h>
#include <sys/mman.h>
#include <stdlib.h>

int main() {
	void* ptr = mmap(0, 0x1000, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_ANONYMOUS | MAP_PRIVATE, -1, 0);
	printf("ptr : %p\n", ptr);

	int retval = mprotect(ptr, 0x1000, PROT_READ);
	if(!retval) puts("Sucess");
	else puts("fail");
	return 0;
}
