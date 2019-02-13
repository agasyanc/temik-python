import time
from random import randint
xp = 100
dam = 10
gold = 0
key = 0
while xp > 0:
    v = ['да', 'нет', 'не взять', 'взять', 'использовать']
    h = ['бежать', 'сражаться']
    r = ['направо', 'налево', 'вперёд', 'назад', 'вперед']
    print("Куда идти? Направо, налево, назад, вперёд?")
    
    j = 1
    while j == 1:
        a = input().lower()
        if a in r:
            print('Идем ' + a)
            j = 0
        else:
            print('Так куда идём?')
    s = randint(0,3)
    time.sleep(3)
    if s == 0:
        print("Ура это сокровищница!")
        gl = randint(1, 3)
        if gl == 1:
            time.sleep(1)
            print("Тут вопрос на сундуке")
            w = randint(1,10000)
            e = randint(1,10000)
            print(w,'+',e,'=?')
            p = input()
            try:
                var = int(p)
            except ValueError:
                var = 0
            if var == w + e:
                un = 1
                print('Правильно')
                sa = randint(1,6)
                qwe = 5
                while  qwe == 5:
                    if sa == 1:
                        print('Тут меч.Взять или нет?')
                        mech = randint(10, 30)
                        print('У него ', mech, ' урона')
                        da = input().lower()
                        if da == v[0] or da == v[2]:
                            dam = 0
                            dam = dam + mech
                            qwe = 1
                        elif da == v[1] or da == [3]:
                            print('Странно...Ну ладно.')
                            qwe = 1
                        else:
                            print('Что?')
                    elif sa == 2: 
                        print('Тут копьё.Взять или нет?')
                        kopio = randint(15, 25)
                        print('У него ', kopio, ' урона')
                        na = input().lower()
                        if na == v[0] or na == v[2]:
                            dam = 0
                            dam = dam + kopio
                            qwe = 1
                        elif na == v[1]:
                            print('Странно...Ну ладно.')
                            qwe = 1
                        else:
                            print('Что?')
                    elif sa == 3:
                        print('Тут секира.Взять или нет?')
                        sekir = randint(25, 30)
                        print('У неё ', sekir, ' урона')
                        ka = input().lower()
                        if ka == v[0] or ka == v[2]:
                            dam = 0
                            qwe = 1
                            dam = dam + sekir
                        elif ka == v[1]:
                            print('Странно...Ну ладно.')
                            qwe = 1
                        else:
                            print('Что?')
                    elif sa == 4:
                        print('Тут зелье здоровья. Взять или нет?')
                        zel = randint(10, 15)
                        print('Оно восстанавливает ', zel, ' жизней')
                        oi = input().lower()
                        if oi == v[0] or oi == v[2]:
                            qwe = 1
                            xp = xp + zel
                        elif oi == v[1]:
                            print('Странно...Ну ладно.')
                            qwe = 1
                        else:
                            print('Что?')
                    elif sa == 5:
                        print('Тут булова.Взять или нет?')
                        bul = randint(27, 33)
                        print('У него ', bul, ' урона')
                        tu = input().lower()
                        if tu == v[0] or tu == v[2]:
                            dam = 0
                            qwe = 1
                            dam = dam + bul
                        elif tu == v[1]:
                            print('Странно...Ну ладно.')
                            qwe = 1
                        else:
                            print('Что?')
                    elif sa == 6:
                        print('Тут зелье силы. Взять или нет?')
                        zela = randint(10, 15)
                        print('Оно усиливает на вас', zela)
                        ot = input().lower()
                        if ot == v[0] or ot == v[2]:
                            qwe = 1
                            dam = dam + zela
                        elif ot == v[1]:
                            print('Странно...Ну ладно.')
                            qwe = 1
                        else:
                            print('Что?')
            else:
                xp = xp - 30
                print('Не правильно')
                lo = randint(1,2)
                if lo == 1:
                    print('О нет, ловушка сработала!')
                    xp = xp - randint(10, 20)
        elif gl == 2:
            print('На сундуке замок')
            time.sleep(1)
            print('Тут нужен ключ')
            if key > 0:
                while  qwe == 5:
                    print('Хочешь использовать свой?')
                    input().lower()
                    if fi == v[0] or fi == v[4]:
                        qwe = 5
                        if sa == 1:
                            print('Тут меч.Взять или нет?')
                            mech = randint(10, 30)
                            print('У него ', mech, ' урона')
                            da = input().lower()
                            if da == v[0] or da == v[2]:
                                dam = 0
                                dam = dam + mech
                                qwe = 1
                            elif da == v[1] or da == [3]:
                                print('Странно...Ну ладно.')
                                qwe = 1
                            else:
                                print('Что?')
                        elif sa == 2: 
                            print('Тут копьё.Взять или нет?')
                            kopio = randint(15, 25)
                            print('У него ', kopio, ' урона')
                            na = input().lower()
                            if na == v[0] or na == v[2]:
                                dam = 0
                                dam = dam + kopio
                                qwe = 1
                            elif na == v[1]:
                                print('Странно...Ну ладно.')
                                qwe = 1
                            else:
                                print('Что?')
                        elif sa == 3:
                            print('Тут секира.Взять или нет?')
                            sekir = randint(25, 30)
                            print('У неё ', sekir, ' урона')
                            ka = input().lower()
                            if ka == v[0] or ka == v[2]:
                                dam = 0
                                qwe = 1
                                dam = dam + sekir
                            elif ka == v[1]:
                                print('Странно...Ну ладно.')
                                qwe = 1
                            else:
                                print('Что?')
                        elif sa == 4:
                            print('Тут зелье здоровья. Взять или нет?')
                            zel = randint(10, 15)
                            print('Оно восстанавливает ', zel, ' жизней')
                            oi = input().lower()
                            if oi == v[0] or oi == v[2]:
                                qwe = 1
                                xp = xp + zel
                            elif oi == v[1]:
                                print('Странно...Ну ладно.')
                                qwe = 1
                            else:
                                print('Что?')
                        elif sa == 5:
                            print('Тут булова.Взять или нет?')
                            bul = randint(27, 33)
                            print('У него ', bul, ' урона')
                            tu = input().lower()
                            if tu == v[0] or tu == v[2]:
                                dam = 0
                                qwe = 1
                                dam = dam + bul
                            elif tu == v[1]:
                                print('Странно...Ну ладно.')
                                qwe = 1
                            else:
                                print('Что?')
                        elif sa == 6:
                            print('Тут зелье силы. Взять или нет?')
                            zela = randint(10, 15)
                            print('Оно усиливает на вас', zela)
                            ot = input().lower()
                            if ot == v[0] or ot == v[2]:
                                qwe = 1
                                dam = dam + zela
                            elif ot == v[1]:
                                print('Странно...Ну ладно.')
                                qwe = 1
                            else:
                                print('Что?')
                else:
                    print('Что?')
                    
            else:    
                print('А у тебя его нет')
 
            
    elif s == 1:
        print("О, нет это монстр! Что делать?")
        time.sleep(1)
        hp = randint(1,50)
        at = randint(1,20)
        print('У него ',hp, 'сердец и ', at, 'урона')
        p = 3
        time.sleep(1)
        while xp > 0 and hp > 0 and p == 3:
            p = 3
            print ('Бежать или сражаться?')
            f = input().lower()
            if f == h[0] :
                print('Хорошооооо')
                p = 2
            elif f == h[1]:
                att = randint(at - 2, at + 2)
                damm = randint(dam - 2, dam + 2)
                xp = xp - att
                hp = hp - damm
                print('Ты нанёс = ', damm)
                print('Тебе нанесли = ', att)
                print('Здоровье = ', xp)
                print('Сердец у монстра = ', hp)
                time.sleep(1)
            else:
                print('Что???')
        qwe = 5
        if hp < 1:
            print('Ты убил монстра!')
            sa = randint(1,5)
            while  qwe == 5:
                if sa == 1:
                    print('Тут меч.Взять или нет?')
                    mech = randint(10, 30)
                    print('У него ', mech, ' урона')
                    da = input().lower()
                    if da == v[0] or da == v[2]:
                        dam = 0
                        dam = dam + mech
                        qwe = 1
                    elif da == v[1] or da == [3]:
                        print('Странно...Ну ладно.')
                        qwe = 1
                    else:
                        print('Что?')
                elif sa == 2: 
                    print('Тут копьё.Взять или нет?')
                    kopio = randint(15, 25)
                    print('У него ', kopio, ' урона')
                    na = input().lower()
                    if na == v[0] or na == v[2]:
                        dam = 0
                        dam = dam + kopio
                        qwe = 1
                    elif na == v[1]:
                        print('Странно...Ну ладно.')
                        qwe = 1
                    else:
                        print('Что?')
                elif sa == 3:
                    print('Тут секира.Взять или нет?')
                    sekir = randint(25, 30)
                    print('У неё ', sekir, ' урона')
                    ka = input().lower()
                    if ka == v[0] or ka == v[2]:
                        dam = 0
                        qwe = 1
                        dam = dam + sekir
                    elif ka == v[1]:
                        print('Странно...Ну ладно.')
                        qwe = 1
                    else:
                        print('Что?')
                elif sa == 4:
                    print('Тут зелье здоровья. Взять или нет?')
                    zel = randint(10, 15)
                    print('Оно восстанавливает ', zel, ' жизней')
                    ka = input().lower()
                    if ka == v[0] or na == v[2]:
                        qwe = 1
                        xp = xp + zel
                    elif ka == v[1]:
                        print('Странно...Ну ладно.')
                        qwe = 1
                    else:
                        print('Что?')
                elif sa == 5:
                    print('Тут ключ.Взять или нет?')
                    ke = randint(25, 30)
                    print('Он полезен')
                    ky = input().lower()
                    if ky == v[0] or ky == v[4]:
                        qwe = 1
                    elif ky == v[1]:
                        print('Странно...Ну ладно.')
                        qwe = 1
                    else:
                        print('Что?')
    elif s == 2:
        print('Здесь ловушки! Берегитесь!!!')
        zxc = randint(1,2)
        if zxc == 1: 
            xp = xp - 20
            print('Чёрт, задела!')
        else:
            print('Хух, пронесло!')
    else:
        print("Здесь ничено нет")
    print('Здоровье = ', xp)
    print('Твой урон = ', dam)
    time.sleep(1)
    if xp < 1:
        l = 3
        print('Ты проиграл')
