#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts node in sorted list
 * @h: address of head pointer
 * @num: number to insert
 * Return: inserted node
 */

listint_t *insert_node(listint_t **h, int num)
{
	listint_t *node = *h, *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);
	new->n = num;
	new->next = NULL;

	if (!node || new->n < node->n)
	{
		new->next = node;
		return (*h = new);
	}
	while (node)
	{
		if (!node->next || new->n < node->next->n)
		{
			new->next = node->next;
			node->next = new;
			return (node);
		}
		node = node->next;
	}
	return (NULL);
}
