import math
import random

class MCTSNode:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.children = []
        self.visits = 0
        self.wins = 0
        self.untried_actions = state.get_actions()

    def uct_select_child(self, exploration_constant=1.414):
        # Upper Confidence Bound applied to Trees (UCT) formula
        return max(self.children, key=lambda c: (c.wins / c.visits) + exploration_constant * math.sqrt(math.log(self.visits) / c.visits))

    def add_child(self, action, state):
        child = MCTSNode(state, parent=self, move=action)
        self.untried_actions.remove(action)
        self.children.append(child)
        return child

    def update(self, result):
        self.visits += 1
        self.wins += result

def mcts_search(root_state, iterations=1000):
    """
    Executes Monte Carlo Tree Search for a given number of iterations.
    """
    root = MCTSNode(state=root_state)

    for _ in range(iterations):
        node = root
        state = root_state

        # 1. Selection
        while not node.untried_actions and node.children:
            node = node.uct_select_child()
            state = state.result(node.move)

        # 2. Expansion
        if node.untried_actions:
            action = random.choice(node.untried_actions)
            state = state.result(action)
            node = node.add_child(action, state)

        # 3. Simulation (Rollout)
        while not state.is_terminal():
            action = random.choice(state.get_actions())
            state = state.result(action)

        # 4. Backpropagation
        # Result from the perspective of the player who just moved
        result = state.utility() 
        while node is not None:
            node.update(result)
            node = node.parent

    # Return the move that got the most visits
    return max(root.children, key=lambda c: c.visits).move
