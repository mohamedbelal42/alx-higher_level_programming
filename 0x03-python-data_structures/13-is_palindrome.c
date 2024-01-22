#include "lists.h"

/**
 * is_palindrome - recursivve palind or not
 * @head: head list
 * Return: 1 if not palind, 0 if palind
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palind(head, *head));
}

/**
 * aux_palind - func to know if palindrom
 * @head: head list
 * @end: end list
 * Return: 1 if not palind, 0 if palind
 */

int aux_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
