#include <stdio.h>
#include <stdlib.h>
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findDiagonalOrder(int** matrix, int matrixRowSize, int matrixColSize, int* returnSize) {
	*returnSize=matrixRowSize*matrixColSize;
	int *result=(int*)calloc(*returnSize,sizeof(int));
	if(*returnSize==0) {
		return result;
	}
	/*-------------*/
	int i=0,j=0;
	int k=0;
	int seq = 1;//Positive:1, Reverse:-1

	if(matrixRowSize==1||matrixColSize==1) {
		for(i=0; i<matrixRowSize; ++i) {
			for(j=0; j<matrixColSize; ++j) {
				result[k++]=matrix[i][j];
			}
		}
		return result;
	}

	while(k<*returnSize-1) {
		result[k++]=matrix[i][j];
		if(i==matrixRowSize-1) {
			++j;
		} else if(j==matrixColSize-1) {
			++i;
		} else if(i==0) {
			++j;
		} else if(j==0) {
			++i;
		}
		if(seq==1&&(i!=matrixRowSize-1||j!=matrixColSize-1)) {
			do {
				result[k++]=matrix[i][j];
				++i;
				--j;
			} while(j!=0&&i!=matrixRowSize-1);
		} else if(seq==-1&&(i!=matrixRowSize-1||j!=matrixColSize-1)) {
			do {
				result[k++]=matrix[i][j];
				--i;
				++j;
			} while(i!=0&&j!=matrixColSize-1);
		}
		seq*=-1;
	}
	result[k]=matrix[i][j];
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
	int returnSize;
	int *result = findDiagonalOrder(matrix,n,n,&returnSize);
	printf("[");
	for (i=0; i<returnSize-1; ++i) {
		printf("%d,",result[i]);
	}
	printf("%d]",result[i]);
}
