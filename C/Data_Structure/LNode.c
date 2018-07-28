# include <stdio.h>
# include <malloc.h>
typedef struct LNode {
	int data;
	struct LNode *next;
} LNode;
void difference(LNode *A,LNode *B) {
	LNode *p=A->next,*q=B->next;
	LNode *pre=A;
	LNode *s;
	while(p!=NULL&&q!=NULL) {
		if(p->data<q->data) {
			pre=p;
			p=p->next;
		}
		else if(p->data>q->data) {
			q=q->next;
		}
		else if(p->data==q->data) {
			pre->next=p->next;
			free(p);
			p=pre->next;
//			s=p;
//			p=p->next;
//			free(s);
		}
	}
}
void creatLNode(LNode *A,int L[],int j) {
	int i;
	LNode *r=A;
	for(i=0; i<j; ++i) {
		LNode *tmp = (LNode*)malloc(sizeof(LNode));
		tmp->data = L[i];
		r->next = tmp;
		r=r->next;
	}
	r->next = NULL;
}
int main() {
	int j;
	LNode *r;
	LNode *A =(LNode*)malloc(sizeof(LNode));
	LNode *B =(LNode*)malloc(sizeof(LNode));
	/*List 1*/
	int L1[10]={1,2,3,4,5};
	j=sizeof(L1)/sizeof(L1[0]);
	creatLNode(A,L1,j);
	/*List 2*/
	int L2[10]={3,4,5,6,7};
	j=sizeof(L2)/sizeof(L2[0]);
	creatLNode(B,L2,j);
	difference(A,B);
	r=A->next;
	while(r!=NULL) {
		if (r->data==0){
			continue;
		}
		else{
			printf("%d",r->data);
			r=r->next;
		}
	}
}
