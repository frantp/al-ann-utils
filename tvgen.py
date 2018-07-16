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


def write_tv_files(folder, valid_percentage):
    filenames = list(list_files(folder, ".jpg"))
    random.shuffle(filenames)
    n = int(len(filenames) * valid_percentage)
    with open('valid.txt', 'w') as f:
        for file in filenames[:n]:
            f.write(file + '\n')
    with open('train.txt', 'w') as f:
        for file in filenames[n:]:
            f.write(file + '\n')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {} <folder> <valid_percentage>'.format(sys.argv[0]))
        exit(1)
    write_tv_files(sys.argv[1], float(sys.argv[2]) / 100)
