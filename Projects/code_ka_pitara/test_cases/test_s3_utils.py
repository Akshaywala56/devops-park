# test_s3_utils.py
import unittest
from unittest.mock import patch
from s3_utils import list_files

class TestS3Utils(unittest.TestCase):
    @patch('s3_utils.s3')
    def test_list_files(self, mock_s3):
        mock_s3.list_objects_v2.return_value = {
            'Contents': [
                {'Key': 'folder/file1.txt'},
                {'Key': 'folder/file2.txt'}
            ]
        }

        result = list_files('my-bucket', 'folder/')
        self.assertEqual(result, ['folder/file1.txt', 'folder/file2.txt'])

if __name__ == '__main__':
    unittest.main()
