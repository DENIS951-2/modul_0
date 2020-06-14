#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
from numpy import array
def game_core_v2(number):
      '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0 # счетчик попыток
    minim=0 # начало чисел
    maxim=101 # конец чисел
    predict = 0 # предполагаемое число
    while number!= predict: # бесконечный цикл
        predict=(minim+maxim)//2
        count+=1 # плюсуем попытку
        if number > predict:
            minim=predict
        elif number < predict:
            maxim=predict
    return(count) # выход из цикла, если угадали
def score_game(game_core_v2):
     '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls=[]
    np.random.seed(1) # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))  #Создаем список из 1000 чисел
    for num in random_array:
        count_ls.append(game_core_v2(num))
    score=int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score) # выход из цикла
score_game(game_core_v2) # Проверяем  


# In[ ]:




