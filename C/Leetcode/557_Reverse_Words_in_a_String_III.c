# include <stdio.h>
# include <string.h>

void exchange(char *a,char *b) {
    *a^=*b;
    *b^=*a;
    *a^=*b;
}

void reverse(int start,int end,char *s) {
    while (start<end) {
        exchange(&s[start],&s[end]);
        ++start;
        --end;
    }
}

char * reverseWords(char * s) {
    int len = strlen(s);    // Strlen is very slowly！
    if (len==0) {
        return "";
    }
    int i,j;
    for (i=0,j=0; j<=len; ++j) {
        if (s[j]== ' ' || s[j] == 0 ) {
            reverse(i,j-1,s);
            i = j+1;
        }
    }
    return s;
}

int main() {
    char s[12]= {'h','e','l','l','o',' ','w','o','r','l','d','!'};
    printf("%s#",reverseWords(s));
}
