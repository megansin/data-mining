import pandas as pd
# Note: please don't import any new package. You should solve this problem using only the package(s) above.
#-------------------------------------------------------------------------

'''
    Problem 3: Elo ranking algorithm (25 points)
    In this problem, you will implement the Elo rating algorithm to rank players based upon match results (win/lose). Assuming all the players' performance are random following a Logistic distribution with a scale of 400

    A list of all variables being used in this problem is provided at the end of this file.
'''

#----------------------------------------------------
'''
    Given the current ratings of player A and player B, compute the expected probability of player A (with rating RA) to win in a game against player B (with rating RB). 
    ---- Inputs: --------
        * RA: the rating of player A (the average performance of the player), a float scalar value.
        * RB: the rating of player B (the average performance of the player), a float scalar value.
    ---- Outputs: --------
        * EA: the expected probability of player A wins when competing with player B in a game, a float scalar value between 0 and 1.
    ---- Hints: --------
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def compute_EA(RA, RB):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    EA = 1/(1+10**((RB-RA)/400))
    #########################################
    return EA
    #------ (5 points / 25 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        python3 -m pytest -v test3.py::test_compute_EA_5pt
        --- OR ---- 
        python -m pytest -v test3.py::test_compute_EA_5pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    Given the expected probability of player A (with rating RA) to win in a game against a player B (with rating RB). 
    ---- Inputs: --------
        * EA: the expected probability of player A wins when competing with player B in a game, a float scalar value between 0 and 1.
    ---- Outputs: --------
        * EB: the expected probability of player B wins when competing with player A in a game, a float scalar value between 0 and 1.
    ---- Hints: --------
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def compute_EB(EA):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    EB = 1 - EA
    #########################################
    return EB
    #------ (5 points / 25 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        python3 -m pytest -v test3.py::test_compute_EB_5pt
        --- OR ---- 
        python -m pytest -v test3.py::test_compute_EB_5pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    Given the result of one game between player A and player B, the current ratings of both players, compute the new rating of player A. 
    ---- Inputs: --------
        * RA: the rating of player A (the average performance of the player), a float scalar value.
        * SA: the result of one game where player A is competing with player B, a scalar value. If player A wins in this game, SA = 1; if player A loses, SA =0.
        * EA: the expected probability of player A wins when competing with player B in a game, a float scalar value between 0 and 1.
        * K: k-factor, a constant number which controls how maximum amount of change that can be applied on the rating of a player based upon the result of one game.
    ---- Outputs: --------
        * RA: the rating of player A (the average performance of the player), a float scalar value.
    ---- Hints: --------
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def update_RA(RA, SA, EA, K=16):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    RA = RA + K * (SA - EA)
    #########################################
    return RA
    #------ (5 points / 25 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        python3 -m pytest -v test3.py::test_update_RA_5pt
        --- OR ---- 
        python -m pytest -v test3.py::test_update_RA_5pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    Given the result of one game between player A and player B, the current ratings of both players, compute the new rating of player B. 
    ---- Inputs: --------
        * RB: the rating of player B (the average performance of the player), a float scalar value.
        * SB: the result of one game where player B is competing with player A, a scalar value. If player B wins in this game, SB = 1; if player B loses, SB =0.
        * EB: the expected probability of player B wins when competing with player A in a game, a float scalar value between 0 and 1.
        * K: k-factor, a constant number which controls how maximum amount of change that can be applied on the rating of a player based upon the result of one game.
    ---- Outputs: --------
        * RB: the rating of player B (the average performance of the player), a float scalar value.
    ---- Hints: --------
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def update_RB(RB, SB, EB, K=16):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    RB = RB + K * (SB - EB)
    #########################################
    return RB
    #------ (5 points / 25 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        python3 -m pytest -v test3.py::test_update_RB_5pt
        --- OR ---- 
        python -m pytest -v test3.py::test_update_RB_5pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    Given the result of one game between player A and player B, the current ratings of both players, compute the new ratings of players A and B. 
    ---- Inputs: --------
        * G: a dataframe of all the game results, a pandas data frame of shape (m by 2), where each row of the matrix G[i] represents the result of the i-th game, and G[i] = (A,B) contains the IDs of the winning team (A) and losing team (B) in the game.
        * n: the total number of players to rank, an integer scalar.
        * K: k-factor, a constant number which controls how maximum amount of change that can be applied on the rating of a player based upon the result of one game.
    ---- Outputs: --------
        * R: the ratings of all the n players, a list of length n, where R[i] represents the current rating of the i-th player.
    ---- Hints: --------
        * Step 1 extract current rating of the winning player (A) of the game from the list R. 
        * Step 2 extract current rating of the losing player (B) of the game from the list R. 
        * Step 3 compute the expected winning probability of player A in the game. 
        * Step 4 compute the expected winning probability of player B in the game. 
        * Step 5 update player A's rating based upon the game result and write it back to the list R. 
        * Step 6 update player B's rating based upon the game result and write it back to the list R. 
        * This problem can be solved using 5 line(s) of code.
'''
#----------------------
def compute_ratings(G, n, K=16):
    R = [400]*n # initialize the ratings of all players with 400
    for index, row in G.iterrows(): # for each game, update the ratings based upon the result of the game
        A,B = row["win_ID"], row["lose_ID"] # # extract the player IDs as A and B
        SA,SB = 1,0 # the game result: Player A wins, Player B loses
        #########################################
        ## INSERT YOUR CODE HERE (5 points)
        probWinA = compute_EA(R[A], R[B])
        probWinB = compute_EB(probWinA)
        R[A] = update_RA(R[A], SA, probWinA, K)
        R[B] = update_RB(R[B], SB, probWinB, K)
        #########################################
    return R
    #------ (5 points / 25 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        python3 -m pytest -v test3.py::test_compute_ratings_5pt
        --- OR ---- 
        python -m pytest -v test3.py::test_compute_ratings_5pt
        ---------------------------------------------------
    '''
    
    


#--------------------------------------------

''' 
    TEST problem 3: (25 points)
        Now you can test the correctness of all the above functions by typing the following in the terminal:
        ---------------------------------------------------
        python3 -m pytest -v test3.py
        --- OR ---- 
        python -m pytest -v test3.py
        ---------------------------------------------------

        If your code passed all the tests, you will see the following message in the terminal:
        ----------- test session starts --------------------- 
        * (5 points) test3.py::compute_EA_5pt  PASSED 
        * (5 points) test3.py::compute_EB_5pt  PASSED 
        * (5 points) test3.py::update_RA_5pt  PASSED 
        * (5 points) test3.py::update_RB_5pt  PASSED 
        * (5 points) test3.py::compute_ratings_5pt  PASSED 
        
        ============ 5 passed in 0.006s ======================
'''

#--------------------------------------------





#--------------------------------------------
'''
    List of All Variables 

* RA:  the rating of player A (the average performance of the player), a float scalar value. 
* RB:  the rating of player B (the average performance of the player), a float scalar value. 
* EA:  the expected probability of player A wins when competing with player B in a game, a float scalar value between 0 and 1. 
* EB:  the expected probability of player B wins when competing with player A in a game, a float scalar value between 0 and 1. 
* SA:  the result of one game where player A is competing with player B, a scalar value. If player A wins in this game, SA = 1; if player A loses, SA =0. 
* SB:  the result of one game where player B is competing with player A, a scalar value. If player B wins in this game, SB = 1; if player B loses, SB =0. 
* K:  k-factor, a constant number which controls how maximum amount of change that can be applied on the rating of a player based upon the result of one game. 
* n:  the total number of players to rank, an integer scalar. 
* m:  the total number of games played, an integer scalar. 
* R:  the ratings of all the n players, a list of length n, where R[i] represents the current rating of the i-th player. 
* G:  a dataframe of all the game results, a pandas data frame of shape (m by 2), where each row of the matrix G[i] represents the result of the i-th game, and G[i] = (A,B) contains the IDs of the winning team (A) and losing team (B) in the game. 

'''
#--------------------------------------------