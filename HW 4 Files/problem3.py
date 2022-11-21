import numpy as np
from problem2 import *
# Note: please don't import any new package. You should solve this problem using only the package(s) above.
#-------------------------------------------------------------------------

'''
    Problem 3: Collaborative Filtering (50 points)
    In this problem, you will implement a collaborative filtering recommender system. We will user matrix decomposition to decompose the rating matrix and find optimal hidden factors for both users and items using alternative coordinate descent
    A list of all variables being used in this problem is provided at the end of this file.
'''

#----------------------------------------------------
'''
    (Extract Training Data for User j) Given the rating vector of the j-th User (R_j) and the hidden factors of all items (I), extract a training dataset for User j, by excluding the missing ratings. 
	  There can be missing values in the rating vector (R_j), 
	      When R_j[i] is NaN (missing), which means that the user j has not yet rated the i-th item, so we should exclude the i-th item from the training dataset; 
	      When R_j[i] is not missing, which means that the user has rated the i-th item, we should include the i-th item in the training dataset. 
	  For example, if we have 4 items, ratings of the j-th user on the 4 items are: 
	      R_j= [1,?,2,?] 
	  Suppose we have 2 hidden factors, the 2 hidden factors of the 4 items are in Matrix I (4 X 2): 
	      I = [[0.1,  0.2], 
	           [0.3,  0.4], 
	           [0.5,  0.6], 
	           [0.7,  0.8]] 
	  In order to train the linear regression model for the j-th user, we have the following training dataset: 
	      X = [[0.1,  0.2], 
	           [0.5,  0.6]] 
	  This is because for user j, we only have ratings in the 1st and 3rd item, so the features of the two items are [0.1,0.2] and [0.5,0.6]. 
	  Now the labels of the linear regression are the ratings of the two items: 
	      y = [1,2] . 
    ---- Inputs: --------
        * R_j: the ratings of all items by the j-th user (including missing ratings), a float numpy vector of length m, where R_j[i] is the rating of j-th user on the i-th item, which could be a float scalar or a NaN (Not a Number, missing rating).
        * I: the hidden factors of all items, a float numpy matrix of shape (m X k), where I[i,j] is the j-th hidden factor of the i-th item.
    ---- Outputs: --------
        * X: the feature matrix of the training samples, where each row X[i] represents the feature vector for the i-th training sample in the training dataset.
        * y: the labels of the training samples, a numpy vector, y[i] represents the label of the i-th training sample in the training dataset.
    ---- Hints: --------
        * This problem can be solved using 2 line(s) of code.
'''
#----------------------
def extract_user_j(R_j, I):
    #########################################
    ## INSERT YOUR CODE HERE (7 points)
    y = R_j[~np.isnan(R_j)]
    X = I[np.where(~np.isnan(R_j))]
    #########################################
    return X, y
    #------ (7 points / 50 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        --- for Mac OS ---- 
        python3 -m pytest -v test3.py::test_extract_user_j_7pt
        --- for Windows OS ---- 
        python -m pytest -v test3.py::test_extract_user_j_7pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    (Train Ridge Regression Model for User j) Given training set for the j-th User (X, y), train a ridge regression model to get the hidden factors of User j (Uj), which is the weights w of the ridge regression model. 
    ---- Inputs: --------
        * X: the feature matrix of the training samples, where each row X[i] represents the feature vector for the i-th training sample in the training dataset.
        * y: the labels of the training samples, a numpy vector, y[i] represents the label of the i-th training sample in the training dataset.
        * a: (alpha) the weight for the regularization term on the hidden factors (to shrink their values), a float scalar.
    ---- Outputs: --------
        * Uj: the hidden factors of the j-th user, a float vector of length (k), where Uj[i] is the i-th hidden factor of the j-th user.
    ---- Hints: --------
        * You could use some function that you have implemented in the previous problem (problem2.py). 
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def train_user_j(X, y, a=1e-05):
    #########################################
    ## INSERT YOUR CODE HERE (7 points)
    Uj = ridge_regression(X, y, a)
    #########################################
    return Uj
    #------ (7 points / 50 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        --- for Mac OS ---- 
        python3 -m pytest -v test3.py::test_train_user_j_7pt
        --- for Windows OS ---- 
        python -m pytest -v test3.py::test_train_user_j_7pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    (Train Ridge Regression Models for All Users) Given the rating matrix for all Users (R) and the hidden factors of all items (I), train the hidden factors for all users (U) by extracting a training dataset and training a ridge regression model on each user. 
	 Suppose we have two users (User 1 and User 2). The ratings of all users (1 and 2) on all items (A,B,C,D): 
	      R = [[ 1,  ? ], 
	           [ ?,  4 ], 
	           [ 5,  ? ], 
	           [ ?,  2 ]] 
	      The rating of User 1 on Item A is 1 ; 
	      The rating of User 1 on Item B is ? (missing); 
	      The rating of User 1 on Item C is 5 ; 
	      The rating of User 1 on Item D is ? (missing). 
	      The rating of User 2 on Item A is ? (missing); 
	      The rating of User 2 on Item B is 4 ; 
	      The rating of User 2 on Item C is ? (missing); 
	      The rating of User 2 on Item D is 2 . 
	 Suppose we have 2 hidden factors, the hidden factors of the 4 items is matrix I (4 X 2): 
	      I = [[0.1, 0.2], 
	           [0.3, 0.4], 
	           [0.5, 0.6], 
	           [0.7, 0.8]] 
	 Now we want to build a ridge regression model for both Users 1 and 2. 
	 For User 1, the training dataset will be : 
	      X1 = [[0.1, 0.2 ], 
	            [0.5, 0.6 ]] 
	      y1 = [1, 5] 
	 After training the ridge regression model, the hidden factors of User 1 is U1: 
	      U1 = [10, 0] 
	 For User 2, the training dataset will be : 
	      X2 = [[0.3, 0.4 ], 
	            [0.7, 0.8 ]] 
	      y2 = [4, 2] 
	 After training the ridge regression model, the hidden factors of User 2 is U2: 
	      U2 = [-60, 55] 
	 Now we can put together the hidden factors for both users: 
	      U = [U1, = [[ 10, 0 ], 
	           U2]    [-60, 55]] . 
    ---- Inputs: --------
        * R: the ratings of all items by all users (including missing ratings), a float numpy matrix of shape (m X n), where R[i,j] is the rating of j-th user on the i-th item, which could be a float scalar or a NaN (Not a Number, missing rating).
        * I: the hidden factors of all items, a float numpy matrix of shape (m X k), where I[i,j] is the j-th hidden factor of the i-th item.
        * a: (alpha) the weight for the regularization term on the hidden factors (to shrink their values), a float scalar.
    ---- Outputs: --------
        * U: the hidden factors of all users, a float numpy matrix of shape (n X k), where U[i,j] is the j-th hidden factor of the i-th user.
    ---- Hints: --------
        * To extract the i-th column of a matrix A, you could use A[:,i]. 
        * This problem can be solved using 4 line(s) of code.
'''
#----------------------
def update_U(R, I, a=1e-05):
    #########################################
    ## INSERT YOUR CODE HERE (7 points)
    U = np.ones((R.shape[1], I.shape[1]))
    for i in range(U.shape[0]):
        X, y = extract_user_j(R[:, i], I) 
        w = train_user_j(X, y, a)
        U[i] = w
    #########################################
    return U
    #------ (7 points / 50 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        --- for Mac OS ---- 
        python3 -m pytest -v test3.py::test_update_U_7pt
        --- for Windows OS ---- 
        python -m pytest -v test3.py::test_update_U_7pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    (Extract Training Data for Item j) Given the rating vector of the i-th Item (Ri_) and the hidden factors of all users (U), extract a training dataset for Item i, by excluding the missing ratings. 
	  There can be missing values in the rating vector (Ri_), 
	      When Ri_[j] is NaN (missing), which means that the user j has not yet rated the i-th item, so we should exclude the j-th user from the training dataset; 
	      When Ri_[j] is not missing, which means that the user j has rated the i-th item, we should include the j-th user in the training dataset. 
	  For example, if we have 4 users, ratings of the 4 users on the i-th item are: 
	      Ri_= [1,?,2,?] 
	  Suppose we have 2 hidden factors, the 2 hidden factors of the 4 users are in the Matrix U (4 X 2): 
	      U = [[0.1,  0.2], 
	           [0.3,  0.4], 
	           [0.5,  0.6], 
	           [0.7,  0.8]] 
	  In order to train the linear regression model for the i-th item, we have the following training dataset: 
	      X = [[0.1,  0.2], 
	           [0.5,  0.6]] 
	  This is because for Item i, we only have ratings in the 1st and 3rd users, so the features of the two items are [0.1,0.2] and [0.5,0.6]. 
	  Now the labels of the linear regression are the ratings of the two users: 
	      y = [1,2] . 
    ---- Inputs: --------
        * Ri_: the ratings of the i-th item by all users (including missing ratings), a float numpy vector of length m, where Ri_[j] is the rating of j-th user on the i-th item, which could be a float scalar or a NaN (Not a Number, missing rating).
        * U: the hidden factors of all users, a float numpy matrix of shape (n X k), where U[i,j] is the j-th hidden factor of the i-th user.
    ---- Outputs: --------
        * X: the feature matrix of the training samples, where each row X[i] represents the feature vector for the i-th training sample in the training dataset.
        * y: the labels of the training samples, a numpy vector, y[i] represents the label of the i-th training sample in the training dataset.
    ---- Hints: --------
        * You could re-use the previous functions in this file. 
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def extract_item_i(Ri_, U):
    #########################################
    ## INSERT YOUR CODE HERE (7 points)
    X, y = extract_user_j(Ri_, U)
    #########################################
    return X, y
    #------ (7 points / 50 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        --- for Mac OS ---- 
        python3 -m pytest -v test3.py::test_extract_item_i_7pt
        --- for Windows OS ---- 
        python -m pytest -v test3.py::test_extract_item_i_7pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    (Train Ridge Regression Model for Item i) Given training set for the i-th Item (X, y), train a ridge regression model to get the hidden factors of Item i (Ii), which is the weights w of the ridge regression model. 
    ---- Inputs: --------
        * X: the feature matrix of the training samples, where each row X[i] represents the feature vector for the i-th training sample in the training dataset.
        * y: the labels of the training samples, a numpy vector, y[i] represents the label of the i-th training sample in the training dataset.
        * a: (alpha) the weight for the regularization term on the hidden factors (to shrink their values), a float scalar.
    ---- Outputs: --------
        * Ii: the hidden factors of the i-th item, a float vector of length (k), where Ii[j] is the j-th hidden factor of the i-th item.
    ---- Hints: --------
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def train_item_i(X, y, a=1e-05):
    #########################################
    ## INSERT YOUR CODE HERE (7 points)
    Ii = train_user_j(X, y, a)
    #########################################
    return Ii
    #------ (7 points / 50 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        --- for Mac OS ---- 
        python3 -m pytest -v test3.py::test_train_item_i_7pt
        --- for Windows OS ---- 
        python -m pytest -v test3.py::test_train_item_i_7pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    (Train Ridge Regression Models for All Items) Given the rating matrix for all Users (R) and the hidden factors of all users (U), train the hidden factors for all items (I) by extracting a training dataset and training a ridge regression model on each item. 
    ---- Inputs: --------
        * R: the ratings of all items by all users (including missing ratings), a float numpy matrix of shape (m X n), where R[i,j] is the rating of j-th user on the i-th item, which could be a float scalar or a NaN (Not a Number, missing rating).
        * U: the hidden factors of all users, a float numpy matrix of shape (n X k), where U[i,j] is the j-th hidden factor of the i-th user.
        * a: (alpha) the weight for the regularization term on the hidden factors (to shrink their values), a float scalar.
    ---- Outputs: --------
        * I: the hidden factors of all items, a float numpy matrix of shape (m X k), where I[i,j] is the j-th hidden factor of the i-th item.
    ---- Hints: --------
        * You could re-use a previous function in this file to solve this problem. 
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def update_I(R, U, a=1e-05):
    #########################################
    ## INSERT YOUR CODE HERE (7 points)
    I = update_U(R.T, U, a)
    #########################################
    return I
    #------ (7 points / 50 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        --- for Mac OS ---- 
        python3 -m pytest -v test3.py::test_update_I_7pt
        --- for Windows OS ---- 
        python -m pytest -v test3.py::test_update_I_7pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    (Collaborative Filtering by Matrix Decomposition) Given the rating matrix R (with missing values), compute the hidden factors of items (I) and users (U) using alternative coordinate descent. . 
    ---- Inputs: --------
        * R: the ratings of all items by all users (including missing ratings), a float numpy matrix of shape (m X n), where R[i,j] is the rating of j-th user on the i-th item, which could be a float scalar or a NaN (Not a Number, missing rating).
        * k: the number of hidden factors for each item/user, an integer scalar.
        * a: (alpha) the weight for the regularization term on the hidden factors (to shrink their values), a float scalar.
        * n_steps: the number of iteration steps for coordinate descent.
    ---- Outputs: --------
        * I: the hidden factors of all items, a float numpy matrix of shape (m X k), where I[i,j] is the j-th hidden factor of the i-th item.
        * U: the hidden factors of all users, a float numpy matrix of shape (n X k), where U[i,j] is the j-th hidden factor of the i-th user.
    ---- Hints: --------
        * (1) update U while fixing I. 
        * (2) update I while fixing U. 
        * This problem can be solved using 2 line(s) of code.
'''
#----------------------
def collaborative_filtering(R, k=5, a=1e-05, n_steps=20):
    m,n = R.shape
    I = np.random.rand(m,k) # randomly initialize matrix I
    U = np.random.rand(n,k) # randomly initialize matrix U
    for _ in range(n_steps): # repeat n_steps
        #########################################
        ## INSERT YOUR CODE HERE (8 points)
        U = update_U(R, I, a)
        I = update_I(R, U, a)
        #########################################
    return I, U
    #------ (8 points / 50 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        --- for Mac OS ---- 
        python3 -m pytest -v test3.py::test_collaborative_filtering_8pt
        --- for Windows OS ---- 
        python -m pytest -v test3.py::test_collaborative_filtering_8pt
        ---------------------------------------------------
    '''
    
    


#--------------------------------------------

''' 
    TEST problem 3: (50 points)
        Now you can test the correctness of all the above functions by typing the following in the terminal:
        ---------------------------------------------------
        --- for Mac OS ---- 
        python3 -m pytest -v test3.py
        --- for Windows OS ---- 
        python -m pytest -v test3.py
        ---------------------------------------------------

        If your code passed all the tests, you will see the following message in the terminal:
        ----------- test session starts --------------------- 
        * (7 points) test3.py::extract_user_j_7pt  PASSED 
        * (7 points) test3.py::train_user_j_7pt  PASSED 
        * (7 points) test3.py::update_U_7pt  PASSED 
        * (7 points) test3.py::extract_item_i_7pt  PASSED 
        * (7 points) test3.py::train_item_i_7pt  PASSED 
        * (7 points) test3.py::update_I_7pt  PASSED 
        * (8 points) test3.py::collaborative_filtering_8pt  PASSED 
        
        ============ 7 passed in 0.006s ======================
'''

#--------------------------------------------





#--------------------------------------------
'''
    List of All Variables 

* m:  the number of items in the recommender system, an integer scalar. 
* n:  the number of users in the recommender system, an integer scalar. 
* k:  the number of hidden factors for each item/user, an integer scalar. 
* R:  the ratings of all items by all users (including missing ratings), a float numpy matrix of shape (m X n), where R[i,j] is the rating of j-th user on the i-th item, which could be a float scalar or a NaN (Not a Number, missing rating). 
* R_j:  the ratings of all items by the j-th user (including missing ratings), a float numpy vector of length m, where R_j[i] is the rating of j-th user on the i-th item, which could be a float scalar or a NaN (Not a Number, missing rating). 
* Ri_:  the ratings of the i-th item by all users (including missing ratings), a float numpy vector of length m, where Ri_[j] is the rating of j-th user on the i-th item, which could be a float scalar or a NaN (Not a Number, missing rating). 
* X:  the feature matrix of the training samples, where each row X[i] represents the feature vector for the i-th training sample in the training dataset. 
* y:  the labels of the training samples, a numpy vector, y[i] represents the label of the i-th training sample in the training dataset. 
* I:  the hidden factors of all items, a float numpy matrix of shape (m X k), where I[i,j] is the j-th hidden factor of the i-th item. 
* Ii:  the hidden factors of the i-th item, a float vector of length (k), where Ii[j] is the j-th hidden factor of the i-th item. 
* U:  the hidden factors of all users, a float numpy matrix of shape (n X k), where U[i,j] is the j-th hidden factor of the i-th user. 
* Uj:  the hidden factors of the j-th user, a float vector of length (k), where Uj[i] is the i-th hidden factor of the j-th user. 
* a:  (alpha) the weight for the regularization term on the hidden factors (to shrink their values), a float scalar. 
* n_steps:  the number of iteration steps for coordinate descent. 

'''
#--------------------------------------------