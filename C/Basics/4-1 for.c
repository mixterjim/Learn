#include <stdio.h>
int main() {
	int n;
	scanf("%d", &n);

	int fact = 1;
	//int i = 1;
	int i = n;
	//for ( i=1; i<=n; i++ ) {
	for ( ; n > 1; n-- ) {
		//fact *= i;
		fact *= n;
	}
	//printf ("%d!=%d\n", n, fact);
	printf ("%d!=%d\n", i, fact);

	return 0;
}

