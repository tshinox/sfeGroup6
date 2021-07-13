import unittest
from sms_pycode import * 

class messageTest(unittest.TestCase):
    def test_markAsRead(self):
        sms = SMSMessage(False, "Hello", "0798653452")
        self.assertTrue(MarkASRead("read",sms))


if __name__ == '__main__':
    unittest.main()