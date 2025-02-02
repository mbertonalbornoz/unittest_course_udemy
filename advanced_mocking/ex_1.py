import unittest
from unittest.mock import MagicMock, patch

from advanced_mocking.my_module import get_content


# Enter your solution here
class TestGetContent(unittest.TestCase):
    @patch('requests.get')
    def test_success(self, get_mock):
        # GIVEN
        url = 'https://fakeurl.com'
        mock_response = MagicMock(
                status_code= 200,
                content=b'This is a successful content.'
        )
        get_mock.return_value = mock_response

        # WHEN
        output = get_content(url)

        # THEN
        get_mock.assert_called_once_with(url)


    @patch('requests.get')
    def test_retry(self, get_mock):
        # GIVEN
        url = 'https://fakeurl.com'
        mock_response = MagicMock(
                status_code=401,
                content=b'Hello, world!'
            )
        get_mock.side_effect = [
            Exception,
            Exception,
            mock_response
        ]

        # WHEN
        output = get_content(url)

        # THEN
        self.assertEqual(3, get_mock.call_count)
        self.assertEqual(output, 'Hello, world!')

