#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# structs/trees/tests/test_binary_trees.py
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

import unittest
from structs.trees import binary_trees

def get_test_suite():
    """
    """
    binary_tree_test_suite = unittest.TestSuite()
    test_loader = binary_tree_test_suite.TestLoader()
    # test_loader.loadTestsFromTestCase()
    return binary_tree_test_suite

def run_test():
    binary_tree_test_suite = get_test_suite()
    tester = unittest.TextTestRunner(verbosity = 2)
    tester.run(binary_tree_test_suite)

if __name__ == '__main__':
    run_test()
