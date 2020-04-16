import random

my_HP = 15  # 자신의 HP
monster_HP = 8  # 몬스터 HP

index = 0  # 공격순서 : 자신이 먼저 한다고 가정
while monster_HP > 0 and my_HP > 0:  # 둘중 하나의 HP가 없어질 때 까지 반복

    attack = random.randint(1,7) # 피해 정도를 랜덤으로 발생
    if index %2 == 0:
        print("몬스터에게" + str(attack) + "의 피해를 입혔다.")
        monster_HP -= attack
    else:
        print("주인공에게" + str(attack) + "의 피해를 입혔다")
        my_HP -= attack
        
    index += 1

## while 문 빠져나옴

if my_HP > 0:  # 승자가 누구인지 판단
    print("몬스터를 격파함!")
else :
    print("주인공이 죽었다!")

    
