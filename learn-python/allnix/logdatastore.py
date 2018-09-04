import numpy as np
import array
from pathlib import Path
import sys
import io

class LogDatastore():
    cout: io.TextIOWrapper = sys.stdout
    cerr: io.TextIOWrapper = sys.stderr

    def __init__(self):
        pass
        #print(__class__)
        # self.cout: io.TextIOWrapper = sys.stdout
        # self.cerr: io.TextIOWrapper = sys.stderr

    def value_as_ndarray(self, path: str) -> np.ndarray:
        raise NotImplementedError()

    def value_as_array(self, path: str) -> array.array:
        raise NotImplementedError()

class FileSystemLogDatastore(LogDatastore):
    root: Path = None

    def __init__(self):
        super().__init__()
        #self.cout.write(str(__class__))

    def value_as_array(self, path: str) -> array.array:
        raise NotImplementedError()
