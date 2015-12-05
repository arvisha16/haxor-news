# -*- coding: utf-8 -*-

# Copyright 2015 Donne Martin. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from __future__ import print_function

import mock
import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

from prompt_toolkit.key_binding.input_processor import KeyPress
from prompt_toolkit.keys import Keys

from hncli.haxor import Haxor


class KeysTest(unittest.TestCase):

    def setUp(self):
        self.haxor = Haxor()
        self.registry = self.haxor.key_manager.manager.registry
        self.processor = self.haxor.cli.input_processor

    def test_F2(self):
        orig_fuzzy = self.haxor.get_fuzzy_match()
        self.processor.feed_key(KeyPress(Keys.F2, ''))
        assert orig_fuzzy != self.haxor.get_fuzzy_match()

    def test_F10(self):
        with self.assertRaises(EOFError):
            self.processor.feed_key(KeyPress(Keys.F10, ''))
