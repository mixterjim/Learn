#include <stdio.h>
int main() {
	int UTC,BJT;
	int a=0,b=0,c=0,d=0;
	
	scanf("%d", &UTC);
	a = UTC/1000*1000;
	UTC = UTC - a;
	b = UTC/100*100;
	UTC = UTC - b;
	c = UTC/10*10;
	d = UTC - c;
	
	if ( a + b < 800 ) {
		a = a + 2000;
		b = b + 400;
	}
	
	BJT = a+b+c+d-800;
	
	printf("%d", BJT);
	
	return 0;
}
