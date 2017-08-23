#include <stdio.h>
int main() {
	int a=10,b=5,c=6,d=15,e=55,f=8;
	
	printf("a++=%d\n", a++);
	a = 10;
	printf("++a=%d\n", ++a);

	a = b+=c++-d+--e/-f;
	//a = b + c+1-d+e/-f-1;
	printf("%d\n", a);
	
	return 0;
}

