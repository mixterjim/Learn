#include <stdio.h>

main()
{
	int a = 1;
	int b = 2;
	int t;
	t = a;
	a = b;
	b = t;
	printf("a=%d,b=%d\n",a ,b);
	return 0;
}
