char_to_num = {
    'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Д': 5, 'Е': 6, 'Ё': 7, 'Ж': 8, 'З': 9, 'И': 10,
    'Й': 11, 'К': 12, 'Л': 13, 'М': 14, 'Н': 15, 'О': 16, 'П': 17, 'Р': 18, 'С': 19,
    'Т': 20, 'У': 21, 'Ф': 22, 'Х': 23, 'Ц': 24, 'Ч': 25, 'Ш': 26, 'Щ': 27, 'Ъ': 28,
    'Ы': 29, 'Ь': 30, 'Э': 31, 'Ю': 32, 'Я': 33, ' ': 34,
    '0': 35, '1': 36, '2': 37, '3': 38, '4': 39, '5': 40, '6': 41, '7': 42, '8': 43, '9': 44
}

num_to_char = {
    1: 'А', 2: 'Б', 3: 'В', 4: 'Г', 5: 'Д', 6: 'Е', 7: 'Ё', 8: 'Ж', 9: 'З', 10: 'И',
    11: 'Й', 12: 'К', 13: 'Л', 14: 'М', 15: 'Н', 16: 'О', 17: 'П', 18: 'Р', 19: 'С',
    20: 'Т', 21: 'У', 22: 'Ф', 23: 'Х', 24: 'Ц', 25: 'Ч', 26: 'Ш', 27: 'Щ', 28: 'Ъ',
    29: 'Ы', 30: 'Ь', 31: 'Э', 32: 'Ю', 33: 'Я', 34: ' ',
    35: '0', 36: '1', 37: '2', 38: '3', 39: '4', 40: '5', 41: '6', 42: '7', 43: '8', 44: '9'
}


def rsa_keys_algorithm(first_digit, second_digit):
    n = first_digit * second_digit
    fi = (first_digit-1) * (second_digit-1)
    e = 0
    for i in range(2, fi):
        if fi % i != 0:
            e = i
            break

    open_key = (e, n)

    d = 0

    for k in range(1, n):
        if (k * fi + 1)/e == (k * fi + 1)//e:
            d = (k * fi + 1)//e
            break

    close_key = (d, n)

    return open_key, close_key


def rsa_encoder(word, open_key):
    ciphergram = []

    for i in word:
        digit = char_to_num[i]
        ciphergram.append(pow(digit, open_key[0]) % open_key[1])

    return ciphergram


def rsa_decoder(ciphergram, close_key):
    word = []

    for i in ciphergram:
        word.append(num_to_char[((pow(i, close_key[0]) % close_key[1]) % 45)])

    return word


first_digit, second_digit = 7, 13
word = input("Введите слово на русском\n").upper()
op_key, cl_key = rsa_keys_algorithm(first_digit, second_digit)
ciphergram = rsa_encoder(word, op_key)
dec_word = rsa_decoder(ciphergram, cl_key)

print(ciphergram, dec_word)
