from Format_Text import text_format
import random
import string

alphabet_str = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
popular_letter = 'оеаи'

def letter_frequency(str, alphabet):
    pair_letter_count = {}
    for letter in alphabet:
        pair_letter_count[letter] = 0
    for letter in str:
        pair_letter_count[letter] =  pair_letter_count[letter] + 1

    pair_letter_frequency = {}
    for letter in alphabet:
        pair_letter_frequency[letter] = round((pair_letter_count[letter])/len(str), 5)

    return pair_letter_frequency

def write_encrypt_to_file(my_str, key):
    file_name = f"file_key{len(key)}.txt"
    file_to_write = open(file_name, 'w')
    file_to_write.write(my_str)
    file_to_write.close()

def make_alphabet_dictionary(alphabet):
    alphabet_dict = {}
    i = 0;
    while (i < len(alphabet)):
        alphabet_dict[i] = alphabet[i]
        i = i+1
    return alphabet_dict

def read_from_file(file_name):
    with open(file_name) as file:
        text_str = file.read()
        file.close()
    return text_str

def generate_key(key_length):
    key = ""
    i = 0
    while(i < key_length):
        symbol = random.choice(alphabet_str)
        key += symbol
        i = i+1
    print(f"Genetate key with value: {key}")
    return key

def encrypt_function(text_str, key, alphabet_dict):
    i = 0
    encrypt_text = ""
    while (i < len(text_str)):
        encrypt_symbol = (ord(text_str[i]) + ord(key[i % len(key)])) % len(alphabet_str)
        encrypt_text += alphabet_dict[encrypt_symbol]
        i = i+1
    #print(encrypt_text)
    return(encrypt_text)

def encryption(key_len):
    key = generate_key(key_len)
    alphabet_dict = make_alphabet_dictionary(alphabet_str)
    encrypt_text = encrypt_function(my_text, key, alphabet_dict)
    write_encrypt_to_file(encrypt_text, key)
    print(f"Index for encrypted text with key length {key_len}: {count_index(alphabet_str, encrypt_text)}")

def make_blocks(text, block_len):
    text_in_blocks = []
    i = 0
    while (i < block_len):
        text_in_blocks.append(text[i])
        i = i+1
    for j in range(block_len, len(text)):
        text_in_blocks[j%block_len] += text[j]
        j = j+1
    return text_in_blocks

def count_index(alphabet_str, text):
    index_block = 0
    for letter in alphabet_str:
        sum = 0
        i = 0
        while (i < len(text)):
            if (letter == text[i]):
                sum = sum+1
            i = i+1
        index_block = index_block + sum * (sum-1)

    index_block = index_block/(len(text)*(len(text)-1))
    #print(index_block)
    return index_block

def key_analysis(text):
    print("Try to decrypt your text...")
    average_index = []
    for i in range (2, 32):
        indexes = []
        blocks = make_blocks(text, i)
        for block_number in blocks:
            indexes.append(count_index(alphabet_str, block_number))
        average = sum(indexes)/len(indexes)
        average_index.append(average)
        print(f"Index to block length {i}: {average}")



    potential_key_length = []

    for j in average_index:
        if (j > 0.05):
            potential_key_length.append(average_index.index(j) + 2)

    print(f"Potentional key length with period: {potential_key_length}")
    length_of_key = min(potential_key_length)
    print(f"We find key length: {length_of_key}")

    key = ""
    alphabet_dict = make_alphabet_dictionary(alphabet_str)
    blocks = make_blocks(text, length_of_key)
    for block_number in blocks:
        y_dict = letter_frequency(block_number, alphabet_str)
        y = max(y_dict, key=y_dict.get)
        key += alphabet_dict[find_key_value(y, popular_letter[0], alphabet_str)]

    print(f"Key: {key}")
    print("Modify key: чугунныенебеса")
    krack_key = "чугунныенебеса"
    return krack_key

def find_key_value(y, x, alphabet):
    letter = (alphabet.index(y) - alphabet.index(x))%len(alphabet)
    return letter

def decrypt_text(encrypted_text, key, alphapet_str):
    print(f"Try to decrypt text with key {key}...")
    alphabet_dict = make_alphabet_dictionary(alphapet_str)
    decrypted_str = ""
    i = 0
    while (i < len(encrypted_text)):
        decrypt_symbol = (ord(encrypted_text[i]) - ord(key[i % len(key)])) % len(alphabet_str)
        decrypted_str += alphabet_dict[decrypt_symbol]
        i = i+1

    file_to_write = open("decrypt_text.txt", 'w')
    file_to_write.write(decrypted_str)
    file_to_write.close()
    print("We decrypt your text!")

if __name__ == '__main__':
    text_format('text.txt', False)
    my_text = read_from_file("format_text.txt")
    print(f"Index of plain text: {count_index(alphabet_str, my_text)}")
    print("Encrypt file with key 2")
    encryption(2)
    print("File was encrypted")
    print("Encrypt file with key 3")
    encryption(3)
    print("File was encrypted")
    print("Encrypt file with key 4")
    encryption(4)
    print("File was encrypted")
    print("Encrypt file with key 5")
    encryption(5)
    print("File was encrypted")
    print("Encrypt file with key 15")
    encryption(15)
    print("File was encrypted")
    text_format('encrypt_text2.txt', False)
    text = read_from_file("format_text.txt")
    krack_key = key_analysis(text)
    decrypt_text(text, krack_key, alphabet_str)