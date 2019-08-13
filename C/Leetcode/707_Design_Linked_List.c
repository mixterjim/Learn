# include <stdio.h>
# include <stdlib.h>

typedef struct MyLinkedList {
    int data;
    struct MyLinkedList *next;
} MyLinkedList;


/** Initialize your data structure here. */

MyLinkedList* myLinkedListCreate() {
    MyLinkedList *A = (MyLinkedList*)malloc(sizeof(MyLinkedList));
    A -> data = 0;
    A -> next = NULL;
    return A;
}

/** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
int myLinkedListGet(MyLinkedList* obj, int index) {
    int i = 0;
    MyLinkedList *p = obj;
    if (index < 0) {
        return -1;
    }
    while (i <= index) {
        p = p -> next;
        if (p == NULL) {
            return -1;
        }
        ++i;
    }
    return p -> data;
}

/** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
void myLinkedListAddAtHead(MyLinkedList* obj, int val) {
    MyLinkedList *node = (MyLinkedList*)malloc(sizeof(MyLinkedList));
    node -> data = val;
    node -> next = obj -> next;
    obj -> next = node;
}

/** Append a node of value val to the last element of the linked list. */
void myLinkedListAddAtTail(MyLinkedList* obj, int val) {
    MyLinkedList *p = obj;
    MyLinkedList *node = (MyLinkedList*)malloc(sizeof(MyLinkedList));
    node -> data = val;
    node -> next = NULL;
    while (p -> next != NULL) {
        p = p -> next;
    }
    p -> next = node;
}

/** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
void myLinkedListAddAtIndex(MyLinkedList* obj, int index, int val) {
    int i = 0;
    MyLinkedList *p = obj;
    MyLinkedList *node = (MyLinkedList*)malloc(sizeof(MyLinkedList));
    node -> data = val;
    while (i < index) {
        p = p -> next;
        if (p == NULL) {
            return;
        }
        ++i;
    }
    node -> next = p -> next;
    p -> next = node;
}

/** Delete the index-th node in the linked list, if the index is valid. */
void myLinkedListDeleteAtIndex(MyLinkedList* obj, int index) {
    int i = 0;
    MyLinkedList *p = obj;
    MyLinkedList *q;
    if(index < 0 || p -> next == NULL) {
        return;
    }
    while (i < index) {
        p = p -> next;
        if (p -> next == NULL) {
            return;
        }
        ++i;
    }
    q = p -> next;
    p -> next = q -> next;
    free(q);
}

void myLinkedListFree(MyLinkedList* obj) {
    MyLinkedList *p;
    while (obj != NULL) {
        p = obj;
        obj = obj -> next;
        free(p);
    }
}

/**
 * Your MyLinkedList struct will be instantiated and called as such:
 * MyLinkedList* obj = myLinkedListCreate();
 * int param_1 = myLinkedListGet(obj, index);

 * myLinkedListAddAtHead(obj, val);

 * myLinkedListAddAtTail(obj, val);

 * myLinkedListAddAtIndex(obj, index, val);

 * myLinkedListDeleteAtIndex(obj, index);

 * myLinkedListFree(obj);
*/

int main() {
    MyLinkedList* obj = myLinkedListCreate();
    MyLinkedList* p =obj;
    myLinkedListAddAtHead(obj, 1);
    myLinkedListAddAtTail(obj, 3);
    myLinkedListAddAtIndex(obj, 1, 2);
    myLinkedListGet(obj, 1);
    myLinkedListDeleteAtIndex(obj, 1);
    myLinkedListGet(obj, 1);
    while (p!=NULL) {
        printf("%d,",p->data);
        p = p->next;
    }
    myLinkedListFree(obj);
    return 0;
}
