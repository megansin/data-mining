import pandas as pd
from problem3 import compute_ratings
# Note: please don't import any new package. You should solve this problem using only the package(s) above.
#-------------------------------------------------------------------------

'''
    Problem 4: Ranking NCAA teams using Elo ranking algorithm (30 points)
    In this problem, you will use the Elo rating algorithm to rank the NCAA teams, based upon a dataset of game results between the teams

    A list of all variables being used in this problem is provided at the end of this file.
'''

#----------------------------------------------------
'''
    (Load Game Data) Load game results from a CSV file into a pandas dataframe. Each row contains two numbers, which represents the IDs of the winning team and losing team in the game in one game. 
	 For example, if  we have three game results in the file: 
	    Game 1: team 0 wins, team 1 loses 
	    Game 2: team 1 wins, team 2 loses 
	    Game 3: team 0 wins, team 2 loses 
	 The dataframe will be: 
	    win_ID  | lose_ID 
	  --------------------- 
	    0       |    1 
	    1       |    2 
	    0       |    2 
	  --------------------- . 
    ---- Inputs: --------
        * filename_G: the file name of game results G, a string..
    ---- Outputs: --------
        * G: a dataframe of all the game results, a pandas data frame of shape (m by 2), where each row of the matrix G[i] represents the result of the i-th game, and G[i] = (A,B) contains the IDs of the winning team (A) and losing team (B) in the game.
    ---- Hints: --------
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def load_G(filename_G='ncaa_games.csv'):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    G = pd.read_csv(filename_G)
    #########################################
    return G
    #------ (5 points / 30 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        python3 -m pytest -v test4.py::test_load_G_5pt
        --- OR ---- 
        python -m pytest -v test4.py::test_load_G_5pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    (Load Team Names) Load the team names from a CSV file into a pandas dataframe. 
	 For example, if we have three teams in the file with names: 
	    Team 0: 'A' 
	    Team 1: 'B' 
	    Team 2: 'C' 
	 The dataframe will be: 
	    ID  | Name 
	  --------------- 
	    0   |   A 
	    1   |   B 
	    2   |   C 
	  --------------- . 
    ---- Inputs: --------
        * filename_teams: the file name of team names, a string. In this file, each row contains a name of a team, and the i-th row of the file contains the name of the i-th team (team ID = i). For example, the 0-th row contains the name of the team ID = 0 ("Liberty"), the 1-st row contains the name of the team ID=1 ("Randolph Col").
    ---- Outputs: --------
        * T: a dataframe of all the team names in NCAA,  such as "Liberty", "Randolph Col","Valparaiso".
    ---- Hints: --------
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def load_teams(filename_teams='ncaa_teams.csv'):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    T = pd.read_csv(filename_teams)
    #########################################
    return T
    #------ (5 points / 30 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        python3 -m pytest -v test4.py::test_load_teams_5pt
        --- OR ---- 
        python -m pytest -v test4.py::test_load_teams_5pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    (compute Elo ratings) Now let's compute the elo ratings of all the NCCA teams in the dataset. Given dataframe (G) containing all the game result between the teams, compute a Elo ratings of all teams. 
	 For example, if we have three teams (n = 3) and after computing Elo ratings, the ratings (R) is: 
	 The dataframe will be: 
	    ID  | Elo 
	  --------------- 
	    0   | 300 
	    1   | 500 
	    2   | 400 
	  ---------------
. 
    ---- Inputs: --------
        * G: a dataframe of all the game results, a pandas data frame of shape (m by 2), where each row of the matrix G[i] represents the result of the i-th game, and G[i] = (A,B) contains the IDs of the winning team (A) and losing team (B) in the game.
        * n: the total number of teams to rank, an integer scalar.
        * K: k-factor, a constant number which controls how maximum amount of change that can be applied on the rating of a team based upon the result of one game.
    ---- Outputs: --------
        * R: a dataframe of the Elo ratings of all the n teams, where i-th row of R contains the ID and the Elo rating of the i-th team.
    ---- Hints: --------
        * You could use some function implemented in problem 3 to solve this problem. 
        * This problem can be solved using 2 line(s) of code.
'''
#----------------------
def compute_elo(G, n, K=16):
    #########################################
    ## INSERT YOUR CODE HERE (10 points)
    R = pd.DataFrame(range(n), columns =['ID'])
    R['Elo'] = compute_ratings(G, n, K)
    #########################################
    return R
    #------ (10 points / 30 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        python3 -m pytest -v test4.py::test_compute_elo_10pt
        --- OR ---- 
        python -m pytest -v test4.py::test_compute_elo_10pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    If you have passed the previous test case, the result data frame should have been saved into a file, called 'ncaa_R.csv. Now the dataset only contains Elo ratings, but no team name is available. We have another CSV file 'ncaa_teams.csv', which contains the team names. It would be better if we can combine these two datasets into one data frame, so the new data frame contains both team names and Elo ratings. 
 (Merge the two dataframes) Given a data frame (T) of team names , and a data frame (R) of Elo ratings (loaded from 'ncaa_R.csv'), Combine the two data frames into one, according to the ID column. . 
    ---- Inputs: --------
        * T: a dataframe of all the team names in NCAA,  such as "Liberty", "Randolph Col","Valparaiso".
        * R: a dataframe of the Elo ratings of all the n teams, where i-th row of R contains the ID and the Elo rating of the i-th team.
    ---- Outputs: --------
        * X: a dataframe of all the team names in NCAA merged with their Elo ratings.
    ---- Hints: --------
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def merge_team(T, R):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    X = T.merge(R, how='inner', on='ID')
    #########################################
    return X
    #------ (5 points / 30 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        python3 -m pytest -v test4.py::test_merge_team_5pt
        --- OR ---- 
        python -m pytest -v test4.py::test_merge_team_5pt
        ---------------------------------------------------
    '''
    
    

#----------------------------------------------------
'''
    If you have passed the previous test case, the result data frame should have been saved into a file, called 'ncaa_X.csv'.  Now let's rank all of these teams using the Elo ratings in descending order. 
(Rank Teams by Elo) Given a dataframe (X) of all the teams, rank all the teams based upon descending order of Elo ratings (Elo). 
 If you have solved this problem and passed the test case, the result data frame will be saved into a file, called 'ncaa_R.csv'. You could take a look at the ranking results of the teams. 
    ---- Inputs: --------
        * X: a dataframe of all the team names in NCAA merged with their Elo ratings.
    ---- Outputs: --------
        * Y: a dataframe of all the team names in NCAA sorted according to the descending order of their Elo ratings.
    ---- Hints: --------
        * This problem can be solved using 1 line(s) of code.
'''
#----------------------
def rank_teams_Elo(X):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    Y = X.sort_values(by='Elo', ascending=False)
    #########################################
    return Y
    #------ (5 points / 30 total points) -----------
    '''  
        TEST: Now you can test the correctness of your code above by typing the following in the terminal:
        ---------------------------------------------------
        python3 -m pytest -v test4.py::test_rank_teams_Elo_5pt
        --- OR ---- 
        python -m pytest -v test4.py::test_rank_teams_Elo_5pt
        ---------------------------------------------------
    '''
    
    


#--------------------------------------------

''' 
    TEST problem 4: (30 points)
        Now you can test the correctness of all the above functions by typing the following in the terminal:
        ---------------------------------------------------
        python3 -m pytest -v test4.py
        --- OR ---- 
        python -m pytest -v test4.py
        ---------------------------------------------------

        If your code passed all the tests, you will see the following message in the terminal:
        ----------- test session starts --------------------- 
        * (5 points) test4.py::load_G_5pt  PASSED 
        * (5 points) test4.py::load_teams_5pt  PASSED 
        * (10 points) test4.py::compute_elo_10pt  PASSED 
        * (5 points) test4.py::merge_team_5pt  PASSED 
        * (5 points) test4.py::rank_teams_Elo_5pt  PASSED 
        
        ============ 5 passed in 0.006s ======================
'''

#--------------------------------------------





#--------------------------------------------
'''
    List of All Variables 

* filename_G:  the file name of game results G, a string.. 
* filename_teams:  the file name of team names, a string. In this file, each row contains a name of a team, and the i-th row of the file contains the name of the i-th team (team ID = i). For example, the 0-th row contains the name of the team ID = 0 ("Liberty"), the 1-st row contains the name of the team ID=1 ("Randolph Col"). 
* G:  a dataframe of all the game results, a pandas data frame of shape (m by 2), where each row of the matrix G[i] represents the result of the i-th game, and G[i] = (A,B) contains the IDs of the winning team (A) and losing team (B) in the game. 
* T:  a dataframe of all the team names in NCAA,  such as "Liberty", "Randolph Col","Valparaiso". 
* R:  a dataframe of the Elo ratings of all the n teams, where i-th row of R contains the ID and the Elo rating of the i-th team. 
* K:  k-factor, a constant number which controls how maximum amount of change that can be applied on the rating of a team based upon the result of one game. 
* n:  the total number of teams to rank, an integer scalar. 
* m:  the total number of games played, an integer scalar. 
* X:  a dataframe of all the team names in NCAA merged with their Elo ratings. 
* Y:  a dataframe of all the team names in NCAA sorted according to the descending order of their Elo ratings. 

'''
#--------------------------------------------