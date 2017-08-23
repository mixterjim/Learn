#include <stdio.h>

int main() {
	int x;
	int digit;
	int result = 0;
	int i = 0;
	double k = 0.5;
	scanf("%d", &x);//input a number
	
	while ( x>0 ) {
		digit = x%10%2;//get end of x's Odd(1)-even(0)
		x /= 10;//remove end of x
		i++;//get the No.
		k *= 2;
		if ( i%2==digit ) {
			result = result + k;
		}
	}
	printf("%d", result);
	
	return 0;
}

