# -*- coding: utf-8 -*-

# a1task2.py - Assignment 1, Task 2
#
# Functions with numeric inputs
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

# function 0

def combine_lists(left, right):
    """ return combine two lists into one sorted list
        input left, right: any list(int)
    """
    if left == []:
        return right
    elif right == []:
        return left    
    else:
        if left[0]<=right[0]:
            return left[:1] +combine_lists(left[1:], right)
        else:
            return right[:1] +combine_lists(left, right[1:])


def merge_sort(values):
    """ return the sort the list of values
        input values: any list(int)
    """
    if len(values)<=1:
        return values
    n =len(values)//2
    left = values[:n]
    right = values[n:]
    if len(right)==1:
        return combine_lists(left, right)
    
    else:
        
        return combine_lists(merge_sort(left),merge_sort(right))





    
    
    
    
    
    
    
    
    
    
    
    
    
    
