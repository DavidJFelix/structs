#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#
# test_nodes.py
#
# Copyright (C) 2011  David J Felix
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.

import unittest
from random import randint
from nodes import *

class TestNode(unittest.TestCase):
    """
    """

    def setUp(self):
        # Have a rand 64b int for testing
        self.test_rand = randint(1, 2**64) - 1
        print('\nTesting with random other =', self.test_rand)

        # Have a rand 64b int for storing
        self.test_int = randint(1, 2**64) - 1
        self.test_node = Node(self.test_int)
        print('Testing with random int value =', self.test_int)

    def test_abs(self):
        # Test abs()
        temp_int = abs(self.test_int)
        temp_node = abs(self.test_node)
        self.assertEqual(temp_int, temp_node)

    def test_ands(self):
        # Test &
        temp_int = self.test_int & self.test_rand
        temp_node = self.test_node & self.test_rand
        self.assertEqual(temp_int, temp_node)

        # Test reverse &
        temp_int = self.test_rand & self.test_int
        temp_node = self.test_rand & self.test_node
        self.assertEqual(temp_int, temp_node)

        # Test &=
        temp_int = self.test_int
        temp_int &= self.test_rand
        temp_node = self.test_node
        temp_node &= self.test_rand
        self.assertEqual(temp_int, temp_node)

    def test_bin(self):
        # Test bin()
        temp_int = bin(self.test_int)
        temp_node = bin(self.test_node)
        self.assertEqual(temp_int, temp_node)

    def test_call(self):
        import sys

        # Test ()
        try:
            temp_int = self.test_int()
            temp_node = self.test_node()
            self.assertEqual(temp_int, temp_node)

        except:
            self.assertRaises(sys.exc_info()[0], self.test_node, ())

    def test_del(self):
        pass

    def test_divs(self):
        # Test /
        temp_int = self.test_int / self.test_rand
        temp_node = self.test_node / self.test_rand
        self.assertEqual(temp_int, temp_node)

        # Test reverse /
        temp_int = self.test_rand / self.test_int
        temp_node = self.test_rand / self.test_node
        self.assertEqual(temp_int, temp_node)

        # Test /=
        temp_int = self.test_int
        temp_int /= self.test_rand
        temp_node = self.test_node
        temp_node /= self.test_rand
        self.assertEqual(temp_int, temp_node)

    def test_divmod(self):
        # Test divmod()
        temp_int = divmod(self.test_int, self.test_rand)
        temp_node = divmod(self.test_node, self.test_rand)
        self.assertEqual(temp_int, temp_node)
        
    def test_eq(self):
        # Test Node equivalence
        temp_bool = self.test_int == self.test_node
        self.assertTrue(temp_bool)
        temp_bool = self.test_node == self.test_int
        self.assertTrue(temp_bool)

        # Test ==
        temp_int = self.test_int == self.test_rand
        temp_node = self.test_node == self.test_rand
        self.assertEqual(temp_int, temp_node)
        temp_int = self.test_rand == self.test_int
        temp_node = self.test_rand == self.test_node
        self.assertEqual(temp_int, temp_node)

    def test_floordivs(self):
        # Test //
        temp_int = self.test_int // self.test_rand
        temp_node = self.test_node // self.test_rand
        self.assertEqual(temp_int, temp_node)

        # Test reverse //
        temp_int = self.test_rand // self.test_int
        temp_node = self.test_rand // self.test_node
        self.assertEqual(temp_int, temp_node)

        # Test //=
        temp_int = self.test_int
        temp_int //= self.test_rand
        temp_node = self.test_node
        temp_node //= self.test_rand
        self.assertEqual(temp_int, temp_node)

    def test_float(self):
        # Test float()
        temp_int = float(self.test_int)
        temp_node = float(self.test_node)
        self.assertEqual(temp_int, temp_node)

    def test_ge(self):
        # Test Node equivalence
        temp_bool = self.test_int >= self.test_node
        self.assertTrue(temp_bool)
        temp_bool = self.test_node >= self.test_int
        self.assertTrue(temp_bool)

        # Test >=
        temp_int = self.test_int >= self.test_rand
        temp_node = self.test_node >= self.test_rand
        self.assertEqual(temp_int, temp_node)
        temp_int = self.test_rand >= self.test_int
        temp_node = self.test_rand >= self.test_node
        self.assertEqual(temp_int, temp_node)

    def test_gt(self):
        # Test Node equivalence
        temp_bool = self.test_int > self.test_node
        self.assertFalse(temp_bool)
        temp_bool = self.test_node > self.test_int
        self.assertFalse(temp_bool)

        # Test >
        temp_int = self.test_int > self.test_rand
        temp_node = self.test_node > self.test_rand
        self.assertEqual(temp_int, temp_node)
        temp_int = self.test_rand > self.test_int
        temp_node = self.test_rand > self.test_node
        self.assertEqual(temp_int, temp_node)

    def test_hex(self):
        # Test hex()
        temp_int = hex(self.test_int)
        temp_node = hex(self.test_node)
        self.assertEqual(temp_int, temp_node)

    def test_le(self):
        # Test Node equivalence
        temp_bool = self.test_int <= self.test_node
        self.assertTrue(temp_bool)
        temp_bool = self.test_node <= self.test_int
        self.assertTrue(temp_bool)

        # Test <=
        temp_int = self.test_int <= self.test_rand
        temp_node = self.test_node <= self.test_rand
        self.assertEqual(temp_int, temp_node)
        temp_int = self.test_rand <= self.test_int
        temp_node = self.test_rand <= self.test_node
        self.assertEqual(temp_int, temp_node)

    def test_lshifts(self):
        # Must use shorter range of randoms to prevent overloading
        temp_rand = randint(1, 2**8) - 1
        test_int = temp_rand
        test_node = Node(temp_rand)
        print('Testing with random 8b =', temp_rand)

        # Test <<
        temp_int = self.test_int << temp_rand
        temp_node = self.test_node << temp_rand
        self.assertEqual(temp_int, temp_node)

        # Test reverse <<
        temp_int = self.test_rand << test_int
        temp_node = self.test_rand << test_node
        self.assertEqual(temp_int, temp_node)

        # Test <<=
        temp_int = self.test_int
        temp_int <<= temp_rand
        temp_node = self.test_node
        temp_node <<= temp_rand
        self.assertEqual(temp_int, temp_node)

    def test_lt(self):
        # Test Node equivalence
        temp_bool = self.test_int < self.test_node
        self.assertFalse(temp_bool)
        temp_bool = self.test_node < self.test_int
        self.assertFalse(temp_bool)

        # Test <
        temp_int = self.test_int < self.test_rand
        temp_node = self.test_node < self.test_rand
        self.assertEqual(temp_int, temp_node)
        temp_int = self.test_rand < self.test_int
        temp_node = self.test_rand < self.test_node
        self.assertEqual(temp_int, temp_node)

    def test_init(self):
        pass

    def test_invert(self):
        # Test ~
        temp_int = ~self.test_int
        temp_node = ~self.test_node
        self.assertEqual(temp_int, temp_node)

    def test_mods(self):
        # Test %
        temp_int = self.test_int % self.test_rand
        temp_node = self.test_node % self.test_rand
        self.assertEqual(temp_int, temp_node)

        # Test reverse %
        temp_int = self.test_rand % self.test_int
        temp_node = self.test_rand % self.test_node
        self.assertEqual(temp_int, temp_node)

        # Test %=
        temp_int = self.test_int
        temp_int %= self.test_rand
        temp_node = self.test_node
        temp_node %= self.test_rand
        self.assertEqual(temp_int, temp_node)

    def test_muls(self):
        # Test *
        temp_int = self.test_int * self.test_rand
        temp_node = self.test_node * self.test_rand
        self.assertEqual(temp_int, temp_node)

        # Test reverse *
        temp_int = self.test_rand * self.test_int
        temp_node = self.test_rand * self.test_node
        self.assertEqual(temp_int, temp_node)

        # Test *=
        self.assertEqual(temp_int, temp_node)
        temp_int = self.test_int
        temp_int *= self.test_rand
        temp_node = self.test_node
        temp_node *= self.test_rand

    def test_ne(self):
        # Test Node equivalence
        temp_bool = self.test_int != self.test_node
        self.assertFalse(temp_bool)
        temp_bool = self.test_node != self.test_int
        self.assertFalse(temp_bool)

        # Test !=
        temp_int = self.test_int != self.test_rand
        temp_node = self.test_node != self.test_rand
        self.assertEqual(temp_int, temp_node)
        temp_int = self.test_rand != self.test_int
        temp_node = self.test_rand != self.test_node
        self.assertEqual(temp_int, temp_node)
        

    def test_neg(self):
        # Test -
        temp_int = -self.test_int
        temp_node = -self.test_node
        self.assertEqual(temp_int, temp_node)

    def test_nonzero(self):
        # Test bool()
        temp_int = bool(self.test_int)
        temp_node = bool(self.test_node)
        self.assertEqual(temp_int, temp_node)

    def test_oct(self):
        # Test oct()
        temp_int = oct(self.test_int)
        temp_node = oct(self.test_node)
        self.assertEqual(temp_int, temp_node)

    def test_ors(self):
        # Test |
        temp_int = self.test_int | self.test_rand
        temp_node = self.test_node | self.test_rand
        self.assertEqual(temp_int, temp_node)

        # Test reverse |
        temp_int = self.test_rand | self.test_int
        temp_node = self.test_rand | self.test_node
        self.assertEqual(temp_int, temp_node)

        # Test |=
        temp_int = self.test_int
        temp_int |= self.test_rand
        temp_node = self.test_node
        temp_node |= self.test_rand
        self.assertEqual(temp_int, temp_node)

    def test_pos(self):
        # Test +
        temp_int = +self.test_int
        temp_node = +self.test_node
        self.assertEqual(temp_int, temp_node)

    ########################### Need to modify to test optional modulo
    def test_pows(self):
        # Must create a lower random int to prevent overloading
        temp_rand1 = randint(1, 2**8)
        temp_rand2 = randint(1, 2**8)
        test_int = temp_rand1
        test_node = Node(temp_rand1)
        print('Testing with random 8bs =', temp_rand1, ',', temp_rand2)

        # Test **
        temp_int = self.test_int ** temp_rand1
        temp_node = self.test_node ** temp_rand1
        self.assertEqual(temp_int, temp_node)

        # Test reverse **
        temp_int = temp_rand2 ** test_int
        temp_node = temp_rand2 ** test_node
        self.assertEqual(temp_int, temp_node)
        
        # Test **=
        temp_int = test_int
        temp_int **= temp_rand2
        temp_node = test_node
        temp_node **= temp_rand2
        self.assertEqual(temp_int, temp_node)

    def test_repr(self):
        # Test repr()
        temp_int = repr(self.test_int)
        temp_node = repr(self.test_node)
        self.assertEqual(temp_int, temp_node)
        

    def test_rshifts(self):
        # Must use shorter range of randoms to prevent overloading
        temp_rand = randint(1, 2**8) - 1
        test_int = temp_rand
        test_node = Node(temp_rand)
        print('Testing with random 8b =', temp_rand)

        # Test >>
        temp_int = self.test_int >> temp_rand
        temp_node = self.test_node >> temp_rand
        self.assertEqual(temp_int, temp_node)

        # Test reverse >>
        temp_int = self.test_rand >> test_int
        temp_node = self.test_rand >> test_node
        self.assertEqual(temp_int, temp_node)

        # Test >>=
        temp_int = self.test_int
        temp_int >>= temp_rand
        temp_node = self.test_node
        temp_node >>= temp_rand
        self.assertEqual(temp_int, temp_node)

    def test_str(self):
        # Test str()
        temp_int = str(self.test_int)
        temp_node = str(self.test_node)
        self.assertEqual(temp_int, temp_node)

    def test_subs(self):
        # Test -
        temp_int = self.test_int - self.test_rand
        temp_node = self.test_node - self.test_rand
        self.assertEqual(temp_int, temp_node)

        # Test reverse -
        temp_int = self.test_rand - self.test_int
        temp_node = self.test_rand - self.test_node
        self.assertEqual(temp_int, temp_node)

        # Test -=
        temp_int = self.test_int
        temp_int -= self.test_rand
        temp_node = self.test_node
        temp_node -= self.test_rand
        self.assertEqual(temp_int, temp_node)

    def test_truedivs(self):
        # Test /
        temp_int = self.test_int / self.test_rand
        temp_node = self.test_node / self.test_rand
        self.assertEqual(temp_int, temp_node)

        # Test reverse /
        temp_int = self.test_rand / self.test_int
        temp_node = self.test_rand / self.test_node
        self.assertEqual(temp_int, temp_node)

        # Test /=
        temp_int = self.test_int
        temp_int /= self.test_rand
        temp_node = self.test_node
        temp_node /= self.test_rand
        self.assertEqual(temp_int, temp_node)


    def test_xors(self):
        # Test ^
        temp_int = self.test_int ^ self.test_rand
        temp_node = self.test_node ^ self.test_rand
        self.assertEqual(temp_int, temp_node)

        # Test reverse ^
        temp_int = self.test_rand ^ self.test_int
        temp_node = self.test_rand ^ self.test_node
        self.assertEqual(temp_int, temp_node)

        # Test ^=
        temp_int = self.test_int
        temp_int ^= self.test_rand
        temp_node = self.test_node
        temp_node ^= self.test_rand
        self.assertEqual(temp_int, temp_node)

if __name__ == '__main__':
    unittest.main()
        

        

    
