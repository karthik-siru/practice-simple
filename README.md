# Intresting-questions .. 


<b text-decoration = "underline">Sum Digits Until One</b>


We're provided a positive integer num. Can you write a method to repeatedly add all of its digits until the result has only one digit?

Here's an example: if the input was 49, we'd go through the following steps:

// start with 49
4 + 9 = 13

// move onto 13
1 + 3 = 4
We would then return 4.

Constraints

   * Input will be in the range between 0 and 1000000000
   * Expected time complexity : O(log n)
   * Expected space complexity : O(1)
   
   
<a href = "https://github.com/karthik-siru/practice-simple/blob/main/day11.py" > Solution </a>

______________________________________________________________________________________________________________

<b text-decoration = "underline"> DARLA-QUESTION </b>


A little girl  darla counts from 1 to 1000 using the fingers of her left hand as
follows. She starts by calling her thumb 1, the first finger 2, middle finger 3,
ring finger 4, and little finger 5. Then she reverses direction, calling the ring
finger 6, middle finger 7, the first finger 8, and her thumb 9, after which she
calls her first finger 10, and so on. If she continues to count in this manner,
on which finger will she stop?


<a href = "https://github.com/karthik-siru/practice-simple/blob/main/fingers_count.py" > Solution </a>

____________________________________________________________________________________________________________

<b text-decoration = "underline">CHECK-PALINDROME-LINKEDLIST</b>

Given a singly linked list node whose values are integers, determine whether the linked list forms a palindrome.

Constraints

    n ≤ 100,000 where n is the length of node

Example 1 
   
  input   --- node = [5, 3, 5]
  Output  --- True 


<a href = "https://github.com/karthik-siru/practice-simple/blob/main/palindrome_linked_list.py" > Solution </a>

_____________________________________________________________________________________________________________________________

<b text-decoration = "underline">RIGHT-ROTATE-LINKEDLIST-BY K PLACES</b>


Given a linked list node and a non-negative integer k, rotate the list to the right by k places.

Note: The linked list is guaranteed to have at least one element, and k is guaranteed to be less than or equal to the length of the list.

Constraints

    k ≤ n ≤ 100,000 where n is the number of nodes in node

Example 1

Input:

    node = [1, 2, 3, 4]
    k = 2

Output:

    [3, 4, 1, 2]

Example 2

Input:

    node = [1, 2, 3, 4]

    k = 4

Output:

    [1, 2, 3, 4]

Example 3
Input

    node = [1, 2, 3, 4]
    k = 0

Output

    [1, 2, 3, 4]
    
    
 <a href = "https://github.com/karthik-siru/practice-simple/blob/main/rotate_linked_list_by_k.py" > Solution </a>

____________________________________________________________________________________________________________________

<b text-decoration = "underline">Best-Time-to-Buy-and-Sell-Stock</b>
 
 
 
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
    
Example 2:

    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.
 
Constraints:

    1 <= prices.length <= 105
    0 <= prices[i] <= 104


<a href = "https://github.com/karthik-siru/practice-simple/blob/main/buy_and_sell_stocks.py" > Solution </a>

_______________________________________________________________________________________________________
