def alpha_beta_search(state):
    """
    Returns the best action using Alpha-Beta Pruning.
    """
    player = state.to_move()
    
    if player == 1:
        value, best_action = ab_max_value(state, float('-inf'), float('inf'))
    else:
        value, best_action = ab_min_value(state, float('-inf'), float('inf'))
        
    return best_action

def ab_max_value(state, alpha, beta):
    if state.is_terminal():
        return state.utility(), None
    
    v = float('-inf')
    best_action = None
    
    for action in state.get_actions():
        v2, _ = ab_min_value(state.result(action), alpha, beta)
        if v2 > v:
            v = v2
            best_action = action
        if v >= beta:
            return v, best_action  # Beta cutoff
        alpha = max(alpha, v)
    return v, best_action

def ab_min_value(state, alpha, beta):
    if state.is_terminal():
        return state.utility(), None
    
    v = float('inf')
    best_action = None
    
    for action in state.get_actions():
        v2, _ = ab_max_value(state.result(action), alpha, beta)
        if v2 < v:
            v = v2
            best_action = action
        if v <= alpha:
            return v, best_action  # Alpha cutoff
        beta = min(beta, v)
    return v, best_action
