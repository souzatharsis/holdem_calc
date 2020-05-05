import time
import holdem_functions
import holdem_argparser
from poker.hand import Combo

suit_dict = {'♠': 's', '♣': 'c', '♥': 'h', '♦': 'd'}

# convert a combo object (package poker) to string
def combo_to_hand_str(combo: Combo) -> str:
    return ([str(combo.first.rank) + suit_dict[str(combo.first.suit)],
             str(combo.second.rank) + suit_dict[str(combo.second.suit)]])

def is_hand_consistent(hand, hand_reference):
    return not (hand[0] in hand_reference or hand[1] in hand_reference)

def are_cards_consistent(board, hero_cards, villan_cards):
    return (is_hand_consistent(hero_cards, board) and 
            is_hand_consistent(villan_cards, board) and 
            is_hand_consistent(hero_cards, villan_cards) )
 

# calculate odds against villan hole cards
def calculate_odds_villan(board, exact, num, input_file, hero_cards, 
                          villan_cards, verbose, print_elapsed_time):
    
    # convert a combo object (package poker) to string
    hero_cards = combo_to_hand_str(hero_cards)
    if villan_cards is None:
        villan_cards = ["?", "?"]
    else:
        villan_cards = combo_to_hand_str(villan_cards)


    if(not are_cards_consistent(board, hero_cards, villan_cards)):
        return None

        
    hole_cards = hero_cards + villan_cards

   
    args = holdem_argparser.LibArgs(board, exact, num, input_file, hole_cards)
    hole_cards, n, e, board, filename = holdem_argparser.parse_lib_args(args)
    return run(hole_cards, n, e, board, filename, verbose, print_elapsed_time)

# calculate odds given table's hole cards
def calculate(board, exact, num, input_file, hole_cards, verbose, print_elapsed_time):
    
    args = holdem_argparser.LibArgs(board, exact, num, input_file, hole_cards)
    hole_cards, n, e, board, filename = holdem_argparser.parse_lib_args(args)
    return run(hole_cards, n, e, board, filename, verbose, print_elapsed_time)

def run(hole_cards, num, exact, board, file_name, verbose, print_elapsed_time=False):
    t0= time.time()
    if file_name:
        input_file = open(file_name, 'r')
        for line in input_file:
            if line is not None and len(line.strip()) == 0:
                continue
            hole_cards, board = holdem_argparser.parse_file_args(line)
            deck = holdem_functions.generate_deck(hole_cards, board)
            run_simulation(hole_cards, num, exact, board, deck, verbose)
            print ("-----------------------------------")
        input_file.close()
    else:
        deck = holdem_functions.generate_deck(hole_cards, board)
        result = run_simulation(hole_cards, num, exact, board, deck, verbose)
        
        if print_elapsed_time:
            print("Time elapsed: ", time.time() - t0)
        
        return result

## it was calculating exact if board is given even if exact flag is False
def run_simulation(hole_cards, num, exact, given_board, deck, verbose):
    num_players = len(hole_cards)
    # Create results data structures which track results of comparisons
    # 1) result_histograms: a list for each player that shows the number of
    #    times each type of poker hand (e.g. flush, straight) was gotten
    # 2) winner_list: number of times each player wins the given round
    # 3) result_list: list of the best possible poker hand for each pair of
    #    hole cards for a given board
    result_histograms, winner_list = [], [0] * (num_players + 1)
    for _ in range(num_players):
        result_histograms.append([0] * len(holdem_functions.hand_rankings))
    # Choose whether we're running a Monte Carlo or exhaustive simulation
    board_length = 0 if given_board is None else len(given_board)

    if exact:
        generate_boards = holdem_functions.generate_exhaustive_boards
    else:
        generate_boards = holdem_functions.generate_random_boards
    if (None, None) in hole_cards:
        hole_cards_list = list(hole_cards)
        unknown_index = hole_cards.index((None, None))
        for filler_hole_cards in holdem_functions.generate_hole_cards(deck):
            hole_cards_list[unknown_index] = filler_hole_cards
            deck_list = list(deck)
            deck_list.remove(filler_hole_cards[0])
            deck_list.remove(filler_hole_cards[1])
            holdem_functions.find_winner(generate_boards, tuple(deck_list),
                                         tuple(hole_cards_list), num,
                                         board_length, given_board, winner_list,
                                         result_histograms)
    else:
        holdem_functions.find_winner(generate_boards, deck, hole_cards, num,
                                     board_length, given_board, winner_list,
                                     result_histograms)
    if verbose:
        players_histograms = holdem_functions.calc_histogram(result_histograms, winner_list)
        
    return [holdem_functions.find_winning_percentage(winner_list), players_histograms]