class HashTable:

    class SLList:

        class Node:
            def __init__(self, _key, _value, _prev = None, _next = None):
                self._key = _key
                self._value = _value
                self._prev = _prev
                self._next = _next

        def __init__(self):
            self._head = None

        def __iter__(self):
            self.current = self._head
            return self

        def __next__(self):
            if self.current is None:
                raise StopIteration
            else:
                node_ptr = self.current
                self.current = self.current._next
                return node_ptr

        def pushFront(self, key, value):
            # creates a node that points to either the head node if it exists or None
            node = self.Node(key, value, _next = self._head)
            # checks if head is None (special case when the list is empty)
            if self._head is not None:
                # sets current head ._prev to the new node
                self._head._prev = node
            # sets the head to the new node
            self._head = node

        def __getitem__(self, key):
            # iterate through the list
            for node in self.__iter__():
                # check if the key matches
                if node._key == key:
                    # returns ptr of node if found
                    return node
            return None

        def __setitem__(self, key, value):
            node = self[key]
            if node is not None:
                node._value = value
            else:
                self.pushFront(key, value)

        def __delitem__(self, key):
            node = self[key]
            if node is not None:
                if node._next is None:
                    node._prev._next = None
                    del node
                elif node._prev is None:
                    node._next._prev = None
                    del node
                else:
                    node._prev._next = node._next
                    node._next._prev = node._prev
                    del node
            else:
                raise KeyError

        def __contains__(self, key):
            node = self[key]
            if node is None:
                return False
            else:
                return True

        def __len__(self):
            length = 0
            for node in self.__iter__():
                length += 1
            return length

    def __init__(self, buckets = 10):
        self._buckets = [self.SLList() for _ in range(0,buckets)]
        self._size = buckets

    def put(self, key, value):
        hash_code = hash(key)
        bucket = hash_code % self._size

        if len(bucket) == 0:
            self._buckets[bucket].pushFront(key, value)
        else:
            if key in self._buckets[bucket]:
                raise KeyError
            else:
                self._buckets[bucket].pushFront(key, value)

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def __contains__(self, key):
        pass