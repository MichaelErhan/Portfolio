#импортируем модуль для перевода чисел в текстовую строку
from num2words import num2words

#словарь данных, откуда берутся входные значения (вводим число текстом - из словаря берётся цифра)
slovar = {
    'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9,
    'десять': 10, 'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14, 'пятнадцать': 15,
    'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19, 'двадцать': 20, 'тридцать': 30,
    'сорок': 40, 'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70, 'восемьдесят': 80, 'девяносто': 90, 'плюс': '+',
    'минус': '-', 'умножить на': '*', 'скобка открывается': '(', 'скобка закрывается': ')', 'в степени': '**',
    'разделить на': '/','двадцать один': 21,'двадцать два': 22,'двадцать три':23,'двадцать четыре':24,
    'двадцать пять':25,'двадцать шесть':26,'двадцать семь':27,'двадцать восемь':28,'двадцать девять':29,'тридцать один': 31,
    'тридцать два': 32,'тридцать три': 33,'тридцать четыре': 34,'тридцать пять': 35,'тридцать шесть': 36,'тридцать семь': 37,
    'тридцать восемь': 38,'тридцать девять': 39,'сорок один': 41,'сорок два': 42,'сорок три': 43,'сорок четыре': 44,'сорок пять': 45,
    'сорок шесть': 46,'сорок семь': 47,'сорок восемь': 48,'сорок девять': 49,'пятьдесят один': 51,'пятьдесят два': 52,
    'пятьдесят три': 53,'пятьдесят четыре': 54,'пятьдесят пять': 55,'пятьдесят шесть': 56,'пятьдесят семь': 57,'пятьдесят восемь': 58,
    'пятьдесят девять': 59,'шестьдесят один': 61,'шестьдесят два': 62,'шестьдесят три': 63,'шестьдесят четыре': 64,'шестьдесят пять': 65,
    'шестьдесят шесть': 66,'шестьдесят семь': 67,'шестьдесят восемь': 68,'шестьдесят девять': 69,'семьдесят один': 71,'семьдесят два': 72,
    'семьдесят три': 73,'семьдесят четыре': 74,'семьдесят пять': 75,'семьдесят шесть': 76,'семьдесят семь': 77,'семьдесят восемь': 78,
    'семьдесят девять': 79,'восемьдесят один': 81,'восемьдесят два': 82,'восемьдесят три': 83,'восемьдесят четыре': 84,
    'восемьдесят пять': 85,'восемьдесят шесть': 86,'восемьдесят семь': 87,'восемьдесят восемь': 88,'восемьдесят девять': 89,
    'девяносто один': 91,'девяносто два': 92,'девяносто три': 93,'девяносто четыре': 94,'девяносто пять': 95,'девяносто шесть': 96,
    'девяносто семь': 97,'девяносто восемь': 98,'девяносто девять': 99,'сто': 100
}

#словарь двойных значений (чтобы программа могла распознать "умножить на", "разделить на" и др.)
slov_doublewords = {'умножить', 'скобка', 'в','разделить','двадцать','тридцать','сорок','пятьдесят','шестьдесят','семьдесят',
                    'восемьдесят','девяносто'}

#строка ввода операции
operation = input('Введите операцию --> ')

#def - функция с параметрами внутри скобки
#параметры - переменные которым будут присваиваться входящих в функцию значения
def calc(slovar, operation):
    #переменные
    op = []
    es = ''
    #split - разделение значений строки через запятую
    operation = operation.split()
    #если слово присутствует в словаре двойных значений к переменной "es" добавляется это слово
    #далее эта переменная работает со словарём (записывая в него значение)
    #если слова нет в словаре двойных значений программа пропускает эту функцию и идёт сразу к "append"
    for word in operation:
        if word in slov_doublewords:
            es += word
            continue
        if es:
            op.append(slovar[es + " " + word])
            es = ''
            continue
        #добавление элемента в словарь
        op.append(slovar[word])
    #вывод входных значений через разделитель в формате цифр
    print(op)
    op = ' '.join(list(map(str, op)))
    #eval - функция, в данном случае считает введённую строку
    op = eval(op)
    #вывод результата с переводом в текстовую строку и на русский язык
    print('Ответ: ', num2words(op, lang= 'ru'))

#конец функции def
calc(slovar, operation)