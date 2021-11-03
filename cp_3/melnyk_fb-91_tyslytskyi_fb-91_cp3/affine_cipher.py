from math_operations import *
from Format_Text import text_format
import collections
import itertools

alphabet_str = 'абвгдежзийклмнопрстуфхцчшщьыэюя'
popular_birams = ["ст", "но", "то", "на", "ен"]
popular_letters = ["о", "е", "а"]
unpopular_letters = ["ф", "э", "щ"]

def read_from_file(file_name):
    with open(file_name) as file:
        text_str = file.read()
        file.close()
    return text_str

def write_to_file(my_str):
    file_to_write = open('result.txt', 'w')
    file_to_write.write(my_str)
    file_to_write.close()

def make_alphabet_dictionary(alphabet):
    alphabet_dict = {}
    i = 0;
    while (i < len(alphabet)):
        alphabet_dict[alphabet[i]] = i
        i = i+1
    return alphabet_dict

def make_alphabet_dictionary2(alphabet):
    alphabet_dict = {}
    i = 0;
    while (i < len(alphabet)):
        alphabet_dict[i] = alphabet[i]
        i = i+1
    return alphabet_dict

def make_bigrams_list(str, alphabet):
    my_list = []
    if len(str) % 2 == 1:
        str += "ь"
    i = 0
    while i < len(str) - 1:
        key = str[i] + str[i + 1]
        my_list.append(key)
        i = i + 2
    return my_list

def letter_frequency(str, alphabet):
    pair_letter_count = {}
    for letter in alphabet:
        pair_letter_count[letter] = 0
    for letter in str:
        pair_letter_count[letter] =  pair_letter_count[letter] + 1

    pair_letter_frequency = {}
    for letter in alphabet:
        pair_letter_frequency[letter] = round((pair_letter_count[letter])/len(str), 5)

    #print(pair_letter_frequency)
    return pair_letter_frequency

def bigram_frequency(str, alphabet, cross = True, en = True):
    pair_bigram_count = {}
    pair_bigram_frequency = {}
    for letter1 in alphabet:
        for letter2 in alphabet:
            dict_key = letter1 + letter2
            pair_bigram_count[dict_key] = 0

    if (cross == True):
        i = 0
        while i < len(str) - 1:
            key = str[i] + str[i+1]
            pair_bigram_count[key] = pair_bigram_count[key] + 1
            i = i + 1

        for key in pair_bigram_count.keys():
            pair_bigram_frequency[key] = round(pair_bigram_count[key]/(len(str)-1), 5)

    else:
        if len(str) % 2 == 1:
            str += "ъ"
        i = 0
        while i < len(str) - 1:
            key = str[i] + str[i+1]
            pair_bigram_count[key] = pair_bigram_count[key] + 1
            i = i + 2

        for key in pair_bigram_count.keys():
            pair_bigram_frequency[key] = round(pair_bigram_count[key]/(len(str)/2), 5)
    if en == True:
        print("Bigram frequency in encrypted text:")
        print(pair_bigram_frequency)
    return pair_bigram_frequency


def five_most_popular(bigram_frequency, bigram=True):
    sorted_values = sorted(bigram_frequency.values(), reverse=True)
    sorted_dict = {}
    for i in sorted_values:
        for j in bigram_frequency.keys():
            if bigram_frequency[j] == i:
                sorted_dict[j] = bigram_frequency[j]
    if bigram == True:
        print("Sorted bigram frequency in encrypted text:")
        print(sorted_dict)
    sorted_bigram_list = list(sorted_dict)
    i = 0
    most_popular_in_text = []
    while i < 5:
        most_popular_in_text.append(sorted_bigram_list[i])
        i = i+1
    if bigram==True:
        print("Most popular 5 bigram in text:")
        print(most_popular_in_text)
    return most_popular_in_text

def pairs_of_the_most_common(list):
    pairs = []
    for i in itertools.product(list, list):
        if i[0] != i[1]:
            pairs.append(i)
    for j in pairs:
        pairs.remove((j[1], j[0]))
    print("All possible pairs variants: ")
    print(pairs)
    return pairs

def pairs_numbers(list, alph_dict, state_pair=True):
    pairs_in_numbers = []
    if state_pair == True:
        for pair in list:
            x1 = alph_dict[pair[0][0]]*31+alph_dict[pair[0][1]]
            x2 = alph_dict[pair[1][0]]*31+alph_dict[pair[1][1]]
            pairs_in_numbers.append((x1,x2))
        print("All possible pairs variants in numbers: ")
        print(pairs_in_numbers)
    else:
        for i in list:
            x1 = alph_dict[i[0]] * 31 + alph_dict[i[1]]
            pairs_in_numbers.append(x1)
    return pairs_in_numbers

def find_pottential_key(pair_X, pair_Y):
    diff_X = int(pair_X[0]) - int(pair_X[1])
    diff_Y = int(pair_Y[0]) - int(pair_Y[1])
    a = modular_equation(diff_X, diff_Y, 31**2)
    if a == 'no solutions':
        return 0
    elif isinstance(a,int):
        b = (int(pair_Y[0]) - a * int(pair_X[0]))%31**2
        return a, b
    else:
        b = (int(pair_Y[0]) - a[0] * int(pair_X[0])) % 31 ** 2
        return a[0], b

def decrypt_bigrams(text, key, test=True):
    decrypt_text_dict = {}
    decrypt_str = ""
    if test==True:
        for i in key:
            if i != 0:
                for j in range (0, 3001):
                    if str(modulo_inverse(i[0], 31**2)) != "Can`t find a^(-1)":
                        x = int(modulo_inverse(i[0], 31**2)) * (text[j] - i[1]) % 31**2
                        x1 = x//31
                        x2 = x%31
                        decrypt_str += alph_number_2[x1] + alph_number_2[x2]
                        j = j+1
                decrypt_text_dict[i] = decrypt_str
                decrypt_str = ""
        #print(decrypt_text_dict)
        return decrypt_text_dict
    else:
        for j in range(0, len(text)):
                x = int(modulo_inverse(key[0], 31 ** 2)) * (text[j] - key[1]) % 31 ** 2
                x1 = x // 31
                x2 = x % 31
                decrypt_str += alph_number_2[x1] + alph_number_2[x2]
                j = j + 1
        write_to_file(decrypt_str)
        print("Decrypted text:")
        print(decrypt_str)

def find_correct_key(decrypt_text_dict):
    print("We try to find correct key...")
    keys_and_popular = {}
    keys_and_popular_big = {}
    for key in decrypt_text_dict.keys():
        if decrypt_text_dict[key] != '':
            freq = letter_frequency(decrypt_text_dict[key], alphabet_str)
            popular = five_most_popular(freq, False)
            if popular[0] in popular_letters and popular[1] in popular_letters and popular[2] in popular_letters:
                keys_and_popular[key] = popular
    print("Matching the frequency of letters")
    print(keys_and_popular)
    for key1 in keys_and_popular:
        bigram_freq = bigram_frequency(decrypt_text_dict[(key1)], alphabet_str, True, False)
        popular_big = five_most_popular(bigram_freq, False)
        if popular_big[0] in popular_birams and popular_big[1] in popular_birams and popular_big[2] in popular_birams:
            keys_and_popular_big[key1] = popular_big
    print("Matching the frequency of bigrams")
    print(keys_and_popular_big)
    return list(keys_and_popular_big.keys())[0]

text_format("12.txt", False)
str_text = read_from_file("format_text.txt")
bigram_frequency_dict = bigram_frequency(str_text, alphabet_str, False)
popular_5 = five_most_popular(bigram_frequency_dict)
lang_popular_5_pairs = pairs_of_the_most_common(popular_birams)
text_popular_5_pairs = pairs_of_the_most_common(popular_5)
alph_number = make_alphabet_dictionary(alphabet_str)
lang_popular_5_pairs_numbers = pairs_numbers(lang_popular_5_pairs, alph_number, True)
text_popular_5_pairs_numbers = pairs_numbers(text_popular_5_pairs, alph_number, True)
potentional_keys = []
for i in lang_popular_5_pairs_numbers:
    for j in text_popular_5_pairs_numbers:
        pot_key = find_pottential_key(i, j)
        potentional_keys.append(pot_key)
print("We find all potential keys for your text: ")
print(potentional_keys)
text_bigrams_list = make_bigrams_list(str_text, alphabet_str)
bigrams_in_numbers = pairs_numbers(text_bigrams_list, alph_number, False)
alph_number_2 = make_alphabet_dictionary2(alphabet_str)
dec_text = decrypt_bigrams(bigrams_in_numbers, potentional_keys)
key = find_correct_key(dec_text)
print(f"We found key for your text: {key}")
decrypt_bigrams(bigrams_in_numbers, key, False)
