import os 
import sys
from FS.FsWalker import FsWalker

def main():
    if len(sys.argv) <= 1 or sys.argv[1] == None:
        sys.exit('need a secret message as first param')
    input_file = open(sys.argv[1], 'r')

    fs_walker = FsWalker()
    fs_walker.addShellCmd(input_file.read().splitlines())

    # part 1
    upper_limit = 100000
    dirs = fs_walker.getDirectoriesNodesWithLimitSize(upper_limit)
    sum_size = 0
    for d in dirs:
        sum_size += d.size

    print('total sum of folder below {} bytes: {}'.format(upper_limit, sum_size))

    # part 2
    fs_total_size = 70000000
    free_space = fs_total_size - fs_walker.fs.childrens[FsWalker.ROOT_DIR].size
    update_space = 30000000
    req_free_space = update_space - free_space
    dirs = fs_walker.getDirectoriesNodesWithLimitSize()
    min_dir = fs_walker.fs.childrens[FsWalker.ROOT_DIR]
    for d in dirs:
        if d.size > req_free_space and d.size < min_dir.size:
            min_dir = d
    
    print('the smallest dir that will free enough space is {} with size of {} '.format(min_dir.name, min_dir.size))

if __name__ == '__main__':
    main()