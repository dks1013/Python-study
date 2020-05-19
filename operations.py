#사칙연산
import unittest

def Add(a,b):
    return a+b

def Subtract(a,b):
    return a-b

def Multiple(a,b):
    return a*b

def Division(a,b):
    return a/b

class operation(unittest.TestCase):
    def test_operation(self):
        self.assertEqual(10, Add(7, 3))
        self.assertEqual(4, Subtract(7, 3))
        self.assertEqual(18, Multiple(6, 3))
        self.assertEqual(2, Division(6, 3))
        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(0, Division(6, 0))

unittest.main()
