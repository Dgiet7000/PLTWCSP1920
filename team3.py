####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team 3.'# Only 10 chars displayed
strategy_name = 'Collude but retaliate'
strategy_description = '''\
Collude first round, then continue to collude unless the other team has more than 3 betrayals in the last 10 rounds.'''

import random

def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    if len(my_history)==0: # It's the first round; collude.
        return 'c'
    elif 'b' in their_history[-10:] > 3:
        if random.random()<0.5:           
            return 'b' # Betray if they were severely punished last time,
        else:
            return 'c' # otherwise collude.
    else:
        return 'c'
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

### 
#over 3 betrays in last 10 rounds 50% chance of betraying