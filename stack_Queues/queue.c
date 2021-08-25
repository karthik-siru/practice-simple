#include <stdio.h>
#include <stdlib.h>

struct queue
{

   int tail;
   int *a;
   int size;
   int head;
};

int isempty(struct queue *s)
{
   if (s->head == -1 || s->head == s->tail)
      return -1;

   else
      return 1;
}

void Dequeue(struct queue *s)
{
   if (isempty(s) == -1)
   {
      printf("-1\n");
      return;
   }

   else
   {

      printf("%d\n", s->a[s->head]);

      s->head = (s->head + 1) % s->size;

      return;
   }
}

void Enqueue(struct queue *s, int k)
{
   if (isfull(s) == -1)
   {
      return;
   }

   else
   {

      s->a[s->tail] = k;

      s->tail = (s->tail + 1) % (s->size);

      if (s->head == -1)
         s->head = s->tail - 1;

      return;
   }
}

int main()
{
   int n, m;
   char c;
   scanf("%d", &n);

   struct queue *s;

   s = (struct queue *)malloc(sizeof(struct queue));

   s->tail = 0;

   s->head = -1;

   s->size = n;

   s->a = (int *)malloc(n * sizeof(int));

   while (1)
   {
      scanf("%c", &c);

      switch (c)
      {
      case 'i':
         scanf("%d", &m);
         Enqueue(s, m);
         break;

      case 'd':
         Dequeue(s);
         break;

      case 'e':
         printf("%d\n", isempty(s));
         break;

      case 'f':
         printf("%d\n", isfull(s));
         break;

      case 't':
         exit(1);
      }
   }

   return 0;
}
