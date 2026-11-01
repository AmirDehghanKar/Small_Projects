#FA
#یک متن از کاربر می‌گیرد و حروف را برعکس می‌کند: حروف کوچک انگلیسی را بزرگ می‌کند و هر چیز دیگر
#(حروف بزرگ، ارقام، علائم) را می‌کند. مثلاً Hello World 1 می‌شود hELLO wORLD 1.
#EN
#It takes text from the user and swaps the letter case: lowercase English letters become uppercase,
#and everything else goes through lower(). For example, Hello World 1 becomes hELLO wORLD 1.

def swap_case():
    text = input('Enter your text: ')
    print(text.swapcase())


swap_case()