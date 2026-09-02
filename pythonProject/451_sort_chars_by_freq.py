from collections import Counter
from typing import List

class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = Counter(s)
        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
            # Sorting the dictionary based on values in ascending order
        sorted_dict = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        # out = sorted(d.items(), key=lambda x: x[1], reverse=True)
        res = "".join(a[0]*a[1] for a in sorted_dict)


s = Solution()
strs = "eeaabcca"
reverse = s.frequencySort(strs)
print(reverse)