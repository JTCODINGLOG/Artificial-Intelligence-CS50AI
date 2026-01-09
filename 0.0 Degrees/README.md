# 0 Search - 0.0 Degrees

This project implements a Breadth-First Search (BFS) algorithm to determine the "degrees of separation" between two actors by traversing a social network of movie cast data.

### 🧠 Logic Implementation
* **Algorithm:** Breadth-First Search (BFS).
* **Objective:** To identify the shortest path between a source actor and a target actor using nodes (actors) and edges (movies).
* **Implementation:** The AI utilizes a queue-based frontier to explore the network, ensuring the first path found is the shortest possible connection.

### 🔍 Impartial Review
* **The Strength:** BFS is objectively optimal for unweighted graphs where the shortest path is required.
* **Optimization:** Large CSV datasets provided by CS50 are excluded from this repository via `.gitignore` to maintain a lightweight, code-focused portfolio.