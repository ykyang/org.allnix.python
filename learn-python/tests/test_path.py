import unittest

from pathlib import Path
import shutil

class PathTest(unittest.TestCase):
    def test_path_exists(self) -> None:
        root: Path
        path: Path
        
        root = Path()
        self.assertTrue(root.exists())
        
        self.assertFalse(root.joinpath('not here').exists())
        
        path = root.joinpath('tests')
        self.assertTrue(path.exists())
    def test_rm_dir(self) -> None:
        """Test create and remove directory
        """
        root: Path = Path()
        path: Path
        
        path = root.joinpath("new test directory")
        # does not exist yet
        self.assertFalse(path.exists())
        for i in range(0,5):
            path.mkdir(parents=True)
            self.assertTrue(path.exists())
            shutil.rmtree(path, ignore_errors=True)
            self.assertFalse(path.exists())