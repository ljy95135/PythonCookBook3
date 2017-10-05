import unittest

#  assertion
large = 1000
f = 1.0
string = "This is a string"

assert large > 100
assert isinstance(string, str)


# PyUnit
class ArithTest(unittest.TestCase):
    def runTest(self):
        self.failUnless(1 + 1 == 2, 'one plus one fails!')
        self.failIf(1 + 1 != 2, 'one plus one fails!')
        self.failUnlessEqual(1 + 1, 2, 'one plus one fails!')


def suite():
    s = unittest.TestSuite()
    s.addTest(ArithTest())
    return s


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
