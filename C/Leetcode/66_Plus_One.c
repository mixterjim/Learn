#include <stdio.h>
#include <stdlib.h>
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize) {
	int p;
	int *digits_new;
	for(p=digitsSize-1; p>=0&&digits[p]==9; --p) { 
	// reversal "digits[p]&&p>=0" will be heap-buffer-overflow
		digits[p]=0;
	}
	if (p<0) {
		*returnSize = digitsSize+1;
		digits_new = (int *)malloc(sizeof(int)**returnSize);
		digits_new[0]=1;
		for(p=1; p<*returnSize; ++p) {
			digits_new[p]=0;
		}
	} else {
		digits[p]+=1;
		*returnSize = digitsSize;
		digits_new = digits;
	}
	return digits_new;
}

int main () {
	int digitsSize = 3;
	int digits[3] = {9,9,9};
	int returnSize;
	int p;
	int *digits_new=plusOne(digits,digitsSize,&returnSize);
	printf("[");
	for(p=0; p<returnSize; ++p) {
		printf("%d",digits_new[p]);
		if(p!=returnSize-1) {
			printf(",");
		}
	}
	printf("]");
}
