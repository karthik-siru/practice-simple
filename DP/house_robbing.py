class Solution:
    def rob(self, money_list: List[int]) -> int:
        n = len(money_list)

        if n < 3 :
            return max(money_list)

        prev_prev   = money_list[0]
        prev        = max(money_list[0] , money_list[1])

        res  =0 

        for i in range(2, n) :
            res  =  max(money_list[i]+prev_prev, prev)
            prev_prev = prev
            prev =  res 

        return res
