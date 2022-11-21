import numpy as np
# Note: please don't import any new package. You should solve this problem using only the package(s) above.
#-------------------------------------------------------------------------

'''
    Problem 2: Getting Familiar with NumPy Package. (22 points)
    In this problem, we will get familiar with numpy package.

    -------------------------
    Package(s) to Install:
        Please install python version 3.7 or above and the following package(s):
        * numpy (for high-performance multidimensional arrays)
    How to Install:
        * numpy: To install 'numpy' using pip, you could type in the terminal: 
            python3 -m pip install numpy
    -------------------------
    A list of all variables being used in this problem is provided at the end of this file.
'''

#----------------------------------------------------
'''
    Create the following 2 x 3 matrix using nd-array in NumPy: 
	 1,2,3 
	 4,5,6. 
    ---- Outputs: --------
        * Z: a numpy matrix (2D array) of shape 2 X 3, where each element in the array is an integer.
    ---- Hints: --------
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def ndarray():
    #########################################
    ## INSERT YOUR CODE HERE (2 points)
    Z = np.array([[1, 2, 3], [4, 5, 6]])
    #########################################
    return Z
    #------ (2 points / 22 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        --- for Mac OS ---- 
        python3 -m pytest -v test2.py::test_ndarray_2pt
        --- for Windows OS ---- 
        python -m pytest -v test2.py::test_ndarray_2pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    Create the following 2 X 3 matrix using nd-array in NumPy: 
	 0.1, 0.2, 0.3 
	 0.4, 0.5, 0.6. 
    ---- Outputs: --------
        * Y: a numpy matrix (2D array) of shape 2 X 3, where each element in the array is a float number.
    ---- Hints: --------
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def float_array():
    #########################################
    ## INSERT YOUR CODE HERE (2 points)
    Y = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])
    #########################################
    return Y
    #------ (2 points / 22 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        --- for Mac OS ---- 
        python3 -m pytest -v test2.py::test_float_array_2pt
        --- for Windows OS ---- 
        python -m pytest -v test2.py::test_float_array_2pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    Given a NumPy matrix, return the number of rows (r) and columns (c) of the matrix. 
    ---- Inputs: --------
        * X: a numpy matrix (2D array) of shape r X c.
    ---- Outputs: --------
        * r: an integer, the number of rows in the matrix X.
        * c: an integer, the number of columns in the matrix X.
    ---- Hints: --------
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def get_shape(X):
    #########################################
    ## INSERT YOUR CODE HERE (2 points)
    r, c = X.shape
    #########################################
    return r, c
    #------ (2 points / 22 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        --- for Mac OS ---- 
        python3 -m pytest -v test2.py::test_get_shape_2pt
        --- for Windows OS ---- 
        python -m pytest -v test2.py::test_get_shape_2pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    Create a numpy matrix of shape r X c, all the values in the matrix should be 1. For example, an all-one matrix of shape 2 X 3 will be 
	 1, 1, 1 
	 1, 1, 1. 
    ---- Inputs: --------
        * r: an integer, the number of rows in the matrix X.
        * c: an integer, the number of columns in the matrix X.
    ---- Outputs: --------
        * O: a numpy matrix of shape r X c, where all elements of the matrix are 1's.
    ---- Hints: --------
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def all_one_matrix(r, c):
    #########################################
    ## INSERT YOUR CODE HERE (2 points)
    O = np.ones((r, c))
    #########################################
    return O
    #------ (2 points / 22 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        --- for Mac OS ---- 
        python3 -m pytest -v test2.py::test_all_one_matrix_2pt
        --- for Windows OS ---- 
        python -m pytest -v test2.py::test_all_one_matrix_2pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    Given a matrix of shape r X c, compute the sum of the elements in each column of the matrix. For example, if we have a matrix X as follows 
	 1, 1, 3 
	 1, 2, 2 
	 1, 3, 2 
 the sum of the elements in each column of the matrix will be s = [3,6,7]. 
    ---- Inputs: --------
        * X: a numpy matrix (2D array) of shape r X c.
    ---- Outputs: --------
        * s: a numpy vector (1D array) of length c, the i-th element of s (s[i]) is the sum of the i-th column of matrix X.
    ---- Hints: --------
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def mat_sum(X):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    s = X.sum(axis=0)
    #########################################
    return s
    #------ (3 points / 22 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        --- for Mac OS ---- 
        python3 -m pytest -v test2.py::test_mat_sum_3pt
        --- for Windows OS ---- 
        python -m pytest -v test2.py::test_mat_sum_3pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    Given a matrix X of shape r X c, and a scalar (a), the compute the product between the matrix and scalar: S = a X For example, if matrix X is: 
	 1, 1, 3 
	 1, 2, 2 
	 1, 2, 1 
 and a = 2, 
 then, ( S = a X ) should be: 
	 2, 2, 6 
	 2, 4, 4 
	 2, 4, 2. 
    ---- Inputs: --------
        * X: a numpy matrix (2D array) of shape r X c.
        * a: a float scalar.
    ---- Outputs: --------
        * S: a numpy matrix (2D array) of shape r X c.
    ---- Hints: --------
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def mat_scalar_multiplication(X, a):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    S = np.multiply(X, a)
    #########################################
    return S
    #------ (3 points / 22 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        --- for Mac OS ---- 
        python3 -m pytest -v test2.py::test_mat_scalar_multiplication_3pt
        --- for Windows OS ---- 
        python -m pytest -v test2.py::test_mat_scalar_multiplication_3pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    Given a matrix X and a column vector y, compute the product X*y = z 
 For example, if matrix X is: 
	 1, 2 
	 3, 4 
 and the column vector y is: 
	 5 
	 10 
 Then the result of the matrix vector multiplication (z = X y ) will be a vector: 
	 25 <--- which is computed as  5*1 + 10 * 2 
	 55 <--- which is computed as  5*3 + 10 * 4. 
    ---- Inputs: --------
        * X: a numpy matrix (2D array) of shape r X c.
        * y: a numpy vector (1D array) of length c.
    ---- Outputs: --------
        * z: a numpy vector of length r, the result of the matrix-vector product X*y.
    ---- Hints: --------
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def matrix_vector_multiplication(X, y):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    z = np.dot(X, y)
    #########################################
    return z
    #------ (3 points / 22 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        --- for Mac OS ---- 
        python3 -m pytest -v test2.py::test_matrix_vector_multiplication_3pt
        --- for Windows OS ---- 
        python -m pytest -v test2.py::test_matrix_vector_multiplication_3pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    Given a vector x of length  c, find indices of all zero elements in x. 
 For example, if vector x is: 0,0,4,0,5,7 
 then result d should be: [0,1,3], which indicates the indexes of the 0 elements in x. 
    ---- Inputs: --------
        * x: a numpy vector of length c, the result of the matrix-vector product X*y.
    ---- Outputs: --------
        * d: a numpy vector of length n, here n is the number of zero elements in the vector x, the i-th element of d (d[i]) is the index of the i-th zero in x.
    ---- Hints: --------
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def find_zeros(x):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    d = np.where(x==0)[0]
    #########################################
    return d
    #------ (3 points / 22 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        --- for Mac OS ---- 
        python3 -m pytest -v test2.py::test_find_zeros_3pt
        --- for Windows OS ---- 
        python -m pytest -v test2.py::test_find_zeros_3pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    Given a vector x of length  c, create a diagonal matrix D of shape (c X c), where the i-th diagonal element D[i,i] = x[i] All the off-diagonal elements of D are zeros: D[i,j] = 0, if i doesn't equal to j. 
 For example, if vector x is 1,2,3 
 then D should be: 
	 1,0,0 
	 0,2,0 
	 0,0,3. 
    ---- Inputs: --------
        * x: a numpy vector of length c, the result of the matrix-vector product X*y.
    ---- Outputs: --------
        * D: a numpy matrix of shape (c X c).
    ---- Hints: --------
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def diag_mat(x):
    #########################################
    ## INSERT YOUR CODE HERE (2 points)
    D = np.zeros((x.size, x.size), dtype = int)
    np.fill_diagonal(D, x)
    #########################################
    return D
    #------ (2 points / 22 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        --- for Mac OS ---- 
        python3 -m pytest -v test2.py::test_diag_mat_2pt
        --- for Windows OS ---- 
        python -m pytest -v test2.py::test_diag_mat_2pt
        ---------------------------------------------------
    '''
    
    


#--------------------------------------------

''' 
    TEST problem 2: (22 points)
        Now you can test the correctness of all the above functions by typing the following in the terminal:
        ---------------------------------------------------
        --- for Mac OS ---- 
        python3 -m pytest -v test2.py
        --- for Windows OS ---- 
        python -m pytest -v test2.py
        ---------------------------------------------------

        If your code passed all the tests, you will see the following message in the terminal:
        ----------- test session starts --------------------- 
        * (2 points) test2.py::ndarray_2pt  PASSED 
        * (2 points) test2.py::float_array_2pt  PASSED 
        * (2 points) test2.py::get_shape_2pt  PASSED 
        * (2 points) test2.py::all_one_matrix_2pt  PASSED 
        * (3 points) test2.py::mat_sum_3pt  PASSED 
        * (3 points) test2.py::mat_scalar_multiplication_3pt  PASSED 
        * (3 points) test2.py::matrix_vector_multiplication_3pt  PASSED 
        * (3 points) test2.py::find_zeros_3pt  PASSED 
        * (2 points) test2.py::diag_mat_2pt  PASSED 
        
        ============ 9 passed in 0.006s ======================
'''

#--------------------------------------------





#--------------------------------------------
'''
    List of All Variables 

* X:  a numpy matrix (2D array) of shape r X c. 
* Y:  a numpy matrix (2D array) of shape 2 X 3, where each element in the array is a float number. 
* Z:  a numpy matrix (2D array) of shape 2 X 3, where each element in the array is an integer. 
* O:  a numpy matrix of shape r X c, where all elements of the matrix are 1's. 
* r:  an integer, the number of rows in the matrix X. 
* c:  an integer, the number of columns in the matrix X. 
* s:  a numpy vector (1D array) of length c, the i-th element of s (s[i]) is the sum of the i-th column of matrix X. 
* y:  a numpy vector (1D array) of length c. 
* a:  a float scalar. 
* S:  a numpy matrix (2D array) of shape r X c. 
* z:  a numpy vector of length r, the result of the matrix-vector product X*y. 
* x:  a numpy vector of length c, the result of the matrix-vector product X*y. 
* d:  a numpy vector of length n, here n is the number of zero elements in the vector x, the i-th element of d (d[i]) is the index of the i-th zero in x. 
* D:  a numpy matrix of shape (c X c). 

'''
#--------------------------------------------