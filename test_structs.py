#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# structs/test_structs.py
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
# the LGPLv2+ (the  "Lesser GNU General Public License version 2 or (at your
# option) any later version"), the GPLv2+ (the "GNU General Public License 
# version 2 or (at your option) any later version"), the AGPLv2+ (the "Affero
# GNU General Public License version 2 or (at your option) any later version"),
# the MPLv1.1+ (the "Mozilla Public License version 1.1 or (at your option) any
# later version"), in which case the provisions of LGPLv2+, GPLv2+, AGPLv2+,
# or MPLv1.1+ are respectively applicable instead of those above. If you wish to
# allow use of your version of this file only under the terms of the LGPLv2+,
# GPLv2+, AGPLv2+ or MPLv1.1 and not to allow others to use your version of this
# file under the Apache License, Version 2.0 or another of the above licenses,
# indicate your decision by deleting the provisions above and replace them with
# the notice and other provisions required by the LGPLv2+, GPLv2+, AGPLv2+, or
# MPLv1.1+ respectively. If you do not delete the provisions above, or modify
# this notice a recipient may use your version of this file under either the
# Apache License, Version  2.0, the LGPLv2+, the GPLv2+, the AGPLv2+ or the
# MPLv1.1+. A full copy of all allowable version of these licenses (at the time
# of this publication) is available in the "licenses" directory, which is
# located in the root directory of this project.

import unittest
from tests import test_nodes

def get_test_suite():
    """
    """
    nodes_test_suite =  test_nodes.get_test_suite()
    structs_test_suite = unittest.TestSuite([nodes_test_suite,
                                            ])
    return structs_test_suite

def run_test()
    structs_test_suite = get_test_suite()
    unittest.TextTestRunner(verbosity = 2).run(structs_test_suite)
    
if __name__ == '__main__':
    run_test()

# FILE FLAGS: NOT FINALIZED, NEEDS TO BE TESTED
