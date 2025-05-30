def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
    
# Example usage:
if __name__ == "__main__":
    num = 0
    print(f"The factorial of {num} is {factorial(num)}")
    