#include <unistd.h>

void  ft_putchar(char c)
{
  write(1, &c, 1);
}

void  ft_putstr(char *str)
{
  int count = 0;
  while (str[count])
  {
    ft_putchar(str[count]);
    count++;
  }
}

int main(void)
{
  ft_putstr("Hello World!\n");
  return 0;
}
