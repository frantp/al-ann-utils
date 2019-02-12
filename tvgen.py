#!/usr/bin/env python3

import sys
import os
import random


def list_files(folder, ext):
    for (dirpath, dirnames, filenames) in os.walk(folder):
        for filename in filenames:
            _, fext = os.path.splitext(filename)
            if (fext == ext):
                yield os.path.join(dirpath, filename)


def write_tv_files(folder, valid_percentage, test_percentage):
    filenames = list(list_files(folder, ".jpg"))
    random.shuffle(filenames)
    l = len(filenames)
    nt = int(l * test_percentage)
    nv = int(l * valid_percentage)
    with open('test.txt', 'w') as f:
        for file in filenames[:nt]:
            f.write(file + '\n')
    with open('valid.txt', 'w') as f:
        for file in filenames[nt:nt+nv]:
            f.write(file + '\n')
    with open('train.txt', 'w') as f:
        for file in filenames[nt+nv:]:
            f.write(file + '\n')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: {0} <folder> [valid_percentage=0] [test_percentage=0]'
            .format(sys.argv[0]))
        exit(1)
    folder = sys.argv[1]
    valid_percentage = float(sys.argv[2]) / 100 if len(sys.argv) > 2 else 0
    test_percentage = float(sys.argv[3]) / 100 if len(sys.argv) > 3 else 0
    write_tv_files(sys.argv[1], valid_percentage, test_percentage)
