from collections import deque

class Solution:
    def maxLevelSum(self, root):
        queue = deque([root])
        level = 1
        max_sum = float('-inf')
        answer = 1

        while queue:
            level_sum = 0
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                answer = level

            level += 1

        return answer
