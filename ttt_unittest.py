import unittest
from tictactoe import *

class tttTest(unittest.TestCase):
    def test_insertLetter(self):
        results = spaceIsFree(1)
        self.assertFalse(results)

    # space is free method testing
    

if __name__ == '__main__':
    unittest.main() 
#zxczxczxc