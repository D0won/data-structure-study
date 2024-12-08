class Node :
    def __init__(self, key, value, height, left=None, right=None):
        self.key = key
        self.value = value
        self.height = height
        self.left = left
        self.right = right

class AVL :
    def __init__(self):
        self.root = None
    
    def height(self, n) :
        if n == None :
            return 0
        return n.height

    def put(self, key, value) :
        self.root = self.put_item(self.root, key, value)

    def put_item(self, n, key, value) :
        if n == None :
            return Node(key, value, 1)
        if n.key > key :
            n.left = self.put_item(n.left, key, value)
        elif n.key < key :
            n.right = self.put_item(n.right, key, value)
        else :
            n.value = value
            return n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)
    
    def balance(self, n) :
        if self.bf(n) > 1 :
            if self.bf(n.left) < 0 :
                n.left = self.rotate_left(n.left)
            n = self.rotate_right(n)

        elif self.bf(n) < -1 :
            if self.bf(n.right) > 0 :
                n.right = self.rotate_right(n.right)
            n = self.rotate_left(n)
        return n
    
    def bf(self, n) :
        return self.height(n.left) - self.height(n.right)
    
    def rotate_right(self, n) :
        x = n.left
        n.left = x.right
        x.right = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x
    
    def rotate_left(self, n) :
        x = n.right
        n.right = x.left
        x.left = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x
    
    def delete(self, key):
        self.root = self.del_node(self.root, key)

    def del_node(self, n, key):
        if not n:
            return n

        if key < n.key:
            n.left = self.del_node(n.left, key)
        elif key > n.key:
            n.right = self.del_node(n.right, key)
        else:
            if not n.left:
                return n.right
            elif not n.right:
                return n.left

            temp = self.minimum(n.right)
            n.key = temp.key
            n.right = self.del_node(n.right, temp.key)

        n.height = 1 + max(self.height(n.left), self.height(n.right))
        return self.balance(n)
    
    def delete_min(self) :
        if self.root == None :
            print('트리가 비어 있음')
        self.root = self.del_min(self.root)

    def del_min(self, n) :
        if n.left == None :
            return n.right
        n.left = self.del_min(n.left)
        return self.balance(n)
    
    def min(self) :
        if self.root == None :
            return None
        
        return self.minimum(self.root)
    
    def minimum(self, n) :
        if n.left == None :
            return n
        return self.minimum(n.left)

   
    def preorder(self, n) :
        if n != None :
            print(str(n.key),'', end='')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)
        else :
            return
    def inorder(self, n):
        if n!= None :
            if n.left:
                self.inorder(n.left)
            print(str(n.key),'', end='')

            if n.right:
                self.inorder(n.right)
        else :
            return
        
    def postorder(self, n):
        if n!= None :
            if n.left:
                self.postorder(n.left)
            if n.right :
                self.postorder(n.right)
            print(str(n.key),'', end='')
        else :
            return
        
    def levelorder(self, root):
        q = []
        q.append(root)
        while len(q) != 0 :
            t = q.pop(0)
            print(str(t.key), ' ', end='')
            if t.left != None:
                q.append(t.left)
            if t.right != None :
                q.append(t.right)
