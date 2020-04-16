import random
print("나랑 숫자 맞히기 게임을 해 보자. :)")
UserName = input("이름을 입력하시오: ")
print("반가워" + UserName + "! 내가 1에서 30이하의 숫자를 하나 가지고 있어. 맞혀봐!")
print("단, 제한 횟수는 5번이야!")

flag = 1
count = 0
limit = 5
ComNum = random.randint(1, 31)
while flag == 1:
    PlayerNum = int(input("추측한 숫자는?"))
    limit -= 1
    count += 1
    if ComNum == PlayerNum:
        break
    elif ComNum > playerNum:
        print("추측한 숫자는 컴퓨터가 가지고 있는 숫자보다 작아요.")
    else :
        print("추측한 숫자는 컴퓨터가 가지고 있는 숫자보다 커요.")

    if limit == 0:
        flag = 0
        
if flag == 1:
    print(count, "번만에 맞혔어요. 축하해요~")

else:
    print("컴퓨터가 가지고 있는 수는 ", ComNum, "입니다.")
