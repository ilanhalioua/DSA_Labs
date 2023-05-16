from slistH import SList
from slistH import SNode

import sys


class SList2(SList):

    def delLargestSeq(self):  # Works O(n)
        # removes the last largest sequence of numbers inside the list
        # A,B,a,b are the index bounds for the largest sequence found and the current sequence processed respectively
        # M denotes the length of the largest sequence and length will be the analogous for the current one processed
        A = 0
        B = 0
        a = 0
        b = 0
        M = 1
        node = self._head
        if node is not None:
            while node.next is not None:
                if node.elem == node.next.elem:
                    b = b + 1
                    length = b - a + 1
                    if length >= M:
                        M = length
                        A = a
                        B = b
                else:
                    length = b - a + 1
                    if length >= M:
                        M = length
                        A = a
                        B = b
                    a = b + 1
                    b = b + 1
                node = node.next

                # exception: case where the sequence is just 1 element long so that the last element should be removed
                if M == 1:
                    A = self._size - 1
                    B = self._size - 1
                ####

            # now that we know that the largest sequence is in the index range A-B we just have to remove it
            if M == self._size:  # the whole list is the sequence
                self._head = None
            elif A == 0:  # we just have to remove the first M nodes
                # with ease, we can take advantage of our function removefirst M times
                for i in range(0, M):
                    self.removeFirst()
            else:
                # we have to link the node at index A-1 with the one at index B+1
                # this deletes the largest(last) sequence (index range A-B) of the list
                left = self._head
                for i in range(0, A - 1):
                    left = left.next
                right = left
                for i in range(0, B - A + 2):  # Same as range (A-1,B+1)
                    right = right.next
                left.next = right

    def fix_loop(self):  # Works O(n)
        # Check if the linked list is empty
        if self.isEmpty() is True:
            return False

        # Initialize two pointers for traversal of the linked list
        slow = fast = self._head

        # Traverse the linked list using two pointers until a loop is detected (if any)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If the pointers meet, it means there is a loop in the linked list
            if slow == fast:
                break

        # If the pointers never meet, there is no loop in the linked list
        if slow != fast:  # "LastNode".next was None so no loop was found in input list
            return False

        # Reset one of the pointers to the head of the linked list
        slow = self._head
        # Traverse the linked list using two pointers until they meet at the start of the loop
        while slow != fast:
            slow = slow.next
            fast = fast.next

        # Traverse the linked list using one pointer to get to the last node of the loop
        while fast.next != slow:
            fast = fast.next

        # Remove the loop by making the last node in the loop point to None
        fast.next = None

        return True
        pass

    def create_loop(self, position): # GIVEN
        # this method is used to force a loop in a singly linked list
        if position < 0 or position > len(self) - 1:
            raise ValueError(f"Position out of range [{0} - {len(self) - 1}]")

        current = self._head
        i = 0

        # We reach position to save the reference
        while current and i < position:
            current = current.next
            i += 1

        # We reach to tail node and set the loop
        start_node = current
        print(f"Creating a loop starting from {start_node.elem}")
        while current.next:
            current = current.next
        current.next = start_node

    def printLoop(self, position):  # Position should be the same as introduced in createLoop function
        # function to print a SList with loop
        temp = self._head
        for i in range(0, self._size + position):
            print(temp.elem, end="->")
            temp = temp.next
        pass

    def leftrightShift(self, left, n):  # Works O(n)
        # implement here your solution
        if 0 < n < self.__len__():
            current_node = self._head

            if left is True:
                p = n-1  # Position in input list of futureLastNode when left == True
            else:
                p = self.__len__() - (n+1)  # Position in input list of futureLastNode when left == False

            # The algorithm designed for 'shifting' is the same for left=True and left=False:
            while (p) != 0:  # Go to the node that will be the last node in the output list
                current_node = current_node.next
                p -= 1

            futureLastNode = current_node  # Save it
            # The next to it, will be the Head in the output list:
            futureHead = current_node.next  # Save it

            while current_node.next:  # Continue passing through nodes, until reaching the last node of input list
                current_node = current_node.next

            current_node.next = self._head  # Link last node with head
            futureLastNode.next = None  # Update end of list
            self._head = futureHead  # Update head of list
        pass


if __name__ == '__main__':
    l = SList2()
    print("list:", str(l))
    print("len:", len(l))

    for i in range(7):
        l.addLast(i + 1)

    print(l)
    print()

    l = SList2()
    print("list:", str(l))
    print("len:", len(l))

    for i in range(7):
        l.addLast(i + 1)

    print(l)
    print()

    # No loop yet, no changes applied
    l.fix_loop()
    print("No loop yet, no changes applied")
    print(l)
    print()

    # We force a loop
    l.create_loop(position=6)
    l.printLoop(3) # ADDED BY US
    print() # ADDED BY US
    l.fix_loop()
    print("Loop fixed, changes applied")
    print(l)
    print()
    print()

    l = SList2()
    for i in [1, 2, 3, 4, 5]:
        l.addLast(i)
    print(l.delLargestSeq())


    l = SList2()
    for i in range(7):
        l.addLast(i + 1)

    print(l)
    l.leftrightShift(False, 2)
    print(l)



