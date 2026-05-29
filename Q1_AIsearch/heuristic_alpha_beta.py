def heuristic_alpha_beta_search(state, max_depth, evaluation_fn):
    """
    Alpha-Beta search that cuts off at max_depth and uses an evaluation_fn.
    """
    player = state.to_move()
    
    if player == 1:
        value, best_action = hab_max_value(state, float('-inf'), float('inf'), 0, max_depth, evaluation_fn)
    else:
        value, best_action = hab_min_value(state, float('-inf'), float('inf'), 0, max_depth, evaluation_fn)
        
    return best_action

def hab_max_value(state, alpha, beta, depth, max_depth, eval_fn):
    if state.is_terminal():
        return state.utility(), None
    if depth == max_depth:
        return eval_fn(state), None
    
    v = float('-inf')
    best_action = None
    
    for action in state.get_actions():
        v2, _ = hab_min_value(state.result(action), alpha, beta, depth + 1, max_depth, eval_fn)
        if v2 > v:
            v = v2
            best_action = action
        if v >= beta:
            return v, best_action
        alpha = max(alpha, v)
    return v, best_action

def hab_min_value(state, alpha, beta, depth, max_depth, eval_fn):
    if state.is_terminal():
        return state.utility(), None
    if depth == max_depth:
        return eval_fn(state), None
    
    v = float('inf')
    best_action = None
    
    for action in state.get_actions():
        v2, _ = hab_max_value(state.result(action), alpha, beta, depth + 1, max_depth, eval_fn)
        if v2 < v:
            v = v2
            best_action = action
        if v <= alpha:
            return v, best_action
        beta = min(beta, v)
    return v, best_action
