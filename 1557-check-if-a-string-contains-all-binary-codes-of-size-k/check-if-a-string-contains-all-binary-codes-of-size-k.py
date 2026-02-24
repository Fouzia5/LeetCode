class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        
        unique_sub = 1 << k   
        st = set()
        
        for i in range(k, len(s) + 1):
            sub = s[i - k:i]
            
            if sub not in st:
                st.add(sub)
                unique_sub -= 1
                
                if unique_sub == 0:
                    return True
        
        return False
        