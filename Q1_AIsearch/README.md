# Adversarial and Tree Search Algorithms

This repository contains clean, modular implementations of four foundational search algorithms used in Artificial Intelligence for decision-making and game theory.

---

## 1. Implemented Algorithms

### 1.1 Minimax Search (`src/minimax.py`)
An exhaustive adversarial search algorithm that determines the optimal move for a player assuming that the opponent is also playing optimally. It traverses the complete game tree depth-first.

### 1.2 Alpha-Beta Pruning Search (`src/alpha_beta.py`)
An optimized version of the Minimax algorithm that decreases the number of nodes evaluated in the search tree. It stops evaluating a move when at least one possibility has been found that proves the move to be worse than a previously examined option.

### 1.3 Heuristic Alpha-Beta Search (`src/heuristic_alpha_beta.py`)
In complex games where the state space is too massive to search to terminal nodes, this variant enforces a fixed `max_depth`. Upon reaching the depth limit, it evaluates non-terminal game states using a custom evaluation/heuristic function (`evaluation_fn`).

### 1.4 Monte-Carlo Tree Search (MCTS) (`src/mcts.py`)
A stochastic search algorithm that builds a search tree asymmetric to the most promising moves. It doesn't require a heuristic function and instead relies on random game simulations (rollouts). It operates over four iterative phases:
1. **Selection:** Traverse down the tree using the Upper Confidence Bound for Trees (UCT) formula.
2. **Expansion:** Create a new child node when a leaf node is reached.
3. **Simulation:** Run a random simulation (rollout) to a terminal state.
4. **Backpropagation:** Update the visit and win statistics up the path to the root.

---

## 2. Repository Structure

```text
ai-search-algorithms/
│
├── src/
│   ├── __init__.py
│   ├── minimax.py
│   ├── alpha_beta.py
│   ├── heuristic_alpha_beta.py
│   └── mcts.py
│
├── tests/
│   ├── __init__.py
│   └── test_algorithms.py
│
└── README.md

