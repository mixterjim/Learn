#include <stdio.h>
#include <stdlib.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* spiralOrder(int** matrix, int matrixRowSize, int matrixColSize) {
    int size=matrixRowSize*matrixColSize;
    int *result = (int*)calloc(size,sizeof(int));
    if(size==0) {
        return result;
    }
    int i=0,j=0;
    int n=0;
    int r = 1,s=0;
    result[n++]=matrix[i][j];
    while(n<size) {
        s=r/4;
        switch (r%4) {
            case 1:
                while(j<matrixColSize-1-s) {
                    ++j;
                    result[n++]=matrix[i][j];
                }
                break;
            case 2:
                while(i<matrixRowSize-1-s) {
                    ++i;
                    result[n++]=matrix[i][j];
                }
                break;
            case 3:
                while(j>s) {
                    --j;
                    result[n++]=matrix[i][j];
                }
                break;
            case 0:
                while(i>s) {
                    --i;
                    result[n++]=matrix[i][j];
                }
                break;
        }
        ++r;
    }
    return result;
}
int main() {
    int i,j,k=1;
    int n=3;
    int **matrix = (int **)malloc(n *sizeof(int *));
    for (i =0; i<n; ++i) {
        matrix[i] = (int *)malloc(n *sizeof(int));
    }
    for(i=0; i<n; ++i) {
        for (j=0; j<n; ++j) {
            matrix[i][j] = k++;
        }
    }
    int *result = spiralOrder(matrix,n,n);
    printf("[");
    for (i=0; i<n*n-1; ++i) {
        printf("%d,",result[i]);
    }
    printf("%d]",result[i]);
}
