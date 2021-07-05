'''

You are given integers n and k. Given that n represents the number of games you will play, return the number of ways in which you win k or less games consecutively. Mod the result by 10 ** 9 + 7.

Constraints

n ≤ 10,000
k ≤ 10

'''


'''

Intuition
DP soln: let f(i, j)f(i,j) be the number of ways to get no more than k wins, on the ith game with j consecutive wins so far.
There are only two possibilities: on the next game, you lose resetting the consecutive win count to 0 OR on the next game you win incrementing the consecutive win count.

f(i,j) = f(i+1, 0) + f(i+1, j+1)f(i,j)=f(i+1,0)+f(i+1,j+1)

'''


class Solution:
    def solve(self, n, k):
        if k == 0:
            return 1

        if k >= n:
            return (2 ** n) % (10 ** 9 + 7)

        m = [0] * (k + 1)

        m[0] = 1
        m[1] = 1

        m = deque(m)

        for i in range(1, n):
            prev = sum(m) % (10 ** 9 + 7)

            m.appendleft(prev)
            m.pop()

        return sum(m) % (10 ** 9 + 7)
