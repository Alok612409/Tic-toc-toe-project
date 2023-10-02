import pygame as p

p.init()


class Square(p.sprite.Sprite):
    def __init__(self, x_id, y_id, number):
        super().__init__()
        self.width = 120
        self.height = 120
        self.x = x_id * self.width
        self.y = y_id * self.height
        self.content = ' '
        self.number = number
        self.image = blank_image
        self.image = p.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = (self.x, self.y)

    def clicked(self, x_val, y_val):
        global turn

        if self.content == ' ':
            if self.rect.collidepoint(x_val, y_val):
                self.content = turn
                board[self.number] = turn

                if turn == 'x':
                    self.image = x_image
                    self.image = p.transform.scale(self.image, (self.width, self.height))
                    turn = 'o'

                else:
                    self.image = o_image
                    self.image = p.transform.scale(self.image, (self.width, self.height))
                    turn = 'x'


def Update():
    win.blit(background, (0, 0))
    square_group.draw(win)
    square_group.update()
    p.display.update()


WIDTH = 500
HEIGHT = 500

win = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('Tic Tac Toe Game world')
clock = p.time.Clock()

blank_image = p.image.load('sddefault.png')
x_image = p.image.load('x.png')
o_image = p.image.load('o.png')
background = p.image.load('Akbg.png')

background = p.transform.scale(background, (WIDTH, HEIGHT))

square_group = p.sprite.Group()
squares = []
board = [' ' for i in range(10)]

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
