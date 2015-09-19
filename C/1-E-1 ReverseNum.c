#include <stdio.h>

main()
{
	int a,b,c,t;
	
	scanf("%d",&t);
	
	a = t/100;
	b = (t-a*100)/10*10;
	c = t%10*100;
	t = a+b+c;
	
	printf("%d",t);
	
	return 0;
}
