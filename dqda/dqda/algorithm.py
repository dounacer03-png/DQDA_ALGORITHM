import math
import time
from typing import Tuple, Optional, Dict, Any

class DQDA:
    """
    Dou's Quadratic Distinctiveness Algorithm for deterministic primality testing.
    """
    
    def is_prime(self, n: int) -> bool:
        """
        Determine primality using DQDA algorithm.
        """
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
            
        if n % 6 not in (1, 5):
            return False
            
        return self._test_6k_plus_1(n) if n % 6 == 1 else self._test_6k_minus_1(n)
    
    def _test_6k_plus_1(self, n: int) -> bool:
        """Test numbers of form n = 6k + 1"""
        k = (n - 1) // 6
        start_r = max(1, k // 5 + 1)
        
        if k % 2 == 0:
            start_r = start_r if start_r % 2 == 0 else start_r + 1
            step = -2
        else:
            start_r = start_r if start_r % 2 == 1 else start_r + 1
            step = -2
        
        for r in range(start_r, 0, step):
            S = n + (3 * r) ** 2
            if self._is_perfect_square(S):
                m = math.isqrt(S)
                if (m - 3*r) * (m + 3*r) == n:
                    return False
        return True
    
    def _test_6k_minus_1(self, n: int) -> bool:
        """Test numbers of form n = 6k - 1"""
        k = (n + 1) // 6
        start_r = max(1, k // 5 + 1)
        
        if k % 2 == 0:
            start_r = start_r if start_r % 2 == 0 else start_r + 1
            step = -2
        else:
            start_r = start_r if start_r % 2 == 1 else start_r + 1
            step = -2
        
        for r in range(start_r, 0, step):
            S = (3 * r) ** 2 - n
            if S >= 0 and self._is_perfect_square(S):
                m = math.isqrt(S)
                if (3*r - m) * (3*r + m) == n:
                    return False
        return True
    
    def _is_perfect_square(self, n: int) -> bool:
        """Efficient perfect square check"""
        if n < 0:
            return False
        root = math.isqrt(n)
        return root * root == n
    
    def analyze(self, n: int) -> Dict[str, Any]:
        """
        Comprehensive analysis with detailed information.
        """
        start_time = time.time()
        
        result = {
            'number': n,
            'is_prime': None,
            'form': None,
            'factors': None,
            'attempts': 0,
            'execution_time': 0,
        }
        
        # Basic cases
        if n < 2:
            result.update({'is_prime': False, 'form': 'invalid'})
            return result
            
        if n in (2, 3):
            result.update({'is_prime': True, 'form': 'special prime'})
            return result
            
        if n % 2 == 0:
            result.update({
                'is_prime': False, 
                'form': 'even', 
                'factors': (2, n//2)
            })
            return result
            
        if n % 3 == 0:
            result.update({
                'is_prime': False, 
                'form': 'multiple of 3', 
                'factors': (3, n//3)
            })
            return result
            
        # Main algorithm analysis
        if n % 6 == 1:
            k = (n - 1) // 6
            result['form'] = f"6k+1 (k={k})"
            prime, factors, attempts = self._analyze_6k_plus_1_detailed(n)
        else:
            k = (n + 1) // 6
            result['form'] = f"6k-1 (k={k})"
            prime, factors, attempts = self._analyze_6k_minus_1_detailed(n)
        
        result.update({
            'is_prime': prime,
            'factors': factors,
            'attempts': attempts,
            'execution_time': time.time() - start_time
        })
        
        return result
    
    def _analyze_6k_plus_1_detailed(self, n: int):
        """Detailed analysis for 6k+1 numbers"""
        k = (n - 1) // 6
        start_r = max(1, k // 5 + 1)
        attempts = 0
        
        if k % 2 == 0:
            start_r = start_r if start_r % 2 == 0 else start_r + 1
            step = -2
        else:
            start_r = start_r if start_r % 2 == 1 else start_r + 1
            step = -2
        
        for r in range(start_r, 0, step):
            attempts += 1
            S = n + (3 * r) ** 2
            if self._is_perfect_square(S):
                m = math.isqrt(S)
                factor1, factor2 = m - 3 * r, m + 3 * r
                if factor1 > 1 and factor2 > 1 and factor1 * factor2 == n:
                    return False, (factor1, factor2), attempts
        
        return True, None, attempts
    
    def _analyze_6k_minus_1_detailed(self, n: int):
        """Detailed analysis for 6k-1 numbers"""
        k = (n + 1) // 6
        start_r = max(1, k // 5 + 1)
        attempts = 0
        
        if k % 2 == 0:
            start_r = start_r if start_r % 2 == 0 else start_r + 1
            step = -2
        else:
            start
