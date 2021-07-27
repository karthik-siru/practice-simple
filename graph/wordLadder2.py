'''
We don't actually have to construct the graph , for solving such questions ;)
 we can do it in this simple way . using bfs 

'''

import collections

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        
        idxs = collections.defaultdict(set)
        words = set(wordList)
		
        if endWord not in words:
            return 0

        for i in wordList:
            for idx, l in enumerate(i):
                idxs[idx].add(l)
        
        q = collections.deque()
        q.append((beginWord, 1))

        seen = set()
        seen.add(beginWord)
        
        while q:
            w, s = q.popleft()
            if w == endWord:
                return s
            for i in range(len(w)):
                for j in idxs[i]:
                    nw = w[:i] + j + w[i+1:]
                    if nw in words and nw not in seen:
                        q.append((nw, s + 1))
                        seen.add(nw)
        
        return 0