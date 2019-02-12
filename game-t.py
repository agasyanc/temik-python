import time
from random import randint
xp = 100
while xp > 0:
    h = ['бежать', 'сражаться']
    r = ['направо', 'налево', 'вперёд', 'назад']
    print("Куда идти? Направо, налево, назад, вперёд?")
    
    j = 1
    while j == 1:
        a = input().lower()
        if a in r:
            print('Идем ' + a)
            j = 0
        else:
            print('Так куда идём?')
            
    s = randint(0,2)
    time.sleep(3)
    if s == 0:
        print("Ура это сокровищница!")
        print("Тут вопрос")
        w = randint(1,10000)
        e = randint(1,10000)
        print(w,'+',e,'=?')
        p = input()
        if int(p) == w + e:
            xp = xp + 10
            print('Правильно')
        else:
            xp = xp - 30
            print('Не правильно')
    elif s == 1:
        print("О, нет это монстр! Что делать? Бежать или сражаться?")
        
        x = 1
        while x == 1:
            f = input().lower()
            if f == h[0] :
                print('Хорошооооо')
                x = 0
            elif f == h[1]:
                x =0
                q = randint(1,5)
                if q == 1:
                    xp = xp - 10
                    print('Ты победил')
                elif q == 2:
                    xp = xp - 20
                    print('Ты победил')
                elif q == 3:
                    xp = xp - 50
                    print('Ты победил')
                elif q == 4:
                    xp = xp - 100
                else:
                    xp = xp - 0
                    print('Ты победил')
            else:
                print('Что???')
    else:
        print("Здесь ничено нет")
    print('Здоровье = ', xp)
    if xp < 1:
        l = 3
        print('Ты проиграл')
