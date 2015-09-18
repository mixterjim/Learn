#include <stdio.h>
main(){
	//Initialization
	int price = 0;
	int bill = 0;
	//scanf prive and bill
	printf("Input price:");
	scanf("%d",&price);
	printf("input bill:",&bill);
	scanf("%d",&bill);
	//Calculation of change
	if (bill >= price){
		printf("Give you %d $\n",bill - price);
	} else {
		printf("Not enough");
	}
	return 0;
}
