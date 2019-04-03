def is_prime(num):
    def expand_x_1(n):
        c = 1
        for i in range(n // 2 + 1):
            c = c * (n - i) // (i + 1)
            yield c

    if num <= 1:
        return False
    if num == 2:
        return True

    for i in expand_x_1(num):
        if i % num:
            return False
    return True


def Primes(num):
    if is_prime(num):
        return "true"
    else:
        return "false"


if __name__ == "__main__":
    print(Primes(1079))
