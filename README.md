Poker Holdem Calculator 
=================

The Holdem Calculator library calculates the probability that a certain Texas Hold'em hand will win. This probability is approximated by running a Monte Carlo method or calculated exactly by simulating the set of all possible hands. The Holdem Calculator also shows how likely each set of hole cards is to make a certain poker hand. The default Monte Carlo simulations are generally accurate to the nearest percent. Accuracy can be improved by increasing the number of simulations that are run, but this will result in a longer running time.

This repository extends the implementation from ktseng/holdem_calc as it allows for odds calculation for poker hand ranges by levering the Python package **poker** which provides a framework for poker-related operations and entities such as Hands, Combos and Ranges.

## Supporting Material

[How to Calculate Poker Probabilities in Python](https://towardsdatascience.com/how-to-calculate-poker-probabilities-in-python-75238c61421e) is an article I published in Towards Data Science, which demonstrates the library's usage.

In this article, we show how to represent basic poker elements in Python, e.g., Hands and Combos, and how to calculate poker odds, i.e., likelihood of win/tie/lose in No-Limit Texas Hold'em. We provide a practical analysis based on a real story in a Night at the Venetian in Las Vegas.

[Here](https://github.com/souzatharsis/holdem_calc/blob/master/Night%20at%20the%20venetian.ipynb) is a corresponding Jupyter Notebook.

## Usage

If you want to use Holdem Calculator as a library, you can import holdem_calc and call calculate_odds_villan(). The order of arguments to calculate_odds_villan() are as follows:

1. board: These are the community cards supplied to the calculation. This is in the form of a list of strings, with each string representing a card. If you do not want to specify community cards, you can set board to be None. Example: ["As", "Ks", "Jd"]
2. exact_calculation: This is a boolean which is True if you want an exact calculation, and False if you want a Monte Carlo simulation.
4. num_sims: This is the number of iterations run in the Monte Carlo simulation. Note that this parameter is ignored if Exact is set to True. This number must be positive, even if Exact is set to true.
5. Input File: The name of the input file you want Holdem Calculator to read from. Mark as None, if you do not wish to read from a file. If Input File is set, library calls will not return anything.
4. hero_hand: This is an object of the type Combo (part of Poker.Hand), which represents the Player's hand
3. villan_hand: This is an object of the type Combo (part of Poker.Hand). None if no prior knowledge is known about the villan
7. verbose: This is a boolean which is True if you want Holdem Calculator to return the odds of the villan making a certain poker hand, e.g., quads, set, straight. It only supports heads-up scenario.
8. print_elapsed_time: This is a boolean which is True if you want to return elapsed time for calculation

Calls to calculate_odds_villan() returns a list with two elements. The first is a dictionary with values of type float which contains the odds of the Player to win/tie/lose. The second element of the list is returned if verbose is set to True and it returns the odds of the villan making a certain poker hand, e.g., quads, set, straight. It only supports heads-up scenario.

	from poker.hand import Combo

	import holdem_calc
	import holdem_functions
	
	board = ["Qc", "Th", "9s"]
	villan_hand = None
	exact_calculation = True
	verbose = True
	num_sims = 1
	read_from_file = None
	
	hero_hand = Combo('KsJc')

	odds = holdem_calc.calculate_odds_villan(board, exact_calculation, 
                            num_sims, read_from_file , 
                            hero_hand, villan_hand, 
                            verbose, print_elapsed_time = True)

	> print(odds[0])
	
	{'tie': 0.04138424018164999,
 	'win': 0.9308440557284221,
 	'lose': 0.027771704089927955}

## Backlog

1. Add multiplayer support when verbose = True
2. Port holdem_calc from string-based to support proper Poker.Hand objects (Hand, Combo, Range)
