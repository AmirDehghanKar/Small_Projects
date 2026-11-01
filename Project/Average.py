#FA
#این کد از کاربر عدد می‌گیرد تا زمانی که -1 وارد شود (نشانه‌ی پایان). در هر دور، عدد را به مجموع اضافه می‌کند
#و شمارنده را یکی زیاد می‌کند. در پایان، میانگین (مجموع ÷ تعداد) را چاپ می‌کند
#EN
#This program keeps asking the user for numbers until -1 is entered (the stop signal). Each time, it
#adds the number to a running total (Sum_N) and increments a counter (Count_N). At the end, it prints the average (total ÷ count).

def Average():

    Sum_N=0
    float(Sum_N)
    Count_N=0
    float(Count_N)
    Average_N=0
    float(Average_N)
    while True:
        Number=float(input('Enter your Number: '))
        if Number == -1:
            break
        Count_N = Count_N +1
        Sum_N = Number + Sum_N
    Average_N = Sum_N / Count_N
    print('Average: ',Average_N)

Average()