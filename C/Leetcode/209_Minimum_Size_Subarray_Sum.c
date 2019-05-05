# include <stdio.h>

int minSubArrayLen(int s, int* nums, int numsSize) {
    int i=0,j=0;
    int sum=0;
    int result=numsSize;
    int flag = 0;
    while ( result!=1 ) {
        if (sum >= s) {
            flag = 1;
            if (result >j-i) {
                result = j-i;
            }
            sum -= nums[i];
            ++i;
            continue;
        }
        if (j == numsSize) {
            break;
        }
        sum += nums[j];
        ++j;
    }
    if (flag==0) {
        return 0;
    }
    return result;
}



int main() {
    int s = 15;
    int nums[5]= {1,2,3,4,5};
    int numsSize=sizeof(nums)/sizeof(int);
    printf("%d",minSubArrayLen(s,nums,numsSize));
    return 0;
}
