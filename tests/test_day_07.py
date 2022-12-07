from unittest import TestCase
from day07.FS.FsWalker import FsWalker
from day07.FS.FsTree import DirNode

class TestFsWalker (TestCase):
    def test_init_fs(self):
        fs_walker = FsWalker()
        self.assertIsInstance(fs_walker.fs, DirNode)

    def test_add_shell_cmd(self):
        """
        Expected file system tree
        - / (dir)
            - a (dir)
                - e (dir)
                    - i (file, size=584)
                - f (file, size=29116)
                - g (file, size=2557)
                - h.lst (file, size=62596)
            - b.txt (file, size=14848514)
            - c.dat (file, size=8504156)
            - d (dir)
                - j (file, size=4060174)
                - d.log (file, size=8033020)
                - d.ext (file, size=5626152)
                - k (file, size=7214296)
        """
        input_cmd = [
            '$ cd /',
            '$ ls',
            'dir a',
            '14848514 b.txt',
            '8504156 c.dat',
            'dir d',
            '$ cd a',
            '$ ls',
            'dir e',
            '29116 f',
            '2557 g',
            '62596 h.lst',
            '$ cd e',
            '$ ls',
            '584 i',
            '$ cd ..',
            '$ cd ..',
            '$ cd d',
            '$ ls',
            '4060174 j',
            '8033020 d.log',
            '5626152 d.ext',
            '7214296 k'
        ]

        fs_walker = FsWalker()
        fs_walker.addShellCmd(input_cmd)
        self.assertEqual('/', fs_walker.fs.childrens[FsWalker.ROOT_DIR].name)
        self.assertEqual(48381165, fs_walker.fs.childrens[FsWalker.ROOT_DIR].size)
        self.assertIsNone(fs_walker.fs.childrens[FsWalker.ROOT_DIR].parent)

        root = fs_walker.fs.childrens[FsWalker.ROOT_DIR]
        self.assertEqual('a', root.childrens['a'].name)
        self.assertEqual('b.txt', root.childrens['b.txt'].name)
        self.assertEqual('c.dat', root.childrens['c.dat'].name)
        self.assertEqual('d', root.childrens['d'].name)
        self.assertEqual(94853, root.childrens['a'].size)
        self.assertEqual(14848514, root.childrens['b.txt'].size)
        self.assertEqual(8504156, root.childrens['c.dat'].size)
        self.assertEqual(24933642, root.childrens['d'].size)

        a_node = root.childrens['a']
        self.assertEqual('e', a_node.childrens['e'].name)
        self.assertEqual('f', a_node.childrens['f'].name)
        self.assertEqual('g', a_node.childrens['g'].name)
        self.assertEqual('h.lst', a_node.childrens['h.lst'].name)
        self.assertEqual(584, a_node.childrens['e'].size)
        self.assertEqual(29116, a_node.childrens['f'].size)
        self.assertEqual(2557, a_node.childrens['g'].size)
        self.assertEqual(62596, a_node.childrens['h.lst'].size)

        e_node = a_node.childrens['e']
        self.assertEqual('i', e_node.childrens['i'].name)
        self.assertEqual(584, e_node.childrens['i'].size)

        d_node = root.childrens['d']
        self.assertEqual('j', d_node.childrens['j'].name)
        self.assertEqual('d.log', d_node.childrens['d.log'].name)
        self.assertEqual('d.ext', d_node.childrens['d.ext'].name)
        self.assertEqual('k', d_node.childrens['k'].name)
        self.assertEqual(4060174, d_node.childrens['j'].size)
        self.assertEqual(8033020, d_node.childrens['d.log'].size)
        self.assertEqual(5626152, d_node.childrens['d.ext'].size)
        self.assertEqual(7214296, d_node.childrens['k'].size)



    def test_get_all_directories_nodes(self):
        input_cmd = [
            '$ cd /',
            '$ ls',
            'dir a',
            '14848514 b.txt',
            '8504156 c.dat',
            'dir d',
            '$ cd a',
            '$ ls',
            'dir e',
            '29116 f',
            '2557 g',
            '62596 h.lst',
            '$ cd e',
            '$ ls',
            '584 i',
            '$ cd ..',
            '$ cd ..',
            '$ cd d',
            '$ ls',
            '4060174 j',
            '8033020 d.log',
            '5626152 d.ext',
            '7214296 k'
        ]

        fs_walker = FsWalker()
        fs_walker.addShellCmd(input_cmd)
        expected_dir_sizes = {
            '/': 48381165,
            'a': 94853,
            'e': 584,
            'd': 24933642
        }
        directories = fs_walker.getDirectoriesNodesWithLimitSize(0)
        
        for dir in directories:
            self.assertIn(dir.name, expected_dir_sizes)
            self.assertEqual(expected_dir_sizes[dir.name], dir.size)

    
    def test_get_all_directories_nodes_with_maxsize(self):
        input_cmd = [
            '$ cd /',
            '$ ls',
            'dir a',
            '14848514 b.txt',
            '8504156 c.dat',
            'dir d',
            '$ cd a',
            '$ ls',
            'dir e',
            '29116 f',
            '2557 g',
            '62596 h.lst',
            '$ cd e',
            '$ ls',
            '584 i',
            '$ cd ..',
            '$ cd ..',
            '$ cd d',
            '$ ls',
            '4060174 j',
            '8033020 d.log',
            '5626152 d.ext',
            '7214296 k'
        ]

        fs_walker = FsWalker()
        fs_walker.addShellCmd(input_cmd)
        expected_dir_sizes = {
            'a': 94853,
            'e': 584,
        }
        directories = fs_walker.getDirectoriesNodesWithLimitSize(10000)
        
        for dir in directories:
            self.assertIn(dir.name, expected_dir_sizes)
            self.assertEqual(expected_dir_sizes[dir.name], dir.size)