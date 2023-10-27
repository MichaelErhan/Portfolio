from PIL import Image, ImageDraw

im = Image.open('C:/Users/Михаил/OneDrive/Рабочий стол/shah/wood2.png')
draw = ImageDraw.Draw(im)


Black_peshka = Image.open('C:/Users/Михаил/OneDrive/Рабочий стол/shah/peshkaBlack.png')
im.paste(Black_peshka, (100,200), Black_peshka)
im.paste(Black_peshka, (200,200), Black_peshka)
im.paste(Black_peshka, (300,200), Black_peshka)
im.paste(Black_peshka, (400,200), Black_peshka)
im.paste(Black_peshka, (500,200), Black_peshka)
im.paste(Black_peshka, (600,200), Black_peshka)
im.paste(Black_peshka, (700,200), Black_peshka)
im.paste(Black_peshka, (800,200), Black_peshka)

Black_lagya = Image.open('C:/Users/Михаил/OneDrive/Рабочий стол/shah/ladyaBlack.png')
im.paste(Black_lagya, (100,100), Black_lagya)
boolBlack_ladya1 = bool
im.paste(Black_lagya, (800,100), Black_lagya)

Black_kony = Image.open('C:/Users/Михаил/OneDrive/Рабочий стол/shah/konyBlack.png')
im.paste(Black_kony, (200,100), Black_kony)
im.paste(Black_kony, (700,100), Black_kony)

Black_slon = Image.open('C:/Users/Михаил/OneDrive/Рабочий стол/shah/slonBlack.png')
im.paste(Black_slon, (300,100), Black_slon)
im.paste(Black_slon, (600,100), Black_slon)

Black_king = Image.open('C:/Users/Михаил/OneDrive/Рабочий стол/shah/kingBlack.png')
im.paste(Black_king, (500,100), Black_king)

Black_ferz = Image.open('C:/Users/Михаил/OneDrive/Рабочий стол/shah/ferzBlack.png')
im.paste(Black_ferz, (400,100), Black_ferz)


White_peshka = Image.open('C:/Users/Михаил/OneDrive/Рабочий стол/shah/peshkaWhite.png')
im.paste(White_peshka, (100,700), White_peshka)
im.paste(White_peshka, (200,700), White_peshka)
im.paste(White_peshka, (300,700), White_peshka)
im.paste(White_peshka, (400,700), White_peshka)
im.paste(White_peshka, (500,700), White_peshka)
im.paste(White_peshka, (600,700), White_peshka)
im.paste(White_peshka, (700,700), White_peshka)
im.paste(White_peshka, (800,700), White_peshka)

White_lagya = Image.open('C:/Users/Михаил/OneDrive/Рабочий стол/shah/ladyaWhite.png')
im.paste(White_lagya, (100,800), White_lagya)
im.paste(White_lagya, (800,800), White_lagya)

White_kony = Image.open('C:/Users/Михаил/OneDrive/Рабочий стол/shah/konyWhite.png')
im.paste(White_kony, (200,800), White_kony)
im.paste(White_kony, (700,800), White_kony)

White_slon = Image.open('C:/Users/Михаил/OneDrive/Рабочий стол/shah/slonWhite.png')
im.paste(White_slon, (300,800), White_slon)
im.paste(White_slon, (600,800), White_slon)

White_king = Image.open('C:/Users/Михаил/OneDrive/Рабочий стол/shah/kingWhite.png')
im.paste(White_king, (500,800), White_king)

White_ferz = Image.open('C:/Users/Михаил/OneDrive/Рабочий стол/shah/ferzWhite.png')
im.paste(White_ferz, (400,800), White_ferz)

w = Image.open('C:/Users/Михаил/OneDrive/Рабочий стол/shah/whitebox.png')


b = Image.open('C:/Users/Михаил/OneDrive/Рабочий стол/shah/blackbox.png')

im.show()

namefigure_pole = ""


playerName = input("\n" + "Введите имя первого игрока - ") # Назначение никнейма для игрока 1

playerName2 = input("\n" +  "Введите имя второго игрока - ") # Назначение никнейма для игрока 2

gameplace = ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR",
             "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP",
             "--", "--", "--", "--", "--", "--", "--", "--",
             "--", "--", "--", "--", "--", "--", "--", "--",
             "--", "--", "--", "--", "--", "--", "--", "--",
             "--", "--", "--", "--", "--", "--", "--", "--",
             "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP",
             "wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR",]


def gamePlay():

    print("\n", '                  Игровое Поле', "\n",
    gameplace[0: 8], "\n", gameplace[8: 16], "\n", gameplace[16: 24], "\n",
    gameplace[24: 32], "\n", gameplace[32: 40], "\n", gameplace[40: 48], "\n",
    gameplace[48: 56], "\n", gameplace[56: 64], "\n")

def Played():

    number_test = 0
    number_test1 = 0

    playerXB = input(playerName + ', ' + 'Введите координату от A до H X = ')
    playerY = input(playerName + ', ' + 'Введите координату от 1 до 8 Y = ')

    if playerXB == "A":
        number_test = 1
    elif playerXB == "B":
        number_test = 2
    elif playerXB == "C":
        number_test = 3
    elif playerXB == "D":
        number_test = 4
    elif playerXB == "E":
        number_test = 5
    elif playerXB == "F":
        number_test = 6
    elif playerXB == "G":
        number_test = 7
    elif playerXB == "H":
        number_test = 8

    playerX = int(number_test)

    if playerX == 0:
        print("\n" + "Попробуте еще раз!")
        Played()
    elif len(playerY) == 0:
        print("\n" + "Попробуте еще раз!")
        Played()

    # Перевод строки в Число
    intPlayerX = int(playerX)
    intPlayerY = int(playerY)

    intPlayerX2 = intPlayerX + 2
    intPlayerY2 = intPlayerY + 2

    strPlayerX = str(playerX)
    strPlayerY = str(playerY)

    # Ограничения для Игрока 1
    if intPlayerX > 8 or intPlayerY == 0:
        print(playerName + ', ' + 'Введите координаты (ОТ 1 ДО 8!)')
        return Played()
    elif intPlayerY > 8 or intPlayerX == 0:
        print(playerName + ', ' + 'Введите координаты (ОТ 1 ДО 8!)')
        return Played()
    elif strPlayerX == "":
        print(playerName + ', ' + 'Введите координаты (ОТ 1 ДО 8!)')
        return Played()
    elif strPlayerY == "":
        print(playerName + ', ' + 'Введите координаты (ОТ 1 ДО 8!)')
        return Played()

    # ВставитьТочкуИгрока1
    metka1 = intPlayerX * intPlayerY + ((8 - intPlayerX) * (intPlayerY - 1) - 1)

    metka12 = intPlayerX2 * intPlayerY2 + ((10 - intPlayerX2) * (intPlayerY2 - 1) - 1)

    metka100 = metka12 * 10


    metka_p_8 = metka1 + 8
    metka_m_8 = metka1 - 8

    metka_p_1 = metka1 + 1
    metka_m_1 = metka1 - 1




    print("\n" + "Координата - ", metka1)
    print("\n" + "Координата фигуры - ", metka100, intPlayerX2, intPlayerY2)
    print("\n" + "Координата фигуры2 - ", metka12)
    print("\n" + "Координата плюс 1 - ", metka_p_1)
    print("\n" + "Координата минус 1 - ", metka_m_1 ,"\n")
    print("\n" + "Координата плюс 8 - ", metka_p_8)
    print("\n" + "Координата минус 8 - ", metka_m_8 ,"\n")

    if gameplace[metka1] == "wR" and gameplace[metka1] != "bR" + "bN" + "bB" + "bQ" + "bK" + "bP":
        namefigure_pole = White_lagya
        pointID_name = "wR"
    elif gameplace[metka1] == "wN" and gameplace[metka1] != "bR" + "bN" + "bB" + "bQ" + "bK" + "bP":
        namefigure_pole = White_kony
        pointID_name = "wN"

    elif gameplace[metka1] == "wB" and gameplace[metka1] != "bR" + "bN" + "bB" + "bQ" + "bK" + "bP":
        namefigure_pole = White_slon
        pointID_name = "wB"

    elif gameplace[metka1] == "wQ" and gameplace[metka1] != "bR" + "bN" + "bB" + "bQ" + "bK" + "bP":
        namefigure_pole = White_king
        pointID_name = "wQ"

    elif gameplace[metka1] == "wK" and gameplace[metka1] != "bR" + "bN" + "bB" + "bQ" + "bK" + "bP":
        namefigure_pole = White_ferz
        pointID_name = "wK"

    elif gameplace[metka1] == "wP" and gameplace[metka1] != "bR" + "bN" + "bB" + "bQ" + "bK" + "bP":
        namefigure_pole = White_peshka
        pointID_name = "wP"

    else:
        print("\n"+"Вы выбрали фигуру опонента! Или фигура не была выбрана")
        print("\n"+"Ошибка! Попробуйте ещё раз!")
        Played()


    playerX2B = input(playerName + ', ' + 'Введите координату от A до H X = ')
    playerY2 = input(playerName + ', ' + 'Введите координату от 1 до 8 Y = ')


    if playerX2B == 0:
        print("\n" + "Попробуте еще раз!")
        Played()
    elif len(playerY2) == 0:
        print("\n" + "Попробуте еще раз!")
        Played()


    if playerX2B == "A":
        number_test1 = 1
    elif playerX2B == "B":
        number_test1 = 2
    elif playerX2B == "C":
        number_test1 = 3
    elif playerX2B == "D":
        number_test1 = 4
    elif playerX2B == "E":
        number_test1 = 5
    elif playerX2B == "F":
        number_test1 = 6
    elif playerX2B == "G":
        number_test1 = 7
    elif playerX2B == "H":
        number_test1 = 8

    playerX2 = int(number_test1)


    intPlayerX2 = int(playerX2)
    intPlayerY2 = int(playerY2)

    if intPlayerX2 > 8 or intPlayerY2 == 0:
        print(playerName + ', ' + 'Введите координаты (ОТ 1 ДО 8!)')
        return Played()
    elif intPlayerY2 > 8 or intPlayerX2 == 0:
        print(playerName + ', ' + 'Введите координаты (ОТ 1 ДО 8!)')
        return Played()
    elif intPlayerX2 == "":
        print(playerName + ', ' + 'Введите координаты (ОТ 1 ДО 8!)')
        return Played()
    elif intPlayerY2 == "":
        print(playerName + ', ' + 'Введите координаты (ОТ 1 ДО 8!)')
        return Played()

    metka2 = intPlayerX2 * intPlayerY2 + ((8 - intPlayerX2) * (intPlayerY2 - 1) - 1)
    print(metka2)

    metkaID = metka2

    print(metkaID)

    if metkaID == 0:
        x = 100
        y = 100
        namebox = w
    elif metkaID == 1:
        x = 200
        y = 100
        namebox = b
    elif metkaID == 2:
        x = 300
        y = 100
        namebox = w
    elif metkaID == 3:
        x = 400
        y = 100
        namebox = b
    elif metkaID == 4:
        x = 500
        y = 100
        namebox = w
    elif metkaID == 5:
        x = 600
        y = 100
        namebox = b
    elif metkaID == 6:
        x = 700
        y = 100
        namebox = w
    elif metkaID == 7:
        x = 800
        y = 100
        namebox = b
    elif metkaID == 8:
        x = 100
        y = 200
        namebox = b
    elif metkaID == 9:
        x = 200
        y = 200
        namebox = w
    elif metkaID == 10:
        x = 300
        y = 200
        namebox = b
    elif metkaID == 11:
        x = 400
        y = 200
        namebox = w
    elif metkaID == 12:
        x = 500
        y = 200
        namebox = b
    elif metkaID == 13:
        x = 600
        y = 200
        namebox = w
    elif metkaID == 14:
        x = 700
        y = 200
        namebox = b
    elif metkaID == 15:
        x = 800
        y = 200
        namebox = w
    elif metkaID == 16:
        x = 100
        y = 300
        namebox = w
    elif metkaID == 17:
        x = 200
        y = 300
        namebox = b
    elif metkaID == 18:
        x = 300
        y = 300
        namebox = w
    elif metkaID == 19:
        x = 400
        y = 300
        namebox = b
    elif metkaID == 20:
        x = 500
        y = 300
        namebox = w
    elif metkaID == 21:
        x = 600
        y = 300
        namebox = b
    elif metkaID == 22:
        x = 700
        y = 300
        namebox = w
    elif metkaID == 23:
        x = 800
        y = 300
        namebox = b
    elif metkaID == 24:
        x = 100
        y = 400
        namebox = b
    elif metkaID == 25:
        x = 200
        y = 400
        namebox = w
    elif metkaID == 26:
        x = 300
        y = 400
        namebox = b
    elif metkaID == 27:
        x = 400
        y = 400
        namebox = w
    elif metkaID == 28:
        x = 500
        y = 400
        namebox = b
    elif metkaID == 29:
        x = 600
        y = 400
        namebox = w
    elif metkaID == 30:
        x = 700
        y = 400
        namebox = b
    elif metkaID == 31:
        x = 800
        y = 400
        namebox = w
    elif metkaID == 32:
        x = 100
        y = 500
        namebox = w
    elif metkaID == 33:
        x = 200
        y = 500
        namebox = b
    elif metkaID == 34:
        x = 300
        y = 500
        namebox = w
    elif metkaID == 35:
        x = 400
        y = 500
        namebox = b
    elif metkaID == 36:
        x = 500
        y = 500
        namebox = w
    elif metkaID == 37:
        x = 600
        y = 500
        namebox = b
    elif metkaID == 38:
        x = 700
        y = 500
        namebox = w
    elif metkaID == 39:
        x = 800
        y = 500
        namebox = b
    elif metkaID == 40:
        x = 100
        y = 600
        namebox = b
    elif metkaID == 41:
        x = 200
        y = 600
        namebox = w
    elif metkaID == 42:
        x = 300
        y = 600
        namebox = b
    elif metkaID == 43:
        x = 400
        y = 600
        namebox = w
    elif metkaID == 44:
        x = 500
        y = 600
        namebox = b
    elif metkaID == 45:
        x = 600
        y = 600
        namebox = w
    elif metkaID == 46:
        x = 700
        y = 600
        namebox = b
    elif metkaID == 47:
        x = 800
        y = 600
        namebox = w
    elif metkaID == 48:
        x = 100
        y = 700
        namebox = w
    elif metkaID == 49:
        x = 200
        y = 700
        namebox = b
    elif metkaID == 50:
        x = 300
        y = 700
        namebox = w
    elif metkaID == 51:
        x = 400
        y = 700
        namebox = b
    elif metkaID == 52:
        x = 500
        y = 700
        namebox =  w
    elif metkaID == 53:
        x = 600
        y = 700
        namebox = b
    elif metkaID == 54:
        x = 700
        y = 700
        namebox = w
    elif metkaID == 55:
        x = 800
        y = 700
        namebox = b
    elif metkaID == 56:
        x = 100
        y = 800
        namebox = b
    elif metkaID == 57:
        x = 200
        y = 800
        namebox = w
    elif metkaID == 58:
        x = 300
        y = 800
        namebox = b
    elif metkaID == 59:
        x = 400
        y = 800
        namebox = w
    elif metkaID == 60:
        x = 500
        y = 800
        namebox = b
    elif metkaID == 61:
        x = 600
        y = 800
        namebox = w
    elif metkaID == 62:
        x = 700
        y = 800
        namebox = b
    elif metkaID == 63:
        x = 800
        y = 800
        namebox = w

    metkaadd = metka1

    if metkaadd == 0:
        x1 = 100
        y1 = 100
        namebox1 = w
    elif metkaadd == 1:
        x1 = 200
        y1 = 100
        namebox1 = b
    elif metkaadd == 2:
        x1 = 300
        y1 = 100
        namebox1 = w
    elif metkaadd == 3:
        x1 = 400
        y1 = 100
        namebox1 = b
    elif metkaadd == 4:
        x1 = 500
        y1 = 100
        namebox1 = w
    elif metkaadd == 5:
        x1 = 600
        y1 = 100
        namebox1 = b
    elif metkaadd == 6:
        x1 = 700
        y1 = 100
        namebox1 = w
    elif metkaadd == 7:
        x1 = 800
        y1 = 100
        namebox1 = b
    elif metkaadd == 8:
        x1 = 100
        y1 = 200
        namebox1 = b
    elif metkaadd == 9:
        x1 = 200
        y1 = 200
        namebox1 = w
    elif metkaadd == 10:
        x1 = 300
        y1 = 200
        namebox1 = b
    elif metkaadd == 11:
        x1 = 400
        y1 = 200
        namebox1 = w
    elif metkaadd == 12:
        x1 = 500
        y1 = 200
        namebox1 = b
    elif metkaadd == 13:
        x1 = 600
        y1 = 200
        namebox1 = w
    elif metkaadd == 14:
        x1 = 700
        y1 = 200
        namebox1 = b
    elif metkaadd == 15:
        x1 = 800
        y1 = 200
        namebox1 = w
    elif metkaadd == 16:
        x1 = 100
        y1 = 300
        namebox1 = w
    elif metkaadd == 17:
        x1 = 200
        y1 = 300
        namebox1 = b
    elif metkaadd == 18:
        x1 = 300
        y1 = 300
        namebox1 = w
    elif metkaadd == 19:
        x1 = 400
        y1 = 300
        namebox1 = b
    elif metkaadd == 20:
        x1 = 500
        y1 = 300
        namebox1 = w
    elif metkaadd == 21:
        x1 = 600
        y1 = 300
        namebox1 = b
    elif metkaadd == 22:
        x1 = 700
        y1 = 300
        namebox1 = w
    elif metkaadd == 23:
        x1 = 800
        y1 = 300
        namebox1 = b
    elif metkaadd == 24:
        x1 = 100
        y1 = 400
        namebox1 = b
    elif metkaadd == 25:
        x1 = 200
        y1 = 400
        namebox1 = w
    elif metkaadd == 26:
        x1 = 300
        y1 = 400
        namebox1 = b
    elif metkaadd == 27:
        x1 = 400
        y1 = 400
        namebox1 = w
    elif metkaadd == 28:
        x1 = 500
        y1 = 400
        namebox1 = b
    elif metkaadd == 29:
        x1 = 600
        y1 = 400
        namebox1 = w
    elif metkaadd == 30:
        x1 = 700
        y1 = 400
        namebox1 = b
    elif metkaadd == 31:
        x1 = 800
        y1 = 400
        namebox1 = w
    elif metkaadd == 32:
        x1 = 100
        y1 = 500
        namebox1 = w
    elif metkaadd == 33:
        x1 = 200
        y1 = 500
        namebox1 = b
    elif metkaadd == 34:
        x1 = 300
        y1 = 500
        namebox1 = w
    elif metkaadd == 35:
        x1 = 400
        y1 = 500
        namebox1 = b
    elif metkaadd == 36:
        x1 = 500
        y1 = 500
        namebox1 = w
    elif metkaadd == 37:
        x1 = 600
        y1 = 500
        namebox1 = b
    elif metkaadd == 38:
        x1 = 700
        y1 = 500
        namebox1 = w
    elif metkaadd == 39:
        x1 = 800
        y1 = 500
        namebox1 = b
    elif metkaadd == 40:
        x1 = 100
        y1 = 600
        namebox1 = b
    elif metkaadd == 41:
        x1 = 200
        y1 = 600
        namebox1 = w
    elif metkaadd == 42:
        x1 = 300
        y1 = 600
        namebox1 = b
    elif metkaadd == 43:
        x1 = 400
        y1 = 600
        namebox1 = w
    elif metkaadd == 44:
        x1 = 500
        y1 = 600
        namebox1 = b
    elif metkaadd == 45:
        x1 = 600
        y1 = 600
        namebox1 = w
    elif metkaadd == 46:
        x1 = 700
        y1 = 600
        namebox1 = b
    elif metkaadd == 47:
        x1 = 800
        y1 = 600
        namebox1 = w
    elif metkaadd == 48:
        x1 = 100
        y1 = 700
        namebox1 = w
    elif metkaadd == 49:
        x1 = 200
        y1 = 700
        namebox1 = b
    elif metkaadd == 50:
        x1 = 300
        y1 = 700
        namebox1 = w
    elif metkaadd == 51:
        x1 = 400
        y1 = 700
        namebox1 = b
    elif metkaadd == 52:
        x1 = 500
        y1 = 700
        namebox1 = w
    elif metkaadd == 53:
        x1 = 600
        y1 = 700
        namebox1 = b
    elif metkaadd == 54:
        x1 = 700
        y1 = 700
        namebox1 = w
    elif metkaadd == 55:
        x1 = 800
        y1 = 700
        namebox1 = b
    elif metkaadd == 56:
        x1 = 100
        y1 = 800
        namebox1 = b
    elif metkaadd == 57:
        x1 = 200
        y1 = 800
        namebox1 = w
    elif metkaadd == 58:
        x1 = 300
        y1 = 800
        namebox1 = b
    elif metkaadd == 59:
        x1 = 400
        y1 = 800
        namebox1 = w
    elif metkaadd == 60:
        x1 = 500
        y1 = 800
        namebox1 = b
    elif metkaadd == 61:
        x1 = 600
        y1 = 800
        namebox1 = w
    elif metkaadd == 62:
        x1 = 700
        y1 = 800
        namebox1 = b
    elif metkaadd == 63:
        x1 = 800
        y1 = 800
        namebox1 = w

    if gameplace[metka2] == "bR" or "bN" or "bB" or "bQ" or "bK" or "bP" or '--':
        if metka1 == metkaadd:
            im.paste(namebox1, (x1, y1), namebox1)
        if metka2 == metkaID:
            im.paste(namebox, (x, y), namebox)
            im.paste(namefigure_pole, (x, y), namefigure_pole)
            im.show()
        gameplace[metka1] = "--"
        gameplace[metka2] = pointID_name
        print("\n", '                  Игровое Поле', "\n",
              gameplace[0: 8], "\n", gameplace[8: 16], "\n", gameplace[16: 24], "\n",
              gameplace[24: 32], "\n", gameplace[32: 40], "\n", gameplace[40: 48], "\n",
              gameplace[48: 56], "\n", gameplace[56: 64], "\n")
        Played2()

    if gameplace[metka2] == "wR" or "wN" or "wB" or "wQ" or "wK" or "wP":
        print("Ошибка!!! Не стреляй в своих!")
        Played()




def Played2():

    number_test = 0
    number_test1 = 0

    playerXB = input(playerName2 + ', ' + 'Введите координату от A до H X = ')
    playerY = input(playerName2 + ', ' + 'Введите координату от 1 до 8 Y = ')

    if playerXB == "A":
        number_test = 1
    elif playerXB == "B":
        number_test = 2
    elif playerXB == "C":
        number_test = 3
    elif playerXB == "D":
        number_test = 4
    elif playerXB == "E":
        number_test = 5
    elif playerXB == "F":
        number_test = 6
    elif playerXB == "G":
        number_test = 7
    elif playerXB == "H":
        number_test = 8

    playerX = int(number_test)

    if playerX == 0:
        print("\n" + "Попробуте еще раз!")
        Played()
    elif len(playerY) == 0:
        print("\n" + "Попробуте еще раз!")
        Played()

    # Перевод строки в Число
    intPlayerX = int(playerX)
    intPlayerY = int(playerY)

    strPlayerX = str(playerX)
    strPlayerY = str(playerY)

    # Ограничения для Игрока 1
    if intPlayerX > 8 or intPlayerY == 0:
        print(playerName2 + ', ' + 'Введите координаты (ОТ 1 ДО 8!)')
        return Played2()
    elif intPlayerY > 8 or intPlayerX == 0:
        print(playerName2 + ', ' + 'Введите координаты (ОТ 1 ДО 8!)')
        return Played2()
    elif strPlayerX == "":
        print(playerName2 + ', ' + 'Введите координаты (ОТ 1 ДО 8!)')
        return Played2()
    elif strPlayerY == "":
        print(playerName2 + ', ' + 'Введите координаты (ОТ 1 ДО 8!)')
        return Played2()

    # ВставитьТочкуИгрока1
    metka1 = intPlayerX * intPlayerY + ((8 - intPlayerX) * (intPlayerY - 1) - 1)



    metkafiguri_X = (metka1 + 2) * 10



    metka_p_8 = metka1 + 8
    metka_m_8 = metka1 - 8

    metka_p_1 = metka1 + 1
    metka_m_1 = metka1 - 1

    print("\n" + "Координата - ", metka1)
    print("\n" + "Координата фигуры - ", metkafiguri_X)
    print("\n" + "Координата плюс 1 - ", metka_p_1)
    print("\n" + "Координата минус 1 - ", metka_m_1 ,"\n")
    print("\n" + "Координата плюс 8 - ", metka_p_8)
    print("\n" + "Координата минус 8 - ", metka_m_8 ,"\n")

    if gameplace[metka1] == "bR" and gameplace[metka1] != "wR" + "wN" + "wB" + "wQ" + "wK" + "wP":
        namefigure_pole = Black_lagya
        pointID_name = "bR"

    elif gameplace[metka1] == "bN" and gameplace[metka1] != "wR" + "wN" + "wB" + "wQ" + "wK" + "wP":
        namefigure_pole = Black_kony
        pointID_name = "bN"

    elif gameplace[metka1] == "bB" and gameplace[metka1] != "wR" + "wN" + "wB" + "wQ" + "wK" + "wP":
        namefigure_pole = Black_slon
        pointID_name = "bB"

    elif gameplace[metka1] == "bQ" and gameplace[metka1] != "wR" + "wN" + "wB" + "wQ" + "wK" + "wP":
        namefigure_pole = Black_ferz
        pointID_name = "bQ"

    elif gameplace[metka1] == "bK" and gameplace[metka1] != "wR" + "wN" + "wB" + "wQ" + "wK" + "wP":
        namefigure_pole = Black_king
        pointID_name = "bK"

    elif gameplace[metka1] == "bP" and gameplace[metka1] != "wR" + "wN" + "wB" + "wQ" + "wK" + "wP":
        namefigure_pole = Black_peshka
        pointID_name = "bP"

    else:
        print("\n"+"Вы выбрали фигуру опонента! Или фигура не была выбрана")
        print("\n"+"Ошибка! Попробуйте ещё раз!")
        Played2()

    playerX2B = input(playerName2 + ', ' + 'Введите координату от A до H X = ')
    playerY2 = input(playerName2 + ', ' + 'Введите координату от 1 до 8 Y = ')


    if playerX2B == 0:
        print("\n" + "Попробуте еще раз!")
        Played2()
    elif len(playerY2) == 0:
        print("\n" + "Попробуте еще раз!")
        Played2()


    if playerX2B == "A":
        number_test1 = 1
    elif playerX2B == "B":
        number_test1 = 2
    elif playerX2B == "C":
        number_test1 = 3
    elif playerX2B == "D":
        number_test1 = 4
    elif playerX2B == "E":
        number_test1 = 5
    elif playerX2B == "F":
        number_test1 = 6
    elif playerX2B == "G":
        number_test1 = 7
    elif playerX2B == "H":
        number_test1 = 8

    playerX2 = int(number_test1)



    intPlayerX2 = int(playerX2)
    intPlayerY2 = int(playerY2)

    if intPlayerX2 > 8 or intPlayerY2 == 0:
        print(playerName2 + ', ' + 'Введите координаты (ОТ 1 ДО 8!)')
        return Played2()
    elif intPlayerY2 > 8 or intPlayerX2 == 0:
        print(playerName2 + ', ' + 'Введите координаты (ОТ 1 ДО 8!)')
        return Played2()
    elif intPlayerX2 == "":
        print(playerName2 + ', ' + 'Введите координаты (ОТ 1 ДО 8!)')
        return Played2()
    elif intPlayerY2 == "":
        print(playerName2 + ', ' + 'Введите координаты (ОТ 1 ДО 8!)')
        return Played2()

    metka2 = intPlayerX2 * intPlayerY2 + ((8 - intPlayerX2) * (intPlayerY2 - 1) - 1)

    print(metka2)

    metkaID = metka2

    print(metkaID)

    if metkaID == 0:
        x = 100
        y = 100
        namebox = w
    elif metkaID == 1:
        x = 200
        y = 100
        namebox = b
    elif metkaID == 2:
        x = 300
        y = 100
        namebox = w
    elif metkaID == 3:
        x = 400
        y = 100
        namebox = b
    elif metkaID == 4:
        x = 500
        y = 100
        namebox = w
    elif metkaID == 5:
        x = 600
        y = 100
        namebox = b
    elif metkaID == 6:
        x = 700
        y = 100
        namebox = w
    elif metkaID == 7:
        x = 800
        y = 100
        namebox = b
    elif metkaID == 8:
        x = 100
        y = 200
        namebox = b
    elif metkaID == 9:
        x = 200
        y = 200
        namebox = w
    elif metkaID == 10:
        x = 300
        y = 200
        namebox = b
    elif metkaID == 11:
        x = 400
        y = 200
        namebox = w
    elif metkaID == 12:
        x = 500
        y = 200
        namebox = b
    elif metkaID == 13:
        x = 600
        y = 200
        namebox = w
    elif metkaID == 14:
        x = 700
        y = 200
        namebox = b
    elif metkaID == 15:
        x = 800
        y = 200
        namebox = w
    elif metkaID == 16:
        x = 100
        y = 300
        namebox = w
    elif metkaID == 17:
        x = 200
        y = 300
        namebox = b
    elif metkaID == 18:
        x = 300
        y = 300
        namebox = w
    elif metkaID == 19:
        x = 400
        y = 300
        namebox = b
    elif metkaID == 20:
        x = 500
        y = 300
        namebox = w
    elif metkaID == 21:
        x = 600
        y = 300
        namebox = b
    elif metkaID == 22:
        x = 700
        y = 300
        namebox = w
    elif metkaID == 23:
        x = 800
        y = 300
        namebox = b
    elif metkaID == 24:
        x = 100
        y = 400
        namebox = b
    elif metkaID == 25:
        x = 200
        y = 400
        namebox = w
    elif metkaID == 26:
        x = 300
        y = 400
        namebox = b
    elif metkaID == 27:
        x = 400
        y = 400
        namebox = w
    elif metkaID == 28:
        x = 500
        y = 400
        namebox = b
    elif metkaID == 29:
        x = 600
        y = 400
        namebox = w
    elif metkaID == 30:
        x = 700
        y = 400
        namebox = b
    elif metkaID == 31:
        x = 800
        y = 400
        namebox = w
    elif metkaID == 32:
        x = 100
        y = 500
        namebox = w
    elif metkaID == 33:
        x = 200
        y = 500
        namebox = b
    elif metkaID == 34:
        x = 300
        y = 500
        namebox = w
    elif metkaID == 35:
        x = 400
        y = 500
        namebox = b
    elif metkaID == 36:
        x = 500
        y = 500
        namebox = w
    elif metkaID == 37:
        x = 600
        y = 500
        namebox = b
    elif metkaID == 38:
        x = 700
        y = 500
        namebox = w
    elif metkaID == 39:
        x = 800
        y = 500
        namebox = b
    elif metkaID == 40:
        x = 100
        y = 600
        namebox = b
    elif metkaID == 41:
        x = 200
        y = 600
        namebox = w
    elif metkaID == 42:
        x = 300
        y = 600
        namebox = b
    elif metkaID == 43:
        x = 400
        y = 600
        namebox = w
    elif metkaID == 44:
        x = 500
        y = 600
        namebox = b
    elif metkaID == 45:
        x = 600
        y = 600
        namebox = w
    elif metkaID == 46:
        x = 700
        y = 600
        namebox = b
    elif metkaID == 47:
        x = 800
        y = 600
        namebox = w
    elif metkaID == 48:
        x = 100
        y = 700
        namebox = w
    elif metkaID == 49:
        x = 200
        y = 700
        namebox = b
    elif metkaID == 50:
        x = 300
        y = 700
        namebox = w
    elif metkaID == 51:
        x = 400
        y = 700
        namebox = b
    elif metkaID == 52:
        x = 500
        y = 700
        namebox = w
    elif metkaID == 53:
        x = 600
        y = 700
        namebox = b
    elif metkaID == 54:
        x = 700
        y = 700
        namebox = w
    elif metkaID == 55:
        x = 800
        y = 700
        namebox = b
    elif metkaID == 56:
        x = 100
        y = 800
        namebox = b
    elif metkaID == 57:
        x = 200
        y = 800
        namebox = w
    elif metkaID == 58:
        x = 300
        y = 800
        namebox = b
    elif metkaID == 59:
        x = 400
        y = 800
        namebox = w
    elif metkaID == 60:
        x = 500
        y = 800
        namebox = b
    elif metkaID == 61:
        x = 600
        y = 800
        namebox = w
    elif metkaID == 62:
        x = 700
        y = 800
        namebox = b
    elif metkaID == 63:
        x = 800
        y = 800
        namebox = w


    metkaadd = metka1

    if metkaadd == 0:
        x1 = 100
        y1 = 100
        namebox1 = w
    elif metkaadd == 1:
        x1 = 200
        y1 = 100
        namebox1 = b
    elif metkaadd == 2:
        x1 = 300
        y1 = 100
        namebox1 = w
    elif metkaadd == 3:
        x1 = 400
        y1 = 100
        namebox1 = b
    elif metkaadd == 4:
        x1 = 500
        y1 = 100
        namebox1 = w
    elif metkaadd == 5:
        x1 = 600
        y1 = 100
        namebox1 = b
    elif metkaadd == 6:
        x1 = 700
        y1 = 100
        namebox1 = w
    elif metkaadd == 7:
        x1 = 800
        y1 = 100
        namebox1 = b
    elif metkaadd == 8:
        x1 = 100
        y1 = 200
        namebox1 = b
    elif metkaadd == 9:
        x1 = 200
        y1 = 200
        namebox1 = w
    elif metkaadd == 10:
        x1 = 300
        y1 = 200
        namebox1 = b
    elif metkaadd == 11:
        x1 = 400
        y1 = 200
        namebox1 = w
    elif metkaadd == 12:
        x1 = 500
        y1 = 200
        namebox1 = b
    elif metkaadd == 13:
        x1 = 600
        y1 = 200
        namebox1 = w
    elif metkaadd == 14:
        x1 = 700
        y1 = 200
        namebox1 = b
    elif metkaadd == 15:
        x1 = 800
        y1 = 200
        namebox1 = w
    elif metkaadd == 16:
        x1 = 100
        y1 = 300
        namebox1 = w
    elif metkaadd == 17:
        x1 = 200
        y1 = 300
        namebox1 = b
    elif metkaadd == 18:
        x1 = 300
        y1 = 300
        namebox1 = w
    elif metkaadd == 19:
        x1 = 400
        y1 = 300
        namebox1 = b
    elif metkaadd == 20:
        x1 = 500
        y1 = 300
        namebox1 = w
    elif metkaadd == 21:
        x1 = 600
        y1 = 300
        namebox1 = b
    elif metkaadd == 22:
        x1 = 700
        y1 = 300
        namebox1 = w
    elif metkaadd == 23:
        x1 = 800
        y1 = 300
        namebox1 = b
    elif metkaadd == 24:
        x1 = 100
        y1 = 400
        namebox1 = b
    elif metkaadd == 25:
        x1 = 200
        y1 = 400
        namebox1 = w
    elif metkaadd == 26:
        x1 = 300
        y1 = 400
        namebox1 = b
    elif metkaadd == 27:
        x1 = 400
        y1 = 400
        namebox1 = w
    elif metkaadd == 28:
        x1 = 500
        y1 = 400
        namebox1 = b
    elif metkaadd == 29:
        x1 = 600
        y1 = 400
        namebox1 = w
    elif metkaadd == 30:
        x1 = 700
        y1 = 400
        namebox1 = b
    elif metkaadd == 31:
        x1 = 800
        y1 = 400
        namebox1 = w
    elif metkaadd == 32:
        x1 = 100
        y1 = 500
        namebox1 = w
    elif metkaadd == 33:
        x1 = 200
        y1 = 500
        namebox1 = b
    elif metkaadd == 34:
        x1 = 300
        y1 = 500
        namebox1 = w
    elif metkaadd == 35:
        x1 = 400
        y1 = 500
        namebox1 = b
    elif metkaadd == 36:
        x1 = 500
        y1 = 500
        namebox1 = w
    elif metkaadd == 37:
        x1 = 600
        y1 = 500
        namebox1 = b
    elif metkaadd == 38:
        x1 = 700
        y1 = 500
        namebox1 = w
    elif metkaadd == 39:
        x1 = 800
        y1 = 500
        namebox1 = b
    elif metkaadd == 40:
        x1 = 100
        y1 = 600
        namebox1 = b
    elif metkaadd == 41:
        x1 = 200
        y1 = 600
        namebox1 = w
    elif metkaadd == 42:
        x1 = 300
        y1 = 600
        namebox1 = b
    elif metkaadd == 43:
        x1 = 400
        y1 = 600
        namebox1 = w
    elif metkaadd == 44:
        x1 = 500
        y1 = 600
        namebox1 = b
    elif metkaadd == 45:
        x1 = 600
        y1 = 600
        namebox1 = w
    elif metkaadd == 46:
        x1 = 700
        y1 = 600
        namebox1 = b
    elif metkaadd == 47:
        x1 = 800
        y1 = 600
        namebox1 = w
    elif metkaadd == 48:
        x1 = 100
        y1 = 700
        namebox1 = w
    elif metkaadd == 49:
        x1 = 200
        y1 = 700
        namebox1 = b
    elif metkaadd == 50:
        x1 = 300
        y1 = 700
        namebox1 = w
    elif metkaadd == 51:
        x1 = 400
        y1 = 700
        namebox1 = b
    elif metkaadd == 52:
        x1 = 500
        y1 = 700
        namebox1 = w
    elif metkaadd == 53:
        x1 = 600
        y1 = 700
        namebox1 = b
    elif metkaadd == 54:
        x1 = 700
        y1 = 700
        namebox1 = w
    elif metkaadd == 55:
        x1 = 800
        y1 = 700
        namebox1 = b
    elif metkaadd == 56:
        x1 = 100
        y1 = 800
        namebox1 = b
    elif metkaadd == 57:
        x1 = 200
        y1 = 800
        namebox1 = w
    elif metkaadd == 58:
        x1 = 300
        y1 = 800
        namebox1 = b
    elif metkaadd == 59:
        x1 = 400
        y1 = 800
        namebox1 = w
    elif metkaadd == 60:
        x1 = 500
        y1 = 800
        namebox1 = b
    elif metkaadd == 61:
        x1 = 600
        y1 = 800
        namebox1 = w
    elif metkaadd == 62:
        x1 = 700
        y1 = 800
        namebox1 = b
    elif metkaadd == 63:
        x1 = 800
        y1 = 800
        namebox1 = w


    if gameplace[metka2] == "wR" or "wN" or "wB" or "wQ" or "wK" or "wP" or "--":
        if metka1 == metkaadd:
            im.paste(namebox1, (x1, y1), namebox1)
        if metka2 == metkaID:
            im.paste(namebox, (x, y), namebox)
            im.paste(namefigure_pole, (x, y), namefigure_pole)
            im.show()
        gameplace[metka1] = "--"
        gameplace[metka2] = pointID_name
        print("\n", '                  Игровое Поле', "\n",
              gameplace[0: 8], "\n", gameplace[8: 16], "\n", gameplace[16: 24], "\n",
              gameplace[24: 32], "\n", gameplace[32: 40], "\n", gameplace[40: 48], "\n",
              gameplace[48: 56], "\n", gameplace[56: 64], "\n")
        Played()

    if gameplace[metka2] == "bR" or "bN" or "bB" or "bQ" or "bK" or "bP":
        print("Ошибка!!! Не стреляй в своих!")
        Played2()

gamePlay()
Played()
Played2()



