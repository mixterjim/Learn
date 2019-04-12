#include <stdio.h>
int dominantIndex(int* nums, int numsSize) {
    int p = 0,k=0;
	int max = 0,sec = 0,tmp = 0;
	while (p<numsSize){
		if(nums[p]>sec){
			sec = nums[p];
			if(max<sec){
				tmp = max;
				max = sec;
				sec = tmp;
				k=p;
			}
		}
		++p;
	}
	if(max>=2*sec){
		return k;
	}
	return -1;
}
int main () {
	int nums[4]={0,0,1,2};
	printf("%d",dominantIndex(nums,4));
}
