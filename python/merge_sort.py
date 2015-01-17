# -*- coding: utf-8 -*-
#!/usr/bin/env 


def merge_sort(unsorted):

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


print merge_sort([4,3,2,1])