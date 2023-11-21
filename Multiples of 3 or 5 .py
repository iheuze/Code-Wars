def solution(number):
    if number < 0:
        return 0

    # Sum all multiples of 3 or 5 below the given number
    result = sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
    
    return result
