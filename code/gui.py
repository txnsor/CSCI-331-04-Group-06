# 2048 GUI
# Implemented by Kevin Daccache

import tkinter as tk

TILE_COLORS = {
    0:  ("#cdc1b4", "#776e65"),
    2:  ("#eee4da", "#776e65"),
    4:  ("#ede0c8", "#776e65"),
    8:  ("#f2b179", "white"),
    16: ("#f59563", "white"),
    32: ("#f67c5f", "white"),
    64: ("#f65e3b", "white"),
    128: ("#edcf72", "#776e65"),
    256: ("#edcc61", "#776e65"),
    512: ("#edc850", "#776e65"),
    1024: ("#edc53f", "white"),
    2048: ("#edc22e", "white"),
}


class TilesGUI:
    """Tkinter grid renderer + status panel for 2048."""

    def __init__(self, root):
        self.root = root
        self.root.title("2048 AI")

        bg = "#bbada0"

        # Main tile grid
        self.frame = tk.Frame(self.root, bg=bg)
        self.frame.pack(padx=10, pady=10)

        self.tiles = []
        for r in range(4):
            row = []
            for c in range(4):
                tile = tk.Label(
                    self.frame,
                    text="",
                    width=4,
                    height=2,
                    font=("Helvetica", 32, "bold"),
                    bg="#cdc1b4",
                    fg="#776e65",
                    relief="ridge",
                    borderwidth=5,
                )
                tile.grid(row=r, column=c, padx=5, pady=5)
                row.append(tile)
            self.tiles.append(row)

        # Message label
        self.message_label = tk.Label(
            self.root,
            text="",
            font=("Helvetica", 16),
            fg="#776e65",
            bg=bg,
            pady=10,
        )
        self.message_label.pack()

        self.score_label = tk.Label(
            self.root,
            text="Score: ",
            font=("Helvetica", 16),
            fg="#776e65",
            bg=bg,
            pady=10,
        )
        self.score_label.pack()

        self.model = None

#updates board, scores and moves. 
    def update(self, model, message=""):
        grid = model.grid
        count = 0
        for r in range(4):
            for c in range(4):
                val = int(grid[r][c])
                tile = self.tiles[r][c]

                bg_color, fg_color = TILE_COLORS.get(val, ("#3c3a32", "white"))
                self.tiles[r][c]
                count += val
                tile.config(
                    text="" if val == 0 else str(val),
                    bg=bg_color,
                    fg=fg_color,
                )
        self.score_label.config(text="Score: "+str(count))
        self.message_label.config(text=message)
        self.root.update_idletasks()
