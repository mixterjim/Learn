# include <stdio.h>
# include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int* getRow(int rowIndex, int* returnSize) {
    *returnSize = rowIndex+1;
    int *result=(int *)malloc(*returnSize*sizeof(int));
    int i,j = *returnSize/2;;
    result[0]=1;
    if (*returnSize==1) {
        return result;
    }
    result[1]=*returnSize-1;
    for (i=2; i<j; ++i) {
        result[i] = (long long int)result[i-1]*(*returnSize-i)/i;
    }
    i = j-1;
    if (*returnSize%2!=0) {
        result[j] = (long long int)result[j-1]*(*returnSize-j)/j;
        ++j;
    }
    while (i>=0) {
        result[j] = result[i];
        ++j;
        --i;
    }
    return result;
}

int main() {
	
    int rowIndex = 33;
    int i;
    int *returnSize = &rowIndex;
    int *row = getRow(rowIndex,returnSize);
    for (i=0; i<*returnSize; ++i) {
        printf("%d,",row[i]);
    }
    return 0;
}
