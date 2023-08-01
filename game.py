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
def generate_situation():
    random_index = random.randint(0, len(situations) - 1)
    return situations[random_index]

# Функция для генерации случайных картинок
def generate_memes(count):
    random_memes = random.sample(memes, count)
    return random_memes

# Функция для отображения игрового интерфейса
def game_interface(screen):
    # Очистка экрана
    screen.fill((255, 255, 255))

    # Генерация случайной ситуации
    situation = generate_situation()

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
    for i in range(4):
        card_rect = pygame.Rect(card_x + i * (card_width + card_spacing), card_y, card_width, card_height)
        meme_image = pygame.image.load(memes[i])
        meme_image = pygame.transform.scale(meme_image, (card_width, card_height))
        screen.blit(meme_image, card_rect)

    # Обновление экрана
    pygame.display.flip()
