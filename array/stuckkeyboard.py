# question :
"""
You are given two strings typed and target. You want to write target, 
but the keyboard is stuck so some characters may be written 1 or more times. 
Return whether it's possible that typed was meant to write target.
"""

# approach :
"""
->  Maintain two pointers, for each string , store the current and the next element, 
->  Check whether the i1 and curr are same 
->  Elif check the i1 with next 
->  Else .. return False 
"""


class Solution:
    def solve(self, typed, target):
        # base case :
        if not typed and not target:
            return True

        if not target:
            return False

        n, m = len(typed), len(target)

        if n < m:
            return False

        if typed[0] != target[0]:
            return False

        i1, i2 = 0, 1

        # length 1 case

        if m == 1:
            if len(set(typed)) == 1:
                return True
            else:
                return False

        curr = target[0]
        next = target[i2]

        while i1 < n:
            # when curr and next are equal
            if curr == next:

                i1 += 1
                if i1 >= n:
                    break
                # less no.of curr's in typed
                if typed[i1] != curr:
                    return False
                i2 += 1
                curr = next
                if i2 >= m:
                    break
                # update next
                next = target[i2]
                continue

            if typed[i1] == curr:
                i1 += 1
            elif typed[i1] == next:
                curr = next
                i2 += 1
                if i2 >= m:
                    break
                next = target[i2]
            else:
                return False
        if i2 < m:
            return False
        # move the i1 to the end.
        while i1 < n:
            if typed[i1] != curr:
                return False
            i1 += 1
        return True

