# 0 Search - 0.1 Tictactoe

An implementation of an unbeatable AI for Tic-Tac-Toe utilizing the Minimax decision algorithm.

### 🧠 Logic Implementation
* **Minimax Algorithm:** The AI evaluates all possible future states to select moves that maximize its own score while assuming the opponent plays optimally.
* **State Management:** Defined core functions to handle the board state, legal actions, player transitions, and terminal conditions.

### 🔍 Impartial Review
* **The Strength:** The logic is mathematically sound; the AI cannot lose.
* **The Improvement:** For larger state spaces, implementing **Alpha-Beta Pruning** is the objective industry standard to optimize performance by reducing the number of nodes evaluated.