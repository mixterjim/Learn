#include <stdio.h>

int main() {
	int n,m;
	scanf("%d %d", &n, &m) ;
	int i;

	for( i=n; i<=m; i++ ) {
		int k;
		int perfect = 0;
		for ( k=i/2; k>0; k-- ) {
			if ( i%k == 0 ) {
				perfect += k;
			}
			if ( perfect == i ) {
				printf("%d", perfect);
			}
		}
	}
	return 0;
}


