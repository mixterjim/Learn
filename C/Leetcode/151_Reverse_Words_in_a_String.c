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
    int k=0;
    int start=0;
    reverse(0,len-1,s);
    for (i=0,j=0; j<len; ++j) {
        if (s[j]!=' ') {
            s[i]=s[j];
            ++i;
            k = 1;
        } else if (k == 1) {
            reverse(start,i-1,s);
            s[i] =' ';
            ++i;
            start = i;
            k = 0;
        }
    }

    if (i==0) {
        /* All spaces */
        return "";
    }

    if(s[--i]==' ') {
    	/* New strlen */
        s[i]='\0';
    } else {
        s[i+1]='\0';
        reverse(start,i,s);
    }
    return s;
}

int main() {
    char s[17]= {' ',' ','h','e','l','l','o',' ',' ','w','o','r','l','d','!',' ',' '};
    printf("%s#",reverseWords(s));
}
