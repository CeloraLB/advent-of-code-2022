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

if __name__ == '__main__':
    main()