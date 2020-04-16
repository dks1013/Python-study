##0~n까지의 숫자가 중복없이 한번씩 랜덤하게 출력되는함수를 작성하라.

import random

n = int(input("n값을 입력하시오 :"))
n_plus_1 = n + 1
list_ran = []
i = 0

while i < n_plus_1:
    ran = random.randint(0, 10)
    if ran in list_ran:
        continue
    else:
        print(ran)
        list_ran.append(ran)
