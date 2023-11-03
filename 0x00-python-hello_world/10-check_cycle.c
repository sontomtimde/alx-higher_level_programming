#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: pointer to the beginning of the node
 * Return: 1 if there is a cycle, 0 if no cycle
 */
int check_cycle(listint_t *list)
{
    listint_t *slow = list;  // Slow pointer moves one step at a time
    listint_t *fast = list;  // Fast pointer moves two steps at a time

    // Traverse the list using slow and fast pointers
    while (slow != NULL && fast != NULL && fast->next != NULL)
    {
        slow = slow->next;          // Move slow pointer one step
        fast = fast->next->next;    // Move fast pointer two steps

        // If slow and fast pointers meet, there is a cycle
        if (slow == fast)
            return (1);
    }

    // If fast pointer reaches the end of the list, there is no cycle
    return (0);
}
