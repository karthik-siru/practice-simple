#include <stdio.h>
#include <stdlib.h>

struct stack
{

   int top;
   int *a;
   int size;
};

int isempty(struct stack *s)
{
   if (s->top == -1)
      return -1;

   else
      return 1;
}

int isfull(struct stack *s)
{
   if (s->top == s->size - 1)
      return -1;

   else
      return 1;
}

void Pop(struct stack *s)
{
   if (isempty(s) == -1)
   {
      printf("-1\n");
      return;
   }
   else
   {
      s->top = s->top - 1;
      printf("%d\n", s->a[s->top + 1]);
      return;
   }
}

void Push(struct stack *s, int k)
{
   if (isfull(s) == -1)
   {
      return;
   }

   else
   {
      s->top = s->top + 1;
      s->a[s->top] = k;
      return;
   }
}

int main()
{
   int n, m;
   char c;
   scanf("%d", &n);

   struct stack *s;

   s = (struct stack *)malloc(sizeof(struct stack));

   s->top = -1;

   s->size = n;

   s->a = (int *)malloc(n * sizeof(int));

   while (1)
   {
      scanf("%c", &c);

      switch (c)
      {
      case 'i':
         scanf("%d", &m);
         Push(s, m);
         break;

      case 'd':
         Pop(s);
         break;

      case 'e':
         printf("%d\n", isempty(s));
         break;

      case 't':
         exit(1);
      }
   }

   return 0;
}
