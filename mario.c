#include <cs50.h>
#include <stdio.h>

void height(int h);

int main(void)

{
    int heightt;
    do
    {
        heightt = get_int("How tall do you want your pyramid to be: ");
    }
    while (heightt < 0 || heightt > 8);

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
