#FA
#یک بازی ریاضی ساده است. دو عدد تصادفی بین ۱ تا ۹ و یک عملگر تصادفی (+، - یا *) انتخاب می‌کند و مثلاً
#این عدد 7 * 3 نشان می‌دهد کاربر جواب را وارد می‌کند. اگر درست بود ✅✅✅✅ و اگر غلط بود ❌❌❌❌ چاپ می‌شود.
#EN
#A simple math quiz. It picks two random numbers (1-9) and a random operator (+, -, *), shows
#something like 7 * 3, and asks for the answer. A correct answer prints ✅✅✅✅, a wrong one prints ❌❌❌❌.

import operator
import random

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def read_answer():
    while True:
        try:
            return int(input('  = '))
        except ValueError:
            print('  Please enter a whole number.')


def calculation():
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    symbol = random.choice(list(OPERATORS))

    print(a, symbol, b)
    answer = read_answer()

    if answer == OPERATORS[symbol](a, b):
        print('✅✅✅✅')
    else:
        print('❌❌❌❌')


calculation()