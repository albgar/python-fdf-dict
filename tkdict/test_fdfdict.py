import unittest
from string import maketrans

from collections import MutableMapping
from tkdict import FDFDict


class TestFDFDict(unittest.TestCase):

    def setUp(self):
        self.FDFDict = FDFDict

    def test_type_checking(self):
        # Both dict() and TKDict() are subtypes of MutableMapping
        self.assertTrue(isinstance(self.FDFDict(), MutableMapping))
        self.assertTrue(isinstance(dict(), MutableMapping))

    def test_key_mutation(self):
        f = self.FDFDict()
        f["MD.Tolerance"] = 3.14
        f["md-tolerance"] = 2.71
        t = f["MD.Tolerance"]
        self.assertEqual(t, 2.71)
        self.assertEqual(f.keys(), ["md-tolerance"])

    def test_key_items(self):
        f = self.FDFDict()
        f["MD.Tolerance"] = 3.14
        f["MD-type-of-run"] = "CG"
        self.assertEqual(f.items(),[("MD-type-of-run","CG"),("MD.Tolerance",3.14)])
        f["md-type-of-run"] = "Broyden"
        t =  f["MD.TypeOfRun"]
        self.assertEqual(t,"Broyden")
        self.assertEqual(f.items(),[("md-type-of-run","Broyden"),("MD.Tolerance",3.14)])

        
    def test_key_iteritems(self):
        f = self.FDFDict()
        f["MD.Tolerance"] = 3.14
        f["MD-type-of-run"] = "CG"
        l = [(k,v) for (k,v) in f.iteritems()]
        self.assertEqual(l,[("MD-type-of-run","CG"),("MD.Tolerance",3.14)])
        f["md-type-of-run"] = "Broyden"
        t =  f["MD.TypeOfRun"]
        self.assertEqual(t,"Broyden")
        l = [(k,v) for (k,v) in f.iteritems()]
        self.assertEqual(l,[("md-type-of-run","Broyden"),("MD.Tolerance",3.14)])
        
    def test_key_iter(self):
        f = self.FDFDict()
        f["MD.Tolerance"] = 3.14
        f["MD-type-of-run"] = "CG"
        l = [k for k in f.iterkeys()]
        self.assertEqual(l,["MD-type-of-run","MD.Tolerance"])
        f["md-type-of-run"] = "Broyden"
        t =  f["MD.TypeOfRun"]
        self.assertEqual(t,"Broyden")
        l = [k for k in f.iterkeys()]
        self.assertEqual(l,["md-type-of-run","MD.Tolerance"])
        
    def test_keys(self):
        f = self.FDFDict(fOO=5, BAr=7)
        self.assertEqual(len(f), 2)
        self.assertIn("fOO", f.keys())
        self.assertIn("BAr", f.keys())

    def test_mutations(self):
        f = self.FDFDict(foo=5, bar=7, baz=13)
        self.assertEqual(len(f), 3)

        del f["B-A.R"]  # delete item with `del` statement
        self.assertEqual(f["Bar"], None)
        self.assertEqual(len(f), 2)

        baz = f.pop("Baz", None)  # pop value out of our FDFDict instance
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
