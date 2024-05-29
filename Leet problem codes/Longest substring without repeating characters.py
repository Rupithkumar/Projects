class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        charset=set()
        left=0
        max_length=0
        for x in range(n):
            if s[x] not in charset:
                charset.add(s[x])
                max_length=max(max_length,x-left+1)
            else:
                while s[x] in charset:
                    charset.remove(s[left])
                    left+=1
                charset.add(s[x])

        return max_length