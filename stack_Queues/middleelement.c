#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
    struct Node *prev;
};

struct Doublell
{
    struct Node *head;
    struct Node *middle;
    struct Node *last;
    int count;
};

struct Node *CreateNode(int val)
{
    struct Node *p = (struct Node *)malloc(sizeof(struct Node));
    p->data = val;
    p->next = NULL;
    p->prev = NULL;
}

void addtoList(struct Doublell *dll, int val)
{
    if (!dll->last)
    {
        dll->head = CreateNode(val);
        dll->middle = dll->head;
        dll->last = dll->head;
        dll->count += 1;
    }
    else
    {
        dll->last->next = CreateNode(val);
        dll->last->next->prev = dll->last;
        dll->last = dll->last->next;
        dll->count += 1;

        if ((dll->count) % 2 == 0)
            dll->middle = dll->middle->next;
    }
}

struct Node *getMiddle(struct Doublell *dll)
{
    return dll->middle;
}

struct Node *deleteMiddle(struct Doublell *dll)
{
    struct Node *middle = dll->middle;
    if (dll->middle->prev)
    {
        struct Node *prev = dll->middle->prev;
        struct Node *next = dll->middle->next;
        prev->next = next;
        next->prev = prev;
        dll->count -= 1;
        if (dll->count % 2)
            dll->middle = prev;
        else
            dll->middle = next;
    }
    else
        dll->head = dll->last = dll->middle = NULL;
    return middle;
}

int main()
{

    int a[] = {1, 2, 3, 4, 5};

    struct Doublell *q = (struct Doublell *)malloc(sizeof(struct Doublell));
    q->head = NULL;
    q->middle = NULL;
    q->count = 0;
    q->last = NULL;

    struct Node *temp;

    for (int i = 0; i < 5; i++)
    {
        addtoList(q, a[i]);
        temp = getMiddle(q);
        printf("%d ", temp->data);
    }
    printf("\n");

    temp = deleteMiddle(q);
    printf("%d ", temp->data);
    temp = getMiddle(q);
    printf("%d ", temp->data);

    printf("\n");

    return 0;
}
