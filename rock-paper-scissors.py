#-*- coding: utf-8 -*-
from random import randint
import time
v = ["Камень", "Ножницы", "Бумага"]
s1 = 0
s2 = 0
while s1 < 3 and s2 < 3:
    print('Камень - 1, ножницы - 2, бумага - 3')
    time.sleep(1)
    print('Камень...')
    time.sleep(1)
    print('...ножницы...')
    time.sleep(1)
    print('...бумага...')
    time.sleep(1)
    print('...раз...')
    time.sleep(1)
    print('...два...')
    time.sleep(1)
    print('...три!')
    time.sleep(1)
    p2 = randint(1, 3)
    p1 = input()
    q = str(p1)+str(p2)
    print('Я: ' + v[int(p1)-1])
    print('Противник:'+ v[p2-1])
    if  q == "12" or q == "23" or q == "31":
        s1 +=1
        print('Ты победил!!!')
    elif  q == "13" or q == "32" or q == "21":
        s2 +=1
        print('Комп победил!')
    else:
        print("Ничья")
    print(str(s1), str(s2))

    time.sleep(5)
