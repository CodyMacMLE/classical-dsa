# (No standard libraries are imported here in this file)

# Third-Party Imports
# import pytest

# Local Application/Library Imports
from codymacmle_dsa import DoublyLinkedList as dLL  # type: ignore


class TestDoublyLinkedList:

    def test_init_empty_data(self):
        test = dLL()
        assert test._getFirst().getData() is None
        assert test._getLast().getData() is None

    def test_init_single_data(self):
        test = dLL("Node 1")
        assert test._getFirst().getData() == "Node 1"
        assert test._getLast().getData() == "Node 1"

    def test_init_multi_data(self):
        test = dLL(["Node 1", "Node 2"])
        expectedData = ["Node 1", "Node 2", None]
        item = test._head
        assert item.getData() is None
        i = 0
        while item.getNext() is not None:
            assert item.getNext().getData() == expectedData[i]
            i += 1
            item = item.getNext()

    def test_iterate_returns_node_pointers(self):
        """Test that _iterate() returns node pointers, not data values."""
        expectedData = ["Node 1", "Node 2", "Node 3"]
        test = dLL(expectedData)

        # Collect all nodes from _iterate()
        nodes = list(test._iterate())

        # Should have 3 nodes (no sentinels)
        assert len(nodes) == 3

        # Verify each node has the correct data
        for node, expected_value in zip(nodes, expectedData):
            assert node.getData() == expected_value

        # Verify these are actual node objects with getNext() method
        assert hasattr(nodes[0], 'getNext')
        assert hasattr(nodes[0], 'getData')

        # Verify the nodes are linked correctly
        assert nodes[0].getNext() == nodes[1]
        assert nodes[1].getNext() == nodes[2]

    def test_iterator(self):
        expectedData = ["Node 1", "Node 2", "Node 3"]
        test = dLL(expectedData)
        for test_item, expected in zip(test, expectedData):
            # test_item and expected are paired together
            assert test_item == expected

    def test_len(self):
        test = dLL()
        assert len(test) == 0
        test = dLL([1,2,3,4,5])
        assert len(test) == 5

    def test_empty(self):
        test = dLL()
        assert test.empty() is True
        test = dLL("1")
        assert test.empty() is False

    def test_push_front(self):
        test = dLL()
        expectedData = ["1", "2", "3", "4"]
        for data in reversed(expectedData):
            test.pushFront(data)

        for expected, test_data in zip(expectedData, test):
            assert expected == test_data

    def test_push_back(self):
        test = dLL()
        expectedData = ["1", "2", "3", "4"]
        for data in expectedData:
            test.pushBack(data)

        for expected, test_data in zip(expectedData, test):
            assert expected == test_data

    def test_add_before(self):
        """Test adding a node before a specified index."""
        # Test adding before index in middle of list
        test = dLL(["Node 1", "Node 2", "Node 3"])
        test.addBefore(1, "New Node")
        expected = ["Node 1", "New Node", "Node 2", "Node 3"]
        assert list(test) == expected
        
        # Test adding before first element (index 0)
        test = dLL(["Node 1", "Node 2"])
        test.addBefore(0, "Front Node")
        expected = ["Front Node", "Node 1", "Node 2"]
        assert list(test) == expected
        
        # Test adding before last element
        test = dLL(["Node 1", "Node 2", "Node 3"])
        test.addBefore(2, "Before Last")
        expected = ["Node 1", "Node 2", "Before Last", "Node 3"]
        assert list(test) == expected
        
        # Test adding to single element list
        test = dLL("Only Node")
        test.addBefore(0, "New Front")
        expected = ["New Front", "Only Node"]
        assert list(test) == expected

        # Test out of bounds - negative index
        test = dLL(["Node 1", "Node 2"])
        try:
            test.addBefore(-1, "Bad Node")
            assert False, "Should have raised IndexError"
        except IndexError as e:
            assert str(e) == "Out of bounds"

        # Test out of bounds - index too large
        test = dLL(["Node 1", "Node 2"])
        try:
            test.addBefore(10, "Bad Node")
            assert False, "Should have raised IndexError"
        except IndexError as e:
            assert str(e) == "Out of bounds"

    def test_add_after(self):
        """Test adding a node after a specified index."""
        # Test adding after index in middle of list
        test = dLL(["Node 1", "Node 2", "Node 3"])
        test.addAfter(1, "New Node")
        expected = ["Node 1", "Node 2", "New Node", "Node 3"]
        assert list(test) == expected
        
        # Test adding after first element (index 0)
        test = dLL(["Node 1", "Node 2"])
        test.addAfter(0, "After First")
        expected = ["Node 1", "After First", "Node 2"]
        assert list(test) == expected
        
        # Test adding after last element
        test = dLL(["Node 1", "Node 2", "Node 3"])
        test.addAfter(2, "Back Node")
        expected = ["Node 1", "Node 2", "Node 3", "Back Node"]
        assert list(test) == expected
        
        # Test adding to single element list
        test = dLL("Only Node")
        test.addAfter(0, "New Back")
        expected = ["Only Node", "New Back"]
        assert list(test) == expected

        # Test out of bounds - negative index
        test = dLL(["Node 1", "Node 2"])
        try:
            test.addAfter(-1, "Bad Node")
            assert False, "Should have raised IndexError"
        except IndexError as e:
            assert str(e) == "Out of bounds"

        # Test out of bounds - index too large
        test = dLL(["Node 1", "Node 2"])
        try:
            test.addAfter(10, "Bad Node")
            assert False, "Should have raised IndexError"
        except IndexError as e:
            assert str(e) == "Out of bounds"

    def test_private_search(self):
        """Test _search() finds and returns pointer to first matching node."""
        # Test finding nodes in a list with multiple items
        test = dLL(["Node 1", "Node 2", "Node 3", "Node 2"])
        
        # Find first node
        ptr1 = test._search("Node 1")
        assert ptr1 is not None
        assert ptr1.getData() == "Node 1"
        assert ptr1 == test._getFirst()
        
        # Find middle node
        ptr2 = test._search("Node 2")
        assert ptr2 is not None
        assert ptr2.getData() == "Node 2"
        # Verify it's the FIRST occurrence (index 1, not 3)
        assert ptr2.getNext().getData() == "Node 3"
        
        # Find last unique node
        ptr3 = test._search("Node 3")
        assert ptr3 is not None
        assert ptr3.getData() == "Node 3"
        
        # Test node not found
        ptr_none = test._search("Node 99")
        assert ptr_none is None
        
        # Test search in single element list
        test_single = dLL("Only Node")
        ptr_single = test_single._search("Only Node")
        assert ptr_single is not None
        assert ptr_single.getData() == "Only Node"
        
        # Test search in empty list
        test_empty = dLL()
        ptr_empty = test_empty._search("Anything")
        assert ptr_empty is None
        
        # Verify returned pointer is a valid node object
        test2 = dLL(["A", "B", "C"])
        ptr = test2._search("B")
        assert hasattr(ptr, 'getData')
        assert hasattr(ptr, 'getNext')
        assert hasattr(ptr, 'getPrev')
        assert ptr.getPrev().getData() == "A"
        assert ptr.getNext().getData() == "C"
        
    def test_search_add(self):
        """Test searchAdd() adds data after found node, or does nothing if not found."""
        # Test adding after found node in middle of list
        test = dLL(["Node 1", "Node 2", "Node 3"])
        test.searchAdd("Node 2", "New Node")
        expected = ["Node 1", "Node 2", "New Node", "Node 3"]
        assert list(test) == expected

        # Test adding after first node
        test = dLL(["A", "B", "C"])
        test.searchAdd("A", "After A")
        expected = ["A", "After A", "B", "C"]
        assert list(test) == expected

        # Test adding after last node
        test = dLL(["A", "B", "C"])
        test.searchAdd("C", "After C")
        expected = ["A", "B", "C", "After C"]
        assert list(test) == expected

        # Test with duplicate values - should add after FIRST occurrence
        test = dLL(["A", "B", "C", "B"])
        test.searchAdd("B", "After First B")
        expected = ["A", "B", "After First B", "C", "B"]
        assert list(test) == expected

        # Test when value NOT found - list should remain unchanged
        test = dLL(["Node 1", "Node 2", "Node 3"])
        original_list = list(test)
        test.searchAdd("Node 99", "Should Not Add")
        assert list(test) == original_list
        assert len(test) == 3

        # Test in single element list when found
        test = dLL("Only Node")
        test.searchAdd("Only Node", "Added")
        expected = ["Only Node", "Added"]
        assert list(test) == expected

        # Test in single element list when NOT found
        test = dLL("Only Node")
        test.searchAdd("Wrong Node", "Should Not Add")
        expected = ["Only Node"]
        assert list(test) == expected

        # Test on empty list - should do nothing
        test = dLL()
        test.searchAdd("Anything", "Should Not Add")
        assert len(test) == 0
        assert list(test) == []

        # Test adding multiple times to same node
        test = dLL(["A", "B"])
        test.searchAdd("A", "First Add")
        test.searchAdd("A", "Second Add")
        expected = ["A", "Second Add", "First Add", "B"]
        assert list(test) == expected

    def test_del_first(self):
        """Test delFirst() deletes the first occurrence of a value from the list."""
        # Test deleting from middle of list
        test = dLL(["Node 1", "Node 2", "Node 3"])
        test.delFirst("Node 2")
        expected = ["Node 1", "Node 3"]
        assert list(test) == expected
        assert len(test) == 2
        
        # Test deleting first node
        test = dLL(["A", "B", "C"])
        test.delFirst("A")
        expected = ["B", "C"]
        assert list(test) == expected
        assert len(test) == 2
        
        # Test deleting last node
        test = dLL(["A", "B", "C"])
        test.delFirst("C")
        expected = ["A", "B"]
        assert list(test) == expected
        assert len(test) == 2
        
        # Test with duplicates - should delete FIRST occurrence only
        test = dLL(["A", "B", "C", "B", "D"])
        test.delFirst("B")
        expected = ["A", "C", "B", "D"]
        assert list(test) == expected
        assert len(test) == 4
        # Verify the second "B" is still there
        assert "B" in list(test)
        
        # Test deleting from single element list
        test = dLL("Only Node")
        test.delFirst("Only Node")
        expected = []
        assert list(test) == expected
        assert len(test) == 0
        assert test.empty() is True
        
        # Test when value NOT found - list should remain unchanged
        test = dLL(["Node 1", "Node 2", "Node 3"])
        original_list = list(test)
        test.delFirst("Node 99")
        assert list(test) == original_list
        assert len(test) == 3
        
        # Test on empty list - should do nothing
        test = dLL()
        test.delFirst("Anything")
        assert len(test) == 0
        assert test.empty() is True
        
        # Test deleting all elements one by one
        test = dLL(["A", "B", "C"])
        test.delFirst("A")
        test.delFirst("B")
        test.delFirst("C")
        assert len(test) == 0
        assert test.empty() is True
        
        # Test that links are properly maintained after deletion
        test = dLL(["A", "B", "C", "D"])
        test.delFirst("B")
        # Verify "A" now links to "C"
        nodes = list(test._iterate())
        assert nodes[0].getData() == "A"
        assert nodes[1].getData() == "C"
        assert nodes[0].getNext() == nodes[1]
        assert nodes[1].getPrev() == nodes[0]

    def test_del_all(self):
        """Test delAll() deletes all occurrences of a value from the list."""
        # Test deleting all duplicates from middle of list
        test = dLL(["A", "B", "C", "B", "D", "B"])
        test.delAll("B")
        expected = ["A", "C", "D"]
        assert list(test) == expected
        assert len(test) == 3
        # Verify all "B"s are gone
        assert "B" not in list(test)

        # Test deleting all occurrences when at different positions
        test = dLL(["X", "A", "X", "B", "X"])
        test.delAll("X")
        expected = ["A", "B"]
        assert list(test) == expected
        assert len(test) == 2

        # Test deleting when only one occurrence exists
        test = dLL(["A", "B", "C"])
        test.delAll("B")
        expected = ["A", "C"]
        assert list(test) == expected
        assert len(test) == 2

        # Test deleting all elements (all same value)
        test = dLL(["A", "A", "A", "A"])
        test.delAll("A")
        expected = []
        assert list(test) == expected
        assert len(test) == 0
        assert test.empty() is True

        # Test deleting consecutive duplicates
        test = dLL(["A", "B", "B", "B", "C"])
        test.delAll("B")
        expected = ["A", "C"]
        assert list(test) == expected
        assert len(test) == 2

        # Test when value NOT found - list should remain unchanged
        test = dLL(["Node 1", "Node 2", "Node 3"])
        original_list = list(test)
        test.delAll("Node 99")
        assert list(test) == original_list
        assert len(test) == 3

        # Test on empty list - should do nothing
        test = dLL()
        test.delAll("Anything")
        assert len(test) == 0
        assert test.empty() is True

        # Test deleting from single element list
        test = dLL("Only Node")
        test.delAll("Only Node")
        expected = []
        assert list(test) == expected
        assert len(test) == 0
        assert test.empty() is True

        # Test deleting all of first element when duplicated
        test = dLL(["A", "A", "B", "C"])
        test.delAll("A")
        expected = ["B", "C"]
        assert list(test) == expected
        assert len(test) == 2

        # Test deleting all of last element when duplicated
        test = dLL(["A", "B", "C", "C", "C"])
        test.delAll("C")
        expected = ["A", "B"]
        assert list(test) == expected
        assert len(test) == 2

        # Test with complex pattern
        test = dLL(["A", "B", "A", "C", "A", "D", "A"])
        test.delAll("A")
        expected = ["B", "C", "D"]
        assert list(test) == expected
        assert len(test) == 3

        # Test that links are properly maintained after multiple deletions
        test = dLL(["A", "X", "B", "X", "C", "X", "D"])
        test.delAll("X")
        nodes = list(test._iterate())
        assert len(nodes) == 4
        assert nodes[0].getData() == "A"
        assert nodes[1].getData() == "B"
        assert nodes[2].getData() == "C"
        assert nodes[3].getData() == "D"
        # Verify proper linking
        assert nodes[0].getNext() == nodes[1]
        assert nodes[1].getPrev() == nodes[0]
        assert nodes[1].getNext() == nodes[2]
        assert nodes[2].getPrev() == nodes[1]

    def test_reverse(self):
        """Test reverse() returns a new reversed DoublyLinkedList."""
        # Test reversing a multi-element list
        test = dLL(["Node 1", "Node 2", "Node 3"])
        reversed_list = test.reverse()

        # Verify reversed order
        expected = ["Node 3", "Node 2", "Node 1"]
        assert list(reversed_list) == expected
        assert len(reversed_list) == 3

        # Verify original list is unchanged
        assert list(test) == ["Node 1", "Node 2", "Node 3"]

        # Verify first and last elements
        assert reversed_list.getFirst() == "Node 3"
        assert reversed_list.getLast() == "Node 1"

        # Test reversing a two-element list
        test = dLL(["A", "B"])
        reversed_list = test.reverse()
        expected = ["B", "A"]
        assert list(reversed_list) == expected

        # Test reversing a single element list
        test = dLL("Only Node")
        reversed_list = test.reverse()
        expected = ["Only Node"]
        assert list(reversed_list) == expected
        assert len(reversed_list) == 1

        # Test reversing an empty list
        test = dLL()
        reversed_list = test.reverse()
        assert list(reversed_list) == []
        assert len(reversed_list) == 0
        assert reversed_list.empty() is True

        # Test that reversed list is a new independent list
        test = dLL(["A", "B", "C"])
        reversed_list = test.reverse()
        test.pushBack("D")  # Modify original
        assert list(test) == ["A", "B", "C", "D"]
        assert list(reversed_list) == ["C", "B", "A"]  # Reversed unchanged

        # Verify node links are correct in reversed list
        test = dLL(["1", "2", "3", "4"])
        reversed_list = test.reverse()
        nodes = list(reversed_list._iterate())

        assert len(nodes) == 4
        assert nodes[0].getData() == "4"
        assert nodes[1].getData() == "3"
        assert nodes[2].getData() == "2"
        assert nodes[3].getData() == "1"

        # Verify forward and backward links
        assert nodes[0].getNext() == nodes[1]
        assert nodes[1].getPrev() == nodes[0]
        assert nodes[1].getNext() == nodes[2]
        assert nodes[2].getPrev() == nodes[1]
        assert nodes[2].getNext() == nodes[3]
        assert nodes[3].getPrev() == nodes[2]

        # Test double reverse returns to original order
        test = dLL(["A", "B", "C"])
        reversed_once = test.reverse()
        reversed_twice = reversed_once.reverse()
        assert list(reversed_twice) == list(test)

    def test_middle_node(self):
        """Test middleNode() returns pointer to the middle node in the list."""
        # Test with odd number of elements (5) - should return exact middle
        test = dLL(["Node 1", "Node 2", "Node 3", "Node 4", "Node 5"])
        middle = test.middleNode()
        assert middle is not None
        assert middle.getData() == "Node 3"

        # Verify it's a node object with proper methods
        assert hasattr(middle, 'getData')
        assert hasattr(middle, 'getNext')
        assert hasattr(middle, 'getPrev')

        # Verify links
        assert middle.getPrev().getData() == "Node 2"
        assert middle.getNext().getData() == "Node 4"

        # Test with even number of elements (4) - should return lower middle
        test = dLL(["Node 1", "Node 2", "Node 3", "Node 4"])
        middle = test.middleNode()
        assert middle is not None
        assert middle.getData() == "Node 2"
        assert middle.getPrev().getData() == "Node 1"
        assert middle.getNext().getData() == "Node 3"

        # Test with three elements
        test = dLL(["A", "B", "C"])
        middle = test.middleNode()
        assert middle is not None
        assert middle.getData() == "B"

        # Test with two elements - should return first
        test = dLL(["A", "B"])
        middle = test.middleNode()
        assert middle is not None
        assert middle.getData() == "A"

        # Test with single element
        test = dLL("Only Node")
        middle = test.middleNode()
        assert middle is not None
        assert middle.getData() == "Only Node"

        # Test with empty list - should return None
        test = dLL()
        middle = test.middleNode()
        assert middle is None

        # Test with six elements (even) - should return lower middle
        test = dLL(["1", "2", "3", "4", "5", "6"])
        middle = test.middleNode()
        assert middle is not None
        assert middle.getData() == "3"

        # Test with seven elements (odd) - should return exact middle
        test = dLL(["1", "2", "3", "4", "5", "6", "7"])
        middle = test.middleNode()
        assert middle is not None
        assert middle.getData() == "4"

        # Verify middle node can be used to traverse both directions
        test = dLL(["A", "B", "C", "D", "E"])
        middle = test.middleNode()
        assert middle.getData() == "C"

        # Go backward from middle
        assert middle.getPrev().getData() == "B"
        assert middle.getPrev().getPrev().getData() == "A"

        # Go forward from middle
        assert middle.getNext().getData() == "D"
        assert middle.getNext().getNext().getData() == "E"

    def test_merge(self):
        """Test merge() combines two sorted lists into a new sorted list."""
        # Test merging two sorted lists
        list1 = dLL([1, 3, 5, 7])
        list2 = dLL([2, 4, 6, 8])
        merged = dLL.merge(list1, list2)
        expected = dLL([1, 2, 3, 4, 5, 6, 7, 8])
        assert list(merged) == list(expected)
        assert len(merged) == len(expected)

        # Verify original lists are unchanged
        assert list(list1) == [1, 3, 5, 7]
        assert list(list2) == [2, 4, 6, 8]

        # Test merging when first list is empty
        list1 = dLL()
        list2 = dLL([1, 2, 3])
        merged = dLL.merge(list1, list2)
        expected = dLL([1, 2, 3])
        assert list(merged) == list(expected)
        assert len(merged) == len(expected)

        # Test merging when second list is empty
        list1 = dLL([1, 2, 3])
        list2 = dLL()
        merged = dLL.merge(list1, list2)
        expected = dLL([1, 2, 3])
        assert list(merged) == list(expected)
        assert len(merged) == len(expected)

        # Test merging both empty lists
        list1 = dLL()
        list2 = dLL()
        merged = dLL.merge(list1, list2)
        expected = dLL()
        assert list(merged) == list(expected)
        assert len(merged) == len(expected)
        assert merged.empty() is True

        # Test merging lists of different lengths
        list1 = dLL([1, 5, 9])
        list2 = dLL([2, 3, 4, 6, 7, 8])
        merged = dLL.merge(list1, list2)
        expected = dLL([1, 2, 3, 4, 5, 6, 7, 8, 9])
        assert list(merged) == list(expected)
        assert len(merged) == len(expected)

        # Test merging with no overlap (all of list1 < all of list2)
        list1 = dLL([1, 2, 3])
        list2 = dLL([4, 5, 6])
        merged = dLL.merge(list1, list2)
        expected = dLL([1, 2, 3, 4, 5, 6])
        assert list(merged) == list(expected)

        # Test merging with no overlap (all of list2 < all of list1)
        list1 = dLL([7, 8, 9])
        list2 = dLL([1, 2, 3])
        merged = dLL.merge(list1, list2)
        expected = dLL([1, 2, 3, 7, 8, 9])
        assert list(merged) == list(expected)

        # Test merging with duplicate values
        list1 = dLL([1, 3, 5, 5])
        list2 = dLL([2, 3, 4, 5])
        merged = dLL.merge(list1, list2)
        expected = dLL([1, 2, 3, 3, 4, 5, 5, 5])
        assert list(merged) == list(expected)

        # Test merging single element lists
        list1 = dLL(5)
        list2 = dLL(3)
        merged = dLL.merge(list1, list2)
        expected = dLL([3, 5])
        assert list(merged) == list(expected)

        # Test merging single element with multi-element list
        list1 = dLL(4)
        list2 = dLL([1, 2, 3, 5, 6])
        merged = dLL.merge(list1, list2)
        expected = dLL([1, 2, 3, 4, 5, 6])
        assert list(merged) == list(expected)

        # Test with strings (sorted alphabetically)
        list1 = dLL(["apple", "cherry", "grape"])
        list2 = dLL(["banana", "date", "fig"])
        merged = dLL.merge(list1, list2)
        expected = dLL(["apple", "banana", "cherry", "date", "fig", "grape"])
        assert list(merged) == list(expected)

        # Test that merged list is independent (modifying doesn't affect originals)
        list1 = dLL([1, 3, 5])
        list2 = dLL([2, 4, 6])
        merged = dLL.merge(list1, list2)
        merged.pushBack(100)
        assert 100 not in list(list1)
        assert 100 not in list(list2)
        assert list(merged) == [1, 2, 3, 4, 5, 6, 100]

    def test_find_max(self):
        # Multi-element list
        test = dLL([1, 3, 2, 10, 7])
        assert test.findMax() == 10

        # With negative numbers
        test = dLL([-10, -5, -20, -3])
        assert test.findMax() == -3

        # With duplicates
        test = dLL([5, 1, 5, 2])
        assert test.findMax() == 5

        # Single element
        test = dLL(42)
        assert test.findMax() == 42

        # Mixed ints/floats
        test = dLL([2, 9.5, 3, 9.4])
        assert test.findMax() == 9.5

        # Empty list returns None
        test = dLL()
        assert test.findMax() is None

    def test_add_sorted(self):
        # Insert into empty list
        test = dLL()
        test.addSorted(5)
        assert list(test) == [5]
        assert len(test) == 1

        # Insert at the front
        test = dLL([2, 4, 6])
        test.addSorted(1)
        assert list(test) == [1, 2, 4, 6]

        # Insert in the middle
        test = dLL([1, 3, 5, 7])
        test.addSorted(4)
        assert list(test) == [1, 3, 4, 5, 7]

        # Insert at the end
        test = dLL([1, 3, 5])
        test.addSorted(9)
        assert list(test) == [1, 3, 5, 9]

        # Insert duplicate (non-decreasing; place after existing equals)
        test = dLL([1, 2, 2, 3])
        test.addSorted(2)
        assert list(test) == [1, 2, 2, 2, 3]

        # Strings (lexicographic order)
        test = dLL(["apple", "cherry", "grape"])
        test.addSorted("banana")
        assert list(test) == ["apple", "banana", "cherry", "grape"]

    def test_remove_duplicates(self):
        # No duplicates
        test = dLL([1, 2, 3, 4])
        test.removeDuplicates()
        assert list(test) == [1, 2, 3, 4]
        assert len(test) == 4

        # Consecutive duplicates
        test = dLL([1, 1, 1, 2, 2, 3, 3, 3])
        test.removeDuplicates()
        assert list(test) == [1, 2, 3]

        # Non-consecutive duplicates (preserve first-occurrence order)
        test = dLL([3, 1, 2, 1, 3, 2, 4, 1])
        test.removeDuplicates()
        assert list(test) == [3, 1, 2, 4]

        # All same values
        test = dLL(["x", "x", "x"])
        test.removeDuplicates()
        assert list(test) == ["x"]
        assert len(test) == 1

        # Strings with case sensitivity
        test = dLL(["a", "A", "a", "b", "B", "b"])
        test.removeDuplicates()
        assert list(test) == ["a", "A", "b", "B"]

        # Single element
        test = dLL(42)
        test.removeDuplicates()
        assert list(test) == [42]
        assert len(test) == 1

        # Empty list
        test = dLL()
        test.removeDuplicates()
        assert list(test) == []
        assert len(test) == 0

        # Idempotency
        test = dLL([1, 2, 2, 3, 3, 3])
        test.removeDuplicates()
        first_pass = list(test)
        test.removeDuplicates()
        assert list(test) == first_pass