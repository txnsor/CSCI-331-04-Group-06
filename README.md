# 2048 AI Agent

## Abstract

This project implements a complete and AI driven framework for the 2048 game utilizing a fully functional game model with the decision making algorithms of minimax and alphabeta pruning. It displays the results with a simple graphical interface allowing you to test and experiment with the algorithms. The two search-based AI algorithms that were implemented are a minimax algorithm operating over an explicit game-state tree and an optimized alpha-beta pruning version with adaptive depth control based on the sparsity of the board. These two algorithms evaluate future plays and simulate the tile placements to select moves trying to maximize the long-term board value.

A Tkinter Gui visualizes the game using a faithful representation of the game with accurate colors and all, also allowing you to choose between both AI implementations and whether the algorithm should run step by step or automatically. The GUI also displays the last move the AI chose allowing the user to learn more about how they work.

Overall, this project provides a clean and efficient platform for testing the heuristic search algorithms on 2048. 

## Developers

- Cole Stowell (@costowell)
- Kevin Daccache (@ke3646)
- Marc Browning (@txnsor)
- Ian Kopke (@ikopke23)

## How to Run

1. Install [Python 3.13](https://www.python.org/downloads/release/python-3130/).
2. Setup a `venv` with the following commands

```sh
python -m venv .venv
source .venv/bin/activate
```

3. Install the dependencies

```sh
pip install -r requirements.txt
```

4. Run the project!

```sh
python main.py
```
