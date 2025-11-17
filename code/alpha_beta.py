from game import Game, DIRECTION

# min
def alpha_beta_rng(game: Game, depth: int, prune: bool, alpha: float, beta: float) -> tuple[float, tuple[int, int] | None]:
    if depth == 0 or game.is_over():
        return game.score(), None

    best = float('inf')
    pos = None
    for p in game.get_free_spaces():
        g = game.copy()
        g.grid[p] = 2

        v, _ = alpha_beta_user(g, depth-1, prune, alpha, beta)
        if v < best:
            best = v
            pos = p
            beta = min(beta, v)

        if beta <= alpha and prune:
            break
    return best, pos

# max
def alpha_beta_user(game: Game, depth: int, prune: bool, alpha: float, beta: float) -> tuple[float, DIRECTION | None]:
    if depth == 0 or game.is_over():
        return game.score(), None

    best = float('-inf')
    dir = None
    for d in [DIRECTION.DOWN, DIRECTION.UP, DIRECTION.LEFT, DIRECTION.RIGHT]:
        g = game.copy()
        if not g.move(d):
            continue
        v, _ = alpha_beta_rng(g, depth-1, prune, alpha, beta)
        if v > best:
            best = v
            dir = d
            alpha = max(alpha, v)
        if beta <= alpha and prune:
            break

    return best, dir

def main():
    game = Game()

    while True:
        game.random_place_tile()
        _, dir = alpha_beta_user(game, 7, True, float('-inf'), float('inf'))

        if dir == None:
            break
        game.move(dir)
        print(game.grid)
        print()

if __name__ == "__main__":
    main()
