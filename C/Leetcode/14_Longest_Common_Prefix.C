# include <stdio.h>
# include <stdlib.h>
# include <string.h>

char * longestCommonPrefix(char ** strs, int strsSize) {
    switch(strsSize) {
        case 0: {
            return "";
        }
        case 1: {
            return strs[0];
        }
    }
    int i,j;
    int min=strlen(strs[0]);
    int max=strlen(strs[0]);
    for(i=1; i<strsSize; ++i) {
        if (strlen(strs[i])<min) {
            min = strlen(strs[i]);
        } else if (strlen(strs[i])>max) {
            max = strlen(strs[i]);
        }
    }
    char * result = (char*)calloc(max+1,sizeof(char)); // The last one is "0".
    
    for (i=0; i<min; ++i) {
        for(j=0; j<strsSize-1; ++j) {
            if(strs[j][i]!=strs[j+1][i]) {
                return result;
            }
        }
        result[i]=strs[0][i];
    }
    return result;
}


int main() {
    int strsSize=3;
    char *strs[3]={"flower","flow","flight"};
    printf(longestCommonPrefix(strs, strsSize));
}
