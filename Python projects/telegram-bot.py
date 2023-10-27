import telebot
from telebot import types
from telebot.types import User

bot = telebot.TeleBot('6213790446:AAGr7Y0vbMJ4Sm58R3wJagFQAkjGfLwmXLU')

user_dict = {}

class User:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.sex = None
        self.uvlechenie = None

#Настраиваем стартовое сообщение + сообщение "меню" + сообщение об имени поздравляемого
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет, " + str(message.from_user.first_name) + ", я - бот подарков. Помогу выбрать подарок для нужного тебе человека, отправлю тебе ссылку на рекомендованные товары, а также поздравлю его.")
    bot.send_message(message.chat.id, "Меню:\n /start - начало работы \n /button - открытие меню кнопок")
    msg = bot.send_message(message.chat.id,"Кому выберем подарок? Напиши его имя.")
    bot.register_next_step_handler(msg,process_name_step)

#Настраиваем кнопки item1,2 (название кнопок в "...")
@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Разработчик")
    markup.add(item1)

#Сообщение при вызове кнопок
    msg = bot.send_message(message.chat.id, 'Выбери, что ты хочешь сделать', reply_markup=markup)
    bot.register_next_step_handler(msg,message_reply)

#Настраиваем кнопки и вывод информации по их нажатии. ".text" - название кнопки из предыдущей настройки
#send_message - в "" то, что должно выходить при нажатии кнопки (ссылки, текст)
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Разработчик":
        bot.send_message(message.chat.id,"https://t.me/Passionne1")
        bot.send_message(message.chat.id, "Нажми /start, чтобы начать заново")

def reloadbot(message):
    bot.send_message(message.chat.id, "Привет, " + str(message.from_user.first_name) + ", я - бот подарков. Помогу выбрать подарок для нужного тебе человека, отправлю тебе ссылку на рекомендованные товары, а также поздравлю его.")
    bot.send_message(message.chat.id, "Меню:\n /start - начало работы \n /button - открытие меню кнопок")
    msg = bot.send_message(message.chat.id, "Кому выберем подарок? Напиши его имя.")
    bot.register_next_step_handler(msg,process_name_step)

#Функция, запоминающая имя поздравляемого человека, а также спрашивает сколько ему лет
def process_name_step(message):
    name = message.text
    user = User(name)
    user_dict[message.chat.id] = user

    if name == "/button":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Разработчик")
        markup.add(item1)
        msg = bot.send_message(message.chat.id, 'Выбери, что ты хочешь сделать', reply_markup=markup)
        bot.register_next_step_handler(msg, message_reply)
    else:
        msg = bot.reply_to(message, "Сколько ему/ей лет?")
        bot.register_next_step_handler(msg, process_age_step)

#Функция, запоминающая возраст поздравляемого человека, а также спрашивает его увлечения
def process_age_step(message):
    age = message.text

    if age == "/button":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Разработчик")
        markup.add(item1)
        msg = bot.send_message(message.chat.id, 'Выбери, что ты хочешь сделать', reply_markup=markup)
        bot.register_next_step_handler(msg, message_reply)
    else:
        if not age.isdigit():
            msg = bot.reply_to(message, "Возраст должен быть числом. Сколько ему/ей лет?")
            bot.register_next_step_handler(msg,process_age_step)
            return
        user = user_dict[message.chat.id]
        user.age = age
        msg = bot.reply_to(message, "Напиши, чем он/она увлекается? (Одно главное увлечение. Если увлечение состоит из двух слов, напиши его в формате (слово+слово)).")
        bot.register_next_step_handler(msg,process_uvlechenie_step)

#Функция, запоминающая увлечения поздравляемого человека
def process_uvlechenie_step(message):
    uvlechenie = message.text
    user = user_dict[message.chat.id]
    user.uvlechenie = uvlechenie

    if uvlechenie == "/button":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Разработчик")
        markup.add(item1)
        msg = bot.send_message(message.chat.id, 'Выбери, что ты хочешь сделать', reply_markup=markup)
        bot.register_next_step_handler(msg, message_reply)
    else:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add("Мужчина", "Женщина")
        msg = bot.reply_to(message, "Пожалуйста, укажи пол поздравляемого через кнопку выбора", reply_markup=markup)
        bot.register_next_step_handler(msg, process_sex_step)

#Функция, запоминающая ответ пользователя о поле + проверка есть ли такой пол
def process_sex_step(message):
    sex = message.text
    user = user_dict[message.chat.id]

    if sex == "/button":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Разработчик")
        markup.add(item1)
        msg = bot.send_message(message.chat.id, 'Выбери, что ты хочешь сделать', reply_markup=markup)
        bot.register_next_step_handler(msg, message_reply)
    else:
        if (sex == u"Мужчина") or (sex == u"Женщина") or (sex == u"мужчина") or (sex == u"женщина"):
            user.sex = sex
            bot.send_message(message.chat.id, " Отлично дай мне секунду!")
        else:
            msg = bot.send_message(message.chat.id, "Выбери верный пол!")
            bot.register_next_step_handler(msg,process_sex_step)

#Сообщение о перепроверке данных
        msg = bot.send_message(message.chat.id, "Давай проверим данные поздравляемого!\n\n" + "Имя - " + str(user.name) + "\nВозраст - " + str(user.age) + "\nПол - " + str(user.sex) + "\nЕго/её увлечения - " + str(user.uvlechenie) + "\n\nВсё верно? (Да или Нет)")
        bot.register_next_step_handler(msg, process_sozdanie_step)

#Проверка ответа пользователя + перепроверка данных при ответе "нет"
def process_sozdanie_step(message):
    otvet = message.text
    user = user_dict[message.chat.id]

    if otvet == "/button":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Разработчик")
        markup.add(item1)
        msg = bot.send_message(message.chat.id, 'Выбери, что ты хочешь сделать', reply_markup=markup)
        bot.register_next_step_handler(msg, message_reply)
    else:
        if otvet == "Да" or otvet == "да":
            bot.send_message(message.chat.id, "Специальное поздравление от меня: \n\n""Дорогой "+user.name+"!"+" Поздравляю тебя с днём рождения! Желаю твоим мечтам сбыться, твоей удаче – находится всегда рядом, указывая жизненный путь, пусть этот путь будет светлее со сбывшимися мечтами, со сбывшимися надеждами, и пусть благополучие гостит всегда в твоей душе.")
#Вывод ссылок на маркетплейсы по увлечению
            bot.send_message(message.chat.id, "Посмотри что я могу тебе предложить в качестве подарков: \n" + "https://www.ozon.ru/search/?text="+user.uvlechenie+"&from_global=true" + "\nИли вот это:\n" + "https://www.wildberries.ru/catalog/0/search.aspx?search="+user.uvlechenie)
        else:
            msg = bot.send_message(message.chat.id, "Тогда давай перепроверим! Напиши имя поздравляемого.")
            bot.register_next_step_handler(msg, process_name_step)

        msg1 = bot.send_message(message.chat.id, "Начать заново?")
        if message.text =="Да" or message.text == "да":
            bot.register_next_step_handler(msg1, reloadbot)



#Функция infinity_polling подразумевает, что бот должен стараться не прекращать работу при возникновении каких-либо ошибок.
#При этом, за ботом нужно следить, ибо сервера Telegram периодически перестают отвечать на запросы или делают это с большой задержкой приводя к ошибкам.
bot.infinity_polling()
