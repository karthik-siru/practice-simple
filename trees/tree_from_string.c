#include <stdio.h>
#include <stdlib.h>

struct node
{
    int key;
    struct node *left;
    struct node *right;
};

struct node *CREATE_NODE(int key)
{
    struct node *p = (struct node *)malloc(sizeof(struct node));
    p->left = NULL;
    p->right = NULL;

    return p;
}

struct node *BUILD_TREE(char *str)
{
    int key = 0;
    int temp = 0;

    if (*str == '(')
    {
        str += 2;
        // empty condition
        if (*str == ')')
        {
            return NULL;
        }
        // get the number
        while (*str >= '0' && *str <= '9')
        {
            key = key * 10 + (*str - 48);
            str++;
        }
        // create the node
        struct node *node = CREATE_NODE(key);

        str++;
        // reccur for the left tree
        node->left = BUILD_TREE(str);
        str++;

        temp = 1;
        // to get the right tree.(to bypass left subtrees )
        while (temp != 0)
        {
            if (*str == '(')
                temp++;
            if (*str == ')')
                temp--;
            str++;
        }

        str++;
        node->right = BUILD_TREE(str);

        return node;
    }
    return NULL;
}

int main()
{

    char s[100];

    scanf("%s", s);

    struct node *root = BUILD_TREE(s);

    return 0;
}
