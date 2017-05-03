""" TKDict unittests by example of .fdf-data dict
"""

import unittest
from string import maketrans

from collections import MutableMapping
from tkdict import TKDict, FDict


class TestFDict(unittest.TestCase):

    def setUp(self):
        self.FDict = FDict

    def test_should_translate_correctly(self):
        f = self.FDict()
        self.assertEqual(f.translate_key("__F.oO-BaR--"), "foo_bar")

    def test_type_checking(self):
        # Both dict() and TKDict() are subtypes of MutableMapping
        self.assertTrue(isinstance(self.FDict(), MutableMapping))
        self.assertTrue(isinstance(dict(), MutableMapping))

    def test_internal_storage_dict(self):
        f = self.FDict(FoO=5, BaR=7)
        self.assertDictEqual(f._storage, {"foo": (5, "FoO"), "bar": (7, "BaR")})

    def test_should_return_correct_value(self):
        f = self.FDict(FoO=5, BaR=7)
        self.assertEqual(f["foo"], 5)
        self.assertEqual(f["_Fo.o"], 5)
        self.assertEqual(f["bar"], 7)
        self.assertEqual(f["b.AR--"], 7)
        self.assertEqual(f["baz"], None)

    def test_should_save_correctly(self):
        f = self.FDict(FoO=5, BaR=7)
        f["_BaZ"] = 13
        self.assertIn("baz", f.keys())
        self.assertEqual(f.get_initial_key("baz"), "_BaZ")

    def test_should_initialize_correctly(self):
        f = self.FDict({"F...oo": 5, "Bar": 7}, BaZ=13, fOO=19)
        self.assertEqual(len(f), 3)     # three unique translated keys
        self.assertEqual(f["foo"], 5)   # only first occurrence saved at init
        self.assertEqual(f.get_initial_key("foo"), "F...oo")  # initial key
        f["-foO-"] = 23
        self.assertEqual(f["foo"], 23)  # the value is rewritten
        self.assertEqual(f.get_initial_key("foo"), "F...oo")  # while initial key stays the same

    def test_mutations(self):
        f = self.FDict(FoO=5, BaR=7, bAZ=13)
        self.assertEqual(len(f), 3)

        del f["_BAR_"]  # delete item with `del` statement
        self.assertEqual(f["Bar"], None)
        self.assertEqual(len(f), 2)

        baz = f.pop("b.a.z", None)  # pop value out of our FDict instance
        self.assertEqual(baz, 13)
        self.assertEqual(f["baz"], None)
        self.assertEqual(len(f), 1)

        f.update(UnI=42)  # update fdict like normal dict
        self.assertIn("uni", f.keys())
        self.assertEqual(f["uni"], 42)
        self.assertEqual(len(f), 2)

        f.clear()  # purge all values from fdict
        self.assertEqual(len(f), 0)


if __name__ == "__main__":
    unittest.main()
