from inspect import isgenerator

def prime_generator(end):
    def prime_num(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for number in range(2, end+1):
        if prime_num(number):
            yield number


gen = prime_generator(1)
assert isgenerator(gen) == True
assert list(prime_generator(10)) == [2, 3, 5, 7]
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13]
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print('Ok')