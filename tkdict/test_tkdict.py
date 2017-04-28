""" TKDict unittests
"""

import unittest
from string import maketrans
from tkdict import TKDict


class TestFDict(unittest.TestCase):

    def setUp(self):

        class FDict(TKDict):
            transtab = maketrans('-', '_')
            stripchars = '-_'
            delchars = '.'

        self.FDict = FDict

    def test_should_translate_correctly(self):
        fd = self.FDict()
        self.assertEqual(fd.translate_key("__F.oO-BaR--"), "foo_bar")


if __name__ == "__main__":
    unittest.main()
