# include <stdio.h>

void reverseString(char* s, int sSize) {
    int i=0,j=sSize-1;
    int tmp;
    while (i<j) {
        tmp = s[i];
        s[i] = s[j];
        s[j] = tmp;
        ++i;
        --j;
    }
}

int main() {
    int i;
    int sSize=5;
    char s[5]="hello";
    reverseString(s, sSize);
    for (i=0; i<sSize; ++i) {
        printf("%c",s[i]);
    }
    return 0;
}
