import pygame
import random

# Список ситуаций
situations = [
    'Когда у тебя есть 5 минут до конца работы',
    'Когда кто-то берет последнюю печеньку',
    'Когда пытаешься понять новую технологию',
    'Когда ты устал, но еще много работы',
    'Когда видишь своих друзей после долгого отсутствия'
]

# Список картинок
memes = [
    'images/meme1.jpg',
    'images/meme2.jpg',
    'images/meme3.jpg',
    'images/meme4.jpg',
    'images/meme5.jpg',
    'images/meme6.jpg',
    'images/meme7.jpg',
    'images/meme8.jpg',
    'images/meme9.jpg',
    'images/meme10.jpg'
]

# Функция для генерации случайной ситуации
def generate_situation(used_situations):
    available_situations = list(set(situations) - set(used_situations))
    if not available_situations:
        available_situations = situations
    situation = random.choice(available_situations)
    used_situations.append(situation)
    return situation, used_situations

# Функция для генерации случайных картинок
def generate_memes(count):
    random_memes = random.sample(memes, count)
    return random_memes

# Функция для отображения игрового интерфейса
def game_interface(screen):
    # Очистка экрана
    screen.fill((255, 255, 255))

    # Генерация случайной ситуации и картинок
    situation, used_situations = generate_situation(game_interface.used_situations)
    memes = generate_memes(4)

    # Отображение текстового окна
    font = pygame.font.Font(None, 24)
    text = font.render(situation, True, (0, 0, 0))
    text_rect = text.get_rect(center=(400, 200))
    screen.blit(text, text_rect)

    # Отображение игральных карт
    card_width = 100
    card_height = 150
    card_spacing = 50
    card_x = (800 - (4 * card_width + 3 * card_spacing)) // 2
    card_y = 400
    for i in range(4):
        card_rect = pygame.Rect(card_x + i * (card_width + card_spacing), card_y, card_width, card_height)
        meme_image = pygame.image.load(memes[i])
        meme_image = pygame.transform.scale(meme_image, (card_width, card_height))
        screen.blit(meme_image, card_rect)

    # Обновление экрана
    pygame.display.flip()

    # Игровой цикл
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                for i in range(4):
                    card_rect = pygame.Rect(card_x + i * (card_width + card_spacing), card_y, card_width, card_height)
                    if card_rect.collidepoint(mouse_pos):
                        # Отображение выбранной картинки в центре экрана
                        selected_meme = pygame.image.load(memes[i])
                        selected_meme = pygame.transform.scale(selected_meme, (400, 600))
                        selected_meme_rect = selected_meme.get_rect(center=(400, 500))
                        screen.blit(selected_meme, selected_meme_rect)
                        pygame.display.flip()

                        # Анимация перемещения картинки
                        start_pos = pygame.math.Vector2(selected_meme_rect.center)
                        end_pos = pygame.math.Vector2(text_rect.center)
                        animation_frames = 60
                        for frame in range(animation_frames):
                            progress = frame / animation_frames
                            current_pos = start_pos.lerp(end_pos, progress)
                            screen.fill((255, 255, 255))
                            screen.blit(text, text_rect)
                            selected_meme_rect.center = current_pos
                            screen.blit(selected_meme, selected_meme_rect)
                            pygame.display.flip()

                        # Ожидание нескольких секунд
                        pygame.time.wait(3000)

                        # Очистка экрана
                        screen.fill((255, 255, 255))

                        # Генерация новой ситуации и картинок
                        situation, used_situations = generate_situation(used_situations)
                        memes = generate_memes(4)

                        # Отображение новой ситуации и картинок
                        text = font.render(situation, True, (0, 0, 0))
                        text_rect = text.get_rect(center=(400, 200))
                        screen.blit(text, text_rect)
                        for j in range(4):
                            card_rect = pygame.Rect(card_x + j * (card_width + card_spacing), card_y, card_width, card_height)
                            meme_image = pygame.image.load(memes[j])
                            meme_image = pygame.transform.scale(meme_image, (card_width, card_height))
                            screen.blit(meme_image, card_rect)
                        pygame.display.flip()

    # Quit the game
    pygame.quit()

# Использованные ситуации
game_interface.used_situations = []
