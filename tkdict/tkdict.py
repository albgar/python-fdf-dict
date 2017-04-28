""" Module with implementation of TKDict (translated-keys-dictionary) class.
"""
# Not compatible with python3 due to string-specific translation.
# `translate_key` could be turned into classmethod.
# `transtab`, `stripchars`, `delchars` could be turned into classproperties.

from string import maketrans
from collections import MutableMapping


class TKDict(MutableMapping):
    """ Dictionary-like class that also contains character translation and deletion data.
    Stores (value, initial-key) tuples accessible by a translated key.
    """

    def translate_key(self, key):
        """ Strips key-string from sides, translate internal chars and set to lowercase. """
        transtab   = getattr(self, 'transtab', maketrans('', ''))
        stripchars = getattr(self, 'stripchars', '')
        delchars   = getattr(self, 'delchars', '')

        return key.strip(stripchars).translate(transtab, delchars).lower()

    def __init__(self, *args, **kw):
        """ Create translated-keys-dictionary from initial data.
        If several input keys translate to same string, only first occurrence is saved.
        """
        # _storage is internal dictionary stored as: {<translated_key>: (<value>, <initial_key>), }
        self._storage = {}
        inp_dict = dict(*args, **kw)

        # store data from initial arguments
        # here only first occurrence of every unique translated key is stored!
        for inp_key in inp_dict.keys():
            if self.translate_key(inp_key) not in self.keys():
                self[inp_key] = inp_dict[inp_key]

    def keys(self):
        # _storage keys are translated keys
        return self._storage.keys()

    def __setitem__(self, key, value):
        """ Store a (value, initial_key) tuple under translated key. """
        trans_key = self.translate_key(key)
        # check if we already have a translated key in _storage
        # if so, overwrite the value in tuple, but not the initial key
        if trans_key in self._storage.keys():
            old_value, initial_key = self._storage[trans_key]
            self._storage.__setitem__(trans_key, (value, initial_key))

        self._storage.__setitem__(trans_key, (value, key))

    def __getitem__(self, key):
        """ Translate the key, unpack value-tuple and return the value if exists or None. """
        try:
            value, initial_key = self._storage[self.translate_key(key)]
            return value
        except KeyError:
            return None

    def get_initial_key(self, key):
        """ Translate the key, unpack value-tuple and return
        the corresponding initial key if exists or None.
        """
        try:
            value, initial_key = self._storage[self.translate_key(key)]
            return initial_key
        except KeyError:
            return None

    def __delitem__(self, key):
        """ Translate the key, purge value-tuple """
        self._d.__delitem__(self.translate_key(key))

    def __iter__(self):
        return iter(self._storage)

    def __len__(self):
        return len(self._storage)
