"""
Basic tests for simpledotfiles
"""
import os
import unittest

from os.path import join
from dots.utils import *

TEMP_DIR = "tmp"
TEMP_DIR_NESTED = os.path.join(TEMP_DIR, "tmp2")
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
TEST_FILES = ["foo.symlink", "bar.symlink", "foobar"]

# Test methods
def touch(fname, times = None):
    """
    Equivalent of unix touch
    Not race free
    """
    with file(fname, 'a'):
        os.utime(fname, times)


def _clean():
    """
    Clean up workpsace
    """
    import subprocess
    subprocess.call("rm -r %s > /dev/null 2>&1" % TEMP_DIR, shell=True)

class TestUtils(unittest.TestCase):
    """
    _collect_files
        Test link collection
    """
    def setUp(self):
        _clean()
        os.mkdir(TEMP_DIR)
        os.mkdir(TEMP_DIR_NESTED)

    def setupSymlinks(self):
        touch(join(TEMP_DIR, "foo.symlink"))
        touch(join(TEMP_DIR, "bar.symlink"))

    def test_symlinks(self):
        self.setupSymlinks()
        res = _collect_files("symlink")
        self.assertEquals(res, [('./tmp', ['bar.symlink', 'foo.symlink'])])

    def test_symlinks_with_nested_dirs(self):
        self.setupSymlinks()
        touch(join(TEMP_DIR_NESTED, "foo.symlink"))
        res = _collect_files("symlink")
        self.assertEquals(res, [('./tmp', ['bar.symlink', 'foo.symlink']),
            ('./tmp/tmp2', ['foo.symlink'])])

    def test_ignore_folder(self):
        self.setupSymlinks()
        res = _collect_files("symlink", ignore_dirs = [TEMP_DIR_NESTED])
        touch(join(TEMP_DIR_NESTED, "ignoreme.symlink"))
        self.assertEquals(res, [('./tmp', ['bar.symlink', 'foo.symlink'])])

    def tearDown(self):
        _clean()

@unittest.skip("todo")
class TestMain(unittest.TestCase):
    """
    Check everything else
    """
    def setUp(self):
        _clean()
        os.mkdir(TEMP_DIR)
        os.mkdir(TEMP_DIR_NESTED)
        touch(join(TEMP_DIR, "foo.symlink"))
        touch(join(TEMP_DIR, "bar.symlink"))
        touch(join(TEMP_DIR_NESTED, "ignoreme.symlink"))

    def test_main(self):
        res = _collect_files("symlink", ignore_dirs = [TEMP_DIR_NESTED])
        self.assertEquals(res, [('./tmp', ['bar.symlink', 'foo.symlink'])])

    def tearDown(self):
        _clean()

if __name__ == '__main__':
    unittest.main()
