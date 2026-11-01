#FA
#یک تولیدکننده‌ی رمز عبور تصادفی است. طول رمز را از کاربر می‌گیرد و به همان تعداد، کاراکتر تصادفی از میان
#حروف انگلیسی (بزرگ و کوچک)، ارقام و علائم نگارشی انتخاب می‌کند و رمز را چاپ می‌کند.
#EN
#A random password generator. It asks for a length, picks that many random characters from letters
#(upper and lower), digits, and punctuation, and prints the result.

import secrets
import string

MIN_LENGTH = 8


def read_length():
    while True:
        try:
            n = int(input(f'Enter password length (min {MIN_LENGTH}): '))
            if n >= MIN_LENGTH:
                return n
        except ValueError:
            pass
        print(f'Please enter a whole number >= {MIN_LENGTH}.')


def generate_password(length):
    groups = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        string.punctuation,
    ]
    all_chars = ''.join(groups)

    # one guaranteed character from each group, rest random
    chars = [secrets.choice(g) for g in groups]
    chars += [secrets.choice(all_chars) for _ in range(length - len(groups))]

    secrets.SystemRandom().shuffle(chars)
    return ''.join(chars)


def password_tool():
    length = read_length()
    print('Your password:', generate_password(length))


password_tool()