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


struct ListNode* removeElements(struct ListNode* head, int val) {
	if (head == NULL) {
		return head;
	}
	struct ListNode *p = head;
	while (p->next != NULL) {
		if (p->next->val == val) {
			p->next = p->next->next;
			continue;
		}
		p = p->next;
	}
	if (head->val == val) {
		head = head->next;
	}
	return head;
}



/**
* Unit Test
*/
int main() {
	#define k 7
	int list[k] = { 1,2,6,3,4,5,6 };
	int val = 6;
	int i;
	ListNode *head = (ListNode*)malloc(sizeof(ListNode));
	ListNode *node;
	ListNode *p = head;
	for (i = 0; i < k; ++i) {
		node = (ListNode*)malloc(sizeof(ListNode));
		node->val = list[i];
		node->next = NULL;
		p->next = node;
		p = node;
	}
	head = head->next;
	head= removeElements(head,val);
	while (head != NULL) {
		printf("%d,",head->val);
		head = head->next;
	}
	printf("\n");
	system("pause");
	return 0;
}
