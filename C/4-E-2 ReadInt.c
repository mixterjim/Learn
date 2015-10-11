#include <stdio.h>

int main() {
	int x;
	scanf("%d", &x);
	
	if ( x < 0) {
		x *= -1;
		printf("Negative ");
	}

	int mask = 1;
	int t = x;
	while ( t > 9 ) {
		t /= 10;
		mask *= 10;
	}
	do {
		int d = x / mask;
		switch( d ) {
			case 1:
				printf("One");
				break;
			case 2:
				printf("Two");
				break;
			case 3:
				printf("Three");
				break;
			case 4:
				printf("Four");
				break;
			case 5:
				printf("Five");
				break;
			case 6:
				printf("Six");
				break;
			case 7:
				printf("Seven");
				break;
			case 8:
				printf("Eight");
				break;
			case 9:
				printf("Nine");
				break;
			case 0:
				printf("Zero");
				break;
		}
		if ( mask > 9 ) {
			printf(" ");
		}
		x %= mask;
		mask /= 10;
	} while ( mask > 0 );
	return 0;
}

