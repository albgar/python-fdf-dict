# Miscellaneous Utilities Pack

- `tkdict` Python dictionary-like collection class with 'translation
        insensitive' keys. For example, in the FDFDict subclass:

        MD.TypeOfRun, md-type-of-run, mdTypeOfRun, mdtypeofrun

        all represent the same key in the dictionary. The actual form of the
        key returned by methods such as 'keys()' is the latest to be used in
        a setting operation.

        Vladimir Dikan and Alberto Garcia, 2017
	
