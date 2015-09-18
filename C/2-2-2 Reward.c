#include <stdio.h>
main(){
	const double RATE = 1000;
	const int STANDARD = 3;
	double pay = 0.0;
	int kills;
	
	printf("Input how many people you kild:");
	scanf("%d", &kills);
	printf("\n");
	if (kills > STANDARD)
		pay = STANDARD * RATE +(kills - STANDARD) * (RATE * 1.5);
	else
		if (kills == 0)
			printf("What are you doing?\n");
		else
			pay = kills * RATE;
	printf("You get %f $\n", pay);
	return 0;
}
