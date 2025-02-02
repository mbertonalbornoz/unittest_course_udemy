import unittest
from unittest import mock
from email_client import EmailClient, EmailSender


# Enter your solution here
class TestEmailSender(unittest.TestCase):
    def test_send_emails(self):
        # GIVEN
        email_client_mock = mock.MagicMock(spec=EmailClient)

        recips = [
            'recip_1@abc.com',
            'recip_2@abc.com',
            'recip_3@abc.com',
        ]
        email_sender = EmailSender(email_client_mock)

        # WHEN
        email_sender.send_emails(recips, 'subject', 'body')

        # THEN
        self.assertEqual(3, email_client_mock.send_email.call_count)
        email_client_mock.send_email.assert_has_calls(
            [
                mock.call(
                    recips[0], 'subject', 'body'
                ),
                mock.call(
                    recips[1], 'subject', 'body'
                ),
                mock.call(
                    recips[2], 'subject', 'body'
                ),
            ]
        )