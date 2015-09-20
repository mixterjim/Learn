#include <stdio.h>
main()
{
	int hour1, min1;
	int hour2,min2;

	scanf("%d %d", &hour1,&min1);
	scanf("%d %d", &hour2,&min2);

	int ih = hour2 - hour1;
	int im = min2 - min1;
	if (im < 0)
		{
			im = 60 + im;
			ih --;
		}

	printf ("There are have %d hours %d minutes.", ih, im);

	return 0;
}
