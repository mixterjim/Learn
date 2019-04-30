# include <stdio.h>
# include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize){
    *returnSize = 2;
    int *result=(int *)calloc(*returnSize,sizeof(int));
    int i=0,j=numbersSize-1;
    int k;
    while (i<j){
    	k = numbers[i]+numbers[j];
    	if(k>target){
    		--j;
		} else if(k<target){
			++i;
		} else {
			result[0]=++i;
			result[1]=++j;
			return result;
		}
	}
	return result;
}

int main() {
	int numbers[4]={2,7,11,15};
	int numbersSize = 4;
	int target = 9;
	int *returnSize = malloc(sizeof(int));
	int *result = twoSum(numbers,numbersSize,target,returnSize);
	printf("%d,%d",result[0],result[1]);
}
