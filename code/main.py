# Main Class used for testing minimax vs alphabeta
# Implemented by Kevin Daccache

from game import Game
from minimax import State_Graph, minimax
from alpha_beta import alpha_beta_user, get_adaptive_depth
from gui import TilesGUI
import tkinter as tk


class MainController:

    def __init__(self):
        self.root = tk.Tk()

        self.game = Game()
        self.game.random_place_tile()
        self.game.random_place_tile()

        self.autoplay_running = False

        self.gui = TilesGUI(self.root)
        self.gui.model = self

        self.update_gui()

        self.algo = tk.StringVar(value="AlphaBeta")
        self.make_control_panel()

        self.root.mainloop()

    def make_control_panel(self):
        panel = tk.Frame(self.root)
        panel.pack(pady=5)

        tk.Label(panel, text="AI:").pack(side="left")
        tk.Label(panel, text="Score: ").pack(side="left")

        tk.OptionMenu(panel, self.algo, "Minimax", "AlphaBeta").pack(side="left", padx=10)
        tk.Label(panel, text="Delay (ms):").pack(side="left", padx=10)

        self.delay_var = tk.StringVar(value="50")
        tk.Entry(panel, textvariable=self.delay_var, width=6).pack(side="left")

        tk.Button(panel, text="Step AI Move", command=self.run_ai_once).pack(side="left", padx=10)
        tk.Button(panel, text="Autoplay", command=self.toggle_autoplay).pack(side="left", padx=10)
        tk.Button(panel, text="New Game", command=self.new_game).pack(side="left")

    def toggle_autoplay(self):
        self.autoplay_running = not self.autoplay_running
        if self.autoplay_running:
            self.autoplay_loop()

    def autoplay_loop(self):
        if not self.autoplay_running:
            return

        if self.game.is_over():
            self.gui.update(self, "GAME OVER")
            self.autoplay_running = False
            return

        self.run_ai_once()

        delay = int(self.delay_var.get())
        self.root.after(delay, self.autoplay_loop)

    def update_gui(self, message="AI Ready"):
        self.grid = self.game.grid.copy()
        self.gui.update(self, message)

    def new_game(self):
        self.autoplay_running = False
        self.game = Game()
        self.game.random_place_tile()
        self.game.random_place_tile()
        self.update_gui("New Game")

    def run_ai_once(self):
        algo = self.algo.get()

        if algo == "Minimax":
            graph = State_Graph(self.game.copy())
            path = minimax(graph)
            if not path or path[0] is None:
                return
            move = path[1][0]

        else:
            depth = get_adaptive_depth(self.game)
            score, move = alpha_beta_user(
                self.game.copy(), depth, True, float("-inf"), float("inf")
            )
            if move is None:
                return

        # Apply move
        self.game.move(move)
        self.game.random_place_tile()
        self.update_gui(f"AI Move: {move}")

        if self.game.is_over():
            self.gui.update(self, "GAME OVER")

if __name__ == "__main__":
    MainController()