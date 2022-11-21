import pandas as pd
# Note: please don't import any new package. You should solve this problem using only the package(s) above.
#-------------------------------------------------------------------------

'''
    Problem 4: (Moneyball) Player Ranking for Oakland A's Baseball Team (OAK) in year 2002 (27 points)
    In this problem, you will rank baseball players for Oakland A's using different methods
    A list of all variables being used in this problem is provided at the end of this file.
'''

#----------------------------------------------------
'''
    (Compute Players' Batting Average) Given a dataframe (X6) of all the candidate players, compute the Batting Average (BA) of each player and insert a new column named 'BA' to store the data. 
    ---- Inputs: --------
        * X6: a dataframe containing all the candidate players for evaluation in the year (2001), who have sufficient experience (at least min_AB) and affordable price tag (at most max_salary).
    ---- Hints: --------
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def compute_players_BA(X6):
    #########################################
    ## INSERT YOUR CODE HERE (4 points)
    X6['BA'] = X6['H']/X6['AB']
    #########################################
    #------ (4 points / 27 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        python3 -m pytest -v test4.py::test_compute_players_BA_4pt
        --- OR ---- 
        python -m pytest -v test4.py::test_compute_players_BA_4pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    If you have passed the previous test case, the result data frame should have been saved into a file, called 'moneyball_X7.csv'.  Now let's rank all of these players using the traditional metric: Batting Average. 
(Rank Players by BA) Given a dataframe (X7) of all the candidate players, rank all the players based upon descending order of Batting Average (BA). 
 If you have solved this problem and passed the test case, the result data frame will be saved into a file, called 'moneyball_R1.csv'. You could take a look at the ranking results of the players. 
    ---- Inputs: --------
        * X7: a dataframe containing all the candidate players info, including Batting Average (BA).
    ---- Outputs: --------
        * R1: a dataframe containing candidate players ranked by descending order of Batting Average (BA).
    ---- Hints: --------
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def rank_players_BA(X7):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    R1 = X7.sort_values(by='BA', ascending=False)
    #########################################
    return R1
    #------ (3 points / 27 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        python3 -m pytest -v test4.py::test_rank_players_BA_3pt
        --- OR ---- 
        python -m pytest -v test4.py::test_rank_players_BA_3pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    (Compute Players' On-Base Percentage) Given a dataframe (X7) of all the candidate players, compute the (OBP) of each player and insert a new column named 'OBP' to store the data. 
    ---- Inputs: --------
        * X7: a dataframe containing all the candidate players info, including Batting Average (BA).
    ---- Hints: --------
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def compute_players_OBP(X7):
    #########################################
    ## INSERT YOUR CODE HERE (4 points)
    X7['OBP'] = (X7['H'] + X7['BB'] + X7['HBP'])/(X7['AB'] + X7['BB'] + X7['HBP'] + X7['SF'])
    #########################################
    #------ (4 points / 27 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        python3 -m pytest -v test4.py::test_compute_players_OBP_4pt
        --- OR ---- 
        python -m pytest -v test4.py::test_compute_players_OBP_4pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    If you have passed the previous test case, the result data frame should have been saved into a file, called 'moneyball_X8.csv'.  Now let's rank all of these players using the new metric: On-Base Percentage. 
(Rank Players by OBP) Given a dataframe (X8) of all the candidate players, rank all the players based upon descending order of On-Base Percentage (OBP). 
 If you have solved this problem and passed the test case, the result data frame will be saved into a file, called 'moneyball_R2.csv'. You could take a look at the ranking results of the players. 
    ---- Inputs: --------
        * X8: a dataframe containing all the candidate players info, including Batting Average (BA) and On-Base Percentage (OBP).
    ---- Outputs: --------
        * R2: a dataframe containing candidate players ranked by descending order of On-Base Percentage (OBP).
    ---- Hints: --------
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def rank_players_OBP(X8):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    R2 = X8.sort_values(by='OBP', ascending=False)
    #########################################
    return R2
    #------ (3 points / 27 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        python3 -m pytest -v test4.py::test_rank_players_OBP_3pt
        --- OR ---- 
        python -m pytest -v test4.py::test_rank_players_OBP_3pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    (Compute Players' 1B) Given a dataframe (X8) of all the candidate players, compute the number of singles (1B) of each player and insert a new column named '1B' to store the data. 
    ---- Inputs: --------
        * X8: a dataframe containing all the candidate players info, including Batting Average (BA) and On-Base Percentage (OBP).
    ---- Hints: --------
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def compute_players_1B(X8):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    X8['1B'] = X8['H'] - (X8['2B'] + X8['3B'] + X8['HR'])
    #########################################
    #------ (3 points / 27 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        python3 -m pytest -v test4.py::test_compute_players_1B_3pt
        --- OR ---- 
        python -m pytest -v test4.py::test_compute_players_1B_3pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    If you have passed the previous test case, the result data frame should have been saved into a file, called 'moneyball_X9.csv'.  Now let's compute the total number bases for each player. 
(Compute Players' TB) Given a dataframe (X9) of all the candidate players, compute the total number of bases (TB) of each player and insert a new column named 'TB' to store the data. 
    ---- Inputs: --------
        * X9: a dataframe containing all the candidate players info, including Batting Average (BA), On-Base Percentage (OBP) and Singles (1B).
    ---- Hints: --------
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def compute_players_TB(X9):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    X9['TB'] = X9['1B'] + 2*X9['2B'] + 3*X9['3B'] + 4*X9['HR']
    #########################################
    #------ (3 points / 27 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        python3 -m pytest -v test4.py::test_compute_players_TB_3pt
        --- OR ---- 
        python -m pytest -v test4.py::test_compute_players_TB_3pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    If you have passed the previous test case, the result data frame should have been saved into a file, called 'moneyball_X10.csv'.  Now let's compute the total number bases for each player. 
(Compute Players' SLG) Given a dataframe (X10) of all the candidate players, compute the slugging percentage (SLG) of each player and insert a new column named 'SLG' to store the data. 
    ---- Inputs: --------
        * X10: a dataframe containing all the candidate players info, including Batting Average (BA), On-Base Percentage (OBP) Singles (1B), and Total Bases (TB).
    ---- Hints: --------
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def compute_players_SLG(X10):
    #########################################
    ## INSERT YOUR CODE HERE (4 points)
    X10['SLG'] = X10['TB']/X10['AB']
    #########################################
    #------ (4 points / 27 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        python3 -m pytest -v test4.py::test_compute_players_SLG_4pt
        --- OR ---- 
        python -m pytest -v test4.py::test_compute_players_SLG_4pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    If you have passed the previous test case, the result data frame should have been saved into a file, called 'moneyball_X11.csv'.  Now let's rank all of these players using the new metric: Slugging Percentage. 
(Rank Players by SLG) Given a dataframe (X11) of all the candidate players, rank all the players based upon descending order of Slugging Percentage (SLG). 
 If you have solved this problem and passed the test case, the result data frame will be saved into a file, called 'moneyball_R3.csv'. You could take a look at the ranking results of the players. 
    ---- Inputs: --------
        * X11: a dataframe containing all the candidate players info, including Batting Average (BA), On-Base Percentage (OBP) Singles (1B), Total Bases (TB) and Slugging Percentage (SLG).
    ---- Outputs: --------
        * R3: a dataframe containing candidate players ranked by descending order of Slugging Percentage (SLG).
    ---- Hints: --------
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def rank_players_SLG(X11):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    R3 = X11.sort_values(by='SLG', ascending=False)
    #########################################
    return R3
    #------ (3 points / 27 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        python3 -m pytest -v test4.py::test_rank_players_SLG_3pt
        --- OR ---- 
        python -m pytest -v test4.py::test_rank_players_SLG_3pt
        ---------------------------------------------------
    '''
    
    


#--------------------------------------------

''' 
    TEST problem 4: (27 points)
        Now you can test the correctness of all the above functions by typing the following in the terminal:
        ---------------------------------------------------
        python3 -m pytest -v test4.py
        --- OR ---- 
        python -m pytest -v test4.py
        ---------------------------------------------------

        If your code passed all the tests, you will see the following message in the terminal:
        ----------- test session starts --------------------- 
        * (4 points) test4.py::compute_players_BA_4pt  PASSED 
        * (3 points) test4.py::rank_players_BA_3pt  PASSED 
        * (4 points) test4.py::compute_players_OBP_4pt  PASSED 
        * (3 points) test4.py::rank_players_OBP_3pt  PASSED 
        * (3 points) test4.py::compute_players_1B_3pt  PASSED 
        * (3 points) test4.py::compute_players_TB_3pt  PASSED 
        * (4 points) test4.py::compute_players_SLG_4pt  PASSED 
        * (3 points) test4.py::rank_players_SLG_3pt  PASSED 
        
        ============ 8 passed in 0.006s ======================
'''

#--------------------------------------------





#--------------------------------------------
'''
    List of All Variables 

* X6:  a dataframe containing all the candidate players for evaluation in the year (2001), who have sufficient experience (at least min_AB) and affordable price tag (at most max_salary). 
* X7:  a dataframe containing all the candidate players info, including Batting Average (BA). 
* X8:  a dataframe containing all the candidate players info, including Batting Average (BA) and On-Base Percentage (OBP). 
* X9:  a dataframe containing all the candidate players info, including Batting Average (BA), On-Base Percentage (OBP) and Singles (1B). 
* X10:  a dataframe containing all the candidate players info, including Batting Average (BA), On-Base Percentage (OBP) Singles (1B), and Total Bases (TB). 
* X11:  a dataframe containing all the candidate players info, including Batting Average (BA), On-Base Percentage (OBP) Singles (1B), Total Bases (TB) and Slugging Percentage (SLG). 
* R1:  a dataframe containing candidate players ranked by descending order of Batting Average (BA). 
* R2:  a dataframe containing candidate players ranked by descending order of On-Base Percentage (OBP). 
* R3:  a dataframe containing candidate players ranked by descending order of Slugging Percentage (SLG). 

'''
#--------------------------------------------