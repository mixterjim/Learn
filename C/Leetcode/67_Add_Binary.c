# include <stdio.h>
# include <stdlib.h>
# include <string.h>

char* addBinary(char* a, char* b) {
    int lenA=strlen(a);
    int lenB=strlen(b);
    int tmp=0;
    int lenMax;
    int i,j=1;
    if (lenA>lenB) {
        lenMax=lenA;
    } else {
        lenMax=lenB;
    }
    char *result = (char*)calloc(lenMax+2,sizeof(char));
//    string[n] = {'1','2','3'...'n-1','\0'}
    for (i=lenMax; i>=0 && lenA>0 && lenB>0; --i) {
    	tmp += *(a+(--lenA))-'0'+(*(b+(--lenB))-'0');
    	if(tmp>1){
    		result[i]=tmp-2+'0';
    		tmp=1;
		}else{
			result[i]=tmp+'0';
			tmp = 0;
		}
    }
    while(lenA>0){
    	if (tmp ==1 && *(a+(lenA-1))-'0'==1){
    		result[i--]=0 +'0';
    		--lenA;
		} else {
			result[i--]= *(a+(lenA-1))-'0'+tmp+'0';
			tmp = 0;
    		--lenA;
		}
	}
    while(lenB>0){
    	if (tmp ==1 && *(b+(lenB-1))-'0'==1){
    		result[i--]=0 +'0';
    		--lenB;
		} else {
			result[i--]= *(b+(lenB-1))-'0'+tmp+'0';
			tmp = 0;
			--lenB;
		} 
	}
    if(tmp){
    	result[i--]=tmp+'0';
	}
    return result+i+1;
}
int main() {
    char *a = "1011";
    char *b = "10";
    puts(addBinary(a,b));
}
