import unittest
from SMS_simulation import *


class MessageTest(unittest.TestCase):
    def test_markAsRead(self):
        sms = SMSMessage(False, "Hello", "0798653452")
        self.assertTrue(sms.MarkASRead("read", sms))

    def test_add_sms(self):
        sms = SMSMessage(False, "Hello", "0798653452")
        lst = []
        self.assertIn(sms, add_sms(lst, sms))

    def test_get_count(self):
        lst = []
        sms1 = SMSMessage(False, "Hello", "0798653452")
        sms2 = SMSMessage(False, "Hey there.", "0795456868")
        lst.append(sms1)
        lst.append(sms2)
        self.assertEqual(get_count(lst), len(lst))

    def test_get_message(self):
        sms = SMSMessage(False, "Hello", "0798653452")
        self.assertEqual(get_message(sms), "Hello")

    def test_get_unread_message_F(self):
        sms = SMSMessage(False, "How are you doing", "0798653452")
        self.assertEqual(get_unread_message(sms), "How are you doing")

    def test_get_unread_message_T(self):
        sms = SMSMessage(True, "He's here.", "0798653452")
        self.assertEqual(get_unread_message(sms), "")

    def test_remove(self):
        self.assertNotIn(self.SMS, remove(self.lst, self.SMS))


if __name__ == '__main__':
    unittest.main()
