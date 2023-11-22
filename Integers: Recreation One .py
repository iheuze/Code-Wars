def list_squared(m, n):
    def sum_of_squared_divisors(number):
        divisors_sum = 0
        for i in range(1, int(number**0.5) + 1):
            if number % i == 0:
                divisors_sum += i**2
                if i != number // i:
                    divisors_sum += (number // i)**2
        return divisors_sum

    result = []
    for num in range(m, n + 1):
        divisors_sum = sum_of_squared_divisors(num)
        sqrt_sum = int(divisors_sum**0.5)
        if sqrt_sum**2 == divisors_sum:
            result.append([num, divisors_sum])

    return result
