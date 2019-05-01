#include<stdio.h>

int removeElement(int* nums, int numsSize, int val){
    int i,j;
    for(i=0,j=0;j<numsSize;++j){
        if (nums[j]!=val){
            nums[i++]=nums[j];
        }
    }
    return i;
}

int main(void) {
    int nums[3]={3,2,2,3};
    int numsSize = sizeof(nums)/sizeof(nums[0]);
    int val = 3;
    int n = removeElement(nums,numsSize,val);
    int i;
    for (i=0;i<n;++i){
        printf("%d,",numsSize);
    }
    return 0;
}
