import pygame,random

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 420

FPS = 10
clock = pygame.time.Clock()

WHITE = (255,255,255)

pic = pygame.image.load("assets/pic.jpeg")
pic_rect = pic.get_rect()
pygame.init()
font = pygame.font.Font("PokemonSolidNormal-xyWR.ttf",50)

congrat_text = font.render("Great",True,WHITE)
congrat_text_rect = congrat_text.get_rect()
congrat_text_rect.center = (WINDOW_WIDTH//2,WINDOW_HEIGHT//2)


window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption(title="My game")

row = 2
col = 2

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
is_solved = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not is_solved:
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

                            is_solved = True
                            for cell in cells:
                                if cell["place"] != cell["position"]:
                                    is_solved = False
    window.fill(WHITE)

    if not is_solved:
        for i,cell in enumerate(cells):
            position = cells[i]["position"]
            cell_rect = pygame.Rect(cells[position]["rect"].x,cells[position]["rect"].y,cell_width,cell_height)
            window.blit(pic,cells[i]["rect"],cell_rect)
            pygame.draw.rect(window, cells[i]["border"], cells[i]["rect"], 1)
    else:
        window.blit(pic,pic_rect)
        window.blit(congrat_text,congrat_text_rect)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()