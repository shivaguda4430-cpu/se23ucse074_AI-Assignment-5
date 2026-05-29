import unittest
from src.minimax import minimax_search
from src.alpha_beta import alpha_beta_search
from src.heuristic_alpha_beta import heuristic_alpha_beta_search
from src.mcts import mcts_search

class MockGameState:
    """ A simple finite game state: Pile of 4 tokens. Take 1 or 2. """
    def __init__(self, tokens=4, player=1):
        self.tokens = tokens
        self._player = player # 1 = Max, -1 = Min

    def is_terminal(self):
        return self.tokens <= 0

    def utility(self):
        # If terminal, the player whose turn it WOULD be lost, meaning previous player won.
        return -1 * self._player

    def get_actions(self):
        if self.tokens >= 2: return [1, 2]
        if self.tokens == 1: return [1]
        return []

    def result(self, action):
        return MockGameState(self.tokens - action, -self._player)

    def to_move(self):
        return self._player

def dummy_evaluation(state):
    # Quick dummy heuristic for evaluation
    return 0 

class TestSearchAlgorithms(unittest.TestCase):
    def setUp(self):
        self.initial_state = MockGameState(tokens=4, player=1)

    def test_minimax(self):
        # Perfect play from 4 tokens means Max should take 1 token 
        # (leaving 3, forcing Min to a losing track)
        best_move = minimax_search(self.initial_state)
        self.assertEqual(best_move, 1)

    def test_alpha_beta(self):
        best_move = alpha_beta_search(self.initial_state)
        self.assertEqual(best_move, 1)

    def test_heuristic_alpha_beta(self):
        best_move = heuristic_alpha_beta_search(self.initial_state, max_depth=2, evaluation_fn=dummy_evaluation)
        self.assertIn(best_move, [1, 2]) # Shorter depth allows either

    def test_mcts(self):
        best_move = mcts_search(self.initial_state, iterations=500)
        self.assertEqual(best_move, 1)

if __name__ == '__main__':
    unittest.main()
