# Standard Library Imports
# (No standard libraries are imported here in this file)

# Third-Party Imports
# import pytest

# Local Application/Library Imports
from codymacmle_dsa import Sort  # type: ignore


class TestSort:
    """
        Tests for Bubble Sort
    """
    def test_bubble_sort_empty_list(self):
        """Test bubble sort with an empty list."""
        result = Sort.BubbleSort([])
        assert result == []

    def test_bubble_sort_single_element(self):
        """Test bubble sort with a single element."""
        result = Sort.BubbleSort([5])
        assert result == [5]

    def test_bubble_sort_already_sorted(self):
        """Test bubble sort with an already sorted list."""
        result = Sort.BubbleSort([1, 2, 3, 4, 5])
        assert result == [1, 2, 3, 4, 5]

    def test_bubble_sort_reverse_sorted(self):
        """Test bubble sort with a reverse sorted list."""
        result = Sort.BubbleSort([5, 4, 3, 2, 1])
        assert result == [1, 2, 3, 4, 5]

    def test_bubble_sort_unsorted(self):
        """Test bubble sort with an unsorted list."""
        result = Sort.BubbleSort([3, 1, 4, 1, 5, 9, 2, 6])
        assert result == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_bubble_sort_duplicates(self):
        """Test bubble sort with duplicate values."""
        result = Sort.BubbleSort([4, 2, 4, 2, 1, 1, 3])
        assert result == [1, 1, 2, 2, 3, 4, 4]

    def test_bubble_sort_negative_numbers(self):
        """Test bubble sort with negative numbers."""
        result = Sort.BubbleSort([-5, 3, -1, 0, 9, -7])
        assert result == [-7, -5, -1, 0, 3, 9]

    def test_bubble_sort_two_elements(self):
        """Test bubble sort with two elements."""
        result = Sort.BubbleSort([2, 1])
        assert result == [1, 2]

    def test_bubble_sort_all_same(self):
        """Test bubble sort with all identical elements."""
        result = Sort.BubbleSort([5, 5, 5, 5, 5])
        assert result == [5, 5, 5, 5, 5]

    """
       Tests for Selection Sort
    """
    def test_selection_sort_empty_list(self):
        """Test selection sort with an empty list."""
        result = Sort.SelectionSort([])
        assert result == []

    def test_selection_sort_single_element(self):
        """Test selection sort with a single element."""
        result = Sort.SelectionSort([5])
        assert result == [5]

    def test_selection_sort_already_sorted(self):
        """Test selection sort with an already sorted list."""
        result = Sort.SelectionSort([1, 2, 3, 4, 5])
        assert result == [1, 2, 3, 4, 5]

    def test_selection_sort_reverse_sorted(self):
        """Test selection sort with a reverse sorted list."""
        result = Sort.SelectionSort([5, 4, 3, 2, 1])
        assert result == [1, 2, 3, 4, 5]

    def test_selection_sort_unsorted(self):
        """Test selection sort with an unsorted list."""
        result = Sort.SelectionSort([3, 1, 4, 1, 5, 9, 2, 6])
        assert result == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_selection_sort_duplicates(self):
        """Test selection sort with duplicate values."""
        result = Sort.SelectionSort([4, 2, 4, 2, 1, 1, 3])
        assert result == [1, 1, 2, 2, 3, 4, 4]

    def test_selection_sort_negative_numbers(self):
        """Test selection sort with negative numbers."""
        result = Sort.SelectionSort([-5, 3, -1, 0, 9, -7])
        assert result == [-7, -5, -1, 0, 3, 9]

    def test_selection_sort_two_elements(self):
        """Test selection sort with two elements."""
        result = Sort.SelectionSort([2, 1])
        assert result == [1, 2]

    def test_selection_sort_all_same(self):
        """Test selection sort with all identical elements."""
        result = Sort.SelectionSort([5, 5, 5, 5, 5])
        assert result == [5, 5, 5, 5, 5]

    """
       Tests for Insertion Sort
    """
    def test_insertion_sort_empty_list(self):
        """Test insertion sort with an empty list."""
        result = Sort.InsertionSort([])
        assert result == []

    def test_insertion_sort_single_element(self):
        """Test insertion sort with a single element."""
        result = Sort.InsertionSort([5])
        assert result == [5]

    def test_insertion_sort_already_sorted(self):
        """Test insertion sort with an already sorted list."""
        result = Sort.InsertionSort([1, 2, 3, 4, 5])
        assert result == [1, 2, 3, 4, 5]

    def test_insertion_sort_reverse_sorted(self):
        """Test insertion sort with a reverse sorted list."""
        result = Sort.InsertionSort([5, 4, 3, 2, 1])
        assert result == [1, 2, 3, 4, 5]

    def test_insertion_sort_unsorted(self):
        """Test insertion sort with an unsorted list."""
        result = Sort.InsertionSort([3, 1, 4, 1, 5, 9, 2, 6])
        assert result == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_insertion_sort_duplicates(self):
        """Test insertion sort with duplicate values."""
        result = Sort.InsertionSort([4, 2, 4, 2, 1, 1, 3])
        assert result == [1, 1, 2, 2, 3, 4, 4]

    def test_insertion_sort_negative_numbers(self):
        """Test insertion sort with negative numbers."""
        result = Sort.InsertionSort([-5, 3, -1, 0, 9, -7])
        assert result == [-7, -5, -1, 0, 3, 9]

    def test_insertion_sort_two_elements(self):
        """Test insertion sort with two elements."""
        result = Sort.InsertionSort([2, 1])
        assert result == [1, 2]

    def test_insertion_sort_all_same(self):
        """Test insertion sort with all identical elements."""
        result = Sort.InsertionSort([5, 5, 5, 5, 5])
        assert result == [5, 5, 5, 5, 5]
