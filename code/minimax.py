from copy import deepcopy
import game as game_model

"""
The maximum depth the tree will generate to.
"""
MAX_DEPTH = 5 # TODO: change this to a reasonable value

"""
Wrapper for a graph of game states, used for minimax.
"""
class State_Graph:
    """
    Generate a graph of nodes keeping track of GAME STATE
    with maximum depth of MAX_DEPTH.
    """
    def __init__(self, game, move_number = 0):
        # TODO: do we need all of this info?
        self.root = Node(
            move_number % 2 == 0, 
            Game_Data(game, None, 0, None),
            [] # TODO: maybe replace with numpy array?
            )
        
        depth = 0
        nodes = [self.root]
        while nodes:
            current_node = nodes.pop()
            node_gen_depth = current_node.data.depth + 1
            if node_gen_depth > MAX_DEPTH: continue
            # for generating the states
            if (current_node.is_max):
                # moves are L, R, U, D
                for dir in game_model.DIRECTION:
                    # copy to maintain internal state after move
                    game_copy = deepcopy(current_node.data.game)
                    game_copy.move(dir)
                    # generate a node
                    new_child = Node(False, Game_Data(game_copy, dir, node_gen_depth, None), [])
                    # children get to have a score value.
                    if node_gen_depth == MAX_DEPTH: new_child.data.score = game_copy.score()
                    # prune games that lose (TODO: can we do this for minimax?)
                    current_node.children.append(new_child)
                    nodes.append(new_child)
                # moves are any free space
            else:
                # TODO: debug this
                for p in current_node.data.game.get_free_spaces():
                    game_copy = deepcopy(current_node.data.game)
                    # TODO: debug this as well
                    game_copy.grid[p] = 2
                    new_child = Node(True, Game_Data(game_copy, p, node_gen_depth, None), [])
                    if node_gen_depth == MAX_DEPTH: new_child.data.score = game_copy.score()
                    current_node.children.append(new_child)
                    nodes.append(new_child)

    """
    Display graph data
    """
    def print_graph(self):
        nodes = [self.root]
        while nodes:
            current = nodes.pop()
            current.print_node()
            print()
            for node in current.children:
                nodes.append(node)

# yet another helper class
class Game_Data:
    def __init__(self, game, last_move, depth, score):
        self.game = game
        self.last_move = last_move
        self.depth = depth
        self.score = score

    def __str__(self): return f"(score: {self.score}, depth: {self.depth}, last_move: {self.last_move})"
    def __repr__(self): return f"(score: {self.score}, depth: {self.depth}, last_move: {self.last_move})"
            
# helper class for the state graph
class Node:
    def __init__(self, is_max = None, data = None, children = None):
        self.is_max = is_max
        self.data = data
        self.children = children
    
    def print_node(self): print(f"data: {self.data}, is_max: {self.is_max}, children: {self.children}")

    def __str__(self): return f"data: {self.data}, is_max: {self.is_max}"
    def __repr__(self): return f"data: {self.data}, is_max: {self.is_max}"

"""
Compute minimax of a state graph.
"""
def minimax(state_graph):
    return _minimax_recursive(state_graph.root)

"""
Recursive functionality of minimax.
"""
def _minimax_recursive(node):
    # base case, child node
    if not node.children: 
        if node.data.score is None: node.data.score = node.data.game.score()
        return node.data.score, []
    
    results = []
    for child in node.children:
        score, path = _minimax_recursive(child)
        results.append((score, [child.data.last_move] + path))

    if node.is_max:
        res = max(results, key = lambda x : x[0])
    else:
        res = min(results, key = lambda x : x[0])

    node.data.score = res[0]
    return res[0], res[1]
def main():
    # make a random game with three initial filled spaces
    game = game_model.Game()
    game.random_place_tile()
    game.random_place_tile()
    game.random_place_tile(4)
    graph = State_Graph(game, 0)
    print(minimax(graph))

if __name__ == "__main__": main()