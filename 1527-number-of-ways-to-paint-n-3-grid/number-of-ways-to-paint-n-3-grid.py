class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Base case for n = 1
        abc = 6  # all different
        aba = 6  # first and third same
        
        for _ in range(2, n + 1):
            new_abc = (abc * 2 + aba * 2) % MOD
            new_aba = (abc * 2 + aba * 3) % MOD
            
            abc, aba = new_abc, new_aba
        
        return (abc + aba) % MOD

        