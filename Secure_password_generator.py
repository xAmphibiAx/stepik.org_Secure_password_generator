from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

pwd_n = int(input('Сколько паролей нужно?\n'))
pwd_len = int(input('Какой длины парол, нужен?\n'))
pwd_digits = input('Включать ли цифры 0123456789? (y/n)\n').strip()
pwd_upper = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)\n').strip()
pwd_lower = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)\n').strip()
pwd_punctuation = input('Включать ли символы !#$%&*+-=?@^_? (y/n)\n').strip()
pwd_exceptions = input('Исключать ли неоднозначные символы "il1Lo0O"? (y/n)\n').strip()

if pwd_digits == 'y':
    chars += digits
if pwd_upper == 'y':
    chars += uppercase_letters
if pwd_lower == 'y':
    chars += lowercase_letters
if pwd_punctuation == 'y':
    chars += punctuation
if pwd_exceptions == 'y':
    for c in chars:
        if c in 'il1Lo0O':
            chars = chars.replace(c, '')


def generate_password(l, ch):
    pwd = ''
    for i in range(l):
        pwd += choice(ch)
    return pwd


for i in range(pwd_n):
    print(generate_password(pwd_len, chars))
