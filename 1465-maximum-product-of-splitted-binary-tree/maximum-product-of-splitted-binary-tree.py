class Solution:
    def maxProduct(self, root):
        mod = 10**9 + 7
        self.ans = 0
        def getSum(node):
            if not node:
                return 0
            return node.val + getSum(node.left) + getSum(node.right)
        total = getSum(root)
        def dfs(node):
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            self.ans = max(self.ans, s * (total - s))
            return s
        dfs(root)
        return self.ans % mod

        