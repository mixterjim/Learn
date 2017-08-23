#include <stdio.h>

int main() {
	const int size = 3;
	int board[size][size];
	int i,j;
	int numOfX;
	int numOfO;
	int result = -1;    //-1:Draw	, 1:X Win	0:O win
	
	//loading Matrix
	for ( i=0; i<size; i++ ) {
		for ( j=0; j<size; j++ ) {
			scanf("%d", &board[i][j]);
		}
	}
	
	//Check on-line
	for ( i=0; i<size && result == -1; i++ ) {
		numOfO = numOfX = 0;
		for ( j=0; j<size; j++ ) {
			if (board[i][j] == 1 ) {
				numOfX ++;
			} else {
				numOfO ++;
			}
		}
		if ( numOfO == size ) {
			result = 0;
		} else if ( numOfX == size ) {
			result = 1;
		}
	}
	
	//Check column
	if (result == -1) {
		for ( j=0; j<size && result == -1; j++ ) {
			numOfO = numOfX = 0;
			for ( i=0; i<size; i++ ) {
				if (board[i][j] == 1 ) {
					numOfX ++;
				} else {
					numOfO ++;
				}
			}
			if ( numOfO == size ) {
				result = 0;
			} else if ( numOfX == size ) {
				result = 1;
			}
		}
	}
	
	//Check Diagonal
	numOfO = numOfX =0;
	for ( i=0; i<size; i++ ) {
		if ( board[i][i] == 1 ) {
			numOfX ++;
		} else {
			numOfO ++;
		}
	}
	if (numOfO == size ) {
		result = 0;
	} else if ( numOfO == size ) {
		result = 0;
	} else if ( numOfX == size ) {
		result = 1;
	}
	numOfO = numOfX =0;
	for ( i=0; i<size; i++ ) {
		if ( board[i][size-i-1] == 1 ) {
			numOfX ++;
		} else {
			numOfO ++;
		}
	}
		if (numOfO == size ) {
		result = 0;
	} else if ( numOfO == size ) {
		result = 0;
	} else if ( numOfX == size ) {
		result = 1;
	}
	if (result == 1) {
	printf ("X Win!");
	} else if (result == 0) {
		printf ("O Win!");
	} else {
		printf ("Love and peace");
	}

	return 0;
}

