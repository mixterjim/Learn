#include <stdio.h>

void sum(int ,int );

int main() {
	sum(1,10);
	sum(20,30);
	sum(35,45);
	return 0;
}

void sum(int x,int y) {
	int i;
	int sum;
	for ( i=x,sum=0; i<=y; i++ ) {
		sum += i;
	}
	printf("%d to %d sum is %d\n", x, y, sum);
}
