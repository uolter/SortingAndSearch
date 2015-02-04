#!/usr/bin/env 
# -*- coding: utf-8 -*-


import unittest


def insertion_sort(seq):
    """
    Insertion sort is a simple sorting algorithm that is relatively efficient for small lists 
    and mostly sorted lists, and often is used as part of more sophisticated algorithms. 
    It works by taking elements from the list one by one and inserting them in their correct position into 
    a new sorted list. 
    In arrays, the new list and the remaining elements can share the array's space, 
    but insertion is expensive, requiring shifting all following elements over by one. 
    Shell sort is a variant of insertion sort that is more efficient for larger lists.
    """

    print 'Start '

    for i in range(1, len(seq)):
        j = i
        print ' ', seq
        while j > 0 and seq[j - 1] > seq[j]:
            seq[j - 1], seq[j] = seq[j], seq[j - 1]
            j -= 1
    
    print 'End.', seq
    return seq
    



class TestSelSort(unittest.TestCase):

   
    def test_sort_empty(self):

        self.assertEqual([], insertion_sort([]))


    def test_sort_one(self):

        self.assertEqual([1], insertion_sort([1]))


    def test_sort_numbers(self):

        self.assertEqual([1,2,3,4], insertion_sort([4, 3,2,1]))

    def test_sort_string(self):

        self.assertEqual(['e', 's', 't', 't'], insertion_sort(list("test")))


if __name__ == '__main__':

    unittest.main()