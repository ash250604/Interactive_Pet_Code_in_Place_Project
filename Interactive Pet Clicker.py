import pygame
import random

# Initialize Pygame
pygame.init()

# Display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Virtual Pet Clicker")

# Colors Used
GRAY = (169, 169, 169)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255, 182, 193)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Loading sounds
pygame.mixer.init()
purr_sound = pygame.mixer.Sound("purr.wav")
meow_sound = pygame.mixer.Sound("meow.wav")
chirp_sound = pygame.mixer.Sound("chirp.wav")

# Draw cat function
def draw_cat(screen, head_clicked=False, body_clicked=False, tail_clicked=False, paw_clicked=False, offsets=None):
    if offsets is None:
        offsets = {'head': (0, 0), 'tail': (0, 0), 'paw_left': (0, 0), 'paw_right': (0, 0)}

    # Body
    pygame.draw.ellipse(screen, GRAY, (300, 300, 200, 100))

    # Head
    pygame.draw.circle(screen, GRAY, (400 + offsets['head'][0], 250 + offsets['head'][1]), 50)
    
    # Ears
    pygame.draw.polygon(screen, GRAY, [(350 + offsets['head'][0], 200 + offsets['head'][1]), (370 + offsets['head'][0], 240 + offsets['head'][1]), (330 + offsets['head'][0], 240 + offsets['head'][1])])
    pygame.draw.polygon(screen, GRAY, [(450 + offsets['head'][0], 200 + offsets['head'][1]), (430 + offsets['head'][0], 240 + offsets['head'][1]), (470 + offsets['head'][0], 240 + offsets['head'][1])])
    
    # Eyes
    eye_color = GREEN if head_clicked else WHITE
    pygame.draw.circle(screen, eye_color, (380 + offsets['head'][0], 240 + offsets['head'][1]), 15)
    pygame.draw.circle(screen, eye_color, (420 + offsets['head'][0], 240 + offsets['head'][1]), 15)
    pygame.draw.circle(screen, BLACK, (380 + offsets['head'][0], 240 + offsets['head'][1]), 7)
    pygame.draw.circle(screen, BLACK, (420 + offsets['head'][0], 240 + offsets['head'][1]), 7)
    
    # Nose
    pygame.draw.polygon(screen, PINK, [(400 + offsets['head'][0], 260 + offsets['head'][1]), (390 + offsets['head'][0], 270 + offsets['head'][1]), (410 + offsets['head'][0], 270 + offsets['head'][1])])
    
    # Mouth
    pygame.draw.line(screen, PINK, (400 + offsets['head'][0], 270 + offsets['head'][1]), (390 + offsets['head'][0], 280 + offsets['head'][1]), 2)
    pygame.draw.line(screen, PINK, (400 + offsets['head'][0], 270 + offsets['head'][1]), (410 + offsets['head'][0], 280 + offsets['head'][1]), 2)
    
    # Tail
    pygame.draw.line(screen, GRAY, (490 + offsets['tail'][0], 330 + offsets['tail'][1]), (550 + offsets['tail'][0], 300 + offsets['tail'][1]), 20)
    
    # Paws
    pygame.draw.circle(screen, GRAY, (320 + offsets['paw_left'][0], 370 + offsets['paw_left'][1]), 20)
    pygame.draw.circle(screen, GRAY, (480 + offsets['paw_right'][0], 370 + offsets['paw_right'][1]), 20)

    if body_clicked:
        pygame.draw.ellipse(screen, YELLOW, (300, 300, 200, 100), 5)
    if tail_clicked:
        pygame.draw.line(screen, YELLOW, (490 + offsets['tail'][0], 330 + offsets['tail'][1]), (550 + offsets['tail'][0], 300 + offsets['tail'][1]), 20)
    if paw_clicked:
        pygame.draw.circle(screen, YELLOW, (320 + offsets['paw_left'][0], 370 + offsets['paw_left'][1]), 25, 5)
        pygame.draw.circle(screen, YELLOW, (480 + offsets['paw_right'][0], 370 + offsets['paw_right'][1]), 25, 5)

# Main game loop
running = True
while running:
    head_clicked = False
    body_clicked = False
    tail_clicked = False
    paw_clicked = False

    offsets = {
        'head': (random.randint(-5, 5), random.randint(-5, 5)),
        'tail': (random.randint(-5, 5), random.randint(-5, 5)),
        'paw_left': (random.randint(-5, 5), random.randint(-5, 5)),
        'paw_right': (random.randint(-5, 5), random.randint(-5, 5)),
    }

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # Head click
            if 350 + offsets['head'][0] < x < 450 + offsets['head'][0] and 200 + offsets['head'][1] < y < 300 + offsets['head'][1]:
                purr_sound.play()
                head_clicked = True
            # Body click
            elif 300 < x < 500 and 300 < y < 400:
                meow_sound.play()
                body_clicked = True
            # Tail click
            elif 490 + offsets['tail'][0] < x < 550 + offsets['tail'][0] and 300 + offsets['tail'][1] < y < 320 + offsets['tail'][1]:
                meow_sound.play()
                tail_clicked = True
            # Paw click
            elif (300 + offsets['paw_left'][0] < x < 340 + offsets['paw_left'][0] and 350 + offsets['paw_left'][1] < y < 390 + offsets['paw_left'][1]) or (460 + offsets['paw_right'][0] < x < 500 + offsets['paw_right'][0] and 350 + offsets['paw_right'][1] < y < 390 + offsets['paw_right'][1]):
                chirp_sound.play()
                paw_clicked = True

    screen.fill(WHITE)
    draw_cat(screen, head_clicked, body_clicked, tail_clicked, paw_clicked, offsets)
    pygame.display.flip()
    pygame.time.delay(100)  # Adds delay to control animation speed

pygame.quit()
