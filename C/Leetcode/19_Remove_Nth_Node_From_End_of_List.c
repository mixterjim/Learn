# include <stdio.h>
# include <stdlib.h>

typedef struct ListNode {
	int data;
	struct ListNode *next;
} ListNode;


/**
* Definition for singly-linked list.
* struct ListNode {
*     int val;
*     struct ListNode *next;
* };
*/


struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
	int i;
	struct ListNode *slow = head;
	struct ListNode *fast = head;
	for (i = 0; i < n; ++i) {
		if (fast == NULL) {
			break;
		}
		fast = fast->next;
	}
	if (fast == NULL && i == n) {
		head = slow->next;
		free(slow);
	}
	while (fast != NULL) {
		fast = fast->next;
		if (fast == NULL) {
			fast = slow->next;
			slow->next = fast->next;
			free(fast);
			break;
		}
		slow = slow->next;
	}
	return head;
}



/**
* Unit Test
*/
int main() {
	# define k 5
	int i;
	int n = 4;
	int list[k] = { 1,2,3,4,5 };
	ListNode *head = (ListNode*)malloc(sizeof(ListNode));
	ListNode *p = head;
	ListNode *node = head;
	for (i = 0; i < k; ++i) {
		node = (ListNode*)malloc(sizeof(ListNode));
		node->data = list[i];
		node->next = NULL;
		p->next = node;
		p = node;
	}
	p = head;
	head = head->next; // remove head node；
	free(p);
	p = removeNthFromEnd(head,n);
	while (p != NULL) {
		printf("%d,",p->data);
		p = p->next;
	}
	printf("\n");
	system("pause");
	return 0;
}
