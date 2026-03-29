class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        s1=list(s1)
        s2=list(s2)
        for i in range(len(s1)):
            for j in range(len(s2)):
                if j-i==2:         
                        if s1[i]==s2[i]:
                            pass
                        else:
                            t=s1[i]
                            s1[i]=s1[j]
                            s1[j]=t
        if s1==s2:
            return True
        return False