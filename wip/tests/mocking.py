from wip.tests.mymodule import rm

from unittest import mock
from unittest import TestCase


class RunTestCase(TestCase):

    @mock.patch('wip.tests.mymodule.os.path')
    @mock.patch('wip.tests.mymodule.os')
    def test_rm(self, mock_os, mock_path):
        # set up the mock
        mock_path.isfile.return_value = False

        rm("any path")

        # test that the remove call was not called
        self.assertFalse(mock_os.remove.called)

        # make the  file 'exist'
        mock_path.isfile.return_value = True

        rm("any path")

        mock_os.remove.assert_called_with("any path")


