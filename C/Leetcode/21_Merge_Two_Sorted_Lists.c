#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

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


struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
	if (l1 == NULL) {
		return l2;
	}
	if (l2 == NULL) {
		return l1;
	}
	if (l1->val < l2->val) {
		l1->next = mergeTwoLists(l1->next, l2);
		return l1;
	}
	else {
		l2->next = mergeTwoLists(l1, l2->next);
		return l2;
	}
}



/**
* Unit Test
*/
int main() {
#define k 3
	int list1[k] = { 1,2,4 };
	int list2[k] = { 1,3,4 };
	int i;
	ListNode *head1 = (ListNode*)malloc(sizeof(ListNode));
	ListNode *head2 = (ListNode*)malloc(sizeof(ListNode));
	ListNode *node;
	ListNode *p = head1;
	for (i = 0; i < k; ++i) {
		node = (ListNode*)malloc(sizeof(ListNode));
		node->val = list1[i];
		node->next = NULL;
		p->next = node;
		p = node;
	}
	head1 = head1->next;
	p = head2;
	for (i = 0; i < k; ++i) {
		node = (ListNode*)malloc(sizeof(ListNode));
		node->val = list2[i];
		node->next = NULL;
		p->next = node;
		p = node;
	}
	head2 = head2->next;
	/*  Test  */
	p = mergeTwoLists(head1, head2);
	while (p != NULL) {
		printf("%d,",p->val);
		p = p->next;
	}
	printf("\n");
	return 0;
}
