# -*- coding: utf-8 -*-


def print_matrix(m, label=''):
    """ creates a nicely-formatted printout of matrix
        input m: list; label: str 
    """
    if label != '':
        print(label+' =')
    print('[',end='')
    for i in range(len(m)):
        print('[',end='')
        for j in range(len(m[i])):
            if j ==len(m[i])-1:
                print('%.2f' %m[i][j], end='')
            else:
                print('%.2f, ' %m[i][j], end='')
        if i==len(m)-1:
            print(']]')
        else:
            print(']')
        print(' ', end='')
#A = [[3,0,2,1],[2,0,-2,3]]
#print_matrix(A,'A')
        
def zeros(n, m=''):
    """ creates and returns an n * m matrix containing all zeros
        input n,m: int 
    """
    if m =='':
        m=n
    zeros_mat = []
    for i in range(n):
        zeros_list = [0 for j in range(m)]
        zeros_mat.append(zeros_list)
    return zeros_mat

#print_matrix(zeros(3,5))
    
def identity_matrix(n):
    """ returns an n * n identity matrix containing the value of 1 along the diagonal.
        input n: int 
    """
    zeros_mat = zeros(n)
    for i in range(n):
        zeros_mat[i][i] = 1
    return zeros_mat

#I = identity_matrix(3)
#print_matrix(I, 'I')
    
def transpose(M):
    """ creates and returns the transpose of a matrix.
        inpur M: list
    """
    tran_mat = []
    for i in range(len(M[0])):
        tran_list = [M[j][i] for j in range(len(M))]
        tran_mat.append(tran_list)
    return tran_mat

#A = [[1,2,3],[4,5,6]]
#print_matrix(A)
#AT = transpose(A)
#print_matrix(AT, 'AT')


def swap_rows(M, src, dest):
    """ perform the elementary row operation that exchanges two rows within the matrix.
        input M:list; src,dest: int
    """
    assert(max(src,dest)<len(M) and min(src,dest)>=0)
    M[src], M[dest] = M[dest],M[src]

#A = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]
#swap_rows(A, 1, 2) # swap rows 1 and 2
#print_matrix(A)
#swap_rows(A, 0, 2)
#print_matrix(A)
    
def mult_row_scalar(M, row, scalar):
    """ perform the elementary row operation that multiplies all values in the row row by the numerical value scalar.
        input M:list; row:int; scalar:flaot
    """
    assert(row>=0 and row<len(M))
    M[row] = [scalar*i for i in M[row]]
    
#A = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]    
#mult_row_scalar(A, 1, -1) # multiply row 1 by 0.5
#print_matrix(A)

def add_row_into(M, src, dest):
    """ performs the elementary-row operation to add the src row into the dest row.
        input M: list; src, dest:int
    """
    assert(max(src,dest)<len(M) and min(src,dest)>=0)
    M[dest] = [M[dest][i]+M[src][i] for i in range(len(M[0]))]
    

#A = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]
#print_matrix(A)
#add_row_into(A, 2, 1) # add row 2 into row 1
#print_matrix(A)
#
#add_row_into(A, 2, 1) # add row 2 into row 1
#print_matrix(A)
































        
    