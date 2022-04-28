import unittest
from add import add
class tst_add(unittest.TestCase):
    def addtst(self):
        self.assertEqual(add(2,4),6)
        self.assertEqual(add(5,6),11)
        self.assertEqual(add(3,-3),0)

unittest.main()        