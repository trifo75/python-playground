'''
trying to build binary trees from lists
'''

class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
        if data <= self.data:
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insert(data)

        if data > self.data:
            if self.right == None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def print_tree(self):
        if self.left:
            self.left.print_tree()

        print(self.data)

        if self.right:
            self.right.print_tree()

    def treelevel(self):
        ldepth = 1
        rdepth = 1
        if self.left:
            print("traversing left - {}".format(self.left.data))
            ldepth += self.left.treelevel()

        if self.right:
            print("traversing right - {}".format(self.right.data))
            rdepth += self.right.treelevel()

        return max(ldepth,rdepth)


# This is the solution that has been turned in
# need to work on it as there are much faster ways 
# without recursion
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = list()
        if root.left:
            self.inorderTraversal(root.left)

        out.append(root.val)

        if root.right:
            self.inorderTraversal(root.right)

        return out
    



input = [12,5,8,2,33,18,32]

