"""
Advanced analysis examples for DQDA Algorithm
Demonstrates comprehensive number analysis and performance
"""

from dqda import DQDA
import time

def performance_demo():
    """Demonstrate algorithm performance"""
    dqda = DQDA()
    
    print("DQDA Algorithm - Advanced Analysis")
    print("=" * 50)
    
    # Test larger numbers with analysis
    test_cases = [
        1009,    # Prime (6k+1)
        1013,    # Prime (6k-1) 
        10000,   # Composite
        10007,   # Prime
        1000001, # Composite (101 × 9901)
        1000003  # Prime
    ]
    
    print("Comprehensive Number Analysis:")
    print("-" * 30)
    
    for number in test_cases:
        start_time = time.time()
        result = dqda.analyze(number)
        execution_time = (time.time() - start_time) * 1000  # Convert to milliseconds
        
        status = "Prime" if result['is_prime'] else "Composite"
        factors = result['factors'] if result['factors'] else "None"
        
        print(f"Number: {number}")
        print(f"Status: {status}")
        print(f"Form: {result['form']}")
        print(f"Attempts: {result['attempts']}")
        print(f"Factors: {factors}")
        print(f"Time: {execution_time:.3f} ms")
        print("-" * 30)

def batch_testing():
    """Demonstrate batch testing capabilities"""
    dqda = DQDA()
    
    print("\nBatch Testing Demonstration:")
    print("-" * 30)
    
    # Test a range of numbers
    start = 100
    end = 150
    
    primes_found = []
    
    for number in range(start, end + 1):
        if dqda.is_prime(number):
            primes_found.append(number)
    
    print(f"Primes between {start} and {end}:")
    print(primes_found)
    print(f"Total primes found: {len(primes_found)}")

if __name__ == "__main__":
    performance_demo()
    batch_testing()
