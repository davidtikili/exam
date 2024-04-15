def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_pairs(limit):
    """Find and display prime number pairs with a difference of 2."""
    print("All pairs within input range:")
    for num in range(3, limit - 1):
        if is_prime(num) and is_prime(num + 2):
            print(num, num + 2)

# Input from the keyboard
limit = int(input("Enter a number less than 10000: "))

# Display prime number pairs
prime_pairs(limit)
 