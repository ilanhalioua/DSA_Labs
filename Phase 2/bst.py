# -*- coding: utf-8 -*-
import sys

from bintree import BinaryNode
from bintree import BinaryTree


class BinarySearchTree(BinaryTree):

    def search(self, elem: object) -> BinaryNode:
        """Returns the node whose elem is elem"""
        return self._search(self._root, elem)

    def _search(self, node: BinaryNode, elem: object) -> BinaryNode:
        """Recursive function"""
        if node is None or node.elem == elem:
            return node
        elif elem < node.elem:
            return self._search(node.left, elem)
        elif elem > node.elem:
            return self._search(node.right, elem)

    def searchit(self, elem: object) -> BinaryNode:
        """iterative function"""
        node = self._root
        while node:
            if node.elem == elem:
                # we have found it!!! we can return it and leave the function
                return node

            if elem < node.elem:
                node = node.left
            else:
                node = node.right
        return node

    def insert(self, elem: object) -> None:
        self._root = self._insert(self._root, elem)

    def _insert(self, node: BinaryNode, elem: object) -> BinaryNode:
        if node is None:
            return BinaryNode(elem)

        if node.elem == elem:
            print('Error: elem already exist ', elem)
            return node

        if elem < node.elem:
            node.left = self._insert(node.left, elem)
        else:
            # elem>node.elem
            node.right = self._insert(node.right, elem)
        return node

    def insert_iterative(self, elem: object) -> None:
        """iterative version of insert"""
        if self._root is None:
            self._root = BinaryNode(elem)  # if tree is empty, new node will be the root
            return  # we can leave!!!

        node = self._root  # to search the place
        not_exist = True
        while not_exist and node:
            if elem < node.elem:
                node = node.left
                if node.left is None: # this is the place to insert it
                    node.left = BinaryNode(elem)
            elif elem > node.elem:
                node = node.right
                if node.right is None:  # this is the place to insert it
                    node.right = BinaryNode(elem)
            else:  # elem == node.elem
                print('duplicate elements not allowed!!')
                not_exist = False

    def _minimum_node(self, node: BinaryNode) -> BinaryNode:
        """returns the  node with the smallest elem
        in the subtree node.
        This is the node that is furthest to the left"""
        min_node = node
        while min_node.left is not None:
            min_node = min_node.left
        return min_node

    def remove(self, elem: object) -> None:
        # update the root with the new subtree after remove elem
        self._root = self._remove(self._root, elem)

    def _remove(self, node: BinaryNode, elem: object) -> BinaryNode:
        """It recursively searches the node. When the node is
        found, the node has to be removed"""
        if node is None:
            print(elem, ' not found')
            return node

        if elem < node.elem:
            node.left = self._remove(node.left, elem)
        elif elem > node.elem:
            node.right = self._remove(node.right, elem)
        else:
            # node.elem == elem, node is the node to remove!!!
            if node.left is None and node.right is None:
                # Case 1: node is a leave
                return None

            # Case 2: node only has a child, so the function has to return it
            if node.left is None:
                # It only has the right child
                return node.right

            elif node.right is None:
                # It only has the left child
                return node.left
            else:
                # Case 3: node.left!=None and node.right!=None
                # we search the smallest node from its right child
                successor = self._minimum_node(node.right)
                # we replace elem with the elem of the successor
                node.elem = successor.elem
                # now, we have to remove successor from the right child
                node.right = self._remove(node.right, successor.elem)

        return node

    def sumTree(self):
        global sum
        sum = 0
        self._sumTree(self._root)
        return

    def _sumTree(self, node):
        if node is None:
            return
        # print('->')
        self._sumTree(node.right)
        global sum
        # print(node.elem)
        temp = node.elem
        node.elem = sum
        sum += temp
        # print('<-')
        self._sumTree(node.left)



    def numChild(self, node):
        if node is None or (node.left is None and node.right is None):
            return 0
        if node.left is not None and node.right is not None:
            return 2
        return 1

    def isStrict(self):
        return self._isStrict(self._root)

    def _isStrict(self, node):
        nchild = self.numChild(node)
        if nchild == 0:
            return True
        if nchild == 1:
            return False
        # print('<-')
        a = self._isStrict(node.left)
        # print('a: ' + str(a))
        # print('->')
        b = self._isStrict(node.right)
        # print('b: ' + str(b))
        # print('a and b: ' + str(a and b))
        return a and b

    def isSameStructure(self, otherBST):
        return self._isSameStructure(self._root, otherBST._root)

    def _isSameStructure(self, node_self, node_other):
        if self.numChild(node_self) == self.numChild(node_other) == 0:
            return True
        if self.numChild(node_self) != self.numChild(node_other):
            return False
        return self._isSameStructure(node_self.left, node_other.left) and self._isSameStructure(node_self.right, node_other.right)


    def total_sumTree(self):
        return self._total(self._root)
    
    def _total(self, node):
        if node == None:
            return 0
        else:
            return node.elem + self._total(node.left) + self._total(node.right)

    def print_X_Order(self,type):
        if type == 'In':
            self._printInOrder(self._root)
        elif type == 'Pre':
            self._printPreOrder(self._root)
        elif type == 'Post':
            self._printPostOrder(self._root)

    def _printInOrder(self, node):
        if node is None:
            return
        self._printInOrder(node.left)
        print(str(node.elem) + ",", end="")
        self._printInOrder(node.right)

    def _printPreOrder(self, node):
        if node is None:
            return
        print(str(node.elem) + ",", end="")
        self._printPreOrder(node.left)
        self._printPreOrder(node.right)

    def _printPostOrder(self, node):
        if node is None:
            return
        self._printPostOrder(node.left)
        self._printPostOrder(node.right)
        print(str(node.elem) + ",", end="")


    def isBST(self):
        return self._isBST(self._root, -sys.maxsize, sys.maxsize)

    def _isBST(self, node, min_value, max_value):
        # max_value --> 'max_value_q_puede_tener_currentNode'
        # min_value --> 'min_value_q_puede_tener_currentNode'
        if node is None:
            return True

        if node.elem < min_value or node.elem > max_value:
            return False

        return self._isBST(node.left, min_value, node.elem) and self._isBST(node.right, node.elem, max_value)
        # Quiero ir actualizando el max_value_q_puede_tener_elSiguienteNode = node.elem si estamos llendo full izq.
        # Quiero ir actualizando el min_value_q_puede_tener_elSiguienteNode = node.elem si estamos llendo full der.

    '''def isBST(self):
        return self._isBST(self._root)

    def _isBST(self, node):
        if node is None:
            return True
        print(node.elem)
        return (node.elem < self._isBST(node.right)) and (node.elem > self._isBST(node.left)) # No se puede pq: node.elem < True??'''

    def outsideRange(self, min: int, max: int):
        if min > max:
            print('min > max')
            return
        result = []
        return self._outsideRange(self._root, min, max, result)

    def _outsideRange(self, node, min, max, result):
        if node is not None:
            self._outsideRange(node.left, min, max, result)
            if node.left is None and node.right is None:
                if node.elem < min or node.elem > max:
                    result.append(node.elem)
            self._outsideRange(node.right, min, max, result)
        return result

    #################

    '''def find_dist_k(self, target, k: int):
        path = []
        targetNode = self.search(target)
        result = self.distance_k(self._root, targetNode, k, path)
        result.sort()
        return result

    def distance_k(self, root: BinaryNode, target: BinaryNode, k: int, path):
        self.findPath(root, target, path)
        result = []
        for i in range(len(path)):
            self.find_k_DistanceFromNode(path[i], k - i, result, None if i == 0 else path[i - 1])
        return result

    def find_k_DistanceFromNode(self, node, dist, result, blocker: BinaryNode):
        if dist < 0 or node is None or (blocker is not None and node == blocker):
            return
        if dist == 0:
            result.append(node.elem)
        self.find_k_DistanceFromNode(node.left, dist - 1, result, blocker)
        self.find_k_DistanceFromNode(node.right, dist - 1, result, blocker)

    def findPath(self, node: BinaryNode, target: BinaryNode, path) -> bool:
        if node is None:
            return False
        if node == target or self.findPath(node.left, target, path) or self.findPath(node.right, target, path):
            path.append(node)
            return True
        return False'''

    ###############

    def find_dist_k(self, n, k):
        # input error handling
        if k < 0:
            print("Error with the input parameter k. It must be >= 0!")
            return []
        # next ,figure out where the node with value n is (in the case where it doesnt exist, search will return none)
        targetNode = self.search(n)
        if targetNode is None:
            print("Node with value n does not exist , sorry.")
            return []
        else:
            # There can be at most two types of nodes which are at a distance k from the target :
            # First type of nodes are all the ones that are successors of the target node and they can be obtained through the recursive function defined above (detailed explanation of utilitu in the body)
            # Second type of nodes are all the ones that are ancestors of the traget node and they cna be ontained through the function defined above (detailed explanation of utilitu in the body)
            result = self.DistanceKnodes(targetNode, k)
            result.sort()
            return result

    def DistanceKnodes(self, node, k):  # returns a list of all the nodes that are at a disance k from the target node
        ancestors = []
        self.Ancestors(self._root, node, ancestors)  # first, obtain all the ancestor nodes of input node

        result = []
        for i in range(0, len(ancestors)):  # then, look for (in the appropiate subtree of ith ancestor) all the successors of ith ancestor at distance k-Distance(ith ancestor,successor)
            if i == 0:
                self.DistanceKSuccessors(ancestors[i], k - i, result, None)
            else:
                self.DistanceKSuccessors(ancestors[i], k - i, result, ancestors[i - 1])
        return result

    def DistanceKSuccessors(self, node, k, result, stopNode):  # returns list of successsor`s values at a distance k from node
        # base case:
        if node is None or k < 0 or (stopNode is not None and node == stopNode):
            return
        if k == 0:
            result.append(node.elem)
        # recursive step:
        self.DistanceKSuccessors(node.left, k - 1, result, stopNode)
        self.DistanceKSuccessors(node.right, k - 1, result, stopNode)

    def Ancestors(self, node: BinaryNode, target: BinaryNode, ancestors) -> bool:
        if node is None:
            return False
        if node == target or self.Ancestors(node.left, target, ancestors) or self.Ancestors(node.right, target, ancestors):
            ancestors.append(node)
            return True
        return False


    def create_tree(self, tree1, tree2, opc):
        if opc == 'merge':
            return self._merge(tree1._root, tree2._root)
        elif opc == 'intersection':
            return self._intersection(tree1._root, tree2._root)
        elif opc == 'difference':
            return self._difference(tree1._root, tree2._root)
        else:
            raise ValueError("Invalid value for opc parameter")

    def _merge(self, t1, t2) -> BinaryNode:
        if not t1:
            return t2
        if not t2:
            return t1
        t1.elem += t2.elem
        t1.left = self._merge(t1.left, t2.left)
        t1.right = self._merge(t1.right, t2.right)
        return t1


    def _intersection(self, node1, node2):
        if node1 is None or node2 is None:
            return None
        if node1.elem == node2.elem:
            new_node = BinaryNode(node1.elem) # new_node = BinarySearchTree.Node(node1.elem)
            new_node.left = self._intersection(node1.left, node2.left)
            new_node.right = self._intersection(node1.right, node2.right)
            return new_node
        else:
            return None

    def _difference(self, node1, node2):
        if node1 is None:
            return None
        if node2 is None:
            return node1
        if node1.elem == node2.elem:
            new_node = BinaryNode(None) # new_node = BinarySearchTree.Node(None)
            new_node.left = self._difference(node1.left, node2.left)
            new_node.right = self._difference(node1.right, node2.right)
            return new_node
        else:
            new_node = BinaryNode(node1.elem) #new_node = BinarySearchTree.Node(node1.elem)
            new_node.left = self._difference(node1.left, node2)
            new_node.right = self._difference(node1.right, node2)
            return new_node


if __name__ == "__main__":
    selftree1 = BinarySearchTree()
    selftree1.insert(20)
    selftree1.insert(10)
    selftree1.insert(30)

    selftree1.draw()


    print()
    T1 = BinarySearchTree()
    T1.insert(14)
    T1.insert(11)
    T1.insert(18)
    T1.insert(10)
    T1.insert(13)
    T1.insert(16)
    T1.insert(19)
    T1.insert(5)
    T1.insert(12)
    T1.insert(15)
    T1.insert(17)
    T1.insert(30)
    T1.insert(4)
    T1.insert(6)
    T1.insert(29)
    T1.insert(31)
    T1.insert(2)
    T1.insert(8)
    T1.insert(24)
    T1.insert(33)
    T1.insert(1)
    T1.insert(3)
    T1.insert(7)
    T1.insert(9)
    T1.insert(23)
    T1.insert(25)
    T1.insert(32)
    T1.insert(34)
    T1.insert(21)
    T1.insert(27)
    T1.insert(36)
    T1.insert(20)
    T1.insert(22)
    T1.insert(26)
    T1.insert(28)
    T1.insert(35)
    T1.insert(37)

    print('Problem 1 Tests:')
    print(T1.find_dist_k(30, 0))  # [30]
    print(T1.find_dist_k(30, 2))  # [18, 24, 33]
    print(T1.find_dist_k(12, 6))  # [2, 8, 15, 17, 30]
    print(T1.find_dist_k(17, 7))  # [4, 6, 23, 25, 32, 34]
    print(T1.find_dist_k(26, 9))  # [11, 15, 17, 36]

    print()
    print('Problem 2 Tests:')
    tree1 = BinarySearchTree()
    tree1.insert(1)
    tree1.insert(2)
    tree1.insert(3)
    tree1.insert(4)
    tree1.insert(5)
    tree1.insert(6)
    print('Tree 1:\n')
    tree1.draw()

    tree2 = BinarySearchTree()
    tree2.insert(4)
    tree2.insert(1)
    tree2.insert(7)
    tree2.insert(3)
    tree2.insert(2)
    tree2.insert(6)
    print('\nTree 2:\n')
    tree2.draw()

    resultTree_merge = BinarySearchTree()
    resultTree_merge.create_tree(tree1, tree2, 'merge')
    resultTree_merge.draww()

    print()
    resultTree_intersection = BinarySearchTree()
    resultTree_intersection.create_tree(tree1, tree2, 'intersection')
    resultTree_intersection.draww()

    print()
    resultTree_difference = BinarySearchTree()
    resultTree_difference.create_tree(tree1, tree2, 'difference')
    resultTree_difference.draww()


    '''print()
    pp2 = BinarySearchTree()
    pp2.insert(3)
    pp2.insert(1)
    pp2.insert(2)
    pp2.insert(5)
    pp2.insert(4)
    pp2.draw()
    print(pp2.outsideRange(3,3))
    
    print()
    s = BinarySearchTree()
    s.insert(3)
    s.insert(1)
    s.insert(2)
    s.insert(5)
    s.insert(4)
    s.draw()

    print()
    o = BinarySearchTree()
    o.insert(4)
    o.insert(2)
    o.insert(3)
    o.insert(6)
    o.insert(5)
    o.insert(20)
    o.draw()

    if s.isSameStructure(o) is True:
        print('Same Structure')
    else:
        print('Different Structure')

    print()

    prueba1 = BinarySearchTree()
    prueba1.insert(50)
    prueba1.insert(25)
    prueba1.insert(20)
    prueba1.insert(45)
    prueba1.insert(80)
    prueba1.insert(60)
    prueba1.insert(90)
    prueba1.insert(55)
    prueba1.insert(65)
    prueba1.insert(19)
    prueba1.insert(21)
    print(prueba1.total_sumTree())
    prueba1.draw()
    if prueba1.isStrict() is True:
        print('True')
    else:
        print('False')

    print()
    prueba = BinarySearchTree()
    prueba.insert(3)
    prueba.insert(1)
    prueba.insert(2)
    prueba.insert(5)
    prueba.insert(4)
    prueba.draw()
    print(prueba.total_sumTree())
    print()

    bst = BinarySearchTree()
    bst.insert(11)
    bst.insert(2)
    bst.insert(1)
    bst.insert(7)
    bst.insert(29)
    bst.insert(15)
    bst.insert(40)
    bst.insert(35)
    bst.draw()
    print('\nIn-order traversal: ')
    bst.print_X_Order('In')
    print('\nPre-order traversal: ')
    bst.print_X_Order('Pre')
    print('\nPost-order traversal: ')
    bst.print_X_Order('Post')
    print("\n\n")
    bst.sumTree()
    bst.draw()

    print()
    aBST = BinarySearchTree()
    aBST.insert(10)
    aBST.insert(5)
    aBST.insert(1)
    aBST.insert(7)
    aBST.insert(12)
    aBST.draw()
    if aBST.isBST() is True:
        print('True: It is a BST')
    else:
        print('False: It is NOT a BST')
    '''
    '''notBST = BinaryTree()
    notBST.insert(1)
    notBST.insert(7)
    notBST.insert(10)
    notBST.insert(5)
    notBST.insert(12)
    notBST.draw()'''
    '''
    aux = BinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        aux.insert(x)
        # aux.draw()

    aux.draw()
    print("after remove 80 (a leaf)")
    aux.remove(80)
    aux.draw()
    print()

    tree = BinarySearchTree()
    for x in [18, 11, 23, 5, 15, 20, 24, 9, 15, 22, 21, 6, 8, 7]:
        tree.insert(x)
    tree.draw()
    print('size:', tree.size())
    print('height:', tree.height())

    tree.remove(18)
    print("after remove 18 (root), replaced with its successor 20")
    tree.draw()

    tree.remove(7)
    print("after remove 7 (a leaf)")
    tree.draw()

    tree.remove(8)
    print("after remove 8 (a leaf)")
    tree.draw()

    tree.remove(5)
    print("after remove 5 (only a child), replaced with its child: 9")
    tree.draw()

    tree.remove(9)
    print("after remove 9 (only a child), replaced with its left child: 6")
    tree.draw()

    tree.remove(11)
    print("after remove 11 (two children), replaced with its successor: 15")
    tree.draw()

    tree.remove(20)
    print("after remove 20 (root), two children, replaced with its successor: 21")
    tree.draw()

    tree.remove(15)
    print("after remove 15 (only left child) -> 6")
    tree.draw()

    tree.remove(6)
    print("after remove 6 (a leaf)")
    tree.draw()

    tree.remove(8)
    print("after remove 8 (does not exist)")
    tree.draw()

    tree.remove(24)
    print("after remove 24 (a leaf)")
    tree.draw()
    print()

    for x in [5, 10, 15, 20]:
        tree.insert(x)
    print("after insert 5,10,15,20")
    tree.draw()

    tree.remove(23)
    print("after remove 23, only a left child -> 22")
    tree.draw()

    # remove a root, with only the left child
    tree.remove(22)
    print("after remove 22 (a leaf)")
    tree.draw()
    # remove a root, with only the right child
    print("after remove 5 (only a right child) ->10")
    tree.remove(5)
    tree.draw()

    print("after remove 21 (root with only a left child) -> 10")
    tree.remove(21)
    tree.draw()
    '''''''''