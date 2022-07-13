// gcc -o gambling gambling.c
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
int win;


int gambling(){
	int money = 1000;
	int bat, luckynum;

	make_random();
	printf("[chall] gambling2\n");
	printf("Start Gambling!\n\n");

	while(money >= 0){
		printf("current your money : %d\n\n", money);
		printf("bat your money\n");
		printf("bat money : ");
		scanf("%d", &bat);
		if(bat < 0){
			bat = bat * (-1); // 
		}
		if(money - bat < 0){
			bat = bat % money; 
		}
		
		printf("choose lucky number : ");
		scanf("%d", &luckynum);
			
		printf("\nlucky number is %d\n", win);
		if(luckynum == win){ // 이곳은 못들어감
			printf("You Win! ");
			printf(" + %d money\n", bat);
			money += bat;
		} else{
			printf("You Lost! ");
			printf(" - %d money\n", bat);
			money -= bat;
		}
    	make_random();

		if(money > 10001){ // 이쪽으로 들어와야함
			printf("GOOD!!!\n");
			return 1;
		}
	}
	printf("BAD!\n");
	return 0;
}

int main(){
	setvbuf(stdin, 0, 2, 0);
	setvbuf(stdout, 0, 2, 0);
	printf("Gambling version2! Let's Hack The Chall\n");

	if(gambling()){
		printf("\n======================================\n");
		printf("Congratulation!\n");
		read_flag();
		printf("======================================\n\n");
	}

	return 0;
}
