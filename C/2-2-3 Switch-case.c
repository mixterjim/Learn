#include <stdio.h>
int main () {
	int type;
	
	scanf("%d", &type);
	
	switch( type ) {
		case 1:
			printf("Hi!");
			break;//Out switch 
		case 2:
			printf("Good moring!");
			break;//Out switch 
		case 3:
			printf("Good night!");
			break;//Out switch 
		case 4:
			printf("Good bye!");
			break;//Out switch 
		default:
			printf("WTF?");
	}
	
	return 0;
}
