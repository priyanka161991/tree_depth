#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 20:54:26 2018

@author: priyanka.v.bhalekar@gmail.com
"""

class Tree(object):
    def __init__(self, tree, root):
        self.tree = tree
        self.root = root
        self.depth = 0
        self.branch_depths = 0
        
        self._find_depth(self.tree)
        
    def _find_depth(self, tree):
        # Traverse each sub tree
        for key, sub_tree in tree.items():
            
            # Move to next level
            self.branch_depths = self.branch_depths + 1
            
            # Look for sub tree
            if type(sub_tree) is dict:
                # Find depth of sub tree
                self._find_depth(sub_tree)
            else:
                # Reached leaf node - compare current branch's 
                # depth with highest depth so far.
                if self.branch_depths > self.depth:
                    # Current branch's depth is highest so far.
                    self.depth = self.branch_depths
            
            # Read next sub tree. Move one level up
            self.branch_depths = self.branch_depths - 1
