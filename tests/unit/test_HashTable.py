# Standard Library Imports
# (No standard libraries are imported here in this file)

# Third-Party Imports
# import pytest

# Local Application/Library Imports
from codymacmle_dsa import HashTable  # type: ignore


class TestHashTable:
    def test__init__(self):
        table = HashTable()
        assert table._size == 10
        assert len(table._buckets) == 10
        for bucket in table._buckets:
            assert len(bucket) == 0
            assert bucket._head is None

    def test_put(self):
        pass
