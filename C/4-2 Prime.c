#include <stdio.h>

int main() {
	int x;

	scanf("%d", &x);

	int i;
	int isPrime = 1;
	for ( i=2; i<x; i++ ) {
		if ( x % i == 0 ) {
			isPrime = 0;
			break;
		}
	}
	if ( isPrime == 1 ) {
		printf("Prime\n");
	} else {
		printf("Not Prime\n");
	}

	return 0;
}

