# Comprehensive Project Guide: Pac-Man Autonomous Search & AI Problem Solving

> **Module / Course:** SE3062 — Intelligent Systems / Artificial Intelligence  
> **Environment:** UC Berkeley AI Pac-Man Search Framework (Python 3)  
> **Evaluation Status:** 26 / 25 Points (Full Score + Bonus)

---

## Table of Contents
1. [Executive Summary (For Complete Beginners)](#1-executive-summary-for-complete-beginners)
2. [What is State Space Search? (The Core AI Concept)](#2-what-is-state-space-search-the-core-ai-concept)
3. [Project Directory & Architecture Breakdown](#3-project-directory--architecture-breakdown)
4. [How the System Works End-to-End (Execution Lifecycle)](#4-how-the-system-works-end-to-end-execution-lifecycle)
5. [In-Depth Algorithm Analysis (Questions 1 to 4)](#5-in-depth-algorithm-analysis-questions-1-to-4)
   - [Q1: Depth-First Search (DFS)](#q1-depth-first-search-dfs)
   - [Q2: Breadth-First Search (BFS)](#q2-breadth-first-search-bfs)
   - [Q3: Uniform-Cost Search (UCS)](#q3-uniform-cost-search-ucs)
   - [Q4: A* Search Algorithm](#q4-a-search-algorithm)
   - [Algorithmic Comparison Matrix](#algorithmic-comparison-matrix)
6. [Search Problems & Heuristics Deep-Dive (Questions 5 to 8)](#6-search-problems--heuristics-deep-dive-questions-5-to-8)
   - [Q5: The Corners Problem (`CornersProblem`)](#q5-the-corners-problem-cornersproblem)
   - [Q6: Corners Heuristic (`cornersHeuristic`)](#q6-corners-heuristic-cornersheuristic)
   - [Q7: Full Food Search & Maze Distance Heuristic (`foodHeuristic`)](#q7-full-food-search--maze-distance-heuristic-foodheuristic)
   - [Q8: Greedy Suboptimal Search (`ClosestDotSearchAgent`)](#q8-greedy-suboptimal-search-closestdotsearchagent)
7. [Mathematical Foundations: Admissibility and Consistency](#7-mathematical-foundations-admissibility-and-consistency)
8. [Autograder & Verification Results](#8-autograder--verification-results)
9. [How to Run and Experiment (Quick Command Reference)](#9-how-to-run-and-experiment-quick-command-reference)
10. [Frequently Asked Questions (FAQ)](#10-frequently-asked-questions-faq)

---

## 1. Executive Summary (For Complete Beginners)

### What is this project about?
When a human plays the classic arcade game **Pac-Man**, the player looks at the screen, notices the walls, spots the food dots, and decides whether to press the Up, Down, Left, or Right arrow keys.

In this project, **no human is touching the keyboard**. Instead, **Pac-Man is controlled by Artificial Intelligence (AI)**. 

Before taking even a single step, the Pac-Man agent:
1. Examines the map layout (the starting position, walls, and food locations).
2. Uses **graph search algorithms** to simulate possible future moves inside its virtual memory.
3. Finds the optimal or most efficient sequence of moves (e.g., `['North', 'East', 'East', 'South']`).
4. Executes those moves on screen step-by-step until it solves the maze.

### The Big Picture Goal
The ultimate goal of this project is to teach an autonomous agent how to navigate complex mazes to accomplish specific missions:
- Reach a fixed coordinate $(x, y)$.
- Visit all four corners of the maze in the fewest possible moves.
- Eat every single food dot scattered across the maze.

---

## 2. What is State Space Search? (The Core AI Concept)

In Classical Artificial Intelligence, navigating a maze is formulated as a **Search Problem**. 

A formal search problem consists of five key components:

```
+--------------------------------------------------------------------------+
|                         FORMAL SEARCH PROBLEM                            |
+--------------------------------------------------------------------------+
| 1. State Space      : All valid situations the agent can be in.          |
| 2. Start State      : Where Pac-Man begins.                              |
| 3. Actions / Moves  : Legal movements (North, South, East, West).         |
| 4. Transition Model : Result of applying an action to the current state. |
| 5. Goal Test        : A condition that checks if the mission is complete.|
| 6. Path Cost        : The cumulative cost/steps taken to reach the goal. |
+--------------------------------------------------------------------------+
```

### Tree Search vs. Graph Search: Why Graph Search is Essential
- In **Tree Search**, if you step back and forth between two tiles (e.g., $(1, 1) \rightarrow (1, 2) \rightarrow (1, 1)$), the search engine explores the same state repeatedly, causing an **infinite loop**.
- In **Graph Search** (which is implemented in this repository), we maintain an **Explored / Visited Set**. Once a coordinate or state is processed, it is never re-opened. This guarantees termination and prevents infinite cycles.

```
       [Start State: (1, 1)]
              |
              v
     +-----------------+
     |  Frontier List  |  <--- States waiting to be investigated
     +-----------------+
              |
      (Pops next state)
              |
              v
      Is Goal State? ---- YES ----> [Return Sequence of Actions!]
              |
              NO
              |
              v
    Already in Visited Set?
      ├── YES ──> Discard and continue
      └── NO  ──> Mark Visited, generate child states, push to Frontier
```

---

## 3. Project Directory & Architecture Breakdown

The project follows a clean, modular object-oriented architecture designed by UC Berkeley.

```
assignment_IA/
│
├── autograder.py         # Automated evaluation engine testing Q1 to Q8
├── grading.py            # Grading logic and point calculator
├── testParser.py         # Parses test case definitions
├── testClasses.py        # Generic unit testing classes
├── searchTestClasses.py  # Specific search evaluation test runners
│
├── pacman.py             # Main entry point and game engine loop
├── game.py               # Core mechanics (Grid, Agent, Actions, Directions)
├── layout.py             # Reads maze text files from layouts/
│
├── search.py             # *** CORE FILE 1 *** Generic search algorithms (DFS, BFS, UCS, A*)
├── searchAgents.py       # *** CORE FILE 2 *** Search problems, heuristics & agent adapters
├── util.py               # Data structures (Stack, Queue, PriorityQueue)
│
├── ghostAgents.py        # Ghost behaviors (inactive in pure search problems)
├── keyboardAgents.py     # Manual keyboard control for humans
├── graphicsDisplay.py    # Graphical UI window (Tkinter based)
├── textDisplay.py        # ASCII terminal graphics fallback
│
├── docs/                 # Assignment documentation
│   ├── ALGORITHMS.md     # Brief summary of algorithms
│   ├── RUN_GUIDE.md      # Installation, execution, and troubleshooting guide
│   ├── TEST_RESULTS.md   # Test outputs and verification log
│   └── PROJECT_EXPLANATION.md # THIS COMPREHENSIVE GUIDE
│
├── layouts/              # Mazes (.lay files) such as tinyMaze, mediumMaze, bigMaze
└── test_cases/           # Hidden and public test specifications for autograder
```

### Key Source Files Modified for the Assignment

| File | Purpose | What was written / implemented |
| :--- | :--- | :--- |
| `search.py` | Universal Graph Search Algorithms | `depthFirstSearch`, `breadthFirstSearch`, `uniformCostSearch`, `aStarSearch` |
| `searchAgents.py` | Pac-Man Specific Problems & Heuristics | `CornersProblem`, `cornersHeuristic`, `foodHeuristic`, `ClosestDotSearchAgent`, `AnyFoodSearchProblem` |

---

## 4. How the System Works End-to-End (Execution Lifecycle)

When you run a command like:
```powershell
python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,prob=PositionSearchProblem,heuristic=manhattanHeuristic
```

Here is the exact step-by-step lifecycle:

```
[1. User Command]
       │
       ▼
[2. pacman.py] reads flags:
       │  • Layout: mediumMaze.lay
       │  • Agent: SearchAgent
       │  • Algorithm: astar
       │  • Problem: PositionSearchProblem
       │  • Heuristic: manhattanHeuristic
       │
       ▼
[3. searchAgents.py] creates Problem & Agent:
       │  • Initializes PositionSearchProblem with start (x0, y0) and goal (xg, yg)
       │  • Injects heuristic function into searchFunction
       │
       ▼
[4. search.py: aStarSearch(problem, heuristic)] executes:
       │  • Explores states using Priority Queue ordered by f(n) = g(n) + h(n)
       │  • Reaches goal state
       │  • Reconstructs and returns list of actions: ['West', 'West', 'North', ...]
       │
       ▼
[5. pacman.py Game Loop]:
       │  • Pac-Man steps through each action in the returned list
       │  • graphicsDisplay updates window animation
       │  • Victory screen is rendered!
```

---

## 5. In-Depth Algorithm Analysis (Questions 1 to 4)

All four search algorithms implemented in `search.py` share a general graph search template, but **differ strictly in the data structure used for the Frontier (open list)**.

---

### Q1: Depth-First Search (DFS)
* **Data Structure:** `util.Stack` (LIFO — Last In, First Out)
* **Exploration Strategy:** Plunges as deep as possible along each branch before backtracking.

```
         (A)
        /   \
      (B)   (C)
      /
    (D)  <-- Explored first before ever looking at (C)
```

* **Behavior in Mazes:** Pac-Man travels deep into corridors, often reaching the goal via an unnecessarily long, winding path.
* **Optimality:** **Not optimal**. It finds *a* path, not the shortest path.
* **Completeness:** Complete on finite graph spaces (because cycles are avoided via `visited`).

---

### Q2: Breadth-First Search (BFS)
* **Data Structure:** `util.Queue` (FIFO — First In, First Out)
* **Exploration Strategy:** Explores states level by level (all states at distance 1, then distance 2, then distance 3).

```
         (A)           Level 0
        /   \
      (B)   (C)        Level 1 (Both explored before Level 2)
      /       \
    (D)       (E)      Level 2
```

* **Behavior in Mazes:** Spreads outward like water filling a maze.
* **Optimality:** **Guaranteed optimal** when all step costs are equal (cost = 1 per move). Pac-Man will always find the shortest path in terms of number of steps.
* **Memory Footprint:** High memory consumption because it stores all frontier nodes at the current depth level.

---

### Q3: Uniform-Cost Search (UCS)
* **Data Structure:** `util.PriorityQueue`
* **Priority Metric:** Cumulative path cost $g(n)$ from the start node:
  $$\text{Priority} = g(n)$$
* **Exploration Strategy:** Always expands the node with the absolute lowest accumulated cost.
* **Behavior in Mazes:** 
  - If all step costs are equal (1), UCS behaves identically to BFS.
  - If some areas are expensive (e.g., muddy terrain or custom cost functions like $2^x$ in `StayWestSearchAgent`), UCS carefully navigates around high-cost tiles to minimize total path expense.
* **Optimality:** **Guaranteed optimal** for any non-negative step costs.

---

### Q4: A* Search Algorithm
* **Data Structure:** `util.PriorityQueue`
* **Priority Metric:** Evaluation function $f(n)$:
  $$f(n) = g(n) + h(n)$$
  - $g(n)$: Exact cost spent to travel from the start node to node $n$.
  - $h(n)$: Heuristic estimate of the remaining cost from node $n$ to the goal.

```
       Start ──[g(n): known cost]──> Node n ──[h(n): estimated cost]──> Goal
       └───────────────────────────── f(n) ────────────────────────────┘
```

* **Why A* is Superior:** 
  - Pure UCS explores blindly in all directions because it only knows $g(n)$.
  - A* uses $h(n)$ as a compass pointing toward the goal, eliminating exploration of corridors heading in the opposite direction.
* **Optimality:** Optimal provided that the heuristic $h(n)$ is **admissible** (never overestimates) and **consistent** (satisfies triangle inequality).

---

### Algorithmic Comparison Matrix

| Algorithm | Frontier Data Structure | Node Selection Criterion | Complete? | Optimal? | Typical Pac-Man Nodes Expanded (mediumMaze) |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **DFS** | Stack (LIFO) | Deepest node first | Yes (finite) | No | 146 (Long path, length 130) |
| **BFS** | Queue (FIFO) | Shallowest node first | Yes | Yes (unit cost) | 269 (Shortest path, length 68) |
| **UCS** | Priority Queue | Lowest $g(n)$ | Yes | Yes | 269 (Shortest path, length 68) |
| **A\*** (Manhattan) | Priority Queue | Lowest $f(n) = g(n) + h(n)$ | Yes | Yes | **221** (Shortest path, length 68) |

*Notice:* A* expands **significantly fewer nodes (221 vs 269)** than BFS/UCS while finding the exact same shortest path (length 68).

---

## 6. Search Problems & Heuristics Deep-Dive (Questions 5 to 8)

While Questions 1–4 deal with *how* to search, Questions 5–8 deal with *what* to search.

---

### Q5: The Corners Problem (`CornersProblem`)

#### The Challenge
Pac-Man must touch all four corners of the maze:
- $(1, 1)$ — Bottom-Left
- $(1, \text{top})$ — Top-Left
- $(\text{right}, 1)$ — Bottom-Right
- $(\text{right}, \text{top})$ — Top-Right

#### The Crucial Insight: State Representation
In a basic maze search, the state is simply Pac-Man's coordinate: `(x, y)`.

**Why does `(x, y)` fail for the Corners Problem?**
If Pac-Man reaches coordinate $(1, 1)$, is that a goal? It depends on whether he has already visited the other three corners! If state is only `(x, y)`, the graph search will visit $(1, 1)$ once, mark it visited, and refuse to ever return there even if needed to reach another corner.

#### The Solution: Augmented State
In `CornersProblem`, a state is formulated as a tuple:
$$\text{State} = \big((x, y), \text{visitedCorners}\big)$$
- Example: `((1, 5), ((1, 1), (1, 10)))`
- Two states at the same $(x, y)$ coordinate are treated as **different states** if the set of visited corners differs.
- **Goal Test:** `len(visitedCorners) == 4`

---

### Q6: Corners Heuristic (`cornersHeuristic`)

To make A* solve the Corners Problem efficiently without exploring thousands of useless states, we must design an admissible heuristic.

#### Logic Implemented:
1. Identify all remaining unvisited corners from the current state.
2. If all corners are visited, return `0`.
3. Calculate the Manhattan distance from Pac-Man's current position to each remaining unvisited corner:
   $$\text{Manhattan}((x_1, y_1), (x_2, y_2)) = |x_1 - x_2| + |y_1 - y_2|$$
4. Return the **maximum** of those distances:
   $$h(\text{state}) = \max_{c \in \text{remainingCorners}} \text{Manhattan}(\text{position}, c)$$

#### Why is this Admissible?
To reach all corners, Pac-Man must at least reach the single corner that is farthest away. Since Pac-Man cannot move through walls and can only move orthogonally, the true maze distance is always $\ge$ the Manhattan distance. Therefore:
$$h(n) \le h^*(n)$$
It never overestimates the true remaining cost, guaranteeing an optimal solution.

---

### Q7: Full Food Search & Maze Distance Heuristic (`foodHeuristic`)

#### The Challenge
Pac-Man must eat **every single food dot** in the maze. 
- State: `(pacmanPosition, foodGrid)`
- If a maze has 30 food dots, the number of possible food states is $2^{30} \approx 1,000,000,000$. This is a massive state space.

#### The Solution: True Maze Distance with Distance Caching
A simple Manhattan distance is too loose in complex mazes with walls, causing A* to expand over 15,000 nodes and fail the grading threshold.

In our implementation:
1. For every remaining food pellet, we compute the **true shortest maze distance** using BFS (accounting for walls).
2. We cache all pair distances in `problem.heuristicInfo['mazeDistances']` so that repeated calls take $O(1)$ dictionary lookups.
3. The heuristic returns the maximum maze distance to any remaining food dot:
   $$h(\text{state}) = \max_{f \in \text{foodList}} \text{mazeDistance}(\text{position}, f)$$

#### Autograder Performance:
- Threshold for full credit: $\le 7,000$ expanded nodes on `trickySearch`.
- **Our Result:** Expanded only **4,137 nodes**, earning **5/4 points (full credit + bonus point)**!

---

### Q8: Greedy Suboptimal Search (`ClosestDotSearchAgent`)

#### The Tradeoff: Optimal vs. Fast
Finding the globally optimal shortest path to collect 100 food dots is an NP-hard problem related to the Traveling Salesperson Problem (TSP). Computing the exact shortest path on large maps takes too long.

#### The Greedy Strategy:
Instead of planning a full global tour all at once:
1. Pac-Man runs a fast BFS (`AnyFoodSearchProblem`) to find the **single closest food dot**.
2. Pac-Man moves there and eats it.
3. Pac-Man repeats the process from his new position until all dots are eaten.

While the total path length may be slightly longer than the absolute mathematical minimum, it computes in a fraction of a second, demonstrating the practical AI engineering balance between **optimality** and **computational speed**.

---

## 7. Mathematical Foundations: Admissibility and Consistency

For heuristic search algorithms like A*, theoretical guarantees depend on two mathematical properties:

### 1. Admissibility
A heuristic $h(n)$ is **admissible** if it never overestimates the true cost to reach the nearest goal:
$$0 \le h(n) \le h^*(n) \quad \forall n$$
*(where $h^*(n)$ is the true optimal cost from $n$ to goal).*

**Theorem:** If tree-search A* uses an admissible heuristic, it is guaranteed to return an optimal solution.

### 2. Consistency (Monotonicity)
A heuristic $h(n)$ is **consistent** if, for every node $n$ and every successor $n'$ generated by action $a$ with step cost $c(n, a, n')$:
$$h(n) \le c(n, a, n') + h(n')$$

This represents the **Triangle Inequality**:
```
          n ────── c(n, a, n') ─────> n'
           \                         /
            \                       /
             h(n)               h(n')
              \                   /
               v                 v
                     [ Goal ]
```

**Theorem:** If graph-search A* uses a consistent heuristic, the values of $f(n)$ along any path are non-decreasing, and the first time any goal state is expanded, its path is guaranteed to be optimal.

---

## 8. Autograder & Verification Results

The test suite evaluates all 8 questions against unit tests and hidden mazes:

```
======================================================================
Question q1 (Depth First Search)                 : 3 / 3
Question q2 (Breadth First Search)               : 3 / 3
Question q3 (Uniform Cost Search)                : 3 / 3
Question q4 (A* Search)                          : 3 / 3
Question q5 (Corners Problem Formulation)        : 3 / 3
Question q6 (Corners Problem Heuristic)          : 3 / 3
Question q7 (Food Search Heuristic)              : 5 / 4  [BONUS EARNED]
Question q8 (Closest Dot Search Agent)           : 3 / 3
======================================================================
TOTAL SCORE                                      : 26 / 25
======================================================================
```

Every test passed without regressions or timeouts.

---

## 9. How to Run and Experiment (Quick Command Reference)

Ensure your Python environment is activated:
```powershell
# In Windows PowerShell:
.\.venv\Scripts\Activate.ps1
```

### 1. Run the Full Autograder
```powershell
python autograder.py
```

### 2. Run Individual Questions
```powershell
python autograder.py -q q1    # Test DFS
python autograder.py -q q2    # Test BFS
python autograder.py -q q3    # Test UCS
python autograder.py -q q4    # Test A*
python autograder.py -q q5    # Test Corners Problem
python autograder.py -q q6    # Test Corners Heuristic
python autograder.py -q q7    # Test Food Search Heuristic
python autograder.py -q q8    # Test Closest Dot Agent
```

### 3. Visually Watch Pac-Man Solve Mazes

**Watch DFS find a path:**
```powershell
python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
```

**Watch BFS find the optimal path:**
```powershell
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
```

**Watch UCS on custom cost maps:**
```powershell
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
```

**Watch A* with Manhattan Heuristic:**
```powershell
python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

**Watch Pac-Man solve the 4 Corners:**
```powershell
python pacman.py -l mediumCorners -p AStarCornersAgent
```

**Watch Pac-Man solve complex food mazes:**
```powershell
python pacman.py -l trickySearch -p AStarFoodSearchAgent
```

**Fast Greedy Dot Eater:**
```powershell
python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5
```

---

## 10. Frequently Asked Questions (FAQ)

### Q: Why does Pac-Man move slowly on screen?
**A:** Graphical rendering includes deliberate frame pauses for human observation. Use the `-t` (text only) or `--frameTime 0` option to run instantly at maximum computational speed:
```powershell
python pacman.py -l trickySearch -p AStarFoodSearchAgent --frameTime 0
```

### Q: What is the difference between `PositionSearchProblem` and `FoodSearchProblem`?
**A:** `PositionSearchProblem` only cares about reaching one fixed coordinate $(x, y)$. `FoodSearchProblem` requires Pac-Man to consume all food dots, meaning the state must keep track of the boolean grid of remaining food pellets.

### Q: Why didn't we use machine learning (neural networks) here?
**A:** Classic search algorithms guarantee **100% mathematical optimality** and are **fully explainable**. In deterministic, fully observable environments with known rules and maps, graph search is mathematically proven to find the absolute shortest path without requiring training data or GPU compute.

---
*Document prepared for academic review and project hand-over.*
