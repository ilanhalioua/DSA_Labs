import unittest
from phase1 import SList2


class Test(unittest.TestCase):

    # setUp is a method which is ran before a test method is executed.
    # This is useful if you need some data (for example) to be present before running a test.
    def setUp(self):
        self.lEmpty = SList2()

        self.l1 = SList2()
        self.l1.addFirst(5)
        self.l1.addFirst(5)
        self.l1.addFirst(6)
        self.l1.addFirst(6)
        self.l1.addFirst(6)

        self.l2 = SList2()
        self.l2.addFirst(5)
        self.l2.addFirst(5)
        self.l2.addFirst(5)
        self.l2.addFirst(6)
        self.l2.addFirst(6)
        self.l2.addFirst(6)

        self.l3 = SList2()
        self.l3.addFirst(4)

        self.l4 = SList2()
        for i in range(4):
            self.l4.addLast(3)

        self.lLoop = SList2()
        self.lLoop.addFirst(2)
        self.lLoop.addFirst(3)
        self.lLoop.addFirst(4)
        self.lLoop.addFirst(6)
        self.lLoop.create_loop(1)

        self.lLoop1 = SList2()
        self.lLoop1.addFirst(3)
        self.lLoop1.create_loop(0)

        pass

    # implement here your test cases

    def test1_delLargestSeq(self):
        print('\nCase 1: delLargestSeq in a Empty list')
        self.lEmpty.delLargestSeq()
        self.expected = SList2()
        # self.assertEqual(largestSeq, None??, "Fail: delLargestSeq in a Empty list")
        self.assertEqual(str(self.lEmpty), str(self.expected), "Fail: delLargestSeq in a Empty list")
        print()

    def test2_delLargestSeq(self):
        print('\nCase 2: delLargestSeq -> Only 1 largest sequence')
        self.l1.delLargestSeq()
        self.expected = SList2()
        self.expected.addFirst(5)
        self.expected.addFirst(5)
        self.assertEqual(str(self.l1), str(self.expected), "Fail: delLargestSeq -> Only 1 largest sequence")
        print()

    def test3_delLargestSeq(self):
        print('\nCase 3: delLargestSeq -> More than one largest sequence. Removes the last one found')
        self.l2.delLargestSeq()
        self.expected = SList2()
        self.expected.addFirst(6)
        self.expected.addFirst(6)
        self.expected.addFirst(6)
        self.assertEqual(str(self.l2), str(self.expected), "Fail: delLargestSeq -> More than one largest sequence")
        print()

    def test4_delLargestSeq(self):
        print('\nCase 4: delLargestSeq -> Input list of size 1 (One sequence). Results in a empty list')
        self.l3.delLargestSeq()
        self.expected = SList2()
        self.assertEqual(str(self.l3), str(self.expected), "Fail: delLargestSeq -> Input list of size 1 (One sequence)")
        print()

    def test5_delLargestSeq(self):
        print('\nCase 5: delLargestSeq -> Input list just contains one sequence. Results in a empty list')
        self.l4.delLargestSeq()
        self.expected = SList2()
        self.assertEqual(str(self.l4), str(self.expected), "Fail: delLargestSeq -> Input list just contains 1 sequence")
        print()

    def test6_fix_loop(self):
        print('\nCase 6: fix_loop in an Empty list. Return False')
        ret = self.lEmpty.fix_loop()
        self.expected = SList2()
        self.assertEqual(ret, False, "Fail: fix_loop in an Empty list")
        self.assertEqual(str(self.lEmpty), str(self.expected), "Fail: fix_loop in an Empty list")
        print()

    def test7_fix_loop(self):
        print('\nCase 7: fix_loop -> No loops. Return False')
        ret = self.l1.fix_loop()
        self.expected = SList2()
        self.expected.addFirst(5)
        self.expected.addFirst(5)
        self.expected.addFirst(6)
        self.expected.addFirst(6)
        self.expected.addFirst(6)
        self.assertEqual(ret, False, "Fail: fix_loop -> No loops")
        self.assertEqual(str(self.l1), str(self.expected), "Fail: fix_loop -> No loops")
        print()

    def test8_fix_loop(self):
        print('\nCase 8: fix_loop -> Input list has a loop at i-th node (i>1). Fix it and return True')
        ret = self.lLoop.fix_loop()
        self.expected = SList2()
        self.expected.addFirst(2)
        self.expected.addFirst(3)
        self.expected.addFirst(4)
        self.expected.addFirst(6)
        self.assertEqual(ret, True, "Fail: fix_loop -> Input list has a loop at i-th node (i>1)")
        self.assertEqual(str(self.lLoop), str(self.expected), "Fail: fix_loop-> Input list has loop at i-th node (i>1)")
        print()

    def test9_fix_loop(self):
        print('\nCase 9: fix_loop -> Input list of size 1 with loop. Fix it and return True')
        ret = self.lLoop1.fix_loop()
        self.expected = SList2()
        self.expected.addFirst(3)
        self.assertEqual(ret, True, "Fail: fix_loop -> Input list of size 1 with loop")
        self.assertEqual(str(self.lLoop1), str(self.expected), "Fail: fix_loop -> Input list of size 1 with loop")
        print()

    def test10_leftrightShift(self):
        print('\nCase 10: leftrightShift in an Empty list')
        left = True  # True/False
        n = 2  # For any n
        self.lEmpty.leftrightShift(left, n)
        self.expected = SList2()
        self.assertEqual(str(self.lEmpty), str(self.expected), "Fail: leftrightShift in an Empty list")
        print()

    def test11_leftrightShift(self):
        print('\nCase 11: leftrightShift -> (n < 0)')
        left = True
        n = -3
        self.l1.leftrightShift(left, n)
        self.expected = SList2()
        self.expected.addFirst(5)
        self.expected.addFirst(5)
        self.expected.addFirst(6)
        self.expected.addFirst(6)
        self.expected.addFirst(6)
        self.assertEqual(str(self.l1), str(self.expected), "Fail: leftrightShift -> (n < 0)")
        print()

    def test12_leftrightShift(self):
        print('\nCase 12: leftrightShift -> (n = 0)')
        left = True
        n = 0
        self.l1.leftrightShift(left, n)
        self.expected = SList2()
        self.expected.addFirst(5)
        self.expected.addFirst(5)
        self.expected.addFirst(6)
        self.expected.addFirst(6)
        self.expected.addFirst(6)
        self.assertEqual(str(self.l1), str(self.expected), "Fail: leftrightShift -> (n = 0)")
        print()

    def test13_leftrightShift(self):
        print('\nCase 13: leftrightShift -> (0 < n < size_of_list) with (Left = True)')
        left = True
        n = 2
        self.l1.leftrightShift(left, n)  # l1: [6,6,6,5,5] -> [6,5,5,6,6]
        self.expected = SList2()
        self.expected.addFirst(6)
        self.expected.addFirst(6)
        self.expected.addFirst(5)
        self.expected.addFirst(5)
        self.expected.addFirst(6)
        self.assertEqual(str(self.l1), str(self.expected), "Fail: leftrightShift -> (0 < n < size_of_list),Left = True")
        print()

    def test14_leftrightShift(self):
        print('\nCase 14: leftrightShift -> (n = size of list)')
        left = True
        n = self.l1.__len__()
        self.l1.leftrightShift(left, n)
        self.expected = SList2()
        self.expected.addFirst(5)
        self.expected.addFirst(5)
        self.expected.addFirst(6)
        self.expected.addFirst(6)
        self.expected.addFirst(6)
        self.assertEqual(str(self.l1), str(self.expected), "Fail: leftrightShift -> (n = size of list)")
        print()

    def test15_leftrightShift(self):
        print('\nCase 15: leftrightShift -> (n > size of list)')
        left = True
        n = self.l1.__len__() + 2
        self.l1.leftrightShift(left, n)
        self.expected = SList2()
        self.expected.addFirst(5)
        self.expected.addFirst(5)
        self.expected.addFirst(6)
        self.expected.addFirst(6)
        self.expected.addFirst(6)
        self.assertEqual(str(self.l1), str(self.expected), "Fail: leftrightShift -> (n > size of list)")
        print()

    def test16_leftrightShift(self):
        print('\nCase 16: leftrightShift -> Argument "left" in function is not of boolean type')
        left = -123
        n = self.l1.__len__() + 2
        self.l1.leftrightShift(left, n)
        self.expected = SList2()
        self.expected.addFirst(5)
        self.expected.addFirst(5)
        self.expected.addFirst(6)
        self.expected.addFirst(6)
        self.expected.addFirst(6)
        self.assertEqual(str(self.l1), str(self.expected), "Fail: leftrightShift -> Argument 'left' in function is not of boolean type")
        print()

    def test17_leftrightShift(self):
        print('\nCase 17: leftrightShift -> (0 < n < size_of_list) with (Left = False)')
        left = False
        n = 2
        self.l1.leftrightShift(left, n)
        self.expected = SList2()
        self.expected.addFirst(6)
        self.expected.addFirst(6)
        self.expected.addFirst(6)
        self.expected.addFirst(5)
        self.expected.addFirst(5)
        self.assertEqual(str(self.l1), str(self.expected), "Fail: leftrightShift-> (0 < n < size_of_list) Left = False")
        print()

    def test18_leftrightShift(self):
        print('\nCase 18: leftrightShift -> Input list of size 1. Results in the same list')
        left = False  # Works for True too
        n = 1
        self.expected = self.l3
        self.l3.leftrightShift(left, n)
        self.assertEqual(str(self.l3), str(self.expected), "Fail: leftrightShift -> Input list of size 1")
        print()

if __name__ == "__main__":
    unittest.main()
