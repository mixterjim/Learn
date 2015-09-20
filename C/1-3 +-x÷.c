#include <stdio.h>
int main ()
{
	double foot;
	double inch;
	
	printf("Input you height:");
	scanf("%lf %lf", &foot, &inch);
	printf("height is %f meter.\n",((foot + inch / 12.0) * 0.3048));
	return 0;
}
