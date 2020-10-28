# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def rightSiblingTree(root):
	parent=[root]
	while parent:
		children=[]
		nextNode=None
		for i in parent:
			if i!=None:
				children.append(i.right)
				children.append(i.left)
				i.right=nextNode
			nextNode=i
		parent=children.copy()
	return root
