import pygame
import numpy as np

WIDTH, HEIGHT = 800, 600 # Определение размеров окна
CELL_SIZE = 10 # Определение размеров клетки
CELLS_W = WIDTH // CELL_SIZE # Определение количества клеток по горизонтали и вертикали
CELLS_H = HEIGHT // CELL_SIZE

def create_empty_grid(): # Создание пустого поля
    return np.zeros((CELLS_W, CELLS_H), dtype=int)

# Функция для отрисовки текущего состояния поля
def draw_grid(screen, grid): # Функция для отрисовки текущего состояния поля
    screen.fill((255, 255, 255))  # Заполнение экрана белым цветом
    for y in range(0, HEIGHT, CELL_SIZE): # Отрисовка сетки
        pygame.draw.line(screen, (200, 200, 200), (0, y), (WIDTH, y))  # Горизонтальные линии
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, HEIGHT))  # Вертикальные линии
    for x in range(CELLS_W): # Отрисовка живых клеток
        for y in range(CELLS_H):
            if grid[x][y] == 1:
                pygame.draw.rect(screen, (255, 0, 0), (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def get_cell_from_mouse(pos): # Определение функции для преобразования координат мыши в координаты ячейки поля
    x, y = pos
    cell_x = x // CELL_SIZE
    cell_y = y // CELL_SIZE
    return cell_x, cell_y


def update_grid(grid): # Функция для обновления состояния поля на следующий шаг
    new_grid = np.copy(grid)
    for x in range(CELLS_W):
        for y in range(CELLS_H):
            neighbors = count_neighbors(grid, x, y)
            if grid[x][y] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[x][y] = 0
            else:
                if neighbors == 3:
                    new_grid[x][y] = 1
    return new_grid

def count_neighbors(grid, x, y): # Функция для определения количества живых соседей для клетки с координатами (x, y)
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= x + i < CELLS_W and 0 <= y + j < CELLS_H:
                count += grid[x + i][y + j]
    return count

# Функция main
def main():

    pygame.init() # Инициализация библиотеки
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Создание окна
    pygame.display.set_caption("Game of Life") # Установка заголовка окна

    font = pygame.font.Font(None, 36) # Создание шрифта для отображения текста
    generation = 0 # Инициализация счетчика поколений

    grid = create_empty_grid() # Создание пустого поля

    editing = True  # Флаг для определения, происходит ли редактирование поля
    running_simulation = False

    while editing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                editing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Начать/остановить генерацию при нажатии пробела
                    running_simulation = not running_simulation
                elif event.key == pygame.K_c:
                    grid = create_empty_grid()
                    generation = 0
                elif event.key == pygame.K_q:
                    editing = False
                    running = False

        if running_simulation:
            grid = update_grid(grid)
            generation += 1

        mouse_pos = pygame.mouse.get_pos()
        cell_x, cell_y = get_cell_from_mouse(mouse_pos)
        mouse_buttons = pygame.mouse.get_pressed() # Изменение состояния клетки при удержании левой кнопки мыши
        if mouse_buttons[0]:  # Левая кнопка мыши нажата
            grid[cell_x][cell_y] = 1

        draw_grid(screen, grid)

        text = font.render(f"Generation: {generation}", True, (0, 0, 0)) # Отображение счетчика генераций
        screen.blit(text, (10, 10))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__": # Запуск основной функции
    main()
