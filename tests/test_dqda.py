import unittest
from dqda import DQDA

class TestDQDAAlgorithm(unittest.TestCase):
    """
    Comprehensive test suite for DQDA Algorithm
    """
    
    def setUp(self):
        self.dqda = DQDA()
    
    def test_basic_primes(self):
        """Test basic prime numbers"""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for prime in primes:
            with self.subTest(prime=prime):
                self.assertTrue(self.dqda.is_prime(prime))
    
    def test_basic_composites(self):
        """Test basic composite numbers"""
        composites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
        for composite in composites:
            with self.subTest(composite=composite):
                self.assertFalse(self.dqda.is_prime(composite))
    
    def test_6k_plus_1_primes(self):
        """Test primes of form 6k+1"""
        primes_6k_plus_1 = [7, 13, 19, 31, 37, 43, 61, 67, 73, 79, 97]
        for prime in primes_6k_plus_1:
            with self.subTest(prime=prime):
                self.assertTrue(self.dqda.is_prime(prime))
    
    def test_6k_minus_1_primes(self):
        """Test primes of form 6k-1"""
        primes_6k_minus_1 = [5, 11, 17, 23, 29, 41, 47, 53, 59, 71, 83, 89]
        for prime in primes_6k_minus_1:
            with self.subTest(prime=prime):
                self.assertTrue(self.dqda.is_prime(prime))
    
    def test_large_primes(self):
        """Test larger prime numbers"""
        large_primes = [1009, 1013, 10007, 10009, 100003, 1000003]
        for prime in large_primes:
            with self.subTest(prime=prime):
                self.assertTrue(self.dqda.is_prime(prime))
    
    def test_composite_6k_plus_1(self):
        """Test composite numbers of form 6k+1"""
        composites = [25, 49, 55, 85, 91, 115, 121, 133, 145]
        for composite in composites:
            with self.subTest(composite=composite):
                self.assertFalse(self.dqda.is_prime(composite))
    
    def test_composite_6k_minus_1(self):
        """Test composite numbers of form 6k-1"""
        composites = [35, 65, 77, 95, 119, 125, 143, 155, 161]
        for composite in composites:
            with self.subTest(composite=composite):
                self.assertFalse(self.dqda.is_prime(composite))
    
    def test_analyze_method(self):
        """Test the comprehensive analysis method"""
        result = self.dqda.analyze(101)
        self.assertIsInstance(result, dict)
        self.assertIn('is_prime', result)
        self.assertIn('form', result)
        self.assertIn('attempts', result)
        self.assertTrue(result['is_prime'])
    
    def test_edge_cases(self):
        """Test edge cases and boundaries"""
        self.assertFalse(self.dqda.is_prime(1))
        self.assertFalse(self.dqda.is_prime(0))
        self.assertFalse(self.dqda.is_prime(-5))
        self.assertTrue(self.dqda.is_prime(2))
        self.assertTrue(self.dqda.is_prime(3))

if __name__ == '__main__':
    unittest.main()
