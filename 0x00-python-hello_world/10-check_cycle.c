#include "lists.h"
/**
  *check_cycle - checks if there is cycle in linked list
  *@list: A the list
  *Return: 0 if no cycle and 1 if cycle
  */

int check_cycle(listint_t *list)
{
	listint_t *temp, *temp2;

	temp = list->next;
	temp2 = list->next->next;
	while (list == NULL || list->next == NULL)
		return (0);
	while (temp && temp2 && temp2->next)
	{
		if (temp == temp2)
			return (1);
		temp = temp->next;
		temp2 = temp2->next->next;
	}

	return (0);
}
