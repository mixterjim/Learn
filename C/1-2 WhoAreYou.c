#include <stdio.h>
int main ()
{
	const int Num = 47;	\\Num read-only
	int Name;
	
	printf("What's you Name?\n");
	scanf("%d", &Name);
	
	Name = Num;
	
	printf ("I know you,No.%d",Name);
	return 0;	
}

