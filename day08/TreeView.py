class TreeView:
    def countVisibleTrees(self, tree_map: list) -> int:
        """
        Calculate how many trees are visible from outside the tree_map grid
        All of the trees around the edge of the grid are visible
        """
        # assuming tree_line is a square matrix
        visible_trees_map = [['-' for col in range(len(tree_map))] for row in range(len(tree_map))]
        visible_trees = 0 
        for rot in range(4):
            # 90 deg rotation counterclockwise
            tree_map = [list(x) for x in zip(*tree_map)][::-1]
            visible_trees_map = [list(x) for x in zip(*visible_trees_map)][::-1]

            for i in range(len(tree_map)):
                tree_line= tree_map[i]
                max = -1
                for j in range(len(tree_line)):
                    tree = int(tree_line[j])
                    if tree > max:
                        max = tree
                        if visible_trees_map[i][j] == '-':
                            visible_trees_map[i][j] = 'x'
                            visible_trees += 1

        return visible_trees