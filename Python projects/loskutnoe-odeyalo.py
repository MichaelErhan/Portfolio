players_char = ['1', '2', '3'] #количество игроков
width = 5 #количество столбцов
height = 4 #кол-во строк
table = [['*'] * width for i in range(height)] #создаём таблицу
#рисуем таблицу с границами по вертикали и горизонтали
def draw_board(a: list):
    print("-" * (len(table) * 5 + 1))
    for i in range(len(a)):
        print("|", end="")
        for j in range(len(a[0])):
            print(f" {a[i][j]} |", end="")
        print("\n" + "-" * (len(table) * 5 + 1))

print('"Лоскутное одеяло" игра для 3-х игроков')
draw_board(table)
print('Введите координаты хода в через пробел формате: НОМЕР_В_СТРОКЕ НОМЕР_СТОЛБЦА \nШтрафные очки подсчитываются в конце игры')

dxy = [[-1, -1], [-1, 0], [-1, 1], \
       [0,  -1],          [0,  1], \
       [1,  -1], [1,  0], [1,  1]  ]
score = [0, 0, 0]

#всего 20 ходов, разделены на троих игроков и проверка на заполяемость поля с выводом ошибки
#если игрок не попал в область таблицы выводит ошибку с комментарием
#если всё верно добавляется 1 ход из 20 и выводится табличка с заполенной ячейкой с цифрой игрока в ней
current_move = 0
while current_move < 20:
        player = current_move % 3
        try:
            x, y = map(int, input(f'Ход игрока {player + 1}: ').split())
        except:
            print('Введите числа в формате: НОМЕР_В_СТРОКЕ НОМЕР_СТОЛБЦА')
            continue
        try:
            if table[y - 1][x - 1] == "*":
                table[y - 1][x - 1] = players_char[player]
            elif table[y - 1][x - 1] != "*":
                print('Поле уже занято')
                current_move -= 1
        except:
            print('Введите числа удовлетворяющие кол-ву строк(1-5) и кол-ву столбцов(1-4)')
            continue
        draw_board(table)
        current_move += 1

for y in range(4):
    for x in range(5):
        for i in range(len(dxy)):
            nx, ny = x + dxy[i][0], y + dxy[i][1]
            if 0 <= nx < 5 and 0 <= ny < 4:
                if table[y][x] == table[ny][nx]:
                    try:
                        score[int(table[y][x]) - 1] += 1
                        print(score)
                    except ValueError:
                        print('Что-то определённо не так(нельзя ставить символы уже на заполненные места)')
                        continue

#Теперь в score удвоенное количество штрафных очков каждого игрока
#Так что их все нужно поделить на 2 и вывести кол-во штрафных очков у всех игроков(если они есть)
score = [i // 2 for i in score]
for i in range(len(players_char)):
    print(f'Игрок {i + 1} получил {score[i]} штрафных очков')
#сравнение результатов и вывод на экран строки с результатом игры (кто победил или ничья)
if score[0] < (score[1] and score[2]):
    print(f'Победил 1-ый игрок')
elif score[1] < (score[0] and score[2]):
    print(f'Победил 2-ой игрок')
elif score[2] < (score[0] and score[1]):
    print(f'Победил 3-ий игрок')
elif (score[0] == score[1]) and score[0] < score[2] and score[1] < score[2]:
    print(f'Победили два игрока 1 и 2')
elif (score[1] == score[2]) and score[1] < score[0] and score[2] < score[0]:
    print(f'Победили два игрока 2 и 3 ')
elif (score[0] == score[2]) and score[0] < score[1] and score[2] < score[1]:
    print(f'Победили два игрока 1 и 3')
elif score[0] == score[1] == score[2]:
    print(f'Полная ничья!')
