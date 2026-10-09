# Pac-Man Search Assignment — Run Guide

**Verified by:** IT24103546 Asma M.A.F
**Date:** 2026-10-09
**Platform:** Windows 11, PowerShell
**Python:** 3.12.13 (conda not available → used Python `venv`)

## Quick Start (TL;DR)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install numpy matplotlib
python pacman.py                          # verify the game opens
python autograder.py -q q1                # run one question
```

---

## 1. Prerequisites

- Python 3.9–3.11 (verified working on 3.12.13)
- `pip`
- Git

## 2. Environment Setup (verified)

Note: `conda` was not available on this machine, so a Python `venv` was used instead.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install numpy matplotlib
```

---

## 3. Running the Game

```powershell
python pacman.py
```

Confirmed the game engine loads and runs. The default agent plays randomly and usually loses — this is expected and not an error.

Example observed output:

```
Pacman died! Score: -633
Average Score: -633.0
Scores:        -633.0
Win Rate:      0/1 (0.00)
Record:        Loss
```

To play interactively with the keyboard:

```powershell
python pacman.py -p KeyboardAgent
```

Use the arrow keys to move. Press `Ctrl + C` in the terminal to quit.


---

## 4. Running the Autograder

Single question:

```powershell
python autograder.py -q q1
```

All questions:

```powershell
python autograder.py
```

Per-question commands:

| Question | Topic | Command |
|----------|-------|---------|
| Q1 | DFS | `python autograder.py -q q1` |
| Q2 | BFS | `python autograder.py -q q2` |
| Q3 | UCS | `python autograder.py -q q3` |
| Q4 | A*  | `python autograder.py -q q4` |
| Q5 | Corners problem | `python autograder.py -q q5` |
| Q6 | Corners heuristic | `python autograder.py -q q6` |
| Q7 | Food heuristic | `python autograder.py -q q7` |


---

## 5. Verified Autograder Results (2026-10-09)

All questions were executed and produced the following results:

| Q | Topic | Result | Key metric |
|---|-------|--------|------------|
| Q1 | DFS | 3/3 PASS | mediumMaze: path 130, 146 nodes expanded |
| Q2 | BFS | 3/3 PASS | mediumMaze: path 68, 269 nodes expanded |
| Q3 | UCS | 3/3 PASS | All 10 tests pass (including `ucs_5_goalAtDequeue`) |
| Q4 | A* | 3/3 PASS | mediumMaze with Manhattan: 221 nodes expanded |
| Q5 | Corners problem | 3/3 PASS | tinyCorner: path length 28 |
| Q6 | Corners heuristic | 3/3 PASS | mediumCorners: 1136 nodes (top band ≤12000 → 8/8) |
| Q7 | Food heuristic | 5/4 PASS | trickySearch: 4137 nodes (top band ≤9000 → 8/8) |

> Q7 reports 5/4 due to bonus credit in the autograder; the node count of 4137 is comfortably within the highest scoring band.

---

## 6. Project File Roles

| File | Role |
|------|------|
| `search.py` | DFS, BFS, UCS, A* implementations (Q1–Q4) |
| `searchAgents.py` | CornersProblem and heuristics (Q5–Q7) |
| `util.py` | Stack, Queue, PriorityQueue (read-only) |
| `pacman.py` | Game engine / runner (reference) |
| `autograder.py` | Automated grading script |
| `grading.py` | Autograder helper (harmless SyntaxWarning on Python 3.12) |


---

## 7. Troubleshooting

- **`conda: not recognized`** → conda not installed. Used Python's built-in `venv` module; all steps work.
- **`.\.venv\Scripts\Activate.ps1` blocked** → run `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` once, then retry.
- **`SyntaxWarning: invalid escape sequence '\ '` at `grading.py:111`** → harmless warning from a course-provided file under Python 3.12. Does not affect results; ignore.
- **Default `python pacman.py` shows a loss** → expected; default agent plays randomly. Use `-p KeyboardAgent` for interactive play.
- **`.venv` getting committed** → ensure `.venv/` is in `.gitignore` before staging.


---

## 8. Common Pitfalls (observed while verifying)

- **Forgetting to activate the venv** before running `pip install` → packages install globally. Always run `.\.venv\Scripts\Activate.ps1` first.
- **Running `python pacman.py` outside the project folder** → `ModuleNotFoundError` for local modules like `game` or `util`. Always run commands from `assignment_IA/`.
- **Committing `.venv/` to Git** → produces 2600+ noise files. Ensure `.venv/` is in `.gitignore` before `git add`.
- **Renaming functions/classes in `search.py` or `searchAgents.py`** → autograder imports them by name; any rename = 0 marks for that question.
- **Using Python built-ins instead of `util.Stack/Queue/PriorityQueue`** → the autograder may reject the implementation.


---

## 9. Verification Statement

All commands above were executed on 2026-10-09 on Windows 11 with Python 3.12.13 in a `venv` environment. The autograder results in Section 5 are the actual observed outputs.

— IT24103546 (Member 3)