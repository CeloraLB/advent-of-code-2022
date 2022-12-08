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

    def test_get_scenic_score_map(self):
        tree_view = TreeView()
        input = [
            '30373',
            '25512',
            '65332',
            '33549',
            '35390'
        ]
        expected_scenic_score = [
            [0, 0, 0, 0, 0],
            [0, 1, 4, 1, 0],
            [0, 6, 1, 2, 0],
            [0, 1, 8, 3, 0],
            [0, 0, 0, 0, 0]
        ]
            
        scenic_score = tree_view.getScenicScoreMap(input)

        self.assertListEqual(expected_scenic_score, scenic_score)