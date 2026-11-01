#FA
#یک شبیه‌ساز ساده‌ی نانوایی است منو سه نان نشان می‌دهد: تُست ، باگت  و لواش  کاربر با
#1، 2 یا 3 نان را انتخاب می‌کند، تعداد را وارد می‌کند و مبلغ کل نمایش داده می‌شود. بعد دو بار فرصت دارد رمز
#کارت (1382) را وارد کند. اگر درست بود «Successful transaction» چاپ می‌شود. با نوشتن Exit برنامه تمام می‌شود.
#EN
#A simple bakery simulator. The menu offers three breads: Toast (4000), Baguette (5000), Lavash
#(1500). The user picks 1, 2, or 3, enters a quantity, and sees the total. Then they get two attempts to
#enter the card password (1382). A correct password prints “Successful transaction”. Typing Exit quits.

BREADS = {
    '1': ('Toast', 4000),
    '2': ('Baguette', 5000),
    '3': ('Lavash', 1500),
}
PASSWORD = '1382'
MAX_TRIES = 2


def show_menu():
    print('Toast(1)  Baguette(2)  Lavash(3)  Exit')


def read_quantity():
    while True:
        try:
            qty = int(input('    Number of bread: '))
            if qty > 0:
                return qty
        except ValueError:
            pass
        print('    Please enter a valid positive number.')


def checkout(name, price):
    print('Hello!')
    qty = read_quantity()
    print(f'    Payment: {price * qty}')
    print('Loading Cart...')

    for _ in range(MAX_TRIES):
        if input('    Password: ') == PASSWORD:
            print('Successful transaction')
            break
        print('The password is incorrect')
    else:
        print('Transaction failed')

    print('Bye')


def bakery():
    show_menu()
    while True:
        choice = input('Enter the desired Bread: ').strip()
        if choice.lower() == 'exit':
            break
        if choice in BREADS:
            checkout(*BREADS[choice])
        else:
            show_menu()


bakery()