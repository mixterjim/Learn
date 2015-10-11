#include <stdio.h>

int main() {
	int n,m;
	int i;
	int xn = 1,x = 2 ;
	int sum = 0;

	scanf("%d %d", &n, &m);

	while (xn <= m) {
		int isPrime = 1;
		for ( i=2; i<x; i++ ) {
			if ( x % i == 0 ) {
				isPrime = 0;
				break;
			}
		}
		if ( isPrime == 1 ) {
			if (xn >=n&&xn <= m) {
				sum += x;
			}
			x++;
			xn++;
		} else {
			x++;
		}
	}
	printf("%d", sum);
	return 0;
}

