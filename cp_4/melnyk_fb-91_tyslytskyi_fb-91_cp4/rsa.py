import random
from math import gcd
from math_functions import *

def generate_RSA_key(numbers_list, param):
    if param == 'A':
        i = 0
    elif param == 'B':
        i = 2
    n = numbers_list[i] * numbers_list[i+1]
    fi = (numbers_list[i] - 1)*(numbers_list[i+1] - 1)
    while True:
        e = random.randint(2, fi-1)
        if gcd(e, fi) == 1:
            break

    d = modulo_inverse(e, fi)

    return (n, e, d)

def encrypt_message_RSA(M, e, n):
    C =horner_scheme(M, e, n)
    return C

def decrypt_message_RSA(C, d, n):
    M = horner_scheme(C, d, n)
    return M

def sign_message_RSA(M, d, n):
    S = horner_scheme(M, d, n)
    print(f"Signed message with S: {S}")
    return S

def sign_verification(M, S, e, n):
    M1 = horner_scheme(S, e, n)
    if M == M1:
        return "Verification state: True"
    else:
        return "Verification state: False"

def send_key(k, e1, n1, d, n):
    k1 = horner_scheme(k, e1, n1)
    S = horner_scheme(k, d, n)
    S1 = horner_scheme(S, e1, n1)
    return (k1, S1)

def receive_key(k1, S1, d1, n1):
    k = horner_scheme(k1, d1, n1)
    S = horner_scheme(S1, d1, n1)
    return (k, S)

def authentication_k(k, S, e, n):
    temp_k = horner_scheme(S, e, n)
    if k == temp_k:
        return "Verification state: True"
    else:
        return "Verification state: False"



#A = {'Name': "", 'n': "", 'e': "", 'd':"", 'n1': "", 'e1': ""}
numbers = generate_prime_numbers(77)
A_RSA_key = generate_RSA_key(numbers, 'A')
B_RSA_key = generate_RSA_key(numbers, 'B')
print("Generate RSA key for A abonent")
print(A_RSA_key)
print("Generate RSA key for B abonent")
print(B_RSA_key)

print("For abonent A: ")
M = random.randint(0, A_RSA_key[0]-1)
print(f"Plain text: {M}")
C = encrypt_message_RSA(M, A_RSA_key[1], A_RSA_key[0])
print(f"Encrypt string: {C}")
M_decrypt = decrypt_message_RSA(C, A_RSA_key[2], A_RSA_key[0])
print(f"Decrypt string: {M_decrypt}")
if M == M_decrypt:
    print("Decription state: True")
else:
    print("False")
S = sign_message_RSA(M, A_RSA_key[2], A_RSA_key[0])
verify = sign_verification(M, S, A_RSA_key[1], A_RSA_key[0])
print(verify)

print("For abonent B: ")
M1 = random.randint(0, B_RSA_key[0]-1)
print(f"Plain text: {M1}")
C1 = encrypt_message_RSA(M1, B_RSA_key[1], B_RSA_key[0])
print(f"Encrypt string: {C1}")
M1_decrypt = decrypt_message_RSA(C1, B_RSA_key[2], B_RSA_key[0])
print(f"Decrypt string: {M1_decrypt}")
if M1 == M1_decrypt:
    print("Decription state: True")
else:
    print("False")
S1 = sign_message_RSA(M1, B_RSA_key[2], B_RSA_key[0])
verify1 = sign_verification(M1, S1, B_RSA_key[1], B_RSA_key[0])
print(verify1)

k = random.randint(0, A_RSA_key[0])
print(f"A generated a secret value k: {k}")
A_message = send_key(k, B_RSA_key[1], B_RSA_key[0], A_RSA_key[2], A_RSA_key[0])
print(f"A formed a message (k1, S1): ({A_message[0]}, {A_message[1]})")
B_received = receive_key(A_message[0], A_message[1], B_RSA_key[2], B_RSA_key[0])
print(f"B received (k, S): ({B_received[0]}, {B_received[1]}")
verify_message = authentication_k(B_received[0], B_received[1], A_RSA_key[1], A_RSA_key[0])
print(verify_message)