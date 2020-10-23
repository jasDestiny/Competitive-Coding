# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        parents=[root]
        while parents:
            children=[]
            prevNode=None
            for i in parents:
                if i.right is not None:
                    children.append(i.right)
                if i.left is not None:
                    children.append(i.left)
                i.next=prevNode
                prevNode=i
            parents=children
        return root
