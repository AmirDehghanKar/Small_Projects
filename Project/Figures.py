#FA
#از کاربر یک عدد (مثلاً 48271) می‌گیرد و بزرگ‌ترین و کوچک‌ترین رقم آن را چاپ می‌کند.
#برای 48271 خروجی می‌شود: بزرگ‌ترین 8 و کوچک‌ترین 1.
#EN
#It takes a number as input (e.g. 48271) and prints its largest and smallest digit. For 48271: max 8, min 1.

def figures():
    while True:
        num = input('Enter your number: ').strip()
        if num.isdigit():
            break
        print('Please enter a non-negative whole number.')

    print('Max digit:', max(num))
    print('Min digit:', min(num))


figures()