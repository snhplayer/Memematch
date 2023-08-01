import pygame

# Function to display the main menu
def main_menu(screen):
    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the game title
    font = pygame.font.Font(None, 48)
    title_text = font.render("Meme Exchange", True, (0, 0, 0))
    title_rect = title_text.get_rect(center=(400, 200))
    screen.blit(title_text, title_rect)

    # Draw the play button
    play_button = pygame.Rect(300, 300, 200, 50)
    pygame.draw.rect(screen, (0, 255, 0), play_button)
    font = pygame.font.Font(None, 32)
    play_text = font.render("Play", True, (0, 0, 0))
    play_rect = play_text.get_rect(center=play_button.center)
    screen.blit(play_text, play_rect)

    # Draw the settings button
    settings_button = pygame.Rect(300, 400, 200, 50)
    pygame.draw.rect(screen, (255, 0, 0), settings_button)
    settings_text = font.render("Settings", True, (0, 0, 0))
    settings_rect = settings_text.get_rect(center=settings_button.center)
    screen.blit(settings_text, settings_rect)

    # Draw the quit button
    quit_button = pygame.Rect(300, 500, 200, 50)
    pygame.draw.rect(screen, (255, 255, 0), quit_button)
    quit_text = font.render("Quit", True, (0, 0, 0))
    quit_rect = quit_text.get_rect(center=quit_button.center)
    screen.blit(quit_text, quit_rect)

    # Update the display
    pygame.display.flip()

    # Return the button rectangles
    return play_button, settings_button, quit_button