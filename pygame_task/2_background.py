# -*- coding: utf-8 -*-
import pygame

pygame.init() # �ʱ�ȭ (�ݵ�� �ʿ�)

# ȭ�� ũ�� ����
screen_width = 480 # ���� ũ��
screen_height = 640 # ���� ũ��
screen = pygame.display.set_mode((screen_width, screen_height))

# ȭ�� Ÿ��Ʋ ����
pygame.display.set_caption("Brilliant") # ���� �̸�

# ��� �̹��� �ҷ�����
background = pygame.image.load("C:/Users/user/Desktop/PygameMadeByGM/pygame_task/Background.png")

# �̺�Ʈ ����
running = True # ������ �������ΰ�?
while running :
    for event in pygame.event.get(): # � �̺�Ʈ�� �߻��Ͽ��°�?
        if event.type == pygame.QUIT: # â�� ������ �̺�Ʈ�� �߻��Ͽ��°�?
            running = False # ������ �������� �ƴ�
    
    # screen.fill((0, 0, 105))
    screen.blit(background, (0, 0)) # ��� �׸���

    pygame.display.update() # ����ȭ���� �ٽ� �׸���!

# pygame ����
pygame.quit()