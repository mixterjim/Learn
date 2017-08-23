#include <stdio.h>
int main() {
	int x;
	scanf("%d", &x);
	
	int digit;
	int ret = 0;
	
	while ( x > 0 ) {
		digit = x%10;
		printf ("%d", digit);//output all number
		ret = ret*10 + digit;
		x /= 10;
	}
	printf("\n");
	printf ("%d", ret);//there is no 0
	return 0;
}

