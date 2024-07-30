import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Stack Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Define game variables
box_width = 100
box_height = 20
box_x = (screen_width - box_width) // 2
box_y = screen_height - box_height
box_speed = 5

stack = []
score = 0
game_over = False

# Load fonts
font = pygame.font.SysFont(None, 36)

def draw_box(box):
    pygame.draw.rect(screen, BLUE, box)

def draw_stack():
    for box in stack:
        draw_box(box)

def draw_score():
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

def game_loop():
    global box_x, box_y, box_speed, stack, score, game_over

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    if len(stack) == 0 or (stack[-1].x < box_x + box_width and stack[-1].x + stack[-1].width > box_x):
                        stack.append(pygame.Rect(box_x, box_y, box_width, box_height))
                        score += 1
                        box_speed += 0.5
                        box_y -= box_height
                    else:
                        game_over = True

        screen.fill(WHITE)

        if not game_over:
            box_x += box_speed
            if box_x <= 0 or box_x + box_width >= screen_width:
                box_speed = -box_speed
            draw_box(pygame.Rect(box_x, box_y, box_width, box_height))

        draw_stack()
        draw_score()

        if game_over:
            game_over_text = font.render("Game Over", True, BLACK)
            screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height() // 2))

        pygame.display.flip()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    game_loop()