from math import gcd

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

def modular_equation(a, b, mod):
    d = gcd(a, mod)
    if d == 1:
        x = (modulo_inverse(a, mod)*b)%mod
        return x
    else:
        if (b%d != 0):
            return "no solutions"
        else:
            results = []
            x = modular_equation(int(a/d), int(b/d), int(mod/d))
            results.append(x)
            for i in range (1, d):
                results.append(x+int(mod/d)*i)
        return results