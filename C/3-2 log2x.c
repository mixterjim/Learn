#include <stdio.h>

int main() {
	int x;
	int ret = 0;

//	scanf("%d", &x);
	x = 128;
	int t = x;
	while ( x > 1 ) {
		x /= 2;
		ret ++;
	}
	printf("Log2 of %d is %d.", t, ret);

	return 0;
}
