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


struct ListNode* oddEvenList(struct ListNode* head) {
	if (!head) {
		return head;
	}
	struct ListNode *odd=head;
	struct ListNode *even_head=head->next;
	struct ListNode *even = even_head;
	while (odd->next != NULL&&even->next != NULL) {
		odd->next = even->next;
		odd = odd->next;
		even->next = odd->next;
		even = even->next;
	}
	odd->next = even_head;
	return head;
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
		p->next = node;#include <stdio.h>
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


struct ListNode* oddEvenList(struct ListNode* head) {
	if (!head) {
		return head;
	}
	struct ListNode *odd=head;
	struct ListNode *even_head=head->next;
	struct ListNode *even = even_head;
	while (odd->next != NULL&&even->next != NULL) {
		odd->next = even->next;
		odd = odd->next;
		even->next = odd->next;
		even = even->next;
	}
	odd->next = even_head;
	return head;
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
	head = oddEvenList(head);
	while (head != NULL) {
		printf("%d,", head->val);
		head = head->next;
	}
	printf("\n");
	system("pause");
	return 0;
}
		p = node;
	}
	head = head->next;
	head = oddEvenList(head);
	while (head != NULL) {
		printf("%d,", head->val);
		head = head->next;
	}
	printf("\n");
	system("pause");
	return 0;
}
