"""
@author: EDA Team
"""

# Classes provided by EDA Team
from bintree import BinaryNode
from bst import BinarySearchTree


# Exercise #1
class BST2(BinarySearchTree):
    def DistanceKSuccessors(self, node, k): #returns list of successsor`s values at a distance k from node
        #base case:
        if node is None or k < 0:
            return []
        if k == 0:
            return [node.elem]
        #recursive step:
        return self.DistanceKSuccessors(node.left, k-1) + self.DistanceKSuccessors(node.right, k-1)

    def Distance(self, node, target): #assuming that there is a node in the bst with element = target, this function computes the distance from node to target
        if node.elem == target.elem: #base case
            return 0
        if target.elem < node.elem: #go to the left st
            return 1 + self.Distance(node.left, target)
        else: #go to the right st
            return 1 + self.Distance(node.right, target)

    def Ancestors(self, node): #this function returns, given a data element called target, a list of all the nodes in the Bst that are ancestors of the node with data attribute equal to target
        current_node = self.root
        Ancestors = []
        while current_node.elem != node.elem:
            Ancestors.append(current_node)
            if node.elem > current_node.elem:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return Ancestors

    def AddInOrder(self): #returns a list with node sorted in increasing order from the contents of self tree object
        return self._AddInOrder(self.root)

    def _AddInOrder(self, node):
        if node is None:
            return []
        return self._AddInOrder(node.left) + [node.elem] + self._AddInOrder(node.right)

    def DistanceKAncestors(self, node, k): #returns a list of all the nodes that are at distance k from the target node
        Ancestors = []
        result = []
        Ancestors = self.Ancestors(node) #first, obtain all the ancestor nodes of input node
        for i in range(0, len(Ancestors)): #then, look for (in the appropiate subtree of ith ancestor) all the successors of the ith ancestor at distance k-Distance(ith ancestor,successor)
            d = self.Distance(Ancestors[i], node)
            #now, based on the subtree where the node is wrt to the current ancestor, the resulting nodes are all those at k-d distance from the current ancestor
            if node.elem > Ancestors[i].elem: #this means that the node is on the right st of the ancestor, so we should only look for those on the left st
                temp = Ancestors[i].right
                Ancestors[i].right = None
                result = self.DistanceKSuccessors(Ancestors[i], k-d) + result
                Ancestors[i].right = temp
            else:
                temp = Ancestors[i].left
                Ancestors[i].left = None
                result = self.DistanceKSuccessors(Ancestors[i], k-d) + result
                Ancestors[i].left = temp
        return result

    def find_dist_k(self, n: int, k: int) -> list:
        #input error handling
        if k < 0:
            print("Error with the input parameter k.It must be >= 0!")
            return []
        #next ,figure out where the node with value n is (in the case where it doesnt exist, search will return none)
        node = self.search(n)
        if node is None:
            print("Node with value n does not exist , sorry.")
            return []
        else:
            #There can be at most two types of nodes which are at a distance k from the target :
            #First type of nodes are all the ones that are successors of the target node and they can be obtained through the recursive function defined above (detailed explanation of utility in function´s body)
            #Second type of nodes are all the ones that are ancestors of the target node and they can be ontained through the function defined above (detailed explanation of utility in the body)
            result = self.DistanceKSuccessors(node, k) + self.DistanceKAncestors(node, k)
            T = BST2()
            for i in range(len(result)):
                T.insert(result[i])
            result = T.AddInOrder()
            return result


    def BST2_insert(self, elem: object) -> None:
        """insert a new node containing this element"""
        self._root = self._BST2_insert(self._root, elem)

    def _BST2_insert(self, node: BinaryNode, elem: object) -> BinaryNode:
        if node is None:
            return BinaryNode(elem)
        if node.elem == elem:
            return node
        if elem < node.elem:
            node.left = self._BST2_insert(node.left, elem)
        else:
            node.right = self._BST2_insert(node.right, elem)
        return node

    def merge(self, node): # merges the tree rooted with node with the self tree object
        if node is not None:
            # then, insert root element and merge both left and right subtrees right after
            # since the insertion function already checks whether the element to be inserted is inside the tree, we do not have to worry about it
            self.BST2_insert(node.elem)
            # now, the recursive call, for both left and right st's
            self.merge(node.left)
            self.merge(node.right)

    def intersection(self, node: BinaryNode, tree: BinarySearchTree):
        if node is not None:
            # then, check if the node element is inside the tree as well
            if tree.search(node.elem) is not None: # found it on the tree object, then insert it
                self.BST2_insert(node.elem)
            # now, just do the same with the left and right children of node
            self.intersection(node.left, tree)
            self.intersection(node.right, tree)
    def difference(self, node: BinaryNode, tree: BinarySearchTree):
        if node is not None:
            # then, check if the node element is inside the tree as well
            if tree.search(node.elem) is None:
                # not in the intersection, so we can just insert it
                self.BST2_insert(node.elem)
            # now, proceed on the left and right children of node
            self.difference(node.left, tree)
            self.difference(node.right, tree)


# Exercise #2
def create_tree(input_tree1: BinarySearchTree, input_tree2: BinarySearchTree, opc: str) -> BinarySearchTree:
    resultTree = BST2()

    if opc == 'merge':
        resultTree.merge(input_tree1._root)
        resultTree.merge(input_tree2._root)
    elif opc == 'intersection':
        resultTree.intersection(input_tree1._root, input_tree2)
    elif opc == 'difference':
        resultTree.difference(input_tree1._root, input_tree2)
    else:
        print("Error. Third argument should be: 'merge' / 'intersection' / 'difference'.")

    return resultTree
    

# Some usage examples
if __name__ == '__main__':

    print()
    T1 = BST2()
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
    print('T1.find_dist_k(30, 0): ' + str(T1.find_dist_k(30, 0)))  # [30]
    print('T1.find_dist_k(30, 2): ' + str(T1.find_dist_k(30, 2)))  # [18, 24, 33]
    print('T1.find_dist_k(12, 6): ' + str(T1.find_dist_k(12, 6)))  # [2, 8, 15, 17, 30]
    print('T1.find_dist_k(17, 7): ' + str(T1.find_dist_k(17, 7)))  # [4, 6, 23, 25, 32, 34]
    print('T1.find_dist_k(26, 9): ' + str(T1.find_dist_k(26, 9)))  # [11, 15, 17, 36]

    print()
    print('Problem 2 Tests:')

    # input_list_01 = [3, 6, 4, 7, 8, 2, 1, 0, 5]
    # input_list_02 = [5, 16, 4, 23, 1, 7]
    # input_list_01 = [5, 1, 7, 9, 23]
    # input_list_02 = [1, 9, 11]
    input_list_01 = [5, 12, 2, 1, 3, 9]
    input_list_02 = [9, 3, 21]


    # Build and draw first tree
    print('Tree1:\n')
    tree1 = BinarySearchTree()
    for x in input_list_01:
        tree1.insert(x)
    tree1.draw()

    # Build and draw second tree
    print('Tree2:\n')
    tree2 = BinarySearchTree()
    for x in input_list_02:
        tree2.insert(x)
    tree2.draw()

    function_names = ["merge", "intersection", "difference"]

    for op_name in function_names:
        res = create_tree(tree1, tree2, op_name)
        print(f"-- Result for {op_name} method. #{res.size()} nodes")
        res.draw()
