import pygame,random

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 420

FPS = 10
clock = pygame.time.Clock()

WHITE = (255,255,255)

pic = pygame.image.load("assets/pic.jpeg")
pic_rect = pic.get_rect()

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption(title="My game")

row = 6
col = 6
cells_num = row*col

cell_width = WINDOW_WIDTH//row
cell_height = WINDOW_HEIGHT//col

cells = []
position_list = list(range(0, cells_num))


for i in range(cells_num):
    x = (i % row) * cell_width
    y = (i // col) * cell_height
    rect = pygame.Rect(x,y,cell_width,cell_height)

    random_position = random.choice(position_list)
    position_list.remove(random_position)
    cells.append({"rect":rect,"border":WHITE,"place":i,"position":random_position})

selected_part = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_position = pygame.mouse.get_pos()

            for cell in cells:
                rect = cell["rect"]
                order = cell["place"]
                if rect.collidepoint(mouse_position):
                    if selected_part == None:
                        selected_part = cell
                        cell["border"] = (255,0,0)
                    else:
                        current_part = cell
                        if current_part["place"] != selected_part["place"]:
                            temp = selected_part["position"]
                            cells[selected_part["place"]]["position"] = cells[current_part["place"]]["position"]
                            cells[current_part["place"]]["position"] = temp

                            cells[selected_part["place"]]["border"] = WHITE
                            selected_part = None
    window.fill(WHITE)

    for i,cell in enumerate(cells):
        position = cells[i]["position"]
        cell_rect = pygame.Rect(cells[position]["rect"].x,cells[position]["rect"].y,cell_width,cell_height)
        window.blit(pic,cells[i]["rect"],cell_rect)
        pygame.draw.rect(window, cells[i]["border"], cells[i]["rect"], 1)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()