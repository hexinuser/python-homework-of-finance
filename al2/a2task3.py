
# a1task2.py - Assignment 1, Task 2
#
# Functions with numeric inputs
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

# function 0
def mult(n,m):
    """ return the product of those integers
        input n,m: any number (int)
    """
    if n == 0:
        return 0 
    elif n < 0:
        return -mult(-n, m)
    else:
        return m + mult(n-1, m)


# function 1
def dot(l1, l2):
    """ return the dot product of those lists
        input l1,l2: any list (int or float)
    """
    if len(l1)!=len(l2):
        return 0.0
    elif l1==[]:
        return 0.0
    else:
        t = l1[0]*l2[0]+dot(l1[1:], l2[1:])
        return t

def letter_score(letter):
    """ returns the value of that letter as a scrabble tile
        input letter: any str
    """
    assert(len(letter) == 1)
    alpha_str ='abcdefghijklmnopqrstuvwxyz'
    num_list = [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]
    if letter in alpha_str:
        i = alpha_str.index(letter)
        return num_list[i]
    else:
        return 0

def scrabble_score(word):
    """ return the scrabble score of that string
        input letter: any str
    """
    if word == '':
        return 0
    else:
        t = letter_score(word[0])
        return t+scrabble_score(word[1:])

print(scrabble_score('a'))    
    
    
    
    
    
    
# optional but encouraged: add test calls for your functions below



def test():
    print(mult(6, 7))
    print(mult(-3, 6))
    print(dot([1, 2, 3, 4], [10, 100, 1000, 10000]))
    print(dot([5, 3], [6]))
    print(letter_score('q'))
    print(letter_score('A'))
    print(scrabble_score('quetzal'))   
#test()