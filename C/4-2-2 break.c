#include <stdio.h>

int main() {
	int x;
	int dime, quater, half;
	int exit = 0;
	
	scanf("%d", &x);
	for ( dime = 1; dime < x*10; dime++ ) {
		for ( quater = 1; quater < x*10/2.5; quater++ ) {
			for ( half = 1;half < x*10/5; half++ ) {
				if ( dime + quater*2.5 + half*5 == x*10 ) {
					printf("You can use %d Dime and %d Quater and %d half dollar to change %d Dollar\n", dime, quater, half, x);
					exit = 1;
					break;
				}
			}
			if ( exit == 1 ) break;
		}
		if ( exit ) break;
	}

	return 0;
}

