# include <stdio.h>
# include <stdlib.h>
# include <string.h>

void getnext(char* needle,int* next) {
    int i=0,j=-1;
    next[0]=-1;
    while(i<strlen(needle)-1) {
        if (j==-1 || needle[i]==needle[j]) {
            // next[++i]=++j; 
            /********* optimization *********/
            ++i;
            ++j;
            if (needle[i]!=needle[j]){
                next[i]=j;
            } else {
                next[i]=next[j];
            }
            /********* End *********/
        } else {
            j=next[j];
        }
    }
}
int strStr_KMP(char* haystack, char* needle) {
    /* KMP */
    int lenH=strlen(haystack); //strlen not return "int", unsigned integer!!! "-1" > 2
    int lenN=strlen(needle);
    if(lenN==0) {
        return 0;
    }
    int i=0,j=0;
    int next[lenN];
    getnext(needle, next);
    while(i<lenH && j<lenN) {
        if(j==-1||haystack[i]==needle[j]) {
            ++i;
            ++j;
        } else {
            j=next[j];
        }
    }
    if(j==lenN) {
        return i-j;
    } else {
        return -1;
    }
}

int strStr(char* haystack, char* needle) {
    int i,j;
    int lenH=strlen(haystack);
    int lenN=strlen(needle);
    if (lenN==0){
        return 0;
    }
    for (i=0;i<lenH-lenN+1;++i){
        for (j=0;j<lenN;++j){
            if (haystack[i+j]!=needle[j]){
                break;
            }
        }
        if(j==lenN) {
            return i;
        }
    }
    return -1;
}

int main() {
    char *haystack="ababcaababcaabc";
    char *needle="ababcaabc";
    printf("%d",strStr(haystack, needle));
}
