import pygame, math

pygame.init()

xy = 300
win = pygame.display.set_mode((xy, xy))
clock = pygame.time.Clock()
run = True
started = False
tiles = []


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = False
        self.rect = pygame.Rect(self.x, self.y, 10, 10)

    def draw(self):
        if self.alive:
            pygame.draw.rect(win, (255, 255, 255), self.rect)
        if not self.alive:
            pygame.draw.rect(win, (0, 0, 0), self.rect)

    def life(self):
        n = len(findNeighbours(self.x, self.y))
        if not self.alive:
            if n == 3:
                self.alive = True
                print("one got revived")
        if self.alive:
            if not n == 2 and not n == 3:
                self.alive = False
                print("one died, Population = ", n)


def makeGrid():
    for y in range(0, 30):
        for x in range(0, 30):
            tiles.append(Tile(x * 10, y * 10))


def euclidian(x1, y1, x2, y2):
    return math.sqrt(((x2 - x1) ** 2) + (y2 - y1) ** 2)


def findNeighbours(x, y):
    neighbors = []

    for tile in tiles:
        if euclidian(x, y, tile.x, tile.y) <= 15:
            if (tile.x, tile.y) == (x + 10, y + 10) and tile.alive:
                neighbors.append(tile)  # DR
            elif (tile.x, tile.y) == (x, y + 10) and tile.alive:
                neighbors.append(tile)  # D
            elif (tile.x, tile.y) == (x + 10, y) and tile.alive:
                neighbors.append(tile)  # R
            elif (tile.x, tile.y) == (x - 10, y - 10) and tile.alive:
                neighbors.append(tile)  # LU
            elif (tile.x, tile.y) == (x - 10, y + 10) and tile.alive:
                neighbors.append(tile)  # LD
            elif (tile.x, tile.y) == (x + 10, y - 10) and tile.alive:
                neighbors.append(tile)  # RU
            elif (tile.x, tile.y) == (x + 10, y + 10) and tile.alive:
                neighbors.append(tile)
            elif (tile.x, tile.y) == (x, y-10) and tile.alive:
                neighbors.append(tile)  # U
            elif (tile.x, tile.y) == (x - 10, y) and tile.alive:
                neighbors.append(tile)  # L

    return neighbors


def redrawWin():
    global started
    mouse = pygame.mouse.get_pressed(3)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        started = True
    if mouse[0]:
        for t in tiles:
            if t.rect.collidepoint(pygame.mouse.get_pos()):
                t.alive = True
    for tile in tiles:
        pygame.draw.rect(win, (20, 20, 20), (tile.x, tile.y, 10, 10))
        tile.draw()
        if started:
            tile.life()
    pygame.display.update()


def main():
    global run, started
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        if run:
            try:
                redrawWin()
            except:
                started = False
                for tile in tiles:
                    tile.alive = False


makeGrid()
main()
