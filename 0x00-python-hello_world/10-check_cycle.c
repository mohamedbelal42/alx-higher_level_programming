#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if list is cyclic
 * @list: pointer to list to check
 * Return: 1 if true, 0 if false
 */

int check_cycle(listint_t *list)
{
	listint_t *s1 = list, *s2 = list;

	while (s2 && s2->next)
	{
		s1 = s1->next;
		s2 = s2->next->next;
		if (s1 == s2)
			return (1);
	}
	return (0);
}
