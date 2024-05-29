class Solution:
    def numSteps(self, s: str) -> int:
        a=int(s,2)
        k=0
        while a != 1:
            if a%2 != 0:
                a=a+1
                k+=1
            else:
                a//=2
                k=k+1
        return k

