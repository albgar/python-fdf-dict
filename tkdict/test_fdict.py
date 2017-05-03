import unittest
from string import maketrans

from collections import MutableMapping
from tkdict import FDict


class TestFDict(unittest.TestCase):

    def setUp(self):
        self.FDict = FDict

    def test_type_checking(self):
        # Both dict() and TKDict() are subtypes of MutableMapping
        self.assertTrue(isinstance(self.FDict(), MutableMapping))
        self.assertTrue(isinstance(dict(), MutableMapping))

    def test_key_mutation(self):
        f = self.FDict()
        f["Pepe"] = 3.14
        f["pePe"] = 2.71
        t = f["Pepe"]
        self.assertEqual(t, 2.71)
        self.assertEqual(f.keys(), ["Pepe"])

    def test_keys(self):
        f = self.FDict(fOO=5, BAr=7)
        self.assertEqual(len(f), 2)
        self.assertIn("fOO", f.keys())
        self.assertIn("BAr", f.keys())

    def test_mutations(self):
        f = self.FDict(foo=5, bar=7, baz=13)
        self.assertEqual(len(f), 3)

        del f["_BAR_"]  # delete item with `del` statement
        self.assertEqual(f["Bar"], None)
        self.assertEqual(len(f), 2)

        baz = f.pop("baz", None)  # pop value out of our FDict instance
        self.assertEqual(baz, 13)
        self.assertEqual(f["baz"], None)
        self.assertEqual(len(f), 1)

        f.update(UnI=42)  # update fdict like normal dict
        self.assertIn("UnI", f.keys())
        self.assertEqual(f["uni"], 42)
        self.assertEqual(len(f), 2)

        f.clear()  # purge all values from fdict
        self.assertEqual(len(f), 0)


if __name__ == "__main__":
    unittest.main()
