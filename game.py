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

# Случайная ситуация
situation = random.choice(situations)

# Функция для генерации случайных картинок
def generate_memes(count):
    random_memes = random.sample(memes, count)
    return random_memes

# Функция для генерации новой ситуации
def generate_new_situation():
    new_situation = random.choice(situations)
    return new_situation

# Функция для отображения игрового интерфейса
def game_interface(screen, situation):
    # Очистка экрана
    screen.fill((255, 255, 255))

    # Отображение текстового окна
    font = pygame.font.Font(None, 24)
    text = font.render(situation, True, (0, 0, 0))
    text_rect = text.get_rect(center=(400, 200))
    screen.blit(text, text_rect)

    # Генерация случайных картинок
    memes = generate_memes(4)

    # Отображение игральных карт
    card_width = 100
    card_height = 150
    card_spacing = 50
    card_x = (800 - (4 * card_width + 3 * card_spacing)) // 2
    card_y = 400
    hovered_card = None
    mouse_pos = pygame.mouse.get_pos()
    for i in range(4):
        card_rect = pygame.Rect(card_x + i * (card_width + card_spacing), card_y, card_width, card_height)
        meme_image = pygame.image.load(memes[i])
        meme_image = pygame.transform.scale(meme_image, (card_width, card_height))

        # Проверка наведения на карту
        if card_rect.collidepoint(mouse_pos):
            hovered_card = memes[i]
            card_rect.y -= 20  # Сдвиг карты вперед

        screen.blit(meme_image, card_rect)

    # Отображение выдвинутой карты
    if hovered_card is not None:
        card_rect = pygame.Rect(card_x + memes.index(hovered_card) * (card_width + card_spacing), card_y - 20, card_width, card_height)
        meme_image = pygame.image.load(hovered_card)
        meme_image = pygame.transform.scale(meme_image, (card_width, card_height))
        screen.blit(meme_image, card_rect)

    # Handle mouse clicks
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i in range(4):
                card_rect = pygame.Rect(card_x + i * (card_width + card_spacing), card_y, card_width, card_height)
                if card_rect.collidepoint(mouse_pos):
                    # Update situation and generate new images
                    situation = generate_new_situation()
                    memes = generate_memes(4)
                    break

    # Обновление экрана
    pygame.display.flip()

    # Return the updated situation
    return situation

