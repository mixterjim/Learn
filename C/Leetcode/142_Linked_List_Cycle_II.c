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
struct ListNode *detectCycle(struct ListNode *head) {
    if (head == NULL){
		return NULL;
	}
    int i = 0;
    int cycle_len = 0;
    struct ListNode *slow = head;
    struct ListNode *fast = head->next;
    while (fast!=NULL && fast->next!=NULL) {
        if (slow == fast) {
			cycle_len = get_cycle_len(slow,fast);
            i = i - cycle_len;
            slow = head;
            while (i > 0) {
                slow = slow -> next;
                --i;
            }
            while (1) {
                fast = slow;
                for (i=0; i<cycle_len; ++i) {
                    fast = fast ->next;
                    if (slow == fast) {
                        return slow;
                    }
                }
                slow = slow -> next;
            }
        }
        ++i;
        slow = slow -> next	;
        fast= fast -> next -> next;
    }
    return NULL;
}

int get_cycle_len(struct ListNode *a,struct ListNode *b){
	int len = 0;
    do {
        ++len;
        b = b -> next;
    } while (a != b);
	return len;
}

/**
 * Unit Test
 */
int main() {
	# define k 5
    int i;
    int list[k] = {1,2,3,4,5};
    int pos = 3;
    ListNode *head = (ListNode*)malloc(sizeof(ListNode));
    ListNode *p = head;
    head -> data =list[0];
    ListNode *node = head;
    for (i=1; i<k; ++i) {
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
    } else {
    	node -> next = NULL;
	}
    p=detectCycle(head);
    pos = 0;
    while(head!=NULL) {
        if (head == p) {
            printf("tail connects to node index %d",pos);
            break;
        }
        ++pos;
        head = head -> next;
    }
    if (head==NULL) {
        printf("no cycle");
    }
    return 0;
}
