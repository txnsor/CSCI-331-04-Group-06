from game import Game, DIRECTION

# min
def alpha_beta_rng(game: Game, depth: int) -> tuple[float, tuple[int, int] | None]:
    if depth == 0 or game.is_over():
        return game.score(), None

    best = float('inf')
    total = 0
    pos = None
    for p in game.get_free_spaces():
        g = game.copy()
        g.grid[p] = 2

        v, _ = alpha_beta_user(g, depth-1)
        total += v
        if v < best:
            best = v
            pos = p
    return best, pos

# max
def alpha_beta_user(game: Game, depth: int) -> tuple[float, DIRECTION | None]:
    if depth == 0 or game.is_over():
        return game.score(), None

    best = float('-inf')
    dir = None
    for d in [DIRECTION.DOWN, DIRECTION.UP, DIRECTION.LEFT, DIRECTION.RIGHT]:
        g = game.copy()
        g.move(d)
        v, _ = alpha_beta_rng(g, depth-1)
        if v > best:
            best = v
            dir = d

    return best, dir

def main():
    game = Game()

    while True:
        game.random_place_tile()
        _, dir = alpha_beta_user(game, 7)
        if dir == None:
            break
        game.move(dir)
        print(game.grid)
        print()

if __name__ == "__main__":
    main()
