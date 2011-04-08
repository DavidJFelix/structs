#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# structs/trees/binary_trees.py
#
# Copyright (c) 2011 David J Felix
#
# Contributors:
#                    [Add your name here]
#
# Licensed under the Apache License, Version 2.0 (the "License");  you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at:
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
#
# Alternatively, the contents of this file may be used under the terms of 
# the LGPLv3+ (the  "Lesser GNU General Public License version 3 or later"),
# the GPLv3+ (the "GNU General Public License version 3 or later"),
# the AGPLv3+ (the "Affero GNU General Public License version 3 or later"),
# the MPLv1.1+ (the "Mozilla Public License version 1.1 or later"), in which
# case the provisions of LGPLv3+, GPLv3+, AGPLv3+, or MPLv1.1+ are respectively
# applicable instead of those above. If you wish to allow use of your version of
# this file only under the terms of the LGPLv3+, GPLv3+, AGPLv3+ or MPLv1.1 and
# not to allow others to use your version of this file under the Apache License,
# Version 2.0 or another of the above licenses, indicate your decision by
# deleting the provisions above and replace them with the notice and other
# provisions required by the LGPLv3+, GPLv3+, AGPLv3+, or MPLv1.1+ respectively.
# If you do not delete the provisions above, or modify this notice a recipient
# may use your version of this file under either the Apache License, Version 
# 2.0, the LGPLv3+, the GPLv3+, the AGPLv3+ or the MPLv1.1+. A full copy of the
# oldest allowable version of these licenses is available in the "licenses"
# directory, which is located in the root directory of this project.

import nodes

class BinaryTree(nodes.BiBinaryNode):
    """A tree data structure in which each node has at most two child nodes"""

    def insert(self):
        pass

    def __iter__(self):
        """Recursively iterate in-order"""
        try:
            for each in self.left:
                yield each

        except(TypeError):
            pass

        yield self.data
        try:
            for each in self.right:
                yield each

        except(TypeError):
            pass

    def iter_in_order(self):
        """Recursively iterate in-order.
    Operates identically to __iter__(), but exists for calling consistancy"""
        return self.__iter__()

    def iter_pre_order(self):
        """Recursively iterate pre-order"""
        yield self.data
        try:
            for each in self.left:
                yield each

        except(TypeError):
            pass

        try:
            for each in self.right:
                yield each

        except(TypeError):
            pass
            
    def iter_post_order(self):
        """Recursively iterate post-order"""
        try:
            for each in self.left:
                yield each

        except(TypeError):
            pass

        try:
            for each in self.right:
                yield each

        except(TypeError):
            pass

        yield self.data
    
class AATree(RedBlackTree):
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
