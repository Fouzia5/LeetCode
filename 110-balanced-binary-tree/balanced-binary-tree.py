class Solution:
    def isBalanced(self, root):
        def height(node):
            if not node:
                return 0
            l = height(node.left)
            if l == -1:
                return -1
            r = height(node.right)
            if r == -1:
                return -1
            if abs(l - r) > 1:
                return -1
            return max(l, r) + 1
        return height(root) != -1
