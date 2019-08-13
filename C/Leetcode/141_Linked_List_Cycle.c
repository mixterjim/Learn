# include <stdio.h>
# include <stdlib.h>
# include <stdbool.h>
# define k 5

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
bool hasCycle(struct ListNode *head) {
    struct ListNode *p = head;
    while (p != NULL && p -> next != NULL) {
        head = head -> next;
        p = p -> next -> next;
        if (head == p) {
            return 1;
        }
    }
    return 0;
}
int main() {
    int i;
    int list[k] = {1,2,3};
    int pos = 1;
    ListNode *head = (ListNode*)malloc(sizeof(ListNode));
    ListNode *p = head;
    ListNode *node;
    for (i=0; i<k; ++i) {
    	node = (ListNode*)malloc(sizeof(ListNode));
        node -> data = list[i];
        node -> next =NULL;
        p -> next = node;
        p = node;
    }
    if (pos != -1) {
        p = head;
        while (pos > 0) {
            --pos;
            p = p -> next;
        }
        node -> next = p;
    }
    printf("%d\n",hasCycle(head));
    return 0;
}
