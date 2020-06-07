def random_pop(n):
    import random
    n_plus_1 = n + 1
    list_ran = []
    i = 0
    while i < n_plus_1:
        ran = random.randint(0, n)
        if ran in list_ran:
            continue
        else:
            print(ran)
            list_ran.append(ran)
            
#함수 실행
list1 = random_pop(int(input("n값을 입력하시오 : ")))


