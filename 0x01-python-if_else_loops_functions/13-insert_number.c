#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - function that insert node in  ascending order
 * @head: the head of the linked list
 * @number: number to insert
 * Return: the adress of the head
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *tmp;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

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
	}

	return (*head);

}
