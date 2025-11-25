"""
Basic usage examples for DQDA Algorithm
Demonstrates simple primality testing functionality
"""

from dqda import DQDA

def main():
    print("DQDA Algorithm - Basic Usage Examples")
    print("=" * 40)
    
    # Initialize the algorithm
    dqda = DQDA()
    
    # Test basic numbers
    test_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    
    print("Basic Primality Tests:")
    print("-" * 20)
    
    for number in test_numbers:
        is_prime = dqda.is_prime(number)
        status = "Prime" if is_prime else "Composite"
        print(f"{number:3} → {status}")
    
    print("\n" + "=" * 40)
    print("Testing 6k±1 forms:")
    print("-" * 20)
    
    # Test numbers specifically of form 6k±1
    special_numbers = [97, 101, 103, 107, 109, 113]
    
    for number in special_numbers:
        is_prime = dqda.is_prime(number)
        form = "6k+1" if number % 6 == 1 else "6k-1"
        status = "Prime" if is_prime else "Composite"
        print(f"{number:3} ({form}) → {status}")

if __name__ == "__main__":
    main()
