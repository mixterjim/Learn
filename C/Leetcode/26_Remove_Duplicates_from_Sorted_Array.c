# include <stdio.h>

int removeDuplicates(int* nums, int numsSize){
    int i,j;
    if(numsSize==0){
        return 0;
    }
    for(i=0,j=1;j<numsSize;++j){
        if(nums[i]!=nums[j]){
            ++i;
            nums[i]=nums[j];
        }
    }
    return i+1;
}

int main() {
    int nums[10]= {0,0,1,1,1,2,2,3,3,4};
    int numsSize = sizeof(nums)/sizeof(int);
    int i;
    numsSize=removeDuplicates(nums, numsSize);
    for (i=0;i<numsSize;++i){
    	printf("%d,",nums[i]);
	}
}
