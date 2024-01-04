using System;

namespace TicTacToe
{
    class Program
    {
        static char[] board = { ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' };
        static char currentPlayer = 'X';
        static bool isGameOver = false;

        static void Main(string[] args)
        {
            Console.WriteLine("Добро пожаловать в игру 'Крестики-нолики'!");

            while (!isGameOver)
            {
                DrawBoard();
                GetPlayerInput();
                CheckGameOver();
                SwapPlayers();
            }

            Console.WriteLine("Игра окончена!");
        }

        static void DrawBoard()
        {
            Console.Clear();
            Console.WriteLine(" {0} | {1} | {2} ", board[0], board[1], board[2]);
            Console.WriteLine("---+---+---");
            Console.WriteLine(" {0} | {1} | {2} ", board[3], board[4], board[5]);
            Console.WriteLine("---+---+---");
            Console.WriteLine(" {0} | {1} | {2} ", board[6], board[7], board[8]);
        }

        static void GetPlayerInput()
        {
            Console.WriteLine("Ход игрока {0}. Введите номер клетки (1-9):", currentPlayer);
            int input = Convert.ToInt32(Console.ReadLine());

            if (input >= 1 && input <= 9 && board[input - 1] == ' ')
            {
                board[input - 1] = currentPlayer;
            }
            else
            {
                Console.WriteLine("Некорректный ввод. Повторите попытку.");
                GetPlayerInput();
            }
        }

        static void CheckGameOver()
        {
            // Проверка выигрышных комбинаций
            if (board[0] == currentPlayer && board[1] == currentPlayer && board[2] == currentPlayer ||
                board[3] == currentPlayer && board[4] == currentPlayer && board[5] == currentPlayer ||
                board[6] == currentPlayer && board[7] == currentPlayer && board[8] == currentPlayer ||
                board[0] == currentPlayer && board[3] == currentPlayer && board[6] == currentPlayer ||
                board[1] == currentPlayer && board[4] == currentPlayer && board[7] == currentPlayer ||
                board[2] == currentPlayer && board[5] == currentPlayer && board[8] == currentPlayer ||
                board[0] == currentPlayer && board[4] == currentPlayer && board[8] == currentPlayer ||
                board[2] == currentPlayer && board[4] == currentPlayer && board[6] == currentPlayer)
            {
                Console.WriteLine("Игрок {0} победил!", currentPlayer);
                isGameOver = true;
            }
            // Проверка на ничью
            else if (!board.Contains(' '))
            {
                Console.WriteLine("Ничья!");
                isGameOver = true;
            }
        }

        static void SwapPlayers()
        {
            currentPlayer = currentPlayer == 'X' ? 'O' : 'X';
        }
    }
}