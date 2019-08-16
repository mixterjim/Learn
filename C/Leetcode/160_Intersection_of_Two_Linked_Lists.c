#include <stdio.h>
#include <stdlib.h>

typedef struct ListNode {
	int val;
	struct ListNode *next;
}ListNode;

/**
* Definition for singly-linked list.
* struct ListNode {
*     int val;
*     struct ListNode *next;
* };
*/
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
	int i = 0;
	if (headA == NULL || headB == NULL) {
		goto end;
	}
	struct ListNode *A = headA;
	struct ListNode *B = headB;
	while (i<3) {
		if (A == B) {
			return A;
		}
		A = A->next;
		B = B->next;
		if (A == NULL) {
			A = headB;
			++i;
		}
		if (B == NULL) {
			B = headA;
			++i;
		}
	}
end:
	return NULL;
}

/**
* Unit Test
*/
int main() {
	#define A 5
	#define B 3
	int listA[A] = { 0,9,1,2,4 };
	int listB[B] = { 3,2,4 };
	int shipA = 3;
	int shipB = 1;
	int i;
	ListNode *headA = (ListNode*)malloc(sizeof(ListNode));
	ListNode *headB = (ListNode*)malloc(sizeof(ListNode));
	ListNode *node;
	ListNode *p;
	ListNode *q;
	p = headA;
	for (i = 0; i < A; ++i) {
		node = (ListNode*)malloc(sizeof(ListNode));
		node->val = listA[i];
		node->next = NULL;
		p->next = node;
		p = node;
	}
	q = headB;
	for (i = 0; i < B; ++i) {
		node = (ListNode*)malloc(sizeof(ListNode));
		node->val = listB[i];
		node->next = NULL;
		q->next = node;
		q = node;
	}
	p = headA;
	headA = headA->next;
	free(p);
	q = headB;
	headB = headB->next;
	free(q);
	p = headA;
	q = headB;
	for (i = 0; i < shipA; ++i) {
		p = p->next;
	}
	for (i = 0; i < shipB; ++i) {
		q = q->next;
	}
	q->next = p;
	node = getIntersectionNode(headA, headB);
	if (node == NULL) {
		printf("null\n");
	}
	else {
		printf("Reference of the node with value = %d\n", node->val);
	}
	system("pause");
	return 0;
}
