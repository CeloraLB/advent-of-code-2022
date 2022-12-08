class TreeView:
    def countVisibleTrees(self, tree_map: list) -> int:
        """
        Calculate how many trees are visible from outside the tree_map grid
        All of the trees around the edge of the grid are visible
        """
        # assuming tree_line is a square matrix
        visible_trees_map = [['-' for col in range(len(tree_map))] for row in range(len(tree_map))]

        visible_trees = 0 
        for i in range(len(tree_map)):
            tree_line= tree_map[i]
            max_r, max_l = (-1, -1)
            # left to right
            for j in range(len(tree_line)):
                tree = int(tree_line[j])
                if tree > max_r:
                    max_r = tree
                    if visible_trees_map[i][j] == '-':
                        visible_trees_map[i][j] = 'x'
                        visible_trees += 1

            
            # right to left
            tree_lin_rev = tree_line[::-1]
            for j in range(len(tree_lin_rev)):
                tree = int(tree_lin_rev[j])
                if tree > max_l:
                    max_l = tree
                    if visible_trees_map[i][len(visible_trees_map)-1-j] == '-':
                        visible_trees_map[i][len(visible_trees_map)-1-j] = 'x'
                        visible_trees += 1

        
        for j in range(len(tree_map)):
            max_t, max_b = (-1, -1)
            # top to bottom
            for i in range(len(tree_map)):
                tree = int(tree_map[i][j])
                if tree > max_t:
                    max_t = tree
                    if visible_trees_map[i][j] == '-':
                        visible_trees_map[i][j] = 'x'
                        visible_trees += 1

            # bottom to top
            tree_map_rev = tree_map[::-1]
            for i in range(len(tree_map_rev)):
                tree = int(tree_map_rev[i][j])
                if tree > max_b:
                    max_b = tree
                    if visible_trees_map[len(visible_trees_map)-1-i][j] == '-':
                        visible_trees_map[len(visible_trees_map)-1-i][j] = 'x'
                        visible_trees += 1

        return visible_trees