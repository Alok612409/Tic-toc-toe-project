import pygame as p

p.init()


class Square(p.sprite.Sprite):
    def __init__(self, x_id, y_id, number):
        super().__init__()
        self.width = 120
        self.height = 120
        self.x = x_id * self.width
        self.y = y_id * self.height
        self.content = ''
        self.number = number
        self.image = blank_image
        self.image = p.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = (self.x, self.y)

    def clicked(self, x_val, y_val):
        global turn, won

        if self.content == '':
            if self.rect.collidepoint(x_val, y_val):
                self.content = turn
                board[self.number] = turn

                if turn == 'x':
                    self.image = x_image
                    self.image = p.transform.scale(self.image, (self.width, self.height))
                    turn = 'o'
                    checkWinner('x')

                    if not won:
                        CompMove()

                else:
                    self.image = o_image
                    self.image = p.transform.scale(self.image, (self.width, self.height))
                    turn = 'x'
                    checkWinner('o')


def checkWinner(player):
    global background, won

    for i in range(8):
        if board[winners[i][0]] == player and board[winners[i][1]] == player and board[winners[i][2]] == player:
            won = True
            break

    if won:
        Update()
        square_group.empty()
        background = p.image.load(player.upper() + ' Wins.png')
        background = p.transform.scale(background, (WIDTH, HEIGHT))


def Winner(player):
    global compMove, move

    for i in range(8):
        if board[winners[i][0]] == player and board[winners[i][1]] == player and board[winners[i][2]] == '':
            compMove = winners[i][2]
            move = False

        elif board[winners[i][0]] == player and board[winners[i][1]] == '' and board[winners[i][2]] == player:
            compMove = winners[i][1]
            move = False

        elif board[winners[i][0]] == '' and board[winners[i][1]] == player and board[winners[i][2]] == player:
            compMove = winners[i][0]
            move = False


def CompMove():
    global move

    move = True

    if move:
        Winner('o')

    if move:
        Winner('x')

    if move:
        checkCentre()

    if move:
        checkCorner()

    if move:
        checkEdge()

    if not move:
        for square in squares:
            if square.number == compMove:
                square.clicked(square.x, square.y)


def checkCentre():
    global compMove, move

    if board[5] == '':
        compMove = 5
        move = False


def checkCorner():
    global compMove, move

    for i in range(1, 11, 2):
        if i != 5:
            if board[i] == '':
                compMove = i
                move = False
                break


def checkEdge():
    global compMove, move

    for i in range(2, 10, 2):
        if board[i] == '':
            compMove = i
            move = False
            break


def Update():
    win.blit(background, (0, 0))
    square_group.draw(win)
    square_group.update()
    p.display.update()


WIDTH = 500
HEIGHT = 500

win = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('Tic Tac Toe world of game')
clock = p.time.Clock()

blank_image = p.image.load('sddefault.png')
x_image = p.image.load('x.png')
o_image = p.image.load('o.png')
background = p.image.load('Akbg.png')

background = p.transform.scale(background, (WIDTH, HEIGHT))

move = True
won = False
compMove = 5

square_group = p.sprite.Group()
squares = []

winners = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
board = ['' for i in range(10)]

num = 1
for y in range(1, 4):
    for x in range(1, 4):
        sq = Square(x, y, num)
        square_group.add(sq)
        squares.append(sq)

        num += 1

turn = 'x'
run = True
while run:
    clock.tick(60)
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

        if event.type == p.MOUSEBUTTONDOWN and turn == 'x':
            mx, my = p.mouse.get_pos()
            for s in squares:
                s.clicked(mx, my)

    Update()
