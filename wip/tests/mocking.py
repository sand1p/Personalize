from wip.tests.mymodule import RemovalService, UploadService

from unittest import mock
from unittest import TestCase


class RemovalServiceTestCase(TestCase):

    @mock.patch('wip.tests.mymodule.os.path')
    @mock.patch('wip.tests.mymodule.os')
    def test_rm(self, mock_os, mock_path):

        # set up the mock
        reference = RemovalService
        mock_path.isfile.return_value = False

        reference.rm("any path")

        # test that the remove call was not called
        self.assertFalse(mock_os.remove.called)

        # make the  file 'exist'
        mock_path.isfile.return_value = True

        reference.rm("any path")

        mock_os.remove.assert_called_with("any path")


class UploadServiceTestCase(TestCase):
    @mock.patch.object(RemovalService, 'rm')
    def test_upload_complete(self, mock_rm):
        # build our dependencies
        removal_service = RemovalService()
        reference = UploadService(removal_service)
        # upload complete which in turn should call rm of removal service
        reference.upload_complete("my uploaded file")
        # check that it called the rm method of any removal service
        self.assertTrue(mock_rm.called)
        # check whether rm was called
        mock_rm.assert_called_with("my uploaded file")
        mock_rm.called
        removal_service.rm.called
        removal_service.rm.assert_called_with("my uploaded file")

