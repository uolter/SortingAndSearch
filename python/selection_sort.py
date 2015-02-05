#!/usr/bin/env 
# -*- coding: utf-8 -*-


import unittest


def selection_sort(unsorted):
    """
        select sort.
        the algorithm is in-place. This means that it uses essentially no extra storage.
        Selection sort is an in-place comparison sort. 
        It has O(n2) complexity, making it inefficient on large lists, 
        and generally performs worse than the similar insertion sort. 
    """

    for step in range(len(unsorted)):
        x = unsorted[step]
        swap = step
        for j in range(step, len(unsorted)):
            if unsorted[j] < x:
                swap = j
                x = unsorted[j]

        unsorted[swap] = unsorted[step]
        unsorted[step] = x

    return unsorted



class TestSelSort(unittest.TestCase):

   
    def test_sort_empty(self):

        self.assertEqual([], selection_sort([]))


    def test_sort_one(self):

        self.assertEqual([1], selection_sort([1]))


    def test_sort_numbers(self):

        self.assertEqual([1,2,3,4], selection_sort([4,3,2,1,]))


    def test_sort_string(self):

        self.assertEqual(['e', 's', 't', 't'], selection_sort(list("test")))

if __name__ == '__main__':

    unittest.main()

