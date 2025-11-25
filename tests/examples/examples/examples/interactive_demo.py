"""
Interactive demo for DQDA Algorithm
Allows users to test numbers interactively
"""

from dqda import DQDA

def interactive_demo():
    """Interactive demonstration of DQDA algorithm"""
    dqda = DQDA()
    
    print("DQDA Algorithm - Interactive Demo")
    print("=" * 40)
    print("Enter numbers to test for primality")
    print("Type 'quit' or 'exit' to end the session")
    print("=" * 40)
    
    while True:
        try:
            user_input = input("\nEnter a number to test: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\nThank you for using DQDA Algorithm!")
                break
            
            number = int(user_input)
            
            # Perform comprehensive analysis
            result = dqda.analyze(number)
            
            print(f"\nResults for {number}:")
            print(f"  Status: {'Prime' if result['is_prime'] else 'Composite'}")
            print(f"  Form: {result['form']}")
            print(f"  Attempts: {result['attempts']}")
            
            if result['factors']:
                print(f"  Factors: {result['factors'][0]} × {result['factors'][1]}")
            else:
                print(f"  Factors: Prime number")
                
            print(f"  Execution time: {result['execution_time']:.6f} seconds")
            
        except ValueError:
            print("Please enter a valid integer")
        except KeyboardInterrupt:
            print("\n\nSession ended by user")
            break

if __name__ == "__main__":
    interactive_demo()
