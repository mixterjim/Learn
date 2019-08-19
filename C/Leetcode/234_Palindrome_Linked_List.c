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


struct ListNode* reverseList(struct ListNode* head) {
	if (head == NULL || head->next == NULL) {
		return head;
	}
	struct ListNode *p = reverseList(head->next);
	head->next->next = head;
	head->next = NULL;
	return p;
}

bool isPalindrome(struct ListNode* head) {
	if (head == NULL || head->next == NULL) {
		return true;
	}
	struct ListNode *slow = head;
	struct ListNode *fast = head->next;
	while (fast != NULL&&fast->next != NULL) {
		slow = slow->next;
		fast = fast->next->next;
	}
	fast = reverseList(slow->next);
	slow = head;
	while (fast != NULL) {
		if (slow->val != fast->val) {
			return false;
		}
		slow = slow->next;
		fast = fast->next;
	}
	return true;
}

/**
* Unit Test
*/
int main() {
#define k 2
	int list[k] = { 1,1 };
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
	/*  Test  */
	if (isPalindrome(head)) {
		printf("true");
	}
	else {
		printf("false");
	}
	printf("\n");
	return 0;
}
