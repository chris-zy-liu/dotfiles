#! /usr/bin/python

import opencc
import sys

converter = opencc.OpenCC('t2s.json')
print(converter.convert(sys.stdin.read()))
