#include <stdio.h>

int isPrime(int x);

int main() {
	int num;
	scanf("%d", &num);
	int ret = 0;
	int t;
	int m = 1;
	int n = num / 2;

	printf("%d=", num);

	while( isPrime(num) == 0) {
		if ( num % n == 0) {
			t = num/n;
			printf("%dx", t);
			ret = t + ret*10;
			m *= 10;
			num /= t;
			n = num / 2;
		} else {
			n--;
		}
	}
	printf("%d", num);

	return 0;
}

int isPrime(int x) {
	int i=1;
	int n;
	for ( n=2; n<x; n++) {
		if( x%n == 0 ) {
			i = 0;
			break;
		}
	}
	return i;
}

