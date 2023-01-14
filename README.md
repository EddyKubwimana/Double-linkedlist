#Doubly_linkedList

A doubly linked list is a variation of a linked list in which each node has an additional pointer that points to the previous node in the list. This allows for both forward and backward traversal of the list(https://www.codecademy.com/learn/linear-data-structures-python/modules/doubly-linked-lists-python/cheatsheet).

Here's the algorithmic analysis of a doubly linked list:

#Time_Complexity:

Insertion at the beginning: O(1) - Since we have a pointer to the head node, we can simply update the head pointer and the next pointers of the new node and the current head node.
Insertion at the end: O(n) - We need to traverse the list to find the last node and update the next pointer of the last node and the previous pointer of the new node.

Insertion at a specific position: O(n) - We need to traverse the list to find the node before the desired position and update the next and previous pointers of the new node, the previous node, and the next node.

Deletion at the beginning: O(1) - Since we have a pointer to the head node, we can simply update the head pointer and the next pointers of the new head node.

Deletion at the end: O(n) - We need to traverse the list to find the last node and update the next pointer of the previous node.

Deletion at a specific position: O(n) - We need to traverse the list to find the node before the desired position and update the next and previous pointers of the previous node and the next node.

#Space_Complexity:

O(n) - where n is the number of elements in the list, since we need to allocate memory for each node in the list and for each additional pointer.

Note: These complexities are for an average case scenario, worst case scenario might be different.




