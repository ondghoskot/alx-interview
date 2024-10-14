#!/usr/bin/python3
"""prime game"""


def sieve_of_eratosthenes(max_n):
    """Generate a list of prime numbers up to max_n
    using the sieve of Eratosthenes."""
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False
    return is_prime


def isWinner(x, nums):
    """Determine the winner of x rounds of the prime game."""
    if not nums or x < 1:
        return None

    max_n = max(nums)
    is_prime = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = 0
        for i in range(1, n + 1):
            if is_prime[i]:
                prime_count += 1

        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
