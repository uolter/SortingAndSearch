# -*- coding: utf-8 -*-
#!/usr/bin/env

import unittest 


def merge_sort(unsorted):

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