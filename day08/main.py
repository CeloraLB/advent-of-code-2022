import os
import sys
from TreeView import TreeView

def main():
    if len(sys.argv) <= 1 or sys.argv[1] == None:
        sys.exit('need a secret message as first param')
    input_file = open(sys.argv[1], 'r')
    tree_map = input_file.read().splitlines()

    tree_view = TreeView()
    visible_trees = tree_view.countVisibleTrees(tree_map)
    print('there are {} visible trees'.format(visible_trees))

    scenic_score_map = tree_view.getScenicScoreMap(tree_map)
    max_scenic_score = 0 
    for row in scenic_score_map:
        for scenic_score in row:
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score
    print('highest scenic score available is {}'.format(max_scenic_score))

if __name__ == '__main__':
    main()