cache = {}


def factorial(number):
    if number in cache:
        return cache[number]

    if number <= 2:
        return number
    else:
        fact = number*factorial(number-1)
        cache[number] = fact
        return fact


if __name__ == '__main__':
    res = factorial(100)
    1==1


