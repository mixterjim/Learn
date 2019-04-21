#include <stdio.h>
#include <stdlib.h>
/**
 * Return an array of arrays.
 * The sizes of the arrays are returned as *columnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** generate(int numRows, int** columnSizes) {
    int i,j;
    int **matrix = (int **)calloc(numRows,sizeof(int*));
    *columnSizes = (int*)calloc(numRows,sizeof(int));
    for (i=0;i<numRows;++i) {
    	matrix[i] = (int *)calloc(i+1,sizeof(int));
        (*columnSizes)[i]=i+1;
        for (j=0;j<=i;++j) {
            if (j==0||j==i) {
                matrix[i][j]=1;
            } else {
                matrix[i][j]=matrix[i-1][j-1]+matrix[i-1][j];
            }
        }
    }
    return matrix;
}
int main() {
    int i,j;
    int n = 0;
    int** columnSizes=(int **)calloc(n,sizeof(int*));
    int **matrix = generate(n, columnSizes);
    for (i=0;i<n;++i){
        for(j=0;j<(*columnSizes)[i];++j){
            printf("%d,",matrix[i][j]);
        }
        printf("\n");
    }
}
