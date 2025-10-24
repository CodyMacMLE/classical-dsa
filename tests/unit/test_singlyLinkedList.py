# Standard Library Imports
# (No standard libraries are imported here in this file)

# Third-Party Imports
import pytest

# Local Application/Library Imports
from codymacmle_dsa import SinglyLinkedList  # type: ignore


class TestSinglyLinkedList:
    def test_init(self):
        sll1 = SinglyLinkedList()
        sll2 = SinglyLinkedList("Node")
        sll3 = SinglyLinkedList(["Node 1", "Node 2"])


        assert sll1._head is None

        assert sll2._head is not None
        assert sll2._head._data == "Node"
        assert sll2._head._next is None

        assert sll3._head is not None
        assert sll3._head._data == "Node 1"
        assert sll3._head._next is not None
        assert sll3._head._next._data == "Node 2"
        assert sll3._head._next._next is None

    def test__eq__(self):
        sll1 = SinglyLinkedList()
        sll2 = SinglyLinkedList("Not Node1")
        sll3 = SinglyLinkedList(["Not Node1", "Not Node2"])
        sll4 = SinglyLinkedList("Node")
        sll5 = SinglyLinkedList("Node")
        sll6 = SinglyLinkedList(["Not Node2", "Not Node1"])
        # one is empty
        assert (sll1 == sll2) is False
        # different size
        assert (sll2 == sll3) is False
        # same size, values different
        assert (sll2 == sll4) is False
        # Same
        assert (sll4 == sll5) is True
        # Same, but different order
        assert (sll3 == sll6) is True
        # sll6 should not have been sorted
        assert sll6._head._data != "Not Node1"

    def test_getFront(self):
        sll1 = SinglyLinkedList()
        sll2 = SinglyLinkedList(["Node 1", "Node 2"])

        assert sll1.getFront() is None
        assert sll2.getFront() is not None
        assert sll2.getFront()._data == "Node 1"
        assert sll2.getFront()._next is not None

    def test_getBack(self):
        sll = SinglyLinkedList(["Node 1", "Node 2"])
        assert sll.getBack() == "Node 2"

    def test__getitem__(self):
        sll = SinglyLinkedList(["Node 1", "Node 2", "Node 3"])

        assert sll[0] == "Node 1"
        assert sll[1] == "Node 2"
        assert sll[2] == "Node 3"

        with pytest.raises(IndexError, match="out of bounds"):
            sll[999]

    def test_pushFront(self):
        sll = SinglyLinkedList()

        sll.pushFront("Node 1")
        assert sll._head is not None
        assert sll._head._data == "Node 1"
        assert sll._head._next is None

        sll.pushFront("Node 2")
        assert sll._head is not None
        assert sll._head._data == "Node 2"
        assert sll._head._next is not None
        assert sll._head._next._data == "Node 1"
        assert sll._head._next._next is None

        sll2 = SinglyLinkedList()
        sll2.pushFront(["Node 1", "Node 2", "Node 3"])
        assert sll2._head is not None
        assert sll2._head._data == "Node 1"
        assert sll2._head._next is not None
        assert sll2._head._next._data == "Node 2"
        assert sll2._head._next._next is not None
        assert sll2._head._next._next._data == "Node 3"
        assert sll2._head._next._next._next is None

    def test_pushBack(self):
        sll = SinglyLinkedList()

        sll.pushBack("Node 1")
        assert sll._head is not None
        assert sll._head._data == "Node 1"
        assert sll._head._next is None
        sll.pushBack("Node 2")
        assert sll._head is not None
        assert sll._head._data == "Node 1"
        assert sll._head._next is not None
        assert sll._head._next._data == "Node 2"
        assert sll._head._next._next is None

    def test__setitem__(self):
        sll = SinglyLinkedList()

        sll[0] = "Node 1"
        assert sll._head is not None
        assert sll._head._data == "Node 1"
        assert sll._head._next is None

        sll[1] = "Node 2"
        assert sll._head is not None
        assert sll._head._data == "Node 1"
        assert sll._head._next is not None
        assert sll._head._next._data == "Node 2"
        assert sll._head._next._next is None

        sll[1] = "Node 3"
        assert sll._head is not None
        assert sll._head._data == "Node 1"
        assert sll._head._next is not None
        assert sll._head._next._data == "Node 3"
        assert sll._head._next._next is not None
        assert sll._head._next._next._data == "Node 2"
        assert sll._head._next._next._next is None

        sll[3] = "Node 4"
        assert sll._head is not None
        assert sll._head._data == "Node 1"
        assert sll._head._next is not None
        assert sll._head._next._data == "Node 3"
        assert sll._head._next._next is not None
        assert sll._head._next._next._data == "Node 2"
        assert sll._head._next._next._next is not None
        assert sll._head._next._next._next._data == "Node 4"

        with pytest.raises(IndexError, match="out of bounds"):
            sll[999] = "Node 5"

    def test_popFront(self):
        sll = SinglyLinkedList(["Node 1", "Node 2"])
        sll.popFront()
        assert sll._head is not None
        assert sll._head._data == "Node 2"
        assert sll._head._next is None

        sll.popFront()
        assert sll._head is None

    def test_popBack(self):
        sll = SinglyLinkedList(["Node 1", "Node 2"])
        sll.popBack()

        assert sll._head is not None
        assert sll._head._data == "Node 1"
        assert sll._head._next is None

        sll.popBack()
        assert sll._head is None

    def test__delitem__(self):
        sll = SinglyLinkedList(["Node 1", "Node 2", "Node 3", "Node 4", "Node 5"])

        del sll[2]
        assert sll._head is not None
        assert sll._head._data == "Node 1"
        assert sll._head._next._data == "Node 2"
        assert sll._head._next._next._data == "Node 4"
        assert sll._head._next._next._next._data == "Node 5"

        del sll[0]
        assert sll._head._data == "Node 2"

        del sll[2]
        assert sll._head._data == "Node 2"
        assert sll._head._next._data == "Node 4"

        with pytest.raises(IndexError, match="out of bounds"):
            del sll[999]

    def test_isEmpty(self):
        sll1 = SinglyLinkedList()
        assert sll1.isEmpty() is True
        sll2 = SinglyLinkedList(["Node 1", "Node 2"])
        assert sll2.isEmpty() is False

    def test_size(self):
        sll1 = SinglyLinkedList()
        assert sll1.size() == 0
        sll2 = SinglyLinkedList(["Node 1", "Node 2"])
        assert sll2.size() == 2

    def test_clear(self):
        sll1 = SinglyLinkedList(["Node 1", "Node 2"])
        sll1.clear()

        assert sll1._head is None

        sll1.clear()
        assert sll1._head is None

    def test_toList(self):
        sll1 = SinglyLinkedList(["Node 1", "Node 2"])
        _list = sll1.toList()

        assert _list == ["Node 1", "Node 2"]
        assert isinstance(_list, list) is True

    def test__len__(self):
        sll1 = SinglyLinkedList(["Node 1", "Node 2"])
        length = len(sll1)
        assert length == 2

    def test__iter__(self):
        pass

    def test__next__(self):
        pass

    def test_middle(self):
        sll1 = SinglyLinkedList(["Node 1", "Node 2", "Node 3", "Node 4", "Node 5"])
        assert sll1.middle()._data == "Node 3"

        sll2 = SinglyLinkedList(["Node 1", "Node 2", "Node 3", "Node 4"])
        assert sll2.middle()._data == "Node 2"

        sll3 = SinglyLinkedList()
        assert sll3.middle() is None

    def test_find(self):
        sll1 = SinglyLinkedList(["Node 1", "Node 2"])
        ptr1 = sll1._head
        ptr2 = sll1._head._next
        assert sll1.find("Node 1") == ptr1
        assert sll1.find("Node 2") == ptr2
        assert sll1.find("Node 3") is None

    def test_contains(self):
        sll1 = SinglyLinkedList(["Node 1", "Node 2"])
        assert sll1.contains("Node 1")
        assert sll1.contains("Node 2")
        assert not sll1.contains("Node 3")

    def test_reverse(self):
        sll1 = SinglyLinkedList(["Node 1", "Node 2", "Node 3"])
        sll1Reversed = sll1.reverse()
        assert sll1Reversed._head is not None
        assert sll1Reversed._head._data == "Node 3"
        assert sll1Reversed._head._next._data == "Node 2"
        assert sll1Reversed._head._next._next._data == "Node 1"
        assert sll1Reversed._head._next._next._next is None

    def test_sort(self):
        sll1 = SinglyLinkedList()
        sll1.sort()
        assert sll1._head is None

        sll1.pushFront("Node 1")
        sll1.sort()
        assert sll1._head is not None
        assert sll1._head._data == "Node 1"

        sll1.pushFront("Node 2")
        sll1.sort()
        assert sll1._head is not None
        assert sll1._head._data == "Node 1"
        assert sll1._head._next._data == "Node 2"
        assert sll1._head._next._next is None

        sll2 = SinglyLinkedList([3, 1 , 2, 2, 12, 33, 7, 9])
        sll2.sort()
        assert sll2._head is not None
        assert sll2._head._data == 1
        assert sll2._head._next._data == 2
        assert sll2._head._next._next._data == 2
        assert sll2._head._next._next._next._data == 3
        assert sll2._head._next._next._next._next._data == 7
        assert sll2._head._next._next._next._next._next._data == 9
        assert sll2._head._next._next._next._next._next._next._data == 12
        assert sll2._head._next._next._next._next._next._next._next._data == 33

        sll3 = SinglyLinkedList([3, 1, 2, 2, 12, 33, 7, 9])
        sll3.sort(True)
        assert sll3._head is not None
        assert sll3._head._data == 33
        assert sll3._head._next._data == 12
        assert sll3._head._next._next._data == 9
        assert sll3._head._next._next._next._data == 7
        assert sll3._head._next._next._next._next._data == 3
        assert sll3._head._next._next._next._next._next._data == 2
        assert sll3._head._next._next._next._next._next._next._data == 2
        assert sll3._head._next._next._next._next._next._next._next._data == 1

    def test_copy(self):
        sll1 = SinglyLinkedList()
        sll1_copy = sll1.copy()
        assert sll1_copy._head is None

        sll2 = SinglyLinkedList([3, 1, 2])
        sll2_copy = sll2.copy()
        assert sll2_copy._head._data == 3
        assert sll2_copy._head._next._data == 1
        assert sll2_copy._head._next._next._data == 2

    def test_merge(self):
        sll1 = SinglyLinkedList()
        sll2 = SinglyLinkedList("Node 1")
        sll3 = SinglyLinkedList(["Node 2", "Node 3"])

        mergedEmpty = SinglyLinkedList.merge(sll1, sll2)
        assert mergedEmpty._head._data == "Node 1"

        mergedFull = SinglyLinkedList.merge(sll2, sll3)
        assert mergedFull._head._data == "Node 1"
        assert mergedFull._head._next._data == "Node 2"
        assert mergedFull._head._next._next._data == "Node 3"