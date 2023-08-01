import pygame
import random

# List of situations
situations = [
    'Когда у тебя есть 5 минут до конца работы',
    'Когда кто-то берет последнюю печеньку',
    'Когда пытаешься понять новую технологию',
    'Когда ты устал, но еще много работы',
    'Когда видишь своих друзей после долгого отсутствия'
]

# Function to generate a random situation
def generate_situation():
    random_index = random.randint(0, len(situations) - 1)
    return situations[random_index]

# Function to display the game interface
def game_interface(screen):
    # Clear the screen
    screen.fill((255, 255, 255))

    # Generate a random situation
    situation = generate_situation()

    # Draw the text window
    font = pygame.font.Font(None, 24)
    text = font.render(situation, True, (0, 0, 0))
    text_rect = text.get_rect(center=(400, 200))
    screen.blit(text, text_rect)

    # Draw the playing cards
    card_width = 100
    card_height = 150
    card_spacing = 50
    card_x = (800 - (4 * card_width + 3 * card_spacing)) // 2
    card_y = 400
    for i in range(4):
        card_rect = pygame.Rect(card_x + i * (card_width + card_spacing), card_y, card_width, card_height)
        pygame.draw.rect(screen, (0, 0, 255), card_rect)

    # Update the display
    pygame.display.flip()