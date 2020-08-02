#include <stdio.h>

void height(int h);

int main(void)

{
    int heightt;
    do
    {
        printf("How tall do you want your pyramid to be: ");
        scanf("%d", &heightt);
    }
    while (heightt < 1 || heightt > 8);

    height(heightt);
}

void height(int h)
{
    if (h == 0)
    {
        return;
    }

    height(h - 1);

    for (int j = 0; j < h; j++)
    {
        printf("#");
    }
    printf("\n");
}
