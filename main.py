# Definition for a binary tree node.
class Node:

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:

  def checkTreeBalance(self, node: Node, height=0):

    if node == None or self.isBalanced == False:
      return height

    leftHeight = self.checkTreeBalance(node.left, height + 1)
    rightHeight = self.checkTreeBalance(node.right, height + 1)

    print('left %d, right %d' % (leftHeight, rightHeight))

    if (abs(leftHeight - rightHeight) > 1):
      self.isBalanced = False

    return max(leftHeight, rightHeight)

  def isBalanced(self, node: Node) -> bool:
    self.isBalanced = True

    self.checkTreeBalance(node)

    return self.isBalanced


my = Solution()
t = Node(1, Node(2, Node(3, Node(4), Node(4)), Node(3)), Node(2))
t = Node(1, Node(2, Node(3), Node(3)), Node(2))
trueAns = False
ans = my.isBalanced(t)
print("ans", ans, ans == trueAns)

# Runtime: 44 ms, faster than 92.53% of Python3 online submissions for Balanced Binary Tree.
# Memory Usage: 19.2 MB, less than 41.13% of Python3 online submissions for Balanced Binary Tree.
