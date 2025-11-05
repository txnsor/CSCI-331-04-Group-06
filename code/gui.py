# gui.py
# Implemented by Kevin Daccache

import tkinter as tk
from tkinter import font

# Create main window
root = tk.Tk()
root.title("2048")



def initialize_gui():
    # Set background color
    root.configure(bg="#bbada0")
    # Add score, Highscore, and Game State
    stats_frame = tk.Frame(root, bg="#bbada0", bd=10)
    stats_frame.grid()
    set_statistics(stats_frame)
    # Create a frame for the game grid
    grid_frame = tk.Frame(root, bg="#bbada0", bd=10)
    grid_frame.grid(padx=10, pady=5)
    # Create empty tiles (just placeholders)
    starting_grid = True
    set_grid_values(grid_frame, starting_grid)
    # Add a Reset button
    reset_button = tk.Button(
        root, text="Reset", bg="#8f7a66", fg="white"
    )
    reset_button.grid(pady=5)


def set_grid_values(grid_frame, starting_grid):
    tiles = []
    for i in range(4):
        row = []
        for j in range(4):
            if(starting_grid):
                tile = tk.Label(
                    grid_frame, text="", width=8, height=4, bg="#cdc1b4", fg="#776e65", borderwidth=5, relief="groove",
                )
            tile.grid(row=i, column=j, padx=5, pady=5)
            row.append(tile)
        tiles.append(row)


def set_statistics(stats_frame):
    score = 10
    status = "Currently Running"
    # Create Score Label
    score_label = tk.Label(
        stats_frame, text=("Score: \n" + str(score)), bg="#bbada0", font=("Times New Roman", 16)
    )
    score_label.grid(row=0, column=0, padx=5)
    # Create High Score Label
    high_score_label = tk.Label(
        stats_frame, text=("High Score: \n" + str(score)), bg="#bbada0", font=("Times New Roman", 16)
    )
    high_score_label.grid(row=0, column=1, padx=5)
    # Create game Status Label
    game_status_label = tk.Label(
        stats_frame, text=("Game Status: \n" + status), bg="#bbada0", font=("Times New Roman", 16)
    )
    game_status_label.grid(row=0, column=2, padx=5)


#testing if Gui Functional
if __name__ == '__main__':
    initialize_gui()
    root.mainloop()
