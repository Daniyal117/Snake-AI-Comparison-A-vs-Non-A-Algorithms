import heapq

def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

class Agent(object):
    class Node:
        def __init__(self, pos, g_cost, h_cost, par=None):
            self.pos = pos
            self.g_cost = g_cost
            self.h_cost = h_cost
            self.par = par

        def f_cost(self):
            return self.g_cost + self.h_cost

        def __lt__(self, other):
            return self.f_cost() < other.f_cost()

    def __init__(self):
        pass

    def SearchSolution(self, state):
        start_node = self.Node((state.snake.HeadPosition.X, state.snake.HeadPosition.Y), 0, 0)
        food_pos = (state.FoodPosition.X, state.FoodPosition.Y)

        visited = []
        closed = set()

        heapq.heappush(visited, (start_node.f_cost(), start_node))

        while visited:
            curr_node = heapq.heappop(visited)[1]

            if curr_node.pos == food_pos:
                return self.generate_path(curr_node)

            closed.add(curr_node.pos)

            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                neighbor = (curr_node.pos[0] + direction[0], curr_node.pos[1] + direction[1])
                if self.is_valid(neighbor, state, closed):
                    g_cost = curr_node.g_cost + 1
                    h_cost = heuristic(neighbor, food_pos)
                    child_node = self.Node(neighbor, g_cost, h_cost, curr_node)
                    heapq.heappush(visited, (child_node.f_cost(), child_node))

        return []

    def is_valid(self, pos, state, closed):
        return (self.inside_maze(pos, state) and
                self.passable(pos, state) and
                pos not in closed)

    def inside_maze(self, pos, state):
        return (0 <= pos[0] < state.maze.WIDTH and 0 <= pos[1] < state.maze.HEIGHT)

    def passable(self, pos, state):
        return state.maze.MAP[pos[1]][pos[0]] != -1

    def generate_path(self, node):
        path = []
        while node.par:
            prev_pos = node.par.pos
            curr_pos = node.pos
            move = self.determine_move(prev_pos, curr_pos)
            path.append(move)
            node = node.par
        path.reverse()
        return path

    def determine_move(self, prev_pos, curr_pos):
        dx = curr_pos[0] - prev_pos[0]
        dy = curr_pos[1] - prev_pos[1]
        if dx == 1:
            return 3  
        elif dx == -1:
            return 9  
        elif dy == 1:
            return 6  
        elif dy == -1:
            return 0  
