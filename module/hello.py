#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'Safa A'

import sys

def test():
    args = sys.argv
    if len(args)==1:
            print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments! Get reckt!')

if __name__=='__main__':
    test()

