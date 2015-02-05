# -*- coding: utf-8 -*-
#!/usr/bin/env

import unittest 


def merge_sort(unsorted):
    """ Merge sort takes advantage of the ease of merging already sorted lists into a new sorted 
    list. 
    It starts by comparing every two elements (i.e., 1 with 2, then 3 with 4...) and swapping them 
    if the first should come after the second. 
    It then merges each of the resulting lists of two into lists of four, then merges those lists 
    of four, and so on; until at last two lists are merged into the final sorted list. 
    Of the algorithms described here, this is the first that scales well to very large lists, 
    because its worst-case running time is O(n log n). It is also easily applied to lists, 
    not only arrays, as it only requires sequential access, not random access. 
    However, it has additional O(n) space complexity, and involves a large number of copies 
    in simple implementations.

    Merge sort has seen a relatively recent surge in popularity for practical implementations, 
    due to its use in the sophisticated algorithm Timsort, which is used for the standard 
    sort routine in the programming languages Python and Java (as of JDK7). 
    Merge sort itself is the standard routine in Perl,[16] among others, 
    and has been used in Java at least since 2000 in JDK1.3
    """

    print unsorted

    result = []
    
    if len(unsorted) < 2:
        return unsorted
    
    mid = int(len(unsorted)/2)
    
    y = merge_sort(unsorted[:mid])
    z = merge_sort(unsorted[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
            if y[i] > z[j]:
                result.append(z[j])
                j += 1
            else:
                result.append(y[i])
                i += 1
    
    result += y[i:]
    result += z[j:]
    

    return result


class TestMergeSort(unittest.TestCase):

   
    def test_sort_empty(self):

        self.assertEqual([], merge_sort([]))


    def test_sort_one(self):

        self.assertEqual([1], merge_sort([1]))


    def test_sort_numbers(self):

        self.assertEqual([1,2,3,4], merge_sort([4, 3,2,1]))

    def test_sort_string(self):

        self.assertEqual(['e', 's', 't', 't'], merge_sort(list("test")))


if __name__ == '__main__':

    unittest.main()