import random
from math import gcd

def miller_rabin_test(k):
    s = 0
    d = int(k) - 1
    while ( d % 2 == 0 ):
        d = d // 2
        s = s + 1
    #print ("s=" + str(s) + " d=" + str(d))

    for i in range(3):
        x = random.randint(2, k - 1)
        #print(x)
        if gcd(x, k) != 1:
            #print("aaa")
            return False
        if horner_scheme(x, d, k) == 1 or horner_scheme(x, d, k) == k-1:
            continue
        else:
            for r in range(0, s):
                deg = d * (2 ** r)
                xr = horner_scheme(x, deg, k)
                if xr == 1:
                    return False
                elif xr == (k-1):
                    break
                if r == s-1:
                    return False
    return True


def horner_scheme(x, a, m):
    a_binary = str(bin(a)[2:])
    x_pow = 1
    counter = 0
    for i in a_binary:
        temp_x = (x ** int(i))
        x_pow = ((x_pow ** 2) * temp_x) %m
        counter += 1
    #print(x_pow)
    return x_pow

def generate_prime_numbers(number_len):
    prostoe = []

    while True:
        min_number = int('1' + '0' * number_len)
        max_number = int('1' + '0' * (number_len+1))
        example = random.randint(min_number, max_number)
        f = open('test_numbers.txt', 'a')
        if (example % 2 == 0):
            example = example + 1
        result = miller_rabin_test(example)
        if result == True:
            prostoe.append(example)
        else:
            false_result = "The number did not pass the simplicity test: " + str(example) + "\n"
            f.write(false_result)
        if len(prostoe) == 4:
            break

    f.close()
    prostoe.sort()

    return prostoe

def extended_euclid(a, b):
    if (a==0):
        return b,0,1

    gcd, x, y = extended_euclid(b % a, a)
    return gcd, y - (b//a) * x, x

def modulo_inverse(a, m):
    if (gcd(a,m) != 1):
        return "Can`t find a^(-1)"
    else:
        u = extended_euclid(a,m)[1]
        return u%m

#numbers = generate_prime_numbers(77)
#print(numbers)