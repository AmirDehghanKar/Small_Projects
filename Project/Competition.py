#FA
#یک مسابقه‌ی اسب‌دوانی متنی است. چهار اسب از صفر شروع می‌کنند و در هر دور هر کدام بین ۱ تا ۴ واحد جلو می‌روند.
#موقعیت هر اسب با فاصله‌ها و شکل |==|<- چاپ می‌شود و خط پایان با | نشان داده می‌شود. وقتی اسبی از ۲۷ رد شود، حلقه تمام می‌شود و برنده اعلام می‌شود.
#EN
#A text-based horse race. Four horses start at 0 and each advances 1-4 units per round. Each horse’s position is drawn with
#spaces and the |==|<- sprite, with | marking the finish line. When a horse passes 27, the loop ends and a winner is announced.

import random
import time

FINISH = 27
HORSE = "|==|->"


def draw(name, pos):
    pos = min(pos, FINISH)
    track = f"{pos}" + " " * (pos - 1) + HORSE
    track = track.ljust(FINISH)[:FINISH] + "|"
    return f"{name:<8} {track}"


def competition():
    horses = {f"Horse_{i}": 0 for i in range(1, 5)}

    while True:
        for name in horses:
            horses[name] += random.randint(1, 4)

        for name, pos in horses.items():
            print(draw(name, pos))
        print("\n" + "= " * 14 + "\n")

        leader = max(horses, key=horses.get)
        if horses[leader] >= FINISH:
            break
        time.sleep(0.4)

    print(f"Hurray, {leader.replace('_', ' ')} wins!!")


competition()

#  ______________
# < I'm horse... >
#  --------------
#         \   ^__^
#          \  (oo)\_______
#             (__)\       )\/\
#                 ||----w |
#                 ||     ||
