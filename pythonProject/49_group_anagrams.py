# https://www.youtube.com/watch?v=vzdNOK2oB2E

# complexity - O(m.n.26) which reduces to O(m.n)
# where m is length of list and n is average length of each string in list
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result={} #or result = defaultdict(list) then you dont have to use if else statement
        for i in strs:
            key = [0] * 26
            for c in i:
                key[ord(c) - ord('a')] += 1
            if tuple(key) in result:
                result[tuple(key)].append(i)
            else:
                result[tuple(key)] = [i]
        return(result.values())

        # anagram_map = defaultdict(list)
        #
        # for s in strs:
        #     key = [0] * 26
        #     for c in s:
        #         index = ord(c) - ord("a")
        #         key[index] += 1
        #     anagram_map[tuple(key)].append(s)
        #
        # return anagram_map.values()

        d = {}
        for s in strs:
            sor = ''.join(sorted(s))
            if sor in d:
                d[sor].append(s)
            else:
                d[sor] = [s]
        ans = list(d.values())
        return ans

s = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
reverse = s.groupAnagrams(strs)
print(reverse)