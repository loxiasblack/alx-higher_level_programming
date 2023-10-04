#include "lists.h"
/**
 * check_cycle - check if the linked list
 * has a cycle
 * @list: node to search in
 * Return: 1 or 0
*/
int check_cycle(listint_t *list)
{
	listint_t *head;

	head = list;
	while (list->next != NULL)
	{
		if (list->next == head)
		{
			return (1);
		}
		list = list->next;
	}
	return (0);
}
