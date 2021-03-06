from wip.tests.mymodule import RemovalService

import os.path
import tempfile
import unittest


class RmTestCase(unittest.TestCase):

    temp_file_path = os.path.join(tempfile.gettempdir(), "tmp-testfile")

    def setUp(self):
        with open(self.temp_file_path, "wb") as f:
            f.write(bytes('Delete me!'.encode()))

    def test_rm(self):
        # remove the file
        reference = RemovalService
        reference.rm(self.temp_file_path)
        # test that it was actually removed
        self.assertFalse(os.path.isfile("tmp-testfile"))
