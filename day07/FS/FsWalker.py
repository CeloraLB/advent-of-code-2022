from .FsTree import Node, DirNode, FileNode

class FsWalker:
    ROOT_DIR = '/'
    PREV_DIR = '..'
    CMD_SH = '$'

    def __init__(self):
        self.fs = DirNode('fs')
        self.fs.addChildren(DirNode(FsWalker.ROOT_DIR))

    def addShellCmd(self, commands: list) -> None:
        """
        Parse each command and updates the filesystem
        """
        current_dir = self.fs

        for i in range(len(commands)):
            cmd = commands[i]
            if self._isShellCmd(cmd):
                cmd_args = cmd.split(' ')
                cmd_sh = cmd_args[1]
                if cmd_sh == 'cd':
                    args = cmd_args[2]
                    if args == FsWalker.PREV_DIR:
                        if not current_dir.parent is None:
                            current_dir = current_dir.parent
                    else:
                        current_dir = current_dir.childrens[args]
                elif cmd_sh == 'ls':
                    continue
            else:
                # Reads all folder from ls
                param1, name = cmd.split(' ')
                if self._isDir(param1):                    
                    current_dir.addChildren(DirNode(name, current_dir))
                else:
                    # param1 is the filesize in case of a file
                    current_dir.addChildren(FileNode(name, current_dir, int(param1)))

    def _isShellCmd(self, cmd_line: str) -> bool:
        return cmd_line.startswith(FsWalker.CMD_SH)

    def _isDir(self, param1: str) -> bool:
        return param1 == 'dir'
        
    def getDirectoriesNodesWithLimitSize(self, max_size: int = -1, min_size: int = -1) -> list:
        directories = self.getAllDirectoryNodes(self.fs.childrens[FsWalker.ROOT_DIR])
        # filter dir here
        filtered_directories = []
        for dir in directories:
            if dir.size <= max_size or max_size == -1:
                filtered_directories.append(dir)
        return filtered_directories

    def getAllDirectoryNodes(self, node: Node) -> list:
        if isinstance(node, FileNode):
            return []

        directories = [node]
        for k in node.childrens:
            directories.extend(self.getAllDirectoryNodes(node.childrens[k]))

        return directories