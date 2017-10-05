import coverage_learning_fun
import unittest


class TestAdd(unittest.TestCase):
    """
    Test the add function from the coverage_learning_fun library
    """

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = coverage_learning_fun.add(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = coverage_learning_fun.add(10.5, 2)
        self.assertEqual(result, 12.5)

    def test_add_strings(self):
        """
        Test the addition of two strings returns the two string as one
        concatenated string
        """
        result = coverage_learning_fun.add('abc', 'def')
        self.assertEqual(result, 'abcdef')


class TestSubtract(unittest.TestCase):
    """
    Test the subtract function from the coverage_learning_fun library
    """

    def test_subtract_integers(self):
        """
        Test that subtracting integers returns the correct result
        """
        result = coverage_learning_fun.subtract(10, 8)
        self.assertEqual(result, 2)


class TestMultiply(unittest.TestCase):
    """
    Test the multiply function from the coverage_learning_fun library
    """

    def test_subtract_integers(self):
        """
        Test that multiplying integers returns the correct result
        """
        result = coverage_learning_fun.multiply(5, 50)
        self.assertEqual(result, 250)


class TestDivide(unittest.TestCase):
    """
    Test the divide function from the coverage_learning_fun library
    """

    def test_divide_by_zero(self):
        """
        Test that multiplying integers returns the correct result
        """
        with self.assertRaises(ZeroDivisionError):
            coverage_learning_fun.divide(8, 0)


if __name__ == '__main__':
    unittest.main()
