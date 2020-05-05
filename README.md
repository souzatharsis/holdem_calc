Poker Holdem Calculator 
=================

The Holdem Calculator library calculates the probability that a certain Texas Hold'em hand will win. This probability is approximated by running a Monte Carlo method or calculated exactly by simulating the set of all possible hands. The Holdem Calculator also shows how likely each set of hole cards is to make a certain poker hand. The default Monte Carlo simulations are generally accurate to the nearest percent. Accuracy can be improved by increasing the number of simulations that are run, but this will result in a longer running time.

## Usage:
If you want to use Holdem Calculator as a library, you can import holdem_calc or parallel_holdem_calc and call calculate(). The order of arguments to calculate() are as follows:

1. Board: These are the community cards supplied to the calculation. This is in the form of a list of strings, with each string representing a card. If you do not want to specify community cards, you can set board to be None. Example: ["As", "Ks", "Jd"]
2. Exact: This is a boolean which is True if you want an exact calculation, and False if you want a Monte Carlo simulation.
3. Number of Simulations: This is the number of iterations run in the Monte Carlo simulation. Note that this parameter is ignored if Exact is set to True. **This number must be positive, even if Exact is set to true.**
4. Input File: The name of the input file you want Holdem Calculator to read from. Mark as None, if you do not wish to read from a file. **If Input File is set, library calls will not return anything.**
5. Hole Cards: These are the hole cards for each of the players. This is in the form of a list of strings, with each string representing a card. Example: ["As", "Ks", "Jd", "Td"]
6. Verbose: This is a boolean which is True if you want Holdem Calculator to print the results.

Calls to calculate() return a list of floats. The first element in the list corresponds to the probability that a tie takes place. Each element after that corresponds to the probability one of the hole cards the user provides wins the hand. These probabilities occur in the order in which you list them.


	$ cat example.py
	import holdem_calc
	import parallel_holdem_calc

	print holdem_calc.calculate(["As", "Ks", "Jd"], True, 1, None, ["8s", "7s", "Qc", "Th"], False)
	print parallel_holdem_calc.calculate(None, True, 1, None, ["8s", "7s", "Ad", "Ac"], False)

	$ python example.py
	[0.00404040404040404, 0.36363636363636365, 0.6323232323232323]
	[0.0029375624889038396, 0.2287397564918379, 0.7683226810192583]
