# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         hashmap = {}
#         substring=[]
#         for index in range(len(t)):
#             if t[index]  in hashmap:
#                 hashmap[t[index]] += 1
#             else :
#                 hashmap[t[index]] =1
#         check_need = len(t)
#         for i in range(len(s)):
#             check_have = 0
#             hash_second = hashmap.copy()
#             if s[i] in hash_second:
#
#                 for j in range(i,len(s)):
#                     if s[j] in hash_second:
#                         check_have = check_have + 1
#                         hash_second[s[j]] = hash_second[s[j]]-1
#                     if check_have == check_need:
#                     # if all(value <= 0 for value in hash_second.values()):
#                         substring.append(s[i:j + 1])
#                         break
#
#         if substring:
#             sorted_list = sorted(substring, key=len)
#             return sorted_list[0]
#         else:  return ""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        # solution1: O(1)
        hashmap_t, hashmap_s = {}, {}

        for i in (t):
            hashmap_t[i] = 1 + hashmap_t.get(i, 0)
        have, need = 0, len(hashmap_t)
        res, reslen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            char = s[r]
            hashmap_s[char] = 1 + hashmap_s.get(char, 0)

            if char in hashmap_t and hashmap_s[char] == hashmap_t[char]:
                have = have + 1
            while have == need:
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = r - l + 1
                # pop from left of our window
                hashmap_s[s[l]] = hashmap_s[s[l]] - 1
                if s[l] in hashmap_t and hashmap_s[s[l]] < hashmap_t[s[l]]:
                    have = have - 1
                l = l + 1
        l, r = res
        return s[l:r + 1] if reslen != float('infinity') else ""


s = Solution()
print(s.minWindow("ADOBECODEBANC","ABC"))