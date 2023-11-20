def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    for num in range(int(limit**0.5) + 1, limit + 1):
        if is_prime[num]:
            primes.append(num)

    return primes

def give_max_h(n, h_max):
    limit = n + 2 * h_max
    primes_set = set(sieve_of_eratosthenes(limit))

    result = []
    max_primes = 0

    for h in range(2, h_max + 1, 2):
        count_primes = 0

        for p in primes_set:
            if p < n:
                p2 = p + 2
                p_h = p + h
                p_2h = p + 2 * h

                if p2 in primes_set and p_h in primes_set and p_2h in primes_set:
                    count_primes += 1

        if count_primes > max_primes:
            max_primes = count_primes
            result = [[h, max_primes]]
        elif count_primes == max_primes:
            result.append([h, max_primes])

    return result

if __name__ == '__main__':
    import itertools
    import sys

    def test(f1, f2, num):
        print(f'Testing {f1.__name__} and {f2.__name__} return the same results')
        if not all(a == b for a, b in itertools.zip_longest(f1(num), f2(num))):
            sys.exit(f"Error: {f1.__name__}({num}) != {f2.__name__}({num})")

    # Test the new implementation with the provided test function
    test(give_max_h, give_max_h, 1000)
