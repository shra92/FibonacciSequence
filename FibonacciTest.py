import Fibonacci
import unittest

class TestFibonacciFunctions(unittest.TestCase):

    def test_series_10(self):
        print('\nTest Series 10')
        wanted_result = [0,1,1,2,3,5,8,13,21,34]
        test_result = Fibonacci.getFibonacci(10)
        self.assertEqual(wanted_result,test_result)

    def test_series_negativeNumber(self):
        print('\nTest Series -1')
        wanted_result = print("Number must be greater than 0")
        test_result = Fibonacci.getFibonacci(-1)
        self.assertEqual(wanted_result,test_result)

    def test_series_nonInteger(self):
        print('\nTest Series nonInteger')
        wanted_result = print("Please enter a number greater than 0")
        test_result = Fibonacci.getFibonacci("a")
        self.assertEqual(wanted_result,test_result)

    def test_series_Zero(self):
        print('\nTest Series Zero')
        wanted_result = print("Number must be greater than 0")
        test_result = Fibonacci.getFibonacci(0)
        self.assertEqual(wanted_result,test_result)


unittest.main()

