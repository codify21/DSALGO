class Solution:
    def countSubstrings(self, s: str) -> int:

        count = 0
        for i in range(len(s)):
            count += self.countpal(s,i,i)
            count += self.countpal(s,i,i+1)

        return count

    def countpal(self,s,l,r):
        res=0
        while l>=0 and r<len(s):
            if s[l]==s[r]:
                res +=1
                l = l - 1
                r = r + 1
        return res

        res=[]
        count=0
        for i in range(len(s)):
            # res.append(s[i])
            count += 1
            for j in range(i+1,len(s)):
                rev =s[i:j+1][::-1]
                if s[i:j+1]==rev:
                    # res.append(s[i:j+1])
                    count += 1

        # return len(res)
        return count


s = Solution()
squares = s.countSubstrings("aaa")
print(squares)