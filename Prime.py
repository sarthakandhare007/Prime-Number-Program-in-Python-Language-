# Prime number check in Python

n = int(input("Enter a number: "))

# 0 and 1 are not prime numbers
if n <= 1:
    print(n, "is NOT a Prime number.")
else:
    is_prime = True
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n, "is a Prime number.")
    else:
        print(n, "is NOT a Prime number.")
