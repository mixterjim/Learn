# include <stdio.h>

int arrayPairSum(int* nums, int numsSize) {
    int i;
    int result = 0;
    int count = 0;
    // int *array=(int *)calloc(20001,sizeof(int));
    int array[20001] = {0};

    for (i = 0; i < numsSize; ++i) {
        ++array[nums[i] + 10000];
    }
    for (i=0; i < 20001 && count < numsSize;) {
        if (array[i] > 0) {
            if (count%2==0) {
                result += (i - 10000);
            }
            ++count;
            --array[i];
        } else {
            ++i;
        }
    }
    return result;
}

int main() {
    int numsSize=6;
    int nums[6]= {1722, -4601, 8127, 6065, 8049, 6962};
    printf("%d",arrayPairSum(nums,numsSize));
    return 0;
}
