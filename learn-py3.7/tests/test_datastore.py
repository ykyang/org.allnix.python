import unittest
import sys
from allnix.logdatastore import FileSystemLogDatastore
from allnix.logdatastore import LogDatastore

class DatastoreTest(unittest.TestCase):
    def test_datastore(self):
        ds = LogDatastore()
        with self.assertRaises(NotImplementedError):
            ds.value_as_array('test')

        with self.assertRaises(NotImplementedError):
            ds.value_as_ndarray('test')

    def test_init(self) -> None:
        ds = FileSystemLogDatastore()