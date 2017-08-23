#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
	srand(time(0));
	int number = rand()%100+1;//get a number form 1~100
	int count = 0;
	int a = 0;

	printf("Guessing a number form 1~100.");
	do {
		printf("\nNumber:");
		scanf("%d", &a);
		count ++;
		if ( a > number ) {
			printf("More");
		} else if (a < number) {
			printf("Less");
		}
	} while (a != number);
	printf("Great,You Win!\nYou guess %d times.", count);

	return 0;
}

