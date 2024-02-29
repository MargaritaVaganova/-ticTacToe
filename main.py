import pygame
import sys
import os
import random
import time


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
                      "Для начала игры  нажмите клавишу на клавиатуре или кнопку мыши!"]

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
        time.sleep(10)
        self.background()

        # Рисовка черного полупрозрачного квадрата
        surf = pygame.Surface((self.height - 20, self.width - 20))
        surf.fill("black")
        surf.set_alpha(110)
        screen.blit(surf, (10, 10))

        intro_text = ["РЕЗУЛЬТАТЫ ПОСЛЕДНИХ ИГР", ""]

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
    def __init__(self, player1_, player2_):
        self.width = 3
        self.height = 3
        self.board = [["-"] * 3 for _ in range(3)]
        # значения по умолчанию
        self.left = 300
        self.top = 100
        self.cell_size = 100
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
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                textA = "X"
                textB = "O"
                font = pygame.font.Font(None, 100)
                if self.board[i][j] == 1:
                    string_rendered1 = font.render(textB, 1, pygame.Color('black'))
                    screen.blit(string_rendered1, [305 + 100 * j, 105 + 100 * i])
                elif self.board[i][j] == 2:
                    string_rendered1 = font.render(textA, 1, pygame.Color('black'))
                    screen.blit(string_rendered1, [305 + 100 * j, 105 + 100 * i])

        # Проверка на выигрыш кого-нибудь из игроков

    def check_for_winnings(self):
        fl = 0
        if self.board[0][0] == self.board[0][1] == self.board[0][2] == 1 or \
                self.board[1][0] == self.board[1][1] == self.board[1][2] == 1 or \
                self.board[2][0] == self.board[2][1] == self.board[2][2] == 1 or \
                self.board[0][0] == self.board[1][0] == self.board[2][0] == 1 or \
                self.board[0][1] == self.board[1][1] == self.board[2][1] == 1 or \
                self.board[0][2] == self.board[1][2] == self.board[2][2] == 1 or \
                self.board[0][0] == self.board[1][1] == self.board[2][2] == 1 or \
                self.board[0][2] == self.board[1][1] == self.board[2][0] == 1:
            fl = 1
        elif self.board[0][0] == self.board[0][1] == self.board[0][2] == 2 or \
                self.board[1][0] == self.board[1][1] == self.board[1][2] == 2 or \
                self.board[2][0] == self.board[2][1] == self.board[2][2] == 2 or \
                self.board[0][0] == self.board[1][0] == self.board[2][0] == 2 or \
                self.board[0][1] == self.board[1][1] == self.board[2][1] == 2 or \
                self.board[0][2] == self.board[1][2] == self.board[2][2] == 2 or \
                self.board[0][0] == self.board[1][1] == self.board[2][2] == 2 or \
                self.board[0][2] == self.board[1][1] == self.board[2][0] == 2:
            fl = 2
        textB = "ПЕРВЫЙ ИГРОК ВЫИГРАЛ!"
        textA = "ВТОРОЙ ИГРОК ВЫИГРАЛ!"
        textC = "НИЧЬЯ!"
        font = pygame.font.Font(None, 45)
        if fl == 1:
            string_rendered = font.render(textA, 1, pygame.Color('red'))
            screen.blit(string_rendered, [240, 20])
            time.sleep(10)
            return 2

        elif fl == 2:
            string_rendered = font.render(textB, 1, pygame.Color('red'))
            screen.blit(string_rendered, [240, 20])
            return 1
        if "-" not in (self.board[0][0], self.board[0][1], self.board[0][2], \
                       self.board[1][0], self.board[1][1], self.board[1][2], \
                       self.board[2][0], self.board[2][2], self.board[2][2]) and fl == 0:
            string_rendered = font.render(textC, 1, pygame.Color('red'))
            screen.blit(string_rendered, [400, 20])
            return 3
        return 0


# класс игроков
class Player():
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


if __name__ == '__main__':
    pygame.init()
    player1 = Player()
    player2 = Player()
    game = Game(500, 900, player1, player2)
    board = Board(player1, player2)
    screen = pygame.display.set_mode((game.height, game.width))
    clock = pygame.time.Clock()
    FPS = 50
    running = True
    game.start_screen()
    fl2 = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                game.base_screen()
                board.render(screen)
                if fl2 != 0:
                    a = event.pos
                    kl = [0, 0]
                    fl = 0
                    if (300 < a[0] < 400) and (100 < a[1] < 200):
                        kl = [0, 0]
                        fl = 1
                    elif (400 < a[0] < 500) and (100 < a[1] < 200):
                        kl = [0, 1]
                        fl = 1
                    elif (500 < a[0] < 600) and (100 < a[1] < 200):
                        kl = [0, 2]
                        fl = 1
                    elif (300 < a[0] < 400) and (200 < a[1] < 300):
                        kl = [1, 0]
                        fl = 1
                    elif (400 < a[0] < 500) and (200 < a[1] < 300):
                        kl = [1, 1]
                        fl = 1
                    elif (500 < a[0] < 600) and (200 < a[1] < 300):
                        kl = [1, 2]
                        fl = 1
                    elif (300 < a[0] < 400) and (300 < a[1] < 400):
                        kl = [2, 0]
                        fl = 1
                    elif (400 < a[0] < 500) and (300 < a[1] < 400):
                        kl = [2, 1]
                        fl = 1
                    elif (500 < a[0] < 600) and (300 < a[1] < 400):
                        kl = [2, 2]
                        fl = 1

                    if board.active_player == 1 and fl == 1:
                        board.board[int(kl[0])][int(kl[1])] = 1
                        board.active_player = 2
                        player1.active_player = 2
                        player2.active_player = 2
                        game.base_screen()
                        board.render(screen)
                        board.draw_cross_zero(screen, a)
                        board.check_for_winnings()
                        #a = board.check_for_winnings()
                        #if a in [1, 2, 3]:
                            #game.final_screen()
                    elif board.active_player == 2 and fl == 1:
                        board.board[int(kl[0])][int(kl[1])] = 2
                        board.active_player = 1
                        player1.active_player = 1
                        player2.active_player = 1
                        game.base_screen()
                        board.render(screen)
                        board.draw_cross_zero(screen, a)
                        board.check_for_winnings()
                        #a = board.check_for_winnings()
                        #if a in [1, 2, 3]:
                            #game.final_screen()
                else:
                    fl2 = 1
            pygame.display.flip()
            clock.tick(FPS)
