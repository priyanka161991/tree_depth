#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 20:25:17 2018

@author: priyanka.v.bhalekar@gmail.com
"""

from tree import Tree


def main():
    print('Start')
    
    tree = {
        'root': {
            'branch_1':{
                'leaf_1': 1,
                'sub_branch_1': {
                    'leaf_11': {
                        'leaf_111': 111
                    }
                }
            },
            'branch_2':{
                'leaf_21': 21,
                'leaf_22': 22
            }
        }
    }
    
    t = Tree(tree, 'root')    
    
    print('Tree depth :', t.depth)
    

if __name__ == '__main__':
    main()
