# -*- coding: utf-8 -*-
import heapq, copy, gc

class TreeNode(object):
    """Class of Tree Node.
    The __init__ method of Tree Node.

    Args:
        val (int): The value of the tree node.

    """
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree(object):
    """Class of Binary Search Tree. Timecomplex(logN).
    With functions of insert, query, find maximum number, find minimum, delete nodes and print tree.
    
    """
    def __init__(self):
        pass


    def insert(self, root, val):
        """Use to insert node to the binary search tree.

        Args:
            root (:obj:`TreeNode`): The root(parent) of the node that currently being inserted.
            val (int): The value of the current node.

        Returns:
            The root node after insert the new node.

        """
        if root == None:
            root = TreeNode(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)         
        elif val > root.val:
            root.right = self.insert(root.right, val)

        return root

    def query(self, root, val):
        """Query whether the input value exists in the binary search tree.

        Args:
            root (:obj:`TreeNode`): The root(parent) of the node.
            val (int): The value of the current node.

        Returns:
            True if exitsts, False if not exitsts.

        """
        if root == None:
            return False
        if root.val == val:
            return True
        elif val < root.val:
            return self.query(root.left, val)
        elif val > root.val:
            return self.query(root.right, val)

    def findMin(self, root):
        """Fine the node of the minimum value in the whold binary search tree.

        Args:
            root (:obj:`TreeNode`): The root(parent) of the node.
        
        Returns:
            The node of the minimum value

        """
        if root.left:
            return self.findMin(root.left)
        else:
            return root

    def findMax(self, root):
        """Fine the node of the maximum value in the whold binary search tree.

        Args:
            root (:obj:`TreeNode`): The root(parent) of the node.
        
        Returns:
            The node of the maximum value

        """
        if root.right:
            return self.findMax(root.right)
        else:
            return root

    def delNode(self, root, val):
        """Delete the node in the binary search tree with the value of val

        Args:
            root (:obj:`TreeNode`): The root(parent) of the node.
            val (int): The value of the node to be delete.

        """
        if root == None:
            return
        if val < root.val:
            root.left = self.delNode(root.left, val)
        elif val > root.val:
            root.right = self.delNode(root.right, val)
        else: # 当val == root.val时，分为三种情况：只有左子树或者只有右子树、有左右子树、即无左子树又无右子树
            if root.left and root.right:
                # 既有左子树又有右子树，则需找到左子树中最大值节点，或者找到右子树中最小值节点，这里选择前者
                temp = self.findMax(root.left)
                root.val = temp.val
                # 再把左右子树中最大值节点删除
                root.left = self.delNode(root.left, temp.val)
            elif root.right == None and root.left == None:
                # 左右子树都为空
                root = None
            elif root.right == None:
                # 只有左子树
                root = root.left
            elif root.left == None:
                # 只有右子树
                root = root.right

        return root

    def printTree(self, root):
        """Print the whole tree for preview (left-middle-right).

        Args:
            root (:obj:`TreeNode`): The root(parent) of the node.

        """
        if root == None:
            return

        self.printTree(root.left)
        print(root.val)
        self.printTree(root.right)


class Heap(object):
    """Class of Heap. Timecomplex(logN).
    The initialization method has a boolean parameter name maxheap to generate a minheap or maxheap.

    Args:
        vals (list): The initialization data before generate a heap.
        maxheap (boolean): True to generate a maxheap, False to generate a minheap.
    
    """
    def __init__(self, vals, maxheap=False):
        self.__heap = []
        self.__maxheap = maxheap

        if maxheap:
            self.__heap = [val*-1 for val in vals]
            heapq.heapify(self.__heap)
        else:
            self.__heap = vals
            heapq.heapify(self.__heap)

    def push(self, val):
        """Push the value item onto the heap, maintaining the heap invariant.

        Args:
            val (int): The value which will be put into the heap.

        """
        if self.__maxheap:
            val = val*-1
            heapq.heappush(self.__heap, val)
        else:
            heapq.heappush(self.__heap, val)

    def pop(self):
        """Pop and return the minimum or maximum(base on boolean parameter maxheap) item from the heap, maintaining the heap invariant.

        Returns:
            The minimum or maximum(base on boolean parameter maxheap) item.

        """
        if self.__maxheap:
            return heapq.heappop(self.__heap)*-1
        else:
            return heapq.heappop(self.__heap)

    def pushpop(self, val):
        """Push item on the heap, then pop and return the minimum or maximum(base on boolean parameter maxheap) item from the heap.The combined action is push followed by a call to pop.
        
        Args:
            val (int): he value which will be push into the heap.

        Returns:
            The minimum or maximum(base on boolean parameter maxheap) item.

        """
        if self.__maxheap:
            val = val*-1
            return heapq.heappushpop(self.__heap, val)*-1
        else:
            return heapq.heappushpop(self.__heap, val)

    def replace(self, val):
        """Pop and return the minimum or maximum(base on boolean parameter maxheap) item from the heap, and also push the new item. The combined action is pop followed by a call to push.

        Args:
            val (int): he value which will be push into the heap.

        Returns:
            The minimum or maximum(base on boolean parameter maxheap) item.

        """
        if self.__maxheap:
            val = val*-1
            return heapq.heapreplace(self.__heap, val)*-1
        else:
            return heapq.heapreplace(self.__heap, val)

    def nsmallest(self, n):
        """Return a list with the n smallest elements from the dataset defined by heap.
        
        Args:
            n (int): N smallest elements.

        Returns:
            A list with n smallest elements.

        """
        if self.__maxheap:
            return [var*-1 for var in heapq.nlargest(n, self.__heap)]
        else:
            return heapq.nsmallest(n, self.__heap)

    def nlargest(self, n):
        """Return a list with the n largest elements from the dataset defined by heap.
        
        Args:
            n (int): N largest elements.

        Returns:
            A list with n largest elements.

        """
        if self.__maxheap:
            return [var*-1 for var in heapq.nsmallest(n, self.__heap)]
        else:
            return heapq.nlargest(n, self.__heap)

    def getSortHeap(self):
        """Get sorted heap data.

        Returns:
            A list with sorted list.

        """
        return self.__getSortHeap()

    def __getSortHeap(self):
        sort_heap = []
        temp = copy.deepcopy(self.__heap)

        if self.__maxheap:
            while (self.__heap):
                sort_heap.append(heapq.heappop(self.__heap)*-1)
        else:
            while (self.__heap):
                sort_heap.append(heapq.heappop(self.__heap))

        self.__heap = temp
        del(temp)
        gc.collect()
        
        return sort_heap


class UnionFind(object):
    """Class of Union-Find. An implementation of union find data structure.
    complexity:
        * find -- :math:`O(\\alpha(N))` where :math:`\\alpha(n)` is
          `inverse ackerman function
          <http://en.wikipedia.org/wiki/Ackermann_function#Inverse>`_.
        * union -- :math:`O(\\alpha(N))` where :math:`\\alpha(n)` is
          `inverse ackerman function
          <http://en.wikipedia.org/wiki/Ackermann_function#Inverse>`_.

    """
    def __init__(self, n):
        """Initialize an empty union find object with N items.

        Args:
            N: Number of items in the union find object.
        """
        self.__union_find = [-1 for i in range(n)]
        self.__sets_count = n

    def find(self, p):
        """Find the set identifier for the item p.

        Args:
            p: Find the root node of value p.

        Returns:
            Root node identifier.

        """
        r = p
        while self.__union_find[p] > 0:
            p = self.__union_find[p]
        while r != p:
            self.__union_find[r], r = p, self.__union_find[r] # Path compression using halving.
        return p

    def union(self, p, q):
        """Combine sets containing p and q into a single set.
        q towards to p.

        Args:
            p: Target value.
            q: Source value.

        """
        proot = self.find(p)
        qroot = self.find(q)
        if proot == qroot:
            return
        elif self.__union_find[proot] > self.__union_find[qroot]:   # 树高度(负数)比较,左边规模更小(负数绝对值越大规模越大,即是树的高度越高)
            self.__union_find[qroot] += self.__union_find[proot]    # 规模小向规模大的合并
            self.__union_find[proot] = qroot
        else:
            self.__union_find[proot] += self.__union_find[qroot]    # 规模合并
            self.__union_find[qroot] = proot
        self.__sets_count -= 1

    def is_connected(self, p, q):
        """Check if the items p and q are on the same set or not."""
        return self.find(p) == self.find(q)

    def count(self):
        """Return the number of items."""
        return self.__sets_count

    def __str__(self):
        """String representation of the union find object."""
        return " ".join([str(x) for x in self.__union_find])

    def __repr__(self):
        """Representation of the union find object."""
        return "UF(" + str(self) + ")"
