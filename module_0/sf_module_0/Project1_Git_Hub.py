import numpy as np
def game_core_v2(number):
    count = 0
    predict = np.random.randint(1,100)
    start = 0
    stop = 100
    mid50 = 50
    mid25 = 25
    while number != predict:
        count+=1
        if number <= mid50 and  number > predict:
            predict = mid50
            mid50 -=1
        elif number <= mid50 and number < predict:
            predict = start
            start +=1
        elif number > mid50 and number > predict:
            predict=mid50
            mid50+=1
        elif number > mid50 and number < predict:
            predict=stop
            stop-=1
    return(count) # выход из цикла, если угадали
def score_game(game_core_v2):
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000)) 
    for number in random_array:
        count_ls.append(game_core_v2(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


score_game(game_core_v2)
