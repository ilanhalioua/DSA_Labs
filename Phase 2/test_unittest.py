# -*- coding: utf-8 -*-
"""
Test program comparing solutions with the builtin list-based one.

@author: EDA Team
"""

# Classes provided by EDA Team
from bst import BinarySearchTree
import unittest
from phase2 import BST2
from phase2 import create_tree



class Test(unittest.TestCase):
    def setUp(self):
        self.emptyT1 = BST2()
        self.emptyTree1 = BinarySearchTree()
        self.emptyTree2 = BinarySearchTree()

        self.T1 = BST2()
        self.T1.insert(3)
        self.T1.insert(5)
        self.T1.insert(1)
        self.T1.insert(6)
        self.T1.insert(2)
        self.T1.insert(0)
        self.T1.insert(8)
        self.T1.insert(7)
        self.T1.insert(4)
        # T1:
        #   _3_
        #  /   \
        #  1   5
        # / \ / \
        # 0 2 4 6_
        #         \
        #         8
        #        /
        #        7

        self.tree1 = BinarySearchTree()
        self.tree1.insert(3)
        self.tree1.insert(6)
        self.tree1.insert(4)
        self.tree1.insert(7)
        self.tree1.insert(8)
        self.tree1.insert(2)
        self.tree1.insert(1)
        self.tree1.insert(0)
        self.tree1.insert(5)
        # tree1:
        #    _3_
        #   /   \
        #   2  _6
        #  /  /  \
        #  1  4  7
        # /    \  \
        # 0    5  8


        self.tree2 = BinarySearchTree()
        self.tree2.insert(5)
        self.tree2.insert(16)
        self.tree2.insert(4)
        self.tree2.insert(23)
        self.tree2.insert(1)
        self.tree2.insert(7)
        # tree2:
        #   _5_
        #  /   \
        #  4  16_
        # /  /   \
        # 1  7  23

        self.tree3 = BinarySearchTree()
        self.tree3.insert(20)
        self.tree3.insert(10)
        self.tree3.insert(30)
        # tree3:
        #   20_
        #  /   \
        # 10  30

        self.tree4 = BinarySearchTree()
        self.tree4.insert(20)
        self.tree4.insert(10)
        self.tree4.insert(30)
        # tree4:
        #   20_
        #  /   \
        # 10  30

    def test1_find_dist_k(self):
        print("\nCase 1: distancek function when the tree is empty")
        self.assertEqual(self.emptyT1.find_dist_k(2, 3), [], "Fail: distanceK function when the tree is empty:  ")
        print()

    def test2_find_dist_k(self):
        print("\nCase 2: distancek function when k is negative")
        self.assertEqual(self.T1.find_dist_k(3, -2), [], "Fail: distancek function when k is negative ")
        print()

    def test3_find_dist_k(self):
        print("\nCase 3: several nodes at distance k")
        self.assertEqual(self.T1.find_dist_k(6, 2), [3, 4, 7], "Fail: several nodes at distance k ")
        print()

    def test4_find_dist_k(self):  # noNodesAtdistK
        print("\nCase 4: k value is greater than height")
        self.assertEqual(self.T1.find_dist_k(2, 7), [], "Fail: k value is greater than height")
        print()

    def test5_find_dist_k(self):
        print("\nCase 5: distance is zero")
        self.assertEqual(self.T1.find_dist_k(2, 0), [2], "Fail: distance is zero")
        print()

    def test6_find_dist_k(self):
        print("\nCase 6: node with value n is not in the tree")
        self.assertEqual(self.T1.find_dist_k(13, 3), [], "Fail:  node with value n is not in the tree")
        print()

    def test7_find_dist_k(self):
        print("\nCase 7: Tree only has ancestors at distance k")
        self.assertEqual(self.T1.find_dist_k(8, 3), [3, 4], "Fail: Tree only has ancestors at distance k ")
        print()

    def test8_find_dist_k(self):
        print("\nCase 8: Tree only has successors at distance k")
        self.assertEqual(self.T1.find_dist_k(3, 2), [0, 2, 4, 6], "Fail: Tree only has successors at distance ")
        print()

    def test_merge(self):
        print("\nCase 9: Test basic usage of create_tree with opc 'merge'")
        resultTree = create_tree(self.tree1, self.tree2, 'merge')
        self.expectedTree = BST2()
        self.expectedTree.insert(3)
        self.expectedTree.insert(2)
        self.expectedTree.insert(6)
        self.expectedTree.insert(1)
        self.expectedTree.insert(4)
        self.expectedTree.insert(7)
        self.expectedTree.insert(0)
        self.expectedTree.insert(5)
        self.expectedTree.insert(8)
        self.expectedTree.insert(16)
        self.expectedTree.insert(23)

        self.assertEqual(resultTree, self.expectedTree, "Fail: basic usage of create_tree with opc 'merge'")
        print()
        
    def test_intersection(self):
        print("\nCase 10: Test basic usage of create_tree with opc 'intersection'")
        resultTree = create_tree(self.tree1, self.tree2, 'intersection')
        self.expectedTree = BST2()
        self.expectedTree.insert(1)
        self.expectedTree.insert(4)
        self.expectedTree.insert(5)
        self.expectedTree.insert(7)
        self.assertEqual(resultTree, self.expectedTree, "Fail: basic usage of create_tree with opc 'intersection'")
        print()

    def test_difference(self):
        print("\nCase 11: Test basic usage of create_tree with opc 'difference'")
        resultTree = create_tree(self.tree1, self.tree2, 'difference')
        self.expectedTree = BST2()
        self.expectedTree.insert(3)
        self.expectedTree.insert(2)
        self.expectedTree.insert(6)
        self.expectedTree.insert(0)
        self.expectedTree.insert(8)
        self.assertEqual(resultTree, self.expectedTree, "Fail: basic usage of create_tree with opc 'difference'")
        print()

    def test_merge_empty_trees(self):
        print("\nCase 12: Merge 2 empty trees")
        resultTree = create_tree(self.emptyTree1, self.emptyTree2, 'merge')
        self.emptyBST = BST2()
        self.assertEqual(resultTree, self.emptyBST, "Fail: Merge 2 empty trees")
        print()

    def test_intersection_empty_trees(self):
        print("\nCase 13: Intersection of 2 empty trees")
        resultTree = create_tree(self.emptyTree1, self.emptyTree2, 'intersection')
        self.emptyBST = BST2()
        self.assertEqual(resultTree, self.emptyBST, "Fail: Intersection of 2 empty trees")
        print()

    def test_difference_empty_trees(self):
        print("\nCase 14: 'Difference' of 2 empty trees")
        resultTree = create_tree(self.emptyTree1, self.emptyTree2, 'difference')
        self.emptyBST = BST2()
        self.assertEqual(resultTree, self.emptyBST, "Fail: 'Difference' of 2 empty trees")
        print()

    def test_merge_one_empty_tree(self):
        print("\nCase 15: 'Merge' with 1 empty tree")
        resultTree = create_tree(self.emptyTree1, self.tree3, 'merge')
        self.expectedTree = BST2()
        self.expectedTree.insert(20)
        self.expectedTree.insert(10)
        self.expectedTree.insert(30)
        self.assertEqual(resultTree, self.expectedTree, "Fail: 'Merge' with 1 empty tree")
        print()

    def test_intersection_one_empty_tree(self):
        print("\nCase 16: 'intersection' with 1 empty tree")
        resultTree = create_tree(self.emptyTree1, self.tree3, 'intersection')
        self.assertEqual(resultTree, self.emptyTree1, "Fail: 'intersection' with 1 empty tree")
        print()

    def test_difference_tree1_isEmpty(self):
        print("\nCase 17: 'difference' with tree1 an Empty Tree and tree2 not")
        resultTree = create_tree(self.emptyTree1, self.tree3, 'difference')
        self.assertEqual(resultTree, self.emptyTree1, "Fail: 'difference' with tree1 an Empty Tree and tree2 not")
        print()

    def test_difference_tree2_isEmpty(self):
        print("\nCase 18: 'difference' with tree2 an Empty Tree and tree1 not")
        resultTree = create_tree(self.tree3, self.emptyTree1, 'difference')
        self.expectedTree = BST2() # Same as tree3
        self.expectedTree.insert(20)
        self.expectedTree.insert(10)
        self.expectedTree.insert(30)
        self.assertEqual(resultTree, self.expectedTree, "Fail: 'difference' with tree2 an Empty Tree and tree1 not")
        print()

    def test_merge_common_elements(self): # Should not duplicate
        print("\nCase 19: 'merge' trees that have common elements")
        resultTree = create_tree(self.tree1, self.tree2, 'merge')
        self.expectedTree = BST2()
        self.expectedTree.insert(3)
        self.expectedTree.insert(2)
        self.expectedTree.insert(6)
        self.expectedTree.insert(1)
        self.expectedTree.insert(4)
        self.expectedTree.insert(7)
        self.expectedTree.insert(0)
        self.expectedTree.insert(5)
        self.expectedTree.insert(8)
        self.expectedTree.insert(16)
        self.expectedTree.insert(23)

        self.assertEqual(resultTree, self.expectedTree, "Fail: 'merge' trees that have common elements. Should not duplicate them.")
        print()

    def test_intersection_no_elements_in_common(self): # Should return an empty tree
        print("\nCase 20: 'intersection' of trees that have 0 elements in common")
        resultTree = create_tree(self.tree2, self.tree3, 'intersection')
        self.assertEqual(resultTree, self.emptyTree1, "Fail: 'intersection' of trees that have 0 elements in common. Should return an empty tree")
        print()

    def test_difference_all_elements_are_common(self): # Should return an empty tree
        print("\nCase 21: 'difference' of trees that have all elements in common")
        resultTree = create_tree(self.tree3, self.tree4, 'difference')
        self.assertEqual(resultTree, self.emptyTree1, "Fail: 'intersection' of trees that have all elements in common. Should return an empty tree")
        print()

    def test_invalid_opc(self):
        print("\nCase 22: Invalid 'opc' introduced")
        resultTree = create_tree(self.tree1, self.tree2, 'notExpectedOPC')
        self.assertEqual(resultTree, self.emptyTree1, "Fail: Invalid 'opc' introduced")
        print()

# Some usage examples
if __name__ == '__main__':
    unittest.main()
