#!/usr/bin/env 
# -*- coding: utf-8 -*-

import unittest

def bubble_sort( seq ):
    """
    Time Complexity of Solution:
    Best O(n^2); Average O(n^2); Worst O(n^2).

      Approach:
       Bubblesort is an elementary sorting algorithm. The idea is to
       imagine bubbling the smallest elements of a (vertical) array to the
       top; then bubble the next smallest; then so on until the entire
       array is sorted. Bubble sort is worse than both insertion sort and
       selection sort. It moves elements as many times as insertion sort
       (bad) and it takes as long as selection sort (bad). On the positive
       side, bubble sort is easy to understand. Also there are highly
       improved variants of bubble sort.
    """
  
    for i in range(len(seq)):
        for k in range(len(seq) - 1, i, -1 ):
            if ( seq[k] < seq[k - 1] ):
                swap( seq, k, k - 1 )

    return seq
 
def swap( seq, x, y ):
    tmp = seq[x]
    seq[x] = seq[y]
    seq[y] = tmp



class TestBubbleSort(unittest.TestCase):
   
    def test_sort_empty(self):

        self.assertEqual([], bubble_sort([]))


    def test_sort_one(self):

        self.assertEqual([1], bubble_sort([1]))


    def test_sort_numbers(self):

        self.assertEqual([1,2,3,4], bubble_sort([4, 3,2,1]))

    def test_sort_string(self):

        self.assertEqual(['e', 's', 't', 't'], bubble_sort(list("test")))


if __name__ == '__main__':

    unittest.main()


