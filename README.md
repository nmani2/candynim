# candynim
Generate sample games of Candy Nim to understand optimal play.


Getting Started: 
Primary user functionality can be found in CandyNimAmount.py. 
Launching this program will prompt you to select a cache size (-1 selects the entire cache, single digits are approximately no cache, and it takes approximately 10 seconds to load every million items in the cache).

Functions: 
Candy Nim games are given by a comma-separated list enclosed in square brackets:
(e.g. [1, 2, 4, 8], [1, 2, 3]). All user-facing functions require as input a Candy Nim game in the above format.

1. OptCandy(G) takes as input a game G given by a square-bracket enclosed comma separated list of positive integers. It returns the number of candies collected by the player who wins the underlying Nim game, assuming optimal play.

2. VerboseOutput(G) provides more information about game play in the Candy Nim game G. If there is a single optimal sequence of moves, the list of intermediate games is printed, along with the number of candies collected by the winner/loser (as well as which of them played first or second), as well as the difference in the number of candies.

3. place(candies,doinfo=False,restrict=True) accepts an integer candies and two boolean values doinfo, restrict (default False). The integer candies must be even. doinfo is a flag for providing verbose output for the game. restrict is a flag for applying a conjectured heuristic described in Conjecture 7.4 of P Play in Candy Nim to speed up computation.

Examples 

1. OptCandy([1, 2, 4, 8]) returns 4, the number of candies collected by the winning (in this case, first) player, assuming optimal play by both players.

2. VerboseOutput([1,2,4,8]) prints the following output:
The moves are:
[1, 2, 4, 7]
[1, 2, 4]
[1, 2, 3]
[1, 2]
Winner (first person):
4
Loser (second person):
11
The difference is:
7

3. If isn’t a single optimal move or sequence of moves, the program will prompt you to make a series of choices by listing all available optimal moves at each stage of game play in a 1-indexed list.  
VerboseOutput([1,4,3,9,5,6,7,8]) prints the following output:  
The moves are: [1, 3, 4, 4, 5, 6, 8, 9].   
Your options are:  [[1, 1, 4, 4, 5, 6, 8, 9], [1, 1, 3, 4, 5, 6, 8, 9], [1, 1, 3, 4, 5, 6, 8, 9], [1, 3, 4, 5, 6, 8, 9], [1, 3, 4, 4, 4, 5, 8, 9], [1, 1, 3, 4, 4, 5, 8, 9], [0, 1, 3, 4, 4, 5, 8, 9]].   
1 for first, 2 for second, so on.     
By selecting an integer, you pick which of the optimal move options you would like to proceed with. For example, say you respond
5  
and then return.   
The program subsequently prints out  
You chose:  [1, 3, 4, 4, 4, 5, 8, 9]  
[1, 1, 4, 4, 4, 5, 8, 9]  
[1, 1, 2, 4, 4, 4, 8, 9]  
Your options are:  [[1, 1, 2, 3, 4, 4, 8, 9], [1, 1, 2, 3, 4, 4, 8, 9]]   
1 is first, 2 is second, ...  
Again, we have a choice. Type in  
2  
and return. Again, you are provided a prompt:  
You chose:  [1, 1, 2, 3, 4, 4, 8, 9]  
Your options are:  [[0, 1, 1, 2, 4, 4, 8, 9], [1, 1, 2, 3, 3, 4, 8, 9], [1, 1, 1, 2, 3, 4, 8, 9], [1, 1, 2, 3, 3, 4, 8, 9], [1, 1, 2, 2, 3, 4, 8, 9], [1, 1, 1, 2, 3, 4, 8, 9], [0, 1, 1, 2, 3, 4, 8, 9]]  
If you choose  
1  
and return the program continues  
You chose:  [0, 1, 1, 2, 4, 4, 8, 9]  
[1, 1, 1, 4, 4, 8, 9]  
Your options are:  [[1, 1, 1, 2, 4, 8, 9], [0, 1, 1, 1, 4, 8, 9], [1, 1, 1, 3, 4, 8, 9], [1, 1, 1, 2, 4, 8, 9], [1, 1, 1, 1, 4, 8, 9], [0, 1, 1, 1, 4, 8, 9], [1, 1, 1, 4, 4, 6, 8]]  
Proceeding in this manner, we can provide input  
2  
You chose:  [0, 1, 1, 1, 4, 8, 9]  
[1, 1, 1, 8, 9]  
[1, 1, 1, 6, 8]  
[1, 1, 1, 6, 7]  
[1, 1, 1, 4, 6]  
[1, 1, 1, 4, 5]  
[1, 1, 1, 2, 4]  
[1, 1, 1, 2, 3]  
[1, 1, 1, 2]  
[1, 1, 1, 1]  
Your options are:  [[0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1]]  
1  
You chose:  [0, 1, 1, 1]  
Your options are:  [[1, 1], [1, 1]]  
1 is first, 2 is second, ...  
1  
You chose:  [1, 1]  
Winner (first person):  
17  
Loser (second person):  
26  
The difference is:  
9  
4. place(16,True,False) returns (with similar user input to VerboseOutput; in this case selecting the first option in both lists of possible moves provided)  
[[1, 1, 1, 2, 4, 7]]  
P  
The moves are:  
[1, 1, 1, 2, 4]  
[1, 1, 1, 2, 3]  
[1, 1, 1, 2]  
[1, 1, 1, 1]  
Your options are:  [[0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1]]  
1  
You chose:  [0, 1, 1, 1]  
Your options are:  [[1, 1], [1, 1]]  
1  
You chose:  [1, 1]  
Loser (first person):  
12  
Winner (second person):  
4  
The difference is:  
8  
[[1, 1, 1, 2, 4, 7]]  
