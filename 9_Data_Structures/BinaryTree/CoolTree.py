''' 
MIT License

Copyright (c) 2023 Khar Woh Leong

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
    def __repr__(self):
        return f"<{self.key}:{self.value}>"

    def __gt__(self, n):
        if self.key > n.key:
            return True
        else:
            return False

    def __lt__(self, n):
        if self.key < n.key:
            return True
        else:
            return False

    def __eq__(self, n):
        if self.key == n.key:
            return True
        else:
            return False

## The ultimate tree class :)
class Tree: ## Wrapper Class
    def __init__(self):
        self.root = None
    
    def insert(self, data): ## data should be a Node object
        if self.root == None:
            self.root = AVLTree(data)
        else:
            self.root = self.root.insert(self.root, data)
        return True
    
    def search(self, k):
        if self.root:
            key = Node(k) if type(self.root) == Node else k
            cur = self.root
            while cur:
                if key == cur.data:
                    return cur
                elif key < cur.data:
                    cur = cur.left
                else:
                    cur = cur.right
            else:
                return None
        else:
            return None

    def delete(self,k):
        
        if self.root == None:
            return False
        elif self.search(k) == None:
            print("Not Found")
            return False
        else:
            key = Node(k) if type(self.root) == Node else k
            self.root = self.root.delete(self.root, key)
            return True
        
    def display(self):
        if self.root == None:
            print("empty tree")
        else:
            self.root.bf_traversal()

    def in_order(self):
        if self.root:
            self.root.in_order()
    def post_order(self):
        if self.root:
            self.root.post_order()
    def pre_order(self):
        if self.root:
            self.root.pre_order()

### Use the above interface to create and use CoolTree.Tree
### AVL Tree is the detailed implementation of CoolTree.Tree        
class AVLTree:
    def __init__(self, data, parent=None):
        self.left = None
        self.data = data
        self.right = None
## AVL AVLTree cannot keep parent, rotation will change parent
    def calc_height(self):
        ## height is the longest edge from this node to a leaf node
        ## base case , leaf node
        if self.left == None  and self.right == None:
            return 0
        if self.left == None:
            return 1 + self.right.calc_height()
        if self.right == None:
            return 1 + self.left.calc_height()
        else:
            return 1 + max ( self.left.calc_height(), self.right.calc_height())
    
    def balanced(self):
        if  self.left == None  and self.right == None:
            return 0
        if self.left == None: ## right heavy
            return -(self.calc_height())
        elif  self.right == None: ## left heavy
            return self.calc_height()
        else:
            return self.left.calc_height() - self.right.calc_height()

    def re_balance(self, root):
        if root.balanced() > 1 : #left heavy 
            if root.left.balanced() >=0: # left heavy
                #print(f"Rotate L L @ {root.data}")
                return self.right_rotate(root)
            else:
                #print(f"Rotate L R @ {root.data}")
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        elif root.balanced() < -1 : ##right heavy
            if root.right.balanced() <= 0 :
                #print(f"Rotate R R @ {root.data}")
                return self.left_rotate(root)
            else:
                #print(f"Rotate R L @ {root.data}")
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root) 
        else:
            return root ## no need to balance

    def insert(self, root, data): ## need to use a root argument instead of just using self because root can be None for 
        if root == None:
            return AVLTree(data)
        if data < root.data:
            root.left = root.insert(root.left, data) ## self.left = self.left.insert(data) will not work if self.left is None
        else:
            root.right = root.insert(root.right, data)         
        return self.re_balance(root)
 ## Nodes Traversals
    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.data)
        if self.right:
            self.right.in_order()
    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.data)
    def pre_order(self):
        print(self.data)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()     
## Rotations 
    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        ## right rotate y
        y.right = z
        z.left = T3
        return y 

    def left_rotate(self,z):
        y = z.right
        T2 = y.left

        ## left rotate y
        y.left = z
        z.right = T2
        return y

## Helpers for _delete    
    def find_largest(self, cur, parent):
        if cur.right == None:
            return cur, parent
        else:
            return self.find_largest(cur.right, cur)

    def find_smallest(self, cur, parent):
        if cur.left == None:
            return cur, parent
        else:
            return self.find_smallest(cur.left, cur)
    def find(self,cur, key):
        if cur == None:
            return False
        elif cur.data == key:
            return True
        elif key < cur.data:
            return self.find(cur.left, key)
        else:
            return self.find(cur.right, key)
    
    def delete(self, cur, key):
        if self.find(cur,key):
            return self._delete(cur, key)
        else:
            print("not found")
            return cur

    def _delete(self,cur,key, parent=None):
        if cur.data == key:
            ## 4 cases : 1 base, 3 recursive  ##
            
            if cur.left == None and cur.right == None:
            ## case 1: leaf node base case ##
                return None
            
            elif cur.left and cur.right == None :
            ## case 2: left subAVLTree only , recursive case   
                #find largest node in left_subAVLTree
                ## Alternate algorithm is just replace with left subtree
                largest, parent = self.find_largest(cur.left, cur)
                tmp = largest.data

                if largest.data > parent.data : ## delete on right subtree
                    parent.right = self._delete(largest,largest.data, parent)
                else: # delete on left subtree
                    parent.left = self._delete(largest,largest.data, parent)
                ## 
                cur.data = tmp
                return self.re_balance (cur)
            
            elif cur.right and cur.left == None:
            ## case 3: right subAVLTree only, recursive case
                # find smallest node in right subAVLTree
                 ## Alternate algorithm is just replace with right subtree
                smallest, parent = self.find_smallest(cur.right, cur)
                tmp = smallest.data
                if smallest.data > parent.data: ## delete on right subtree
                    parent.right = self._delete(smallest, smallest.data, parent)
                else: #delete on left subtree
                    parent.left = self._delete(smallest, smallest.data, parent)
                cur.data = tmp
                return self.re_balance (cur)
            
            else:
            ## case 4: both left and right subAVLTree
                largest, parent = self.find_largest(cur.left, cur)
                tmp = largest.data
                if largest.data > parent.data :
                    parent.right = self._delete(largest,largest.data, parent)
                else:
                    parent.left = self._delete(largest,largest.data, parent)
                cur.data = tmp
                return self.re_balance(cur)
        
        #recursive case
        if key < cur.data:
            cur.left = self._delete(cur.left, key, cur) 

        else:
            cur.right =  self._delete(cur.right, key, cur)

        return self.re_balance(cur)


### BFS and printing of AVLTree
    def printAVLTree(self,complete):
        h = len(complete)
        ws = (2**h)-1

        def printSpace(n):
            for _ in range(n):
                print(" ", end="")
        for level in complete:
            ws = ws //2
            for i, x in enumerate(level):
                if i == 0:
                    printSpace(ws)
                if x == None:
                    x = " "
                print(x, end="")
                printSpace(1+2*ws)
            print()
    def bf_traversal(self):
        ## Breadth First traversal
        ## Traverse list while appending to it

        cur_level = [self]
        next_level = []
        complete = [] ## complete AVLTree , containing a list for level 0,1, ..n 
                      ## the number of nodes in each level is a GP, 1,2,4,8,..2^n
        while True:
            level=[]
            for node in cur_level:
                if node :
                    level.append(f"{node.data}")
                    if node.left :
                        next_level.append(node.left)
                    else:
                        next_level.append(None)

                    if node.right:
                        next_level.append(node.right)
                    else:
                        next_level.append(None)
                else: # leaf node
                    level.append(None)
                    next_level.append(None)
                    next_level.append(None)
            complete.append(level)
            if any ( next_level):
                cur_level = next_level
                next_level = []
            else:
                ## next level has no nodes
                break    
        self.printAVLTree(complete)
        #print_levels(complete)
