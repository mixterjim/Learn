# include <stdio.h>

void moveZeroes(int* nums, int numsSize){
    int i;
    int j=0;
    while (j<numsSize && nums[j]!=0){
        ++j;
    }
    for(i=j,j+=1;j<numsSize;++j){
        if (nums[j]!=0){
            nums[i]=nums[j];
            nums[j]=0;
            ++i;
        }
    }
}

int main() {
    int nums[5]= {0,1,0,3,12};
    int numsSize = sizeof(nums)/sizeof(int);
    int i;
    moveZeroes(nums, numsSize);
    for (i=0;i<numsSize;++i){
    	printf("%d,",nums[i]);
	}
}
