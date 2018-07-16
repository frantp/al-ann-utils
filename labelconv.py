#!/usr/bin/env python3

import sys
import os
import json


def read_json_files(folder):
    for (dirpath, dirnames, filenames) in os.walk(folder):
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if (ext != '.json'):
                continue
            filepath = os.path.join(dirpath, filename)
            print('Reading {}'.format(filepath))
            with open(filepath, 'r') as f:
                yield json.load(f)


def write_yolo_files(folder, data, width, height):
    for file in data:
        filename = file['filename'].split('/')[-1].split('\\')[-1]
        basename, _ = os.path.splitext(filename)
        filepath = os.path.join(folder, basename + '.txt')
        print(' - Writing {}'.format(filepath))
        with open(filepath, 'w') as f:
            for rect in file['annotations']:
                x = (rect['x'] + 0.5 * rect['width']) / width
                y = (rect['y'] + 0.5 * rect['height']) / height
                w = rect['width'] / width
                h = rect['height'] / height
                f.write('{} {} {} {} {}\n'.format(0, x, y, w, h))


def labelconv(width, height, infolder, outfolder):
    if not os.path.exists(outfolder):
        os.makedirs(outfolder)
    for data in read_json_files(infolder):
        write_yolo_files(outfolder, data, width, height)


if __name__ == '__main__':
    if len(sys.argv) != 4 and len(sys.argv) != 5:
        print('Usage: {} <width> <height> <infolder> [<outfolder>]'
            .format(sys.argv[0]))
        exit(1)
    labelconv(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[-1])
