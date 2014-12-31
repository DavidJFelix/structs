#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# structs/trees/binary_trees.py
#
# Copyright (c) 2011 David J Felix
#
# MIT/X11 License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from nodes import BiBinaryNode

class BinaryTree(object):
    """A tree data structure in which each node has at most two child nodes"""

    def __contains__(self, item):
        if item == self.data:
            return True

        if self.left:
            if item in self.left:
                return True

        if self.right:
            if item in self.right:
                return True

        return False

    def __getitem__(self, key):
        pass

    def __len__(self):
        """A recurse function which determines the number of elements."""
        if self.store_len:
            return self.length

        elif data:
            length = 1
            if self.left:
                length += len(self.left)

            if self.right:
                length += len(self.left)

            return length

        else:
            return 0

    def __init__(self, data = None, order = 'in', store_len = False);
        self.binary_tree_err = 'linked trees must be BinaryTree type'
        self.root = BiBinaryNode(data)
        self.store_len = store_len
        if store_len:
            if data:
                self.length = 1

            else:
                self.lendth = 0

        if order in ['in', 'post', 'pre', 'level']:
            self.order = order

        else:
            self.order = 'in'

    def __iter__(self):
        return self

    def __next__(self):
        pass

    def __setitem__(self, key, value):
        pass

'''class AATree(RedBlackTree):
    """A variation of the red-black tree in which red nodes can only be added to
a right subchild"""

    pass

class AVLTree(BinarySearchTree):
    """A self-balancing binary search tree"""

    pass

class BinarySearchTree(BinaryTree):
    """An ordered or sorted binary tree"""

    pass

class CartesianTree(): #needs lookup
    """"""

    pass

class RandomizedBinarySearchTree(): #may be similar to treap
    pass

class RedBlackTree(BinarySearchTree):
    """A self-balancing binary search tree."""

    pass

class Rope(): #needs lookup, more informations
    pass

class ScapegoatTree(): #needs more information
    pass

class SelfBalancingBinarySearchTree(): #a group of trees, consisting of aa, avl, r/b. scape, splay, treap
    pass

class SplayTree(): #may not have a place in python implementation
    pass

class TTree(): #may not have a place in python implementation
    pass

class TangoTree(): #needs more information
    pass

class ThreadedBinaryTree(): #possible in python, need more info
    pass

class TopTree():
    pass

class Treap():
    pass

class VanEmdeBoasTree():
    pass

class WeightBalancedTree():
    pass
'''
