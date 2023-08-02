
import random
import pygame
from menu import main_menu
from game import game_interface, situations

# Initialize pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Meme Exchange")

# Define the initial situation
situation = random.choice(situations)

# Run the main menu
play_button_rect, settings_button_rect, quit_button_rect = main_menu(screen)

# Game loop
running = True
show_menu = True  # Флаг для отображения главного меню
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if play_button_rect.collidepoint(mouse_pos):
                    show_menu = False  # Скрыть главное меню
                elif quit_button_rect.collidepoint(mouse_pos):
                    running = False

    if show_menu:
        # Отображение главного меню
        play_button_rect, settings_button_rect, quit_button_rect = main_menu(screen)
    else:
        # Отображение игрового интерфейса
        situation = game_interface(screen, situation)

    # Обновление экрана
    pygame.display.flip()

# Quit the game
pygame.quit()
