#!/usr/bin/env python3
# Purpose: Say hello

# 命令行可以输入可选参数，用 -n，--name 代替
import argparse

parser = argparse.ArgumentParser(description='Say hello')
parser.add_argument('-n', '--name', metavar='name',
                    default='World', help='Name to greet')
args = parser.parse_args()
print('Hello, ' + args.name + '!')
