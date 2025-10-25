

class DoublyLinkedList:
    class Node:
        def __init__(self, data, _prev = None, _next = None):
            self._prev = _prev
            self._data = data
            self._next = _next

        def setPrev(self, _prev):
            self._prev = _prev

        def setData(self, data):
            self._data = data

        def setNext(self, _next):
            self._next = _next

        def getPrev(self):
            return self._prev

        def getData(self):
            return self._data

        def getNext(self):
            return self._next

    def __init__(self, data = None):
        if data:
            self._tail = self.Node(None, None, None)
            nextNode = self._tail
            if isinstance(data, list):
                for item in reversed(data):
                    newNode = self.Node(item, None, nextNode)
                    nextNode.setPrev(newNode)
                    nextNode = newNode
            else:
                newNode = self.Node(data, None, self._tail)
                nextNode.setPrev(newNode)
                nextNode = newNode
            self._head = self.Node(None, None, nextNode)
            self._head.getNext().setPrev(self._head)

        else:
            self._head = self.Node(None)
            self._tail = self.Node(None, _prev = self._head)
            self._head.setNext(self._tail)

    def _getFirst(self):
        return self._head.getNext()

    def _getLast(self):
        return self._tail.getPrev()

    def getFirst(self):
        return self._getFirst().getData()

    def getLast(self):
        return self._getLast().getData()

    def _iterate(self):
        item = self._getFirst()
        while item.getData() is not None:
            yield item
            item = item.getNext()

    def __iter__(self):
        current = self._getFirst()
        while current.getData() is not None:
            yield current.getData()
            current = current.getNext()

    def __len__(self):
        counter = 0
        for _ in self.__iter__():
            counter += 1
        return counter

    def empty(self):
        if self._getFirst() == self._tail:
            return True
        return False

    def pushFront(self, data):
        firstNode = self._getFirst()
        newNode = self.Node(data, self._head, firstNode)
        self._head.setNext(newNode)
        firstNode.setPrev(newNode)

    def pushBack(self, data):
        lastNode = self._getLast()
        newNode = self.Node(data, lastNode, self._tail)
        self._tail.setPrev(newNode)
        lastNode.setNext(newNode)

    def addBefore(self, index, data):
        if index < 0 or index > len(self):
            raise IndexError("Out of bounds")

        if self.empty() or index == 0:
            self.pushFront(data)
            return

        rightNode = self._getFirst()
        for _ in range(0, index):
            rightNode = rightNode.getNext()

        leftNode = rightNode.getPrev()
        newNode = self.Node(data, leftNode, rightNode)
        leftNode.setNext(newNode)
        rightNode.setPrev(newNode)

    def addAfter(self, index, data):
        if index < 0 or index > len(self):
            raise IndexError("Out of bounds")

        if self.empty():
            self.pushFront(data)
            return

        leftNode = self._getFirst()
        for _ in range(0, index):
            leftNode = leftNode.getNext()

        rightNode = leftNode.getNext()
        newNode = self.Node(data, leftNode, rightNode)
        leftNode.setNext(newNode)
        rightNode.setPrev(newNode)

    def _search(self, data):
        ptr = None
        for node in self._iterate():
            if data == node.getData():
                ptr = node
                break
        return ptr

    def searchAdd(self, search, data):
        leftNode = self._search(search)
        if leftNode is not None:
            rightNode = leftNode.getNext()
            newNode = self.Node(data, leftNode, rightNode)
            leftNode.setNext(newNode)
            rightNode.setPrev(newNode)

    def _delete(self, ptr):
        # Manually unlink the node from the list
        leftNode = ptr.getPrev()
        rightNode = ptr.getNext()

        # Connect the neighbors to each other
        leftNode.setNext(rightNode)
        rightNode.setPrev(leftNode)

        # Now delete the node reference
        del ptr

    def delFirst(self, search):
        if search is None:
            return

        ptr_node = self._search(search)
        if ptr_node is not None:
            self._delete(ptr_node)

    def delAll(self, search):
        for node in self._iterate():
            if search == node.getData():
                self._delete(node)

    def reverse(self):
        dLL = DoublyLinkedList()
        for node_data in self:
            dLL.pushFront(node_data)

        return dLL

    def middleNode(self):
        if self.empty():
            return None

        length = len(self)
        if length == 1:
            return self._getFirst()

        middle = None
        if length % 2:
            middle = length/2
        else:
            middle = (length/2) - 0.5

        middle = int(middle)

        node_ptr = self._getFirst()
        for _ in range (0, middle):
            node_ptr = node_ptr.getNext()

        return node_ptr

    @staticmethod
    def merge(leftList, rightList):
        if len(leftList) == 0:
            return rightList
        if len(rightList) == 0:
            return leftList

        left = list(leftList)
        right = list(rightList)
        leftIdx = 0
        rightIdx = 0
        newList = DoublyLinkedList()
        while leftIdx < len(left) and rightIdx < len(right):
            if left[leftIdx] < right[rightIdx]:
                newList.pushBack(left[leftIdx])
                leftIdx += 1
            else:
                newList.pushBack(right[rightIdx])
                rightIdx += 1

        while leftIdx < len(left):
            newList.pushBack(left[leftIdx])
            leftIdx += 1
        while rightIdx < len(right):
            newList.pushBack(right[rightIdx])
            rightIdx += 1

        return newList

    def findMax(self):
        if self.empty():
            return None

        _max = self.getFirst()
        for item in self:
            if item > _max:
                _max = item
        return _max

    def addSorted(self, value):
        if self.empty():
            self.pushFront(value)
            return

        if self.getFirst() > value:
            self.pushFront(value)
            return

        for ptr in self._iterate():
            nxt = ptr.getNext()
            nxt_data = nxt.getData()

            if nxt_data is None:
                self.pushBack(value)
                return

            if ptr.getData() <= value and nxt_data > value:
                newNode = self.Node(value, ptr, ptr.getNext())
                ptr.getNext().setPrev(newNode)
                ptr.setNext(newNode)
                return

    def removeDuplicates(self):
        duplicates = dict()

        for ptr in self._iterate():
            ptrData = ptr.getData()
            if ptrData in duplicates:
                duplicates[ptrData].append(ptr)
            if ptrData not in duplicates:
                duplicates[ptrData] = []

        for key, value in duplicates.items():
            for ptr in value:
                prev_ptr = ptr.getPrev()
                next_ptr = ptr.getNext()
                prev_ptr.setNext(next_ptr)
                next_ptr.setPrev(prev_ptr)
                del ptr





