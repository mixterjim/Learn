# include <stdio.h>
# include <stdlib.h>

void exchangenum(int *a,int *b) {
    *a^=*b;
    *b^=*a;
    *a^=*b;
}

void rotate(int* nums, int numsSize, int k) {
    int i,j;
    int n = k%numsSize;
    if (n==numsSize || n==0 ) {
        return;
    }
    for (i=0,j=numsSize-1; i<j; ++i,--j) {
        exchangenum(&nums[i],&nums[j]);
    }
    for (i=0,j=n-1; i<j; ++i,--j) {
        exchangenum(&nums[i],&nums[j]);
    }
    for (i=n,j=numsSize-1; i<j; ++i,--j) {
        exchangenum(&nums[i],&nums[j]);
    }
}

void rotate2(int* nums, int numsSize, int k) {
    int i,j;
    int n = k%numsSize;
    int *tmp = (int *)calloc(numsSize,sizeof(int));
    for (i=0; i<numsSize; ++i) {
        tmp[i]=nums[i];
    }
    for (i=0,j=n; i<numsSize; ++i) {
        nums[j]=tmp[i];
        if (j==numsSize-1) {
            j = 0;
        } else {
            ++j;
        }
    }
}

int main() {
    int i;
    int k = 4;
    int nums[3]= {1,2,3};
    int numsSize=sizeof(nums)/sizeof(int);
    rotate(nums, numsSize,k);
    for(i=0; i<numsSize; ++i) {
        printf("%d,",nums[i]);
    }
}
