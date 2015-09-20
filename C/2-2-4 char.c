#include <stdio.h> 
int main() {
	int score = 0;
	char *rank;
	
	printf ("Achievement:");
	scanf("%d", &score);
	
	score /=10;
	//score = score/10
	
	switch (score) {
		
		case 9: {
			rank = "A";
			break;
		}
		case 8: {
			rank = "B";
			break;
		}
		case 7: {
			rank = "C";
			break;
		}
		default: {
			rank = "E";
		}
	}
	
	printf ("%s\n", rank); 
	
	return 0;
}
