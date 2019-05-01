#include<stdio.h>

int findMaxConsecutiveOnes(int* nums, int numsSize){
    int i,j;
    int result=0;
    for (i=-1,j=0;j<numsSize;++j){
        if (nums[j]!=1){
            if(result<j-i-1){
                result = j-i-1;
            }
            i=j;
        }
    }
    if (nums[j-1]==1 && result<j-i-1){
        result = j-i-1;
    }
    return result;
}

int main(void) {
    int nums[6]={1,1,0,1,1,1};
    int numsSize = sizeof(nums)/sizeof(nums[0]);
    printf("%d",findMaxConsecutiveOnes(nums,numsSize));
    return 0;
}
