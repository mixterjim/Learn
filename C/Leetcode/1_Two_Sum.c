/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int i,j;
    int sub;
    int *find=(int*)calloc(2,sizeof(int));
    for(i=0;i<numsSize;++i){
        sub = target-nums[i];
        for (j=i+1;j<numsSize;++j){
            if (nums[j]==sub){
                find[0]=i;
                find[1]=j;
            }
        }
    }
    return find;
}
