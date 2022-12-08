class TreeView:
    def countVisibleTrees(self, tree_map: list) -> int:
        """
        Calculate how many trees are visible from outside the tree_map grid
        All of the trees around the edge of the grid are visible
        """
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

    def getScenicScoreMap(self, tree_map: list) -> list:
        """
        A tree's scenic score is found by multiplying together its viewing distance in each of the four directions.
        If a tree is right on the edge, at least one of its viewing distances will be zero.
        """
        scenic_score_map = [[1 for col in range(len(tree_map))] for row in range(len(tree_map))]
        for rot in range(4):
            # 90 deg rotation counterclockwise
            tree_map = [list(x) for x in zip(*tree_map)][::-1]
            scenic_score_map = [list(x) for x in zip(*scenic_score_map)][::-1]
            for i in range(len(tree_map)):
                tree_line= tree_map[i]
                for j in range(len(tree_line)):
                    scenic_score = 0
                    if (not i in [0, len(tree_map)-1]) and (not j in [0, len(tree_map)-1]): # skip if it is on the matrix border 
                        remainder_tree_line = tree_line[j+1::]
                        for k in range(len(remainder_tree_line)):
                            scenic_score += 1
                            if tree_line[j] <= remainder_tree_line[k]:
                                break
                    scenic_score_map[i][j] *= scenic_score
                        
        return scenic_score_map