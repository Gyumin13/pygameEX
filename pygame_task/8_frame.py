# -*- coding: utf-8 -*-
import pygame
####################################################################
# �⺻ �ʱ�ȭ (�ݵ�� �ؾ� �ϴ� �͵�)
pygame.init()

# ȭ�� ũ�� ����
screen_width = 480 # ���� ũ��
screen_height = 640 # ���� ũ��
screen = pygame.display.set_mode((screen_width, screen_height))

# ȭ�� Ÿ��Ʋ ����
pygame.display.set_caption("Both Side Poker") # ���� �̸�

# FPS
clock = pygame.time.Clock()
######################################################################

# 1. ����� ���� �ʱ�ȭ (��� ȭ��, ���� �̹���, ��ǥ, �ӵ�, ��Ʈ ��)

running = True 
while running :
    dt = clock.tick(100) #

    # 2. �̺�Ʈ ó�� (Ű����, ���콺 ��)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

    # 3. ���� ĳ���� ��ġ ����
            
    # 4. �浹 ó��
            
    # 5. ȭ�� �׸���
            
    pygame.display.update()

pygame.time.delay(2000) 

pygame.quit()