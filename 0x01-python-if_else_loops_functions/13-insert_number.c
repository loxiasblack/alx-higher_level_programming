#include "lists.h"
#include <stdlib.h>
listint_t *add_nodeint_first(listint_t **head , const int n);
/**
 * insert_node - function that insert node in  ascending order
 * @head: the head of the linked list
 * @number: number to insert
 * Return: the adress of head
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *tmp = NULL;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (current->n > new->n)
		*head = new, new->next = current;
	if (*head == NULL)
		*head = new;
	else
	{
		tmp = NULL;
		while (current->next != NULL)
		{
			if (current->n < new->n && current->next->n > new->n)
			{
				tmp = current->next;
				current->next = new;
				new->next = tmp;
			}
			current = current->next;
		}
		if (current->n < new->n)
			add_nodeint_end(head, new->n);
	}
	return (*head);
}

