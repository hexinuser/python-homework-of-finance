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

def copy(s, n):
    """ return a string in which n copies of s have been concatenated together
        input s: any str, n: any number (int)
    """
    if n <= 0:
        return ''
    else:
        return s+copy(s,n-1)
    

        
def double(s):
    """  return the string formed by doubling each character in the string
        input s: any str
    """
    if s == '':
        return ''
    else:
        return s[0]*2+double(s[1:])


def weave(s1, s2):
    """ return a new string that is formed by “weaving” together the characters
           in the strings s1 and s2 to create a single string
        input s1, s2: any str
    """
    if s1 == '':
        return s2
    elif s2 == '':
        return s1
    else:
        return s1[0]+s2[0]+weave(s1[1:],s2[1:])


def find_min(items):
    """ return the minimum from a list of items
        input items: any list
    """
    if len(items)==1:
        return items[0]
    else:
        if items[0]>=find_min(items[1:]):
            return find_min(items[1:])
        else:
            return items[0]

#print(find_min([42]))
    
def index(elem, seq):
    """ return the index of the first occurrence of elem in seq
        input elem: int or str, seq: any list
    """
    if elem in seq:
        if elem == seq[0]:
            return 0
        return 1+index(elem,seq[1:])
    else:
        return None
    
print(index('hi', ['hello', 111, True]))













    
    
    
    
    
    
    
    
    
    
    
    
    
    