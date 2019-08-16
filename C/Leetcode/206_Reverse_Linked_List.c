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


struct ListNode* reverseList(struct ListNode* head) {
	if (head == NULL || head->next == NULL) {
		return head;
	}
	struct ListNode *p = reverseList(head->next);
	head->next->next = head;
	head->next = NULL;
	return p;
}

/**
* Unit Test
*/
int main() {
	#define k 5
	int list[k] = { 1,2,3,4,5 };
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
	head=reverseList(head);
	while (head != NULL) {
		printf("%d,",head->val);
		head = head->next;
	}
	printf("\n");
	system("pause");
	return 0;
}
