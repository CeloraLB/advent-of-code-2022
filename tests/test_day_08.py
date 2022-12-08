from unittest import TestCase
from day08.TreeView import TreeView

class TestTreeView (TestCase):
    def test_count_visible_trees(self):
        tree_view = TreeView()
        input = [
            '30373',
            '25512',
            '65332',
            '33549',
            '35390'
        ]

        self.assertEqual(21, tree_view.countVisibleTrees(input))