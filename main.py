import pygame
from menu import main_menu
from game import game_interface

# Initialize pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Meme Exchange")

# Run the main menu
play_button_rect, settings_button_rect, quit_button_rect = main_menu(screen)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if play_button_rect.collidepoint(mouse_pos):
                    game_interface(screen)
                elif quit_button_rect.collidepoint(mouse_pos):
                    running = False

# Quit the game
pygame.quit()