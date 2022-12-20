import math

class HillClimber():
    def __init__(self) -> None:
        pass

    def getMinStepsToGoal(self, height_map: list) -> int:
        """
        the heightmap are marks for your current position (S) and the location that should get the best signal (E). 
        Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.
        """
        min_steps = 800000

        # I mixed up the x's and the y's. x's is going for the rows and y's are going for the columns

        # get position of (S) and (E)
        sx, sy, ex, ey = self._getStartingAndGoalPosition(height_map)
        # A*
        visited_nodes = [['' for j in range(len(height_map[i]))] for i in range(len(height_map))]
        nodes = [(sx, sy, self._getDistanceFromNodes(height_map, sx, sy, ex, ey), 0)] # (S)

        while len(nodes) > 0:
            debug = nodes.pop(0)
            # print(debug)
            node_x, node_y, distance, visited_n = debug
            # node_x, node_y, distance, visited_n = nodes.pop(0)
            visited_nodes[node_x][node_y] = 'x'

            if node_x == ex and node_y == ey:
                # print('found new path. steps {}'.format(visited_n))
                # if visited_n < min_steps:
                #     min_steps = visited_n
                # continue # test

                min_steps = visited_n
                break

            # get all visitable nodes for the node popped
            new_nodes = {}
            for dir in ['n', 'e', 's', 'w']:
                if dir == 'n':
                    next_node_x = node_x - 1 
                    next_node_y = node_y
                elif dir == 's':
                    next_node_x = node_x + 1
                    next_node_y = node_y
                elif dir == 'e':
                    next_node_x = node_x 
                    next_node_y = node_y + 1
                elif dir == 'w':
                    next_node_x = node_x 
                    next_node_y = node_y - 1

                # check if the node is valid
                if self._isNodeOutOfBorder(height_map, next_node_x, next_node_y):
                    # print('node {} {} not in map'.format(next_node_x, next_node_y))
                    continue

                # check if we can climb the node
                if not self._isNodeClimbable(height_map[node_x][node_y], height_map[next_node_x][next_node_y]):
                    # print('node {} {} not climbable'.format(next_node_x, next_node_y))
                    continue

                # new node should be visitable
                if visited_nodes[next_node_x][next_node_y] == 'x':
                    # print('node {} {} not visible'.format(next_node_x, next_node_y))
                    continue

                # calculate new nodes distance to end
                distance_to_goal = self._getDistanceFromNodes(height_map, next_node_x, next_node_y, ex, ey)

                # bucket sort the new_nodes dict
                if not distance_to_goal in new_nodes:
                    new_nodes[distance_to_goal] = []

                # insert new nodes in nodes list with visited_n + 1
                new_nodes[distance_to_goal].append((next_node_x, next_node_y, distance_to_goal, visited_n+1))

            # order the nodes starting from the furthest to the shorted (bucket sort)
            new_nodes_keys = list(new_nodes.keys())
            new_nodes_keys.sort(reverse=True)
            for d in new_nodes_keys:
                for n in new_nodes[d]:
                    nodes.insert(0, n)

        return min_steps

    def _getStartingAndGoalPosition(self, height_map: list) -> tuple:
        sx, sy = (-1, -1)
        ex, ey = (-1, -1)
        for i in range(len(height_map)):
            for j in range(len(height_map[i])):
                node = height_map[i][j]
                if node == 'S':
                    sx = i
                    sy = j
                elif node == 'E':
                    ex = i
                    ey = j

                if min(sx, sy, ex, ey) > -1: 
                    # Found them all!
                    break

        return (sx, sy, ex, ey)

    def _getDistanceFromNodes(self, height_map: list, ax: int, ay: int, bx: int, by: int) -> float:
        """
        This function is the key to find the shortest path
        """
        dx = abs(ax - bx)
        dy = abs(ay - by)
        dh = self._convertHeightToInt(height_map[bx][by]) - self._convertHeightToInt(height_map[ax][ay]) # >0 if we go up
        # return dh # 1290 steps
        # return math.sqrt(dx**2 + dy**2) # Euclidean Distance - 892 steps
        # return dx + dy # Manhattan Distance - 724 steps
        # return dx + dy + dh # 710 steps
        # return dx + dy + math.sqrt(2) * min(dx, dy) # Diagonal Distance - 682 steps
        # return dx + dy + math.sqrt(2) * min(dx, dy) + dh * 100 # 614 steps
        return dx + dy + math.sqrt(2) * min(dx, dy) + dh * 100


    def _isNodeOutOfBorder(self, height_map: list, node_x: int, node_y: int) -> bool:
        return not (node_x >= 0 and node_x < len(height_map) and node_y >= 0 and node_y < len(height_map[0]))

    def _isNodeClimbable(self, height_a: str, height_b: str) -> bool:
        ha = self._convertHeightToInt(height_a)
        hb = self._convertHeightToInt(height_b)

        return ha >= hb - 1 # you can go down (hb < ha) or you can go up by one ha+1 = hb
    
    def _convertHeightToInt(self, height_str: str) -> int:
        if height_str == 'S':
            h = 0
        elif height_str == 'E':
            h = 25
        else:
            h = ord(height_str) - 97

        return h
