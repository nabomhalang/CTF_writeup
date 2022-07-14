#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdint.h>

void setup(){
	setvbuf(stdout,0,2,0);
	setvbuf(stdin,0,2,0);
}

void shell(){
	system("/bin/sh");
}

void menu(){
	puts("====================");
	printf("Get Shell(%p)!\n",shell);
	puts("====================");
	printf("> ");
}

void hidden(){
	uint8_t buf[108];
	int32_t size;
	
	puts("===========");
	puts("Hidden Menu");
	puts("===========");

	printf("Size : ");
	scanf("%d",&size);

	printf("Content : ");
	read(0,buf,size);

	printf("[*] Your name : %s",buf);

	puts("Bye~");
}

void getname(){
	uint8_t buf[108];
	printf("Content : ");
	read(0,buf,sizeof(buf)-1);
	printf("[*] Your name : %s",buf);
	puts("Bye~");
}

int main(){
	int8_t size;
	int64_t val1;
	int64_t val2 = 0x31337;
	setup();
	menu();

	scanf("%lu",&val1);

	if(val1 + val2 < 0x1337)
		 hidden();
	else
		getname();

	return 0;
}