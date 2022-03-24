# breath first search
# depth first search
## inorder LPR
## preorder PLR
## postorder LRP

import collections


class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def bfs(self):
        op = []
        queue = collections.deque()
        queue.append(self)
        while(len(queue)>0):
            cur = queue.popleft()
            op.append(cur.data)
            if(cur.left != None):
                queue.append(cur.left)
            if(cur.right != None):
                queue.append(cur.right)
        return op

    def dfs(self):
        op = []
        stack = [self]
        while(len(stack) > 0):
            cur = stack.pop()

            op.append(cur.data)
            if(cur.right!=None):
                stack.append(cur.right)
            if(cur.left!=None):
                stack.append(cur.left)
        return op

    def add_child(self, data):
        if data == self.data:
            return 
        
        if data<self.data:
            # add to the left
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            # add data to roght sub tree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)
    
                
    def inorderTraversal(self):
        ## inorder LPR
        elements = []
        
        # visiting left subtree
        if self.left:
            elements += self.left.inorderTraversal()
        
        # visiting self
        elements.append(self.data)

        # visiting right subtree
        if self.right:
            elements += self.right.inorderTraversal()

        return elements

    def preorderTraversal(self):
        ## preorder PLR
        elements = []

        # visiting self
        elements.append(self.data)

        # visiting left subtree
        if self.left:
            elements += self.left.preorderTraversal()

        # visiting right subtree
        if self.right:
            elements += self.right.preorderTraversal()

        return elements


    def postorderTraversal(self):
        ## postorder LRP
        elements = []

        # visiting left subtree
        if self.left:
            elements += self.left.postorderTraversal()

        # visiting right subtree
        if self.right:
            elements += self.right.postorderTraversal()

        # visiting self
        elements.append(self.data)

        return elements
    
    def search_elem(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            # val might be in left subtree
            if self.left:
                return self.left.search_elem(val)
            else:
                return False

        if val > self.data:
            # val might be in right subtree
            if self.right:
                return self.right.search_elem(val)
            else:
                return False
    
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data
    
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data
    
    def delete_node(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_node(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_node(val)
        else:
            if self.left is None and self.right is None:
                return None
            
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete_node(min_val)
        
        return self
    
    def delete_node_with_left(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_node(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_node(val)
        else:
            if self.left is None and self.right is None:
                return None
            
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete_node(max_val)
        
        return self



def buildTree(number):
    root = BinarySearchTree(number[0])

    for x in range(1, len(number)):
        root.add_child(number[x])

    return root

if __name__=="__main__":
    number = [17,4,1,20, 9, 23, 18, 34]

    tree = buildTree(number)
    print("In order traversal: ", tree.inorderTraversal())
    print("Pre order traversal: ", tree.preorderTraversal())
    print("Post order traversal: ", tree.postorderTraversal())

    print("Search Element: ", tree.search_elem(19))
    print(tree.find_min())
    print(tree.find_max())
    print("In order traversal before delete: ", tree.inorderTraversal())
    tree.delete_node(17)
    print("In order traversal before after: ", tree.inorderTraversal())

    # 18
    # 4   20
    #1 9 23 34
    print("print dfs: ", tree.dfs(), "\n")
    print("print bfs: ", tree.bfs(), "\n")



    #     def trav(self, node, alpha):
        # rootCloned = 0
        # if alpha == "L":
        #     rootCloned = node.left
        # if alpha == "R":
        #     rootCloned = node.right
        # if alpha=="GOT":
        #     rootCloned = node
        # return rootCloned