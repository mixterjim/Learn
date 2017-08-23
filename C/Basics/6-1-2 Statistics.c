#include <stdio.h>

int main() {
	const int number = 10; //Array size
	int x;
	int count[number]; //Array
//	int count[10] = {0,};
	int i;
	
	for ( i=0; i<number; i++ ) { //Initialization
		count[i] = 0;
	}
	scanf("%d", &x);
	while ( x != -1 ) {
		if ( x >= 0 && x<=9 ) {
		count[x] ++; // Array Operation
		}
		scanf("%d", &x);
	}
	for ( i=0; i<number; i++ ) { // Output Array
		printf("%d:%d\n", i, count[i]);
	}
	return 0;
}

