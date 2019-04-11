#include <stdio.h>
int pivotIndex(int* nums, int numsSize) {
	int left=0,right=0;
	int p =0;
	int i = 0;
	if (numsSize<2) {
		return -1;
	}
	for (i=1; i<numsSize; ++i) {
		right += nums[i];
	}
	while(left != right && p < numsSize-1) {
		left += nums[p];
		right -= nums[p+1];
		++p;
	}
	if (left==right) {
		return p;
	}
	return -1;
}
int main () {
//	int nums[0];
//	int nums[6] = {-1,-1,-1,-1,-1,0};
//	int nums[6] = {-1,-1,-1,-1,-1,-1};
	int nums[6] = {1, 7, 3, 6, 5, 6};
	printf("%d",pivotIndex(nums,6));
}
