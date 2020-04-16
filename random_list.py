##0~100까지 숫자로 랜덤한 리스트 만드는 함수를 작성하라
import random

list_num = []

for i in range(0, 101):
    list_num.append(random.randint(0, 101))

print (list_num)
