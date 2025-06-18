# Write a function that returns all prime numbers up to n. 

def prime_upto_n(n):
    primes = []
    for num in range(2, n + 1):       
        is_prime = True
        for i in range(2, int(num**0.5) + 1):  
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


n = int(input("Enter a number: "))
print("Prime numbers up to", n, ":", prime_upto_n(n))
