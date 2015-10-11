#include <stdio.h>
int main() {
	int Num = 0;
	int i = 0;
	int Odd = 0;
	int Even = 0;
	
	while (Num != -1) {
		scanf("%d", &Num);
		i = Num % 2;
		if (i == 0){
			Even += 1;
		} else {
			Odd += 1;
		}
	}
	printf ("%d %d", Odd-1, Even);
	return 0;
}

