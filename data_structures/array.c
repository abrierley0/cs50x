// This code demonstrates how tedious dynamic memory
// allocation is when using arrays in C

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // Allocate memory
    // int list[3];
    int *list = malloc(3 * sizeof(int));

    if (list == NULL)
    {
        return 1;
    }

    // Temporary storage
    int *tmp = malloc(4 * sizeof(int));
    if (tmp == NULL)
    {
        free(list);
        return 1;
    }

    list[0] = 4;
    list[1] = 7;
    list[2] = 8;

    // Copy to new 
    for (int i = 0; i < 3; i++)
    {
        tmp[i] = list[i];
    }
    tmp[3] = 7;

    free(list);
    list = tmp;

    // Print new list
    for (int i = 0; i < 4; i++)
    {
        printf("%i\n", list[i]);
    }

    free(list);
    return 0;
}