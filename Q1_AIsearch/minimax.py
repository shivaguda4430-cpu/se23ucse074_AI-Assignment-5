def minimax_search(state):
    """
    Returns the best action for the current state using classic Minimax.
    """
    player = state.to_move()
    
    if player == 1: # Maximizer
        value, best_action = max_value(state)
    else: # Minimizer
        value, best_action = min_value(state)
        
    return best_action

def max_value(state):
    if state.is_terminal():
        return state.utility(), None
    
    v = float('-inf')
    best_action = None
    
    for action in state.get_actions():
        v2, _ = min_value(state.result(action))
        if v2 > v:
            v = v2
            best_action = action
    return v, best_action

def min_value(state):
    if state.is_terminal():
        return state.utility(), None
    
    v = float('inf')
    best_action = None
    
    for action in state.get_actions():
        v2, _ = max_value(state.result(action))
        if v2 < v:
            v = v2
            best_action = action
    return v, best_action
