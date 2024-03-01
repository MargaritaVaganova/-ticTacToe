import pygame
import sys
import os
import random
import time
import sqlite3


# Класс игры
class Game:
    # Инициализация
    def __init__(self, width_, height_, player1_, player2_):
        self.width = width_
        self.height = height_
        self.backgroundPicture = 'fon.png'
        self.player = 'player.png'
        self.player1 = player1_
        self.player2 = player2_

    # Закрытие игры
    def terminate(self):
        pygame.quit()
        sys.exit()

    # Стартовое окно
    def start_screen(self):
        intro_text = ["КРЕСТИКИ - НОЛИКИ", "",
                      "Правила игры:",
                      "Один из игроков играет «крестиками», второй — «ноликами».",
                      "Игроки по очереди ставят на свободные клетки поля знаки,",
                      "один всегда крестики, другой всегда нолики. Первый, ",
                      "выстроивший в ряд 3 своих фигур по вертикали, горизонтали",
                      "или диагонали, выигрывает.",
                      " ",
                      "Для начала игры  выберите уровень:"]

        # Загрузка фона
        self.background()

        # Рисовка черного полупрозрачного квадрата
        surf = pygame.Surface((self.height - 20, self.width - 20))
        surf.fill("black")
        surf.set_alpha(110)
        screen.blit(surf, (10, 10))

        # Вывод текста
        text_coord = 50
        font = pygame.font.Font(None, 30)
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 15
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

    # Загрузка фона
    def background(self):
        a = pygame.image.load(self.backgroundPicture).convert()
        fon = pygame.transform.scale(a, (self.height, self.width))
        screen.blit(fon, (0, 0))

    # Рисовка основного экрана с игрой
    def base_screen(self):
        game.background()

        # Рисовка черных полупрозрачных квадратов
        surf = pygame.Surface((200, 65))
        surf.fill("black")
        surf.set_alpha(110)
        screen.blit(surf, (10, 10))

        surf = pygame.Surface((200, 65))
        surf.fill("black")
        surf.set_alpha(110)
        screen.blit(surf, (690, 10))

        surf = pygame.Surface((300, 300))
        surf.fill("black")
        surf.set_alpha(110)
        screen.blit(surf, (300, 100))

        # рисовка человечков
        game.drawPlayers()

        # Рисовка надписей
        self.player1.drawPlayersInscription()

    # Рисовка финального окна
    def final_screen(self):
        # Загрузка фона
        self.background()

        # Рисовка черного полупрозрачного квадрата
        surf = pygame.Surface((self.height - 20, self.width - 20))
        surf.fill("black")
        surf.set_alpha(110)
        screen.blit(surf, (10, 10))

        # Конечная надпись
        intro_text = ["КОНЕЦ ИГРЫ", "", "", "ВОЗВРАЩАЙТЕСЬ СНОВА!"]

        # Вывод текста
        text_coord = 50
        font = pygame.font.Font(None, 65)
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 15
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        pygame.display.flip()
        time.sleep(4)
        self.terminate()

    # Рисовка человечков
    def drawPlayers(self):
        a = pygame.image.load(self.player).convert()
        player = pygame.transform.scale(a, (350, 350))
        player.set_colorkey("white")
        screen.blit(player, [-50, 100])

        b = pygame.image.load(self.player).convert()
        player = pygame.transform.scale(b, (350, 350))
        player.set_colorkey("white")
        screen.blit(player, [610, 100])


# Класс клетчатого поля
class Board:
    # Создание поля
    def __init__(self, player1_, player2_, level_):
        self.level = level_
        if level_ == 2:
            self.width = 3
            self.height = 3
            self.board = [["-"] * 3 for _ in range(3)]
            # значения по умолчанию
            self.left = 300
            self.top = 100
            self.cell_size = 100
        if level_ == 1:
            self.width = 2
            self.height = 2
            self.board = [["-"] * 2 for _ in range(2)]
            # значения по умолчанию
            self.left = 300
            self.top = 100
            self.cell_size = 150
        self.active_player = 1
        self.player1 = player1_
        self.player2 = player2_

    # Отрисовка поля
    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)

    # Отрисовка нулей и единиц
    def draw_cross_zero(self, screen, a):
        #print(self.board)
        # Если второй уровень
        if self.level == 2:
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    textA = "X"
                    textB = "O"
                    font = pygame.font.Font(None, 155)
                    if self.board[i][j] == 1:
                        string_rendered1 = font.render(textB, 1, pygame.Color('black'))
                        screen.blit(string_rendered1, [305 + 100 * j, 105 + 100 * i])
                    elif self.board[i][j] == 2:
                        string_rendered1 = font.render(textA, 1, pygame.Color('black'))
                        screen.blit(string_rendered1, [305 + 100 * j, 105 + 100 * i])
        #Если первый уровень
        elif self.level == 1:
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    textA = "X"
                    textB = "O"
                    font = pygame.font.Font(None, 225)
                    if self.board[i][j] == 1:
                        string_rendered1 = font.render(textB, 1, pygame.Color('black'))
                        screen.blit(string_rendered1, [305 + 150 * j, 105 + 150 * i])
                    elif self.board[i][j] == 2:
                        string_rendered1 = font.render(textA, 1, pygame.Color('black'))
                        screen.blit(string_rendered1, [305 + 150 * j, 105 + 150 * i])


    # Проверка на выигрыш кого-нибудь из игроков
    def check_for_winnings(self):
        # Если второй уровень
        if self.level == 2:
            flag = 0
            if self.board[0][0] == self.board[0][1] == self.board[0][2] == 1 or \
                    self.board[1][0] == self.board[1][1] == self.board[1][2] == 1 or \
                    self.board[2][0] == self.board[2][1] == self.board[2][2] == 1 or \
                    self.board[0][0] == self.board[1][0] == self.board[2][0] == 1 or \
                    self.board[0][1] == self.board[1][1] == self.board[2][1] == 1 or \
                    self.board[0][2] == self.board[1][2] == self.board[2][2] == 1 or \
                    self.board[0][0] == self.board[1][1] == self.board[2][2] == 1 or \
                    self.board[0][2] == self.board[1][1] == self.board[2][0] == 1:
                flag = 1
            elif self.board[0][0] == self.board[0][1] == self.board[0][2] == 2 or \
                    self.board[1][0] == self.board[1][1] == self.board[1][2] == 2 or \
                    self.board[2][0] == self.board[2][1] == self.board[2][2] == 2 or \
                    self.board[0][0] == self.board[1][0] == self.board[2][0] == 2 or \
                    self.board[0][1] == self.board[1][1] == self.board[2][1] == 2 or \
                    self.board[0][2] == self.board[1][2] == self.board[2][2] == 2 or \
                    self.board[0][0] == self.board[1][1] == self.board[2][2] == 2 or \
                    self.board[0][2] == self.board[1][1] == self.board[2][0] == 2:
                flag = 2
            textB = "ПЕРВЫЙ ИГРОК ВЫИГРАЛ!"
            textA = "ВТОРОЙ ИГРОК ВЫИГРАЛ!"
            textC = "НИЧЬЯ!"
            font = pygame.font.Font(None, 45)

            if flag == 1:
                string_rendered = font.render(textA, 1, pygame.Color('red'))
                screen.blit(string_rendered, [240, 20])
                return 2

            elif flag == 2:
                string_rendered = font.render(textB, 1, pygame.Color('red'))
                screen.blit(string_rendered, [240, 20])
                return 1

            if "-" not in (self.board[0][0], self.board[0][1], self.board[0][2], \
                           self.board[1][0], self.board[1][1], self.board[1][2], \
                           self.board[2][0], self.board[2][2], self.board[2][2]) and flag == 0:
                string_rendered = font.render(textC, 1, pygame.Color('red'))
                screen.blit(string_rendered, [400, 20])
                return 3

            return 0
        # Если первый уровень
        elif self.level == 1:
            flag = 0
            if self.board[0][0] == self.board[0][1] == 1 or \
                    self.board[1][0] == self.board[1][1] == 1 or \
                    self.board[0][0] == self.board[1][0] == 1 or \
                    self.board[0][1] == self.board[1][1] == 1 or \
                    self.board[0][0] == self.board[1][1] == 1 or \
                    self.board[0][1] == self.board[1][0] == 1:
                flag = 1
            elif self.board[0][0] == self.board[0][1] == 2 or \
                    self.board[1][0] == self.board[1][1] == 2 or \
                    self.board[0][0] == self.board[1][0] == 2 or \
                    self.board[0][1] == self.board[1][1] == 2 or \
                    self.board[0][0] == self.board[1][1] == 2 or \
                    self.board[0][1] == self.board[1][0] == 2:
                flag = 2
            textB = "ПЕРВЫЙ ИГРОК ВЫИГРАЛ!"
            textA = "ВТОРОЙ ИГРОК ВЫИГРАЛ!"
            textC = "НИЧЬЯ!"
            font = pygame.font.Font(None, 45)

            if flag == 1:
                string_rendered = font.render(textA, 1, pygame.Color('red'))
                screen.blit(string_rendered, [240, 20])
                pygame.display.flip()
                time.sleep(3)
                return 2

            elif flag == 2:
                string_rendered = font.render(textB, 1, pygame.Color('red'))
                screen.blit(string_rendered, [240, 20])
                pygame.display.flip()
                time.sleep(2)
                return 1

            if "-" not in (self.board[0][0], self.board[0][1],\
                           self.board[1][0], self.board[1][1]) and flag == 0:
                string_rendered = font.render(textC, 1, pygame.Color('red'))
                screen.blit(string_rendered, [400, 20])
                pygame.display.flip()
                time.sleep(2)
                return 3

            return 0


# Класс игроков
class Player:
    def __init__(self):
        # первым ходит 1 игрок
        self.active_player = 1

    # Отрисовка надписей
    def drawPlayersInscription(self):
        textA = "ИГРОК 1"
        textB = "ИГРОК 2"
        font = pygame.font.Font(None, 60)
        if self.active_player == 2:
            string_rendered1 = font.render(textA, 1, pygame.Color('green'))
        else:
            string_rendered1 = font.render(textA, 1, pygame.Color('white'))
        screen.blit(string_rendered1, [20, 20])

        if self.active_player == 1:
            string_rendered2 = font.render(textB, 1, pygame.Color('green'))
        else:
            string_rendered2 = font.render(textB, 1, pygame.Color('white'))
        screen.blit(string_rendered2, [700, 20])


# Класс кнопок для определения уровня сложности
class Button:
    def __init__(self, x_, y_, width_, height_, text_, activity_):
        self.x = x_
        self.y = y_
        self.width = width_
        self.height = height_
        self.text = text_
        self.activity = activity_

    # Рисование кнопки
    def draw(self, screen):
        # Сама кнопка
        surf = pygame.Surface((self.width, self.height))
        surf.fill("black")
        surf.set_alpha(110)
        screen.blit(surf, (self.x, self.y))

        # Надпись в кнопке
        font = pygame.font.Font(None, 25)
        string_rendered1 = font.render(self.text, 1, pygame.Color('white'))
        screen.blit(string_rendered1, [self.x + 5, self.y + 5])
        pygame.display.flip()

    # Проверка на нажатие кнопки
    def check_button_click(self, a):
        if (self.x < a[0] < self.x + 100) and (self.y < a[1] < self.y + 50):
            # Перерисовываем более темную кнопку если она нажата
            # Сама кнопка
            surf = pygame.Surface((self.width, self.height))
            surf.fill("black")
            screen.blit(surf, (self.x, self.y))

            # Надпись в кнопке
            font = pygame.font.Font(None, 25)
            string_rendered1 = font.render(self.text, 1, pygame.Color('white'))
            screen.blit(string_rendered1, [self.x + 5, self.y + 5])
            pygame.display.flip()

            # Изменеиие состояния кнопки
            self.activity = 1


if __name__ == '__main__':

    # Cоздаем игроков, основное поле, игровое поле, кнопки
    pygame.init()
    player1 = Player()
    player2 = Player()
    game = Game(500, 900, player1, player2)
    #board = Board(player1, player2)
    btn1 = Button(400, 300, 100, 50, "лёгкий", 0)
    btn2 = Button(505, 300, 100, 50, "обычный", 0)

    pygame.display.set_caption('КРЕСТИКИ-НОЛИКИ')
    screen = pygame.display.set_mode((game.height, game.width))
    clock = pygame.time.Clock()
    FPS = 50
    game.start_screen()
    btn1.draw(screen)
    btn2.draw(screen)
    flag2 = 0
    flag3 = 0
    flag4 = 0
    running = True

    # Основной цикл
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if btn1.activity == 0 and btn2.activity == 0:
                    btn2.check_button_click(event.pos)
                    btn1.check_button_click(event.pos)
                    if btn1.activity == 1 or btn2.activity == 1:
                        flag3 = 1
                # Если выбран обычный уровень
                if btn2.activity == 1:
                    if flag4 == 0:
                        board = Board(player1, player2, 2)
                        flag4 = 1
                    game.base_screen()
                    board.render(screen)
                    if flag2 != 0:
                        a = event.pos
                        kl = [0, 0]
                        flag = 0
                        if (300 < a[0] < 400) and (100 < a[1] < 200):
                            kl = [0, 0]
                            flag = 1
                        elif (400 < a[0] < 500) and (100 < a[1] < 200):
                            kl = [0, 1]
                            flag = 1
                        elif (500 < a[0] < 600) and (100 < a[1] < 200):
                            kl = [0, 2]
                            flag = 1
                        elif (300 < a[0] < 400) and (200 < a[1] < 300):
                            kl = [1, 0]
                            flag = 1
                        elif (400 < a[0] < 500) and (200 < a[1] < 300):
                            kl = [1, 1]
                            flag = 1
                        elif (500 < a[0] < 600) and (200 < a[1] < 300):
                            kl = [1, 2]
                            flag = 1
                        elif (300 < a[0] < 400) and (300 < a[1] < 400):
                            kl = [2, 0]
                            flag = 1
                        elif (400 < a[0] < 500) and (300 < a[1] < 400):
                            kl = [2, 1]
                            flag = 1
                        elif (500 < a[0] < 600) and (300 < a[1] < 400):
                            kl = [2, 2]
                            flag = 1

                        # Если игроки закончили свою игру
                        if board.active_player == 1 and flag == 1:
                            board.board[int(kl[0])][int(kl[1])] = 1
                            board.active_player = 2
                            player1.active_player = 2
                            player2.active_player = 2
                            game.base_screen()
                            board.render(screen)
                            board.draw_cross_zero(screen, a)

                            a = board.check_for_winnings()
                            if a in [1, 2, 3]:
                                pygame.display.flip()
                                time.sleep(3)
                                game.final_screen()

                        elif board.active_player == 2 and flag == 1:
                            board.board[int(kl[0])][int(kl[1])] = 2
                            board.active_player = 1
                            player1.active_player = 1
                            player2.active_player = 1
                            game.base_screen()
                            board.render(screen)
                            board.draw_cross_zero(screen, a)

                            a = board.check_for_winnings()
                            if a in [1, 2, 3]:
                                pygame.display.flip()
                                time.sleep(3)
                                game.final_screen()
                    else:
                        flag2 = 1

                # Если выбран легкий уровень
                elif btn1.activity == 1:
                    if flag4 == 0:
                        board = Board(player1, player2, 1)
                        flag4 = 1
                    game.base_screen()
                    board.render(screen)

                    if flag2 != 0:
                        a = event.pos
                        kl = [0, 0]
                        flag = 0
                        if (300 < a[0] < 450) and (100 < a[1] < 250):
                            kl = [0, 0]
                            flag = 1
                        elif (450 < a[0] < 600) and (100 < a[1] < 250):
                            kl = [0, 1]
                            flag = 1
                        elif (300 < a[0] < 450) and (250 < a[1] < 400):
                            kl = [1, 0]
                            flag = 1
                        elif (450 < a[0] < 600) and (250 < a[1] < 400):
                            kl = [1, 1]
                            flag = 1

                        # Если игроки закончили свою игру
                        if board.active_player == 1 and flag == 1:
                            board.board[int(kl[0])][int(kl[1])] = 1
                            board.active_player = 2
                            player1.active_player = 2
                            player2.active_player = 2
                            game.base_screen()
                            board.render(screen)
                            board.draw_cross_zero(screen, a)

                            a = board.check_for_winnings()
                            if a in [1, 2, 3]:
                                pygame.display.flip()
                                time.sleep(1)
                                game.final_screen()

                        elif board.active_player == 2 and flag == 1:
                            board.board[int(kl[0])][int(kl[1])] = 2
                            board.active_player = 1
                            player1.active_player = 1
                            player2.active_player = 1
                            game.base_screen()
                            board.render(screen)
                            board.draw_cross_zero(screen, a)

                            a = board.check_for_winnings()
                            if a in [1, 2, 3]:
                                pygame.display.flip()
                                time.sleep(1)
                                game.final_screen()
                    else:
                        flag2 = 1

                pygame.display.flip()
                clock.tick(FPS)
