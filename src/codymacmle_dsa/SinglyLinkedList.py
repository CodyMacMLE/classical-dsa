
# A classical single linked list
class SinglyLinkedList:
    # A Node for data and next
    class Node:
        def __init__(self, data, _next = None):
            self._data = data
            self._next = _next

    def __init__(self, data = None):
        self._head = None
        # If the data was entered => enter
        if data is not None:
            self.pushFront(data)

    """
    Allows the use of len() on a singly linked list.
    """
    def __len__(self):
        return self.size()

    """
    Helper method to allow client to use "in" operator.
    This member function keeps track of the current iteration
    """
    def __iter__(self):
        self.current = self._head
        return self

    """
    Helper method to allow client to use "in" operator. 
    This member function returns the data in the current iteration and sets to the next node. If current node is null it
    will stop the iteration.
    """
    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current._data
            self.current = self.current._next
            return data

    """
        Helper method to allow client to use == operator. 
        This function checks if the data is the same as the another list
    """
    def __eq__(self, other):
        if self.isEmpty() or other.isEmpty():
            return False

        self_len = len(self)
        other_len = len(other)

        if self_len != other_len:
            return False

        self_copy = self.copy()
        other_copy = other.copy()
        self_copy.sort()
        other_copy.sort()
        it_self = self_copy._head
        it_other = other_copy._head
        while it_self is not None and it_other is not None:
            if it_other._data == it_self._data:
                it_other = it_other._next
                it_self = it_self._next
            else:
                return False

        return True

    """
        Helper method to allow client to use != operator. 
        This function checks if the data is not the same as the another list
    """
    def __ne__(self, other):
        if self == other:
            return False
        else:
            return True

    """
    getFront() returns the data of the first node in the list
    Parameters: None
    Returns (data): the data of the first node in the list 
    """
    def getFront(self):
        return self._head

    """
    getBack() returns the data of the last node in the list
    Parameters: None
    Returns (data): the data of the last node in the list 
    """
    def getBack(self):
        if self._head is None:
            return None
        else:
            current = self._head
            while current._next is not None:
                current = current._next
            return current._data

    """
    list[index] returns the data of the node specified by index
    Parameters: [index position]
    Returns (data): the data of the node specified by index 
    """
    def __getitem__(self, index):
        if index < 0 or index > self.size():
            raise IndexError("out of bounds")
        else:
            current = self._head
            for i in range(0, index):
                if current._next is None:
                    raise IndexError("out of bounds")
                current = current._next
            return current._data

    """
    pushFront(data) accepts either data type or an iterable list of data types that will be pushed to the front of the list.
    The data will be pushed to the front of the list in the same order it appears in the list.
    Parameter:
        - Data (data type || list): data to be pushed to the front of the list.
    Returns:
        - None
    """
    def pushFront(self, data):
        # if the data is in a list => enter
        if isinstance(data, list):
            # reversed loop so that the first item in the list is pushed last
            for item in reversed(data):
                # call push front to push front a single data type in the list
                self.pushFront(item)
        # if the data is a single data type and not in a list => enter
        else:
            # if the list is empty => enter
            if self._head is None:
                # set the head to a new node with its _next attribute set to None (default)
                self._head = self.Node(data)
                # exit
                return
            # if the list has at least one node => enter
            else:
                # store the front node as current
                current = self._head
                # store the new front node as front with the _next attribute set to current
                front = self.Node(data, current)
                # move _head ref from current to point to front
                self._head = front

    """
    pushBack(data) accepts either data type or an iterable list of data types that will be pushed to the back of the list.
    The data will be pushed to the back of the list in the same order it appears in the list.
    Parameter:
        - Data (data type || list): data to be pushed to the back of the list.
    Returns:
        - None
    """
    def pushBack(self, data):
        # get the last node in the list
        last = self._head
        while last is not None and last._next is not None:
            last = last._next
        # if the data is a list => enter
        if isinstance(data, list):
            # iterate through the list
            for item in data:
                # create a new node with _next pointing to None
                newNode = self.Node(item)
                # set the last node to point to the new node
                last._next = newNode
                # set last to newNode so the next iteration using the new back node
                last = newNode
        else:
            # if the list is empty
            if self._head is None:
                self._head = self.Node(data)
            else:
                # create a new node with _next pointing to None
                newNode = self.Node(data)
                # set the last node to point to the new node
                last._next = newNode

    """
    SinglyLinkedList[index] = data accepts either data type or an iterable list of data types that will be pushed at 
    and behind the specified index in the list. The data will be pushed into the list in the same order it appears in the list.
    Parameter:
        - None
    Returns:
        - None
    """
    def __setitem__(self, index, data):
        if index < 0 or index > self.size():
            raise IndexError("out of bounds")

        currentIdx = self._head
        # check if the head is empty before finding the index point, call push front
        if currentIdx is None or index == 0:
            self.pushFront(data)
            return

        # iterate, but keep the current Node one before the index
        for _ in range(0, index - 1):
            currentIdx = currentIdx._next

        # if the node is at the back of the list call pushBack()
        if currentIdx._next is None:
            self.pushBack(data)
            return

        # if the data is a list, iterate in reverse and push new nodes
        if isinstance(data, list):
            for item in reversed(data):
                newNode = self.Node(item, currentIdx._next)
                currentIdx._next = newNode
        # the data is a single type
        else:
            newNode = self.Node(data, currentIdx._next)
            currentIdx._next = newNode

    """
    popFront() deletes the first node in the list
    Parameters: None
    Returns: Data of the deleted node or None if it is an empty list
    """
    def popFront(self):
        if self.isEmpty():
            return None

        front = self._head
        data = front._data
        self._head = front._next
        del front
        return data

    """
    popBack() deletes the last node in the list
    Parameters: None
    Returns: Data of the deleted node or None if it is an empty list
    """
    def popBack(self):
        # special case where the list is already empty
        if self.isEmpty():
            return None

        # special case where only one item is in the list
        if self._head._next is None:
            return self.popFront()

        # case where nodes in the list is > 2
        previousNode = self._head
        # the previous node is set to one before the last Node
        while previousNode._next._next is not None:
            previousNode = previousNode._next


        data = previousNode._next._data
        del previousNode._next
        previousNode._next = None
        return data

    """
    del singlyLinkedList[index] deletes the node in the list at the specified index
    parameters: None
    Returns: Data of the deleted node or None if it is an empty list
    """
    def __delitem__(self, index):
        if index < 0 or index > self.size():
            raise IndexError("out of bounds")

        # if the list is empty
        if self._head is None:
            return None

        # if the list only has one node
        if index == 0:
            return self.popFront()

        # iterating to the node previous to the specified index
        previousNode = self._head
        for _ in range(0, index - 1):
            previousNode = previousNode._next

        # if the node after the index is None, call popBack()
        if previousNode._next._next is None:
            return self.popBack()

        data = previousNode._next._data
        nextNode = previousNode._next._next
        del previousNode._next
        previousNode._next = nextNode
        return data

    """
    clear() removes all nodes in the list
    Parameters: None
    Returns: None
    """
    def clear(self):
        currentNode = self._head
        if currentNode is None:
            return

        while currentNode._next is not None:
            nextNode = currentNode._next
            del currentNode
            currentNode = nextNode
        self._head = None

    """
    Checks if the list is empty.
    Parameters: None
    Returns: True/False
    """
    def isEmpty(self):
        if self._head is None:
            return True
        else:
            return False

    """
    Iterate through the list and counts the size of the list.
    Parameters: None
    Returns: integer
    """
    def size(self):
        # if empty return 0
        if self.isEmpty():
            return 0
        # count as we iterate
        i = 1
        current = self._head
        while current._next is not None:
            i += 1
            current = current._next
        # return the number of iterations
        return i

    """
    middle() finds the middle node in the list or the node before it if the exact middle does not exist. If the list is empty, return None.
    Parameters: None
    Returns: pointer to middle node or None
    """
    def middle(self):
        # if the list is empty, return none
        if self.isEmpty():
            return None

        # find the middle
        result = self.size() / 2
        # if the middle is a floating point, then enter
        if result % 1 != 0:
            # find the middle (floor) add one
            result = self.size() // 2 + 1

        # iterate through the list to the middle and return the node's pointer
        currentNode = self._head
        for _ in range(0, int(result) - 1):
            currentNode = currentNode._next
        return currentNode

    """
    find() finds the first node in the list of the specified value
    Parameters: data: value to find
    Returns: pointer to first node or None
    """
    def find(self, data):
        if self.isEmpty():
            return None

        currentNode = self._head
        while currentNode is not None:
            if currentNode._data == data:
                return currentNode
            currentNode = currentNode._next
        return None

    """
    contains finds if the value exists in the list
    Parameters: data: value to find
    Returns: true or false
    """
    def contains(self, data):
        if self.isEmpty():
            return False
        ptr = self.find(data)
        if ptr is None:
            return False
        else:
            return True

    """
    sort() will sort the list using 
    Parameters: None
    Returns: None
    """
    def sort(self, reverse=False):
        # check if the array is 0
        if self.isEmpty():
            return
        # create an iterator to go through the list
        it = self._head
        # create a sorted list with self._head as first data
        sortedList = SinglyLinkedList(it._data)

        # make the iterator the second node in the list
        it = it._next
        # checks if the second node in the list is none
        if it is None:
            return

        if it._data > sortedList._head._data:
            sortedList.pushBack(it._data)
        else:
            sortedList.pushFront(it._data)

        # make the iterator the third node in the list
        it = it._next
        # loop through the current list (n - 2)
        while it is not None:
            # create an iterator for the sorted list
            sortedIt = sortedList._head
            idx = 0  # index of the sorted list
            # for each iteration for the unsorted list, loop through the unsorted list
            while sortedIt is not None:
                if sortedIt._next is None:
                    sortedList.pushBack(it._data)
                    break
                elif sortedIt._data <= it._data < sortedIt._next._data:
                    sortedList[idx + 1] = it._data
                    break
                else:
                    idx+= 1
                    sortedIt = sortedIt._next

            # increments iterator (prevents infinite loop)
            it = it._next

        self.clear()
        sortedIt = sortedList._head
        if reverse:
            while sortedIt is not None:
                self.pushFront(sortedIt._data)
                sortedIt = sortedIt._next
        else:
            while sortedIt is not None:
                self.pushBack(sortedIt._data)
                sortedIt = sortedIt._next

    """
    Description:
        Reverses the list 
    Parameters: 
        None
    Returns:
        A new SinglyLinkedList in reverse order
    """
    def reverse(self):
        newSll = SinglyLinkedList()

        it = self._head
        while it is not None:
            newSll.pushFront(it._data)
            it = it._next

        return newSll

    """
    toList converts the singlyLinkedlist into a python list.
    Parameters: None
    Returns: List
    """
    def toList(self):
        pyList = []
        for i in self:
            pyList.append(i)
        return pyList

    """
    Description:
        Copies one singly linked list into a new singly linked list.
    Parameters: 
        None
    Returns: 
        A new singly linked list of the same data and order.
    """
    def copy(self):
        it = self._head
        newSll = SinglyLinkedList()

        if self.isEmpty():
            return newSll

        while it is not None:
            newSll.pushBack(it._data)
            it = it._next

        return newSll

    """
    Description:
        Merges one singly linked list onto another singly linked list
    Parameters: 
        List1: The first singly linked list (left side of merge)
        List2: The second singly linked list (right side of merge)
    Returns: 
        A new singly linked list of the same data and order (L-list, R-list).
    """
    @staticmethod
    def merge(list1, list2):
        if list1.isEmpty():
            return list2.copy()
        if list2.isEmpty():
            return list1.copy()

        mergedList = SinglyLinkedList()
        list1_iter = list1._head
        list2_iter = list2._head
        while list1_iter is not None:
            mergedList.pushBack(list1_iter._data)
            list1_iter = list1_iter._next
        while list2_iter is not None:
            mergedList.pushBack(list2_iter._data)
            list2_iter = list2_iter._next

        return mergedList