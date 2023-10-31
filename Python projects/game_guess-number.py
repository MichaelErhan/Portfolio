import random
import json
import csv
import tkinter as tk
from tkinter import messagebox, filedialog

class NumberGameBuilder:
   def __init__(self):
       self.game = NumberGame()

   def set_difficulty(self, difficulty):
       self.game.difficulty = difficulty

   def set_max_attempts(self, max_attempts):
       self.game.max_attempts = max_attempts

   def build(self):
       return self.game

class NumberGame:
   def __init__(self):
       self.difficulty = 10
       self.max_attempts = 5
       self.secret_number = random.randint(1, 100)
       self.hint_provider = None
       self.accuracy = None

class NumberGameGUI:
    def __init__(self):
        self.filename =""
        self.game = NumberGame()
        self.attempts = 0
        self.accuracy = 0

        self.window = tk.Tk()
        self.window.title("Игра Угадай число!")

        self.label = tk.Label(self.window, text="Введите число от 1 до 100:")
        self.label.pack()

        self.entry = tk.Entry(self.window)
        self.entry.pack()

        self.button = tk.Button(self.window, text="Проверить", command=self.check_guess)
        self.button.pack()

        self.button = tk.Button(self.window, text="Выгрузить в .json", command= self.save_game_data_to_json)
        self.button.pack()

        self.button = tk.Button(self.window, text="Выгрузить в .csv", command= self.save_game_data_to_csv)
        self.button.pack()

        self.button = tk.Button(self.window, text="Загрузить из .json", command= self.load_game_data_from_json)
        self.button.pack()

        self.button = tk.Button(self.window, text="Загрузить из .csv", command= self.load_game_data_from_csv)
        self.button.pack()

    def check_guess(self):
        guess = int(self.entry.get())
        self.attempts += 1
        self.accuracy = 100.0 / self.attempts
        if guess == self.game.secret_number:
            messagebox.showinfo("Игра окончена!", "Поздравляю! Вы угадали число!\n"+"Точность угадывания - " + str(self.accuracy)+"%")
        elif self.attempts == self.game.max_attempts:
            self.accuracy = 0.0
            messagebox.showinfo("Игра окончена!", "К сожалению, вы не угадали число. Загаданное число было: " + str(self.game.secret_number)+"\nТочность угадывания - "+ str(self.accuracy)+"%")
        elif guess < self.game.secret_number:
            messagebox.showinfo("Подсказка", "Загаданное число больше, чем " + str(guess))
        elif guess > self.game.secret_number:
            messagebox.showinfo("Подсказка", "Загаданное число меньше, чем " + str(guess))

    # Функция для загрузки игровых данных в json файл
    def save_game_data_to_json(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=(("JSON files", "*.json"), ("All files", "*.*")))
        if file_path:
            game_data = {
                "difficulty": self.game.difficulty,
                "max_attempts": self.game.max_attempts,
                "secret_number": self.game.secret_number,
                "accuracy": self.accuracy
            }
            with open(file_path, "w") as file:
                json.dump(game_data, file)
                messagebox.showinfo("Экспорт выполнен успешно", "Данные игры успешно экспортированы в формате JSON.")

    # Функция для загрузки игровых данных из json файла
    def load_game_data_from_json(self):
        file_path = filedialog.askopenfilename(filetypes=(("JSON files", "*.json"), ("All files", "*.*")))
        if file_path:
            with open(file_path, "r") as file:
                game_data = json.load(file)
                self.game.difficulty = game_data["difficulty"]
                self.game.max_attempts = game_data["max_attempts"]
                self.game.secret_number = game_data["secret_number"]
                self.game.accuracy = game_data["accuracy"]

                messagebox.showinfo("Импорт выполнен успешно", f"Данные игры успешно импортированы в формате JSON.\n"
                                                         f"difficulty: {self.game.difficulty}\n"
                                                         f"max_attempts: {self.game.max_attempts}\n"
                                                         f"secret_number: {self.game.secret_number}\n"
                                                         f"accuracy: {self.game.accuracy}%")

    # Функция для сохранения игровых данных в csv файл
    def save_game_data_to_csv(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
        if file_path:
            game_data = [
                ["difficulty", "max_attempts", "secret_number", "accuracy"],
                [self.game.difficulty, self.game.max_attempts, self.game.secret_number, self.accuracy]
            ]
            with open(file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(game_data)
                messagebox.showinfo("Экспорт выполнен успешно", "Данные игры успешно экспортированы в формате CSV.")
    # Функция для загрузки игровых данных из csv файла
    def load_game_data_from_csv(self):
        file_path = filedialog.askopenfilename(filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
        if file_path:
            with open(file_path, "r") as file:
                reader = csv.reader(file)
                game_data = list(reader)
                self.game.difficulty = game_data[1][0]
                self.game.max_attempts = int(game_data[1][1])
                self.game.secret_number = int(game_data[1][2])
                self.game.accuracy = str(game_data[1][3])
                messagebox.showinfo("Импорт выполнен успешно", "Данные игры успешно импортированы в формате CSV.\n"
                                                         f"difficulty: {self.game.difficulty}\n"
                                                         f"max_attempts: {self.game.max_attempts}\n"
                                                         f"secret_number: {self.game.secret_number}\n"
                                                         f"accuracy: {self.game.accuracy}%")


game_gui = NumberGameGUI()
game_gui.window.mainloop()
game_builder = NumberGameBuilder()
game_builder.set_difficulty(10)
game_builder.set_max_attempts(5)
game = game_builder.build()