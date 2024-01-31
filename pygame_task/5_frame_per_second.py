# -*- coding: utf-8 -*-
import pygame

pygame.init() # �ʱ�ȭ (�ݵ�� �ʿ�)

# ȭ�� ũ�� ����
screen_width = 480 # ���� ũ��
screen_height = 640 # ���� ũ��
screen = pygame.display.set_mode((screen_width, screen_height))

# ȭ�� Ÿ��Ʋ ����
pygame.display.set_caption("Brilliant") # ���� �̸�

# FPS
clock = pygame.time.Clock()

# ��� �̹��� �ҷ�����
background = pygame.image.load("C:/Users/user/Desktop/PygameMadeByGM/pygame_task/Background.png")

# ĳ����(��������Ʈ) �ҷ�����
character = pygame.image.load("C:/Users/user/Desktop/PygameMadeByGM/pygame_task/character.png")
character_size = character.get_rect().size # �̹����� ũ�⸦ ���ؿ�
character_width = character_size[0] # ĳ������ ���� ũ��
character_height = character_size[1] # ĳ������ ���� ũ��
character_x_pos = screen_width / 2 - character_width / 2 # ȭ�� ������ ���� ũ�⿡ �ش��ϴ� ���� ���� ��ġ
character_y_pos = screen_height - character_height # ȭ�� ���� ũ�� ���� �Ʒ��� �ش��ϴ� ���� ���� ��ġ

#�̵��� ��ǥ
to_x = 0
to_y = 0

#�̵� �ӵ�
character_speed = 0.5

# �̺�Ʈ ����
running = True # ������ �������ΰ�?
while running :
    dt = clock.tick(100) # ���� ȭ���� �ʴ� ������ ���� ����

# ĳ���Ͱ� 100 ��ŭ �̵��� �ؾ� ��
# 10 fps : 1�� ���� 10�� ���� 
# 20 fps : 1�� ���� 20�� ����

    print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get(): # � �̺�Ʈ�� �߻��Ͽ��°�?
        if event.type == pygame.QUIT: # â�� ������ �̺�Ʈ�� �߻��Ͽ��°�?
            running = False # ������ �������� �ƴ�

        if event.type == pygame.KEYDOWN: # Ű�� ���ȴ��� Ȯ��
            if event.key == pygame.K_LEFT: # ĳ���͸� ��������
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: 
                to_x += character_speed
            elif event.key == pygame.K_UP: 
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: 
                to_y += character_speed

        if event.type == pygame.KEYUP: #����Ű�� ���� ����
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
            
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # ���� ��谪 ó��
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #���� ��谪 ó��
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
    # screen.fill((0, 0, 105))
    screen.blit(background, (0, 0)) # ��� �׸���

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # ����ȭ���� �ٽ� �׸���!

# pygame ����
pygame.quit()