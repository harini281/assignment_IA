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