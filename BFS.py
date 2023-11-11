import pygame
import random
from collections import deque

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 40

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

def generate_random_maze(rows, cols, start_symbol='S', end_symbol='E', wall_symbol='#'):
    # Generate a random maze with a given number of rows and columns
    maze = [['.' for _ in range(cols)] for _ in range(rows)]

    # Place the start and end points randomly
    start_x, start_y = random.randint(0, rows - 1), random.randint(0, cols - 1)
    end_x, end_y = random.randint(0, rows - 1), random.randint(0, cols - 1)

    # Ensure start and end points are different
    while start_x == end_x and start_y == end_y:
        end_x, end_y = random.randint(0, rows - 1), random.randint(0, cols - 1)

    maze[start_x][start_y] = start_symbol
    maze[end_x][end_y] = end_symbol

    # Place random walls
    num_walls = (rows * cols) // 4  # Adjust the number of walls as needed
    for _ in range(num_walls):
        wall_x, wall_y = random.randint(0, rows - 1), random.randint(0, cols - 1)
        maze[wall_x][wall_y] = wall_symbol

    return maze, (start_x, start_y), (end_x, end_y)

def is_valid_move(maze, x, y):
    if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#':
        return True
    return False

def bfs_solver(maze, start, end):
    queue = deque([start])
    visited = set()
    came_from = {}

    while queue:
        x, y = queue.popleft()

        if (x, y) == end:
            path = [(x, y)]
            while (x, y) != start:
                x, y = came_from[(x, y)]
                path.append((x, y))
            path.reverse()
            return path

        visited.add((x, y))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if is_valid_move(maze, new_x, new_y) and (new_x, new_y) not in visited:
                came_from[(new_x, new_y)] = (x, y)
                queue.append((new_x, new_y))

    return None

def draw_maze(screen, maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == '#':
                pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif maze[row][col] == 'S':
                pygame.draw.rect(screen, GREEN, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif maze[row][col] == 'E':
                pygame.draw.rect(screen, RED, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def animate_path(screen, maze, path):
    for x, y in path:
        screen.fill((0, 0, 0))
        draw_maze(screen, maze)
        pygame.draw.rect(screen, BLUE, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.display.flip()
        pygame.time.delay(500)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze Game")

    maze_rows = 10
    maze_cols = 10

    maze, start, end = generate_random_maze(maze_rows, maze_cols)
    player_x, player_y = start

    clock = pygame.time.Clock()
    running = True

    # Solve the maze using BFS algorithm
    path = bfs_solver(maze, start, end)

    if path:
        animate_path(screen, maze, path)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
