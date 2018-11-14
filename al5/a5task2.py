# -*- coding: utf-8 -*-


from a5task1 import *

def add_matrices(A, B):
    """ returns a new matrix which is the element-wise sum of the matrices A and B.
        input: A,B:list
    """
    dim = 'cannot add '+ str((len(A),len(A[0])))+ ' with '+ str((len(B),len(B[0])))+'!'
    assert(len(A) == len(B) and len(A[0])==len(B[0])), 'incompatible dimensions: %s' %dim 
    C = []
    for i in range(len(A)):
        row_list = [A[i][j]+B[i][j] for j in range(len(A[0]))]
        C.append(row_list)
    return C

#A = [[1,2],[4,5]]
#B = [[4,5,6],[1,2,3]]
#S = add_matrices(A, B)
#print_matrix(S, 'S')
    
def sub_matrices(A, B):
    """ returns a new matrix which is the element-wise difference of the matrices A and B.
        input: A,B:list
    """
    dim = 'cannot sub '+ str((len(A),len(A[0])))+ ' with '+ str((len(B),len(B[0])))+'!'
    assert(len(A) == len(B) and len(A[0])==len(B[0])), 'incompatible dimensions: %s' %dim 
    C = []
    for i in range(len(A)):
        row_list = [A[i][j]-B[i][j] for j in range(len(A[0]))]
        C.append(row_list)
    return C

#A = [[1,2],[4,5]]
#B = [[4,5,6],[1,2,3]]
#D = sub_matrices(A, B)
#print_matrix(D, 'D')

def mult_scalar(M,s):
    """ returns a new matrix containing the values of the original matrix multiplied by the scalar value.
        input: M:list; s:float
    """
    C = []
    for i in range(len(M)):
        row_list = [j*s for j in M[i]]
        C.append(row_list)
    return C

#A = [[3,0,2,1],[2,0,-2,3]]
#print_matrix(A)
#B = mult_scalar(A, 3)
#print_matrix(B)

def dot_product(M, N):
    """ returns a new matrix containing dot product of these matrices.
        input: M, N: list;
    """    
    dim = 'cannot dot_product '+ str((len(M),len(M[0])))+ ' with '+ str((len(M),len(M[0])))+'!'
    assert(len(M[0]) == len(N)), 'incompatible dimensions: %s' %dim 
    C = []
    for i in range(len(M)):
        row_list = []
        for j in range(len(N[0])):
            row_list.append(sum([M[i][k]*N[k][j] for k in range(len(N))]))
        C.append(row_list)
    return C
#A = [[1,2,3],[4,5,6]]
#B = [[4,3,2],[3,2,1]]
#P = dot_product(A,B)
#print_matrix(P, 'P')    

       
def create_sub_matrix(M, exclude_row, exclude_col):
    """ returns a sub-matrix of M, with all values that are not in row exclude_row or column exclude_col
        input M:list; exclude_row, exclude_col: int
    """
    row = list(range(len(M)))
    col = list(range(len(M[0])))
    row.remove(exclude_row)
    col.remove(exclude_col)
    C = []
    for i in row:
        row_list = [M[i][j] for j in col]
        C.append(row_list)
    return C

#A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#print_matrix(A)
#print_matrix(create_sub_matrix(A, 0, 0)) # exclude row 0 and column 0
#print_matrix(create_sub_matrix(A, 2, 3)) # exclude row 2 and column 3
    
def determinant(M):
    """ takes a parameter M that is a (non-singular) matrix, and returns its determinant.
        M:list
    """
    dim = 'incompatible dimensions: '+str((len(M),len(M[0])))+'!'
    assert(len(M[0]) == len(M)), "incompatible dimensions: %s!" % dim
    assert(len(M)>1), 'determinant requires at least a 2x2 matrix'
    if len(M)==2:
        return M[0][0]*M[1][1]-M[0][1]*M[1][0]
    else:
        det = 0
        for i in range(len(M)):
            det += (-1)**(i)*M[i][0]*determinant(create_sub_matrix(M,i,0))
        return det 
    
#A = [[3,4],[8,6], [10,7]]
#print(determinant(A))
      


def matrix_of_minors(M):
    minors_mat = []
    for i in range(len(M)):
        minors_list=[]
        for j in range(len(M)):
            if len(M)>2:
                t = determinant(create_sub_matrix(M,i,j))
            else:
                t = create_sub_matrix(M,i,j)[0][0]
            minors_list.append(t)
        minors_mat.append(minors_list)
    return minors_mat
#A = [[3,0,2],[2,0,-2],[0,1,1]]
#print_matrix(matrix_of_minors(A))
#    
#def determinant_1(M):
#    dim = 'incompatible dimensions: '+str((len(M),len(M[0])))+'!'
#    assert(len(M[0]) == len(M)), "incompatible dimensions: %s!" % dim
##    assert(len(M)!=1), 'determinant requires at least a 2x2 matrix'
#    if len(M)==1:
#        return M[0][0]
#    count = 0
#    for i in range(len(M)):
#        count += M[i][0]*(-1)**(i)*determinant_1(create_sub_matrix(M, i, 0))
#        
#    return count
        
#def inverse_matrix(M):
#    """ that takes a parameter that is a (non-singular) matrix, and returns its inverse
#        input: M: list
#    """
#    cofactor_mat = []
#    for i in range(len(M)):
#        cofactor_list = [(-1)**(i+j)*determinant_1(create_sub_matrix(M,i,j)) for j in range(len(M))]
#        cofactor_mat.append(cofactor_list)
#    adj_mat = transpose(cofactor_mat)
#    return mult_scalar(adj_mat,1/determinant(M))


def inverse_matrix(M):
    """ that takes a parameter that is a (non-singular) matrix, and returns its inverse
        input: M: list
    """
    minors =  matrix_of_minors(A)
    
    for i in range(len(M)):
        minors[i] = [(-1)**(i+j) for j in range(len(M))]
    adj_mat = transpose(minors)
    return mult_scalar(adj_mat,1/determinant(M))

A = [[3,2,0,1],[4,0,1,2],[3,0,2,1],[9,2,3,1]]
print_matrix(A, 'A')
print(determinant(A))
AI = inverse_matrix(A)
print_matrix(AI, 'AI')
#DP = dot_product(A,AI)
#print_matrix(DP)








