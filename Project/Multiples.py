#FA
#این کد از میان اعداد لیست ، اعدادی را پیدا می‌کند که هم مضرب ۶ باشند
#و هم جایگاهشان (شمارنده‌ی ۱-مبنا) مضرب ۶ باشد، سپس آن‌ها را بدون تکرار و مرتب‌شده چاپ می‌کند
#EN
#This code identifies numbers from the list `nums` that are multiples of 6 and whose positions 
#(using 1-based indexing) are also multiples of 6; it then prints these numbers, sorted and with duplicates removed.

nums = [0,10,6,4,7,54,1,88,79,11,45,54,19,59,21,15,23,18]
counter = 1

arr = []
flag = False
for i in nums:
    if i % 6 == 0 and counter % 6 == 0:
        arr.append(i)
        flag = True
    counter += 1

if flag:
    arr.sort()
    # print("\n",arr,"\n")
    # arr =  # -> {} is empty dictionary
    for something in set(arr):
        print(something, end=" - ")

else:
    print("\nNothing")
