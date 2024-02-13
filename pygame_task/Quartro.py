import pygame
import sys
import random

pygame.init()

# 화면 크기 설정
screen_width = 1200  # 가로 크기
screen_height = 800  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("QUARTRO")  # 게임 이름

# FPS
clock = pygame.time.Clock()

# 게임 상태
player_hand = []
computer_hand = []
turn = "player"  # 시작은 플레이어의 차례로 설정

selected_card = None  # 플레이어가 선택한 카드

# 카드 이미지 로드 및 크기 조절
card_images = [
    pygame.transform.scale(pygame.image.load(f"card2.jpg"), (100, 200)),  # 0카드
    pygame.transform.scale(pygame.image.load(f"card2.jpg"), (100, 200)),  # 1카드
    pygame.transform.scale(pygame.image.load(f"card2.jpg"), (100, 200)),  # 2카드
    pygame.transform.scale(pygame.image.load(f"card2.jpg"), (100, 200)),  # 3카드
    pygame.transform.scale(pygame.image.load(f"card2.jpg"), (100, 200)),  # 4카드
    pygame.transform.scale(pygame.image.load(f"card2.jpg"), (100, 200)),  # 5카드
]

# 0카드는 검정색으로 설정
card_colors = [(0, 0, 0)] + [(255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 0, 255)]  # 빨강, 초록, 노랑, 파랑

def deal_cards():
    numbers = list(range(1, 7))
    colors = list(range(1, 5))
    
    all_cards = [(number, color) for number in numbers for color in colors] * 2
    random.shuffle(all_cards)
    
    # 중복된 숫자와 색상 체크
    while any(all_cards[i] == all_cards[i + 1] for i in range(len(all_cards) - 1)):
        random.shuffle(all_cards)

    player_hand = [card[0] for card in all_cards[:4]]
    computer_hand = [card[0] for card in all_cards[4:8]]
    
    return player_hand, computer_hand

def draw_screen(player_hand):
    screen.fill((255, 255, 255))  # 화면을 흰색으로 지우기

    # 여기에 화면에 그려야 할 내용을 추가
    draw_player_hand(player_hand)

    pygame.display.update()  # 화면 업데이트

def draw_player_hand(player_hand):
    card_spacing = 20  # 카드 간격

    for i, card in enumerate(player_hand):
        if selected_card == i:
            card_image = pygame.transform.flip(card_images[card], True, False)
        else:
            card_image = card_images[card]

        card_rect = card_image.get_rect()
        card_rect.topleft = (i * (card_rect.width + card_spacing) + 50, screen_height - card_rect.height - 50)
        screen.blit(card_image, card_rect)

        if selected_card is not None and selected_card == i:
            # 선택한 카드의 숫자와 색깔을 화면에 표시
            font = pygame.font.Font(None, 36)
            color = card_colors[card] if 0 <= card < len(card_colors) else (0, 0, 0)
            text = font.render(str(card), True, color)
            text_rect = text.get_rect(center=card_rect.center)
            screen.blit(text, text_rect)

# 초기화
player_hand, computer_hand = deal_cards()

running = True
while running:
    dt = clock.tick(30)  # 30 FPS로 설정

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            # 마우스 클릭한 위치가 카드의 영역 안인지 확인
            for i, card in enumerate(player_hand):
                card_rect = card_images[card].get_rect()
                card_rect.topleft = (i * (card_rect.width + 20) + 50, screen_height - card_rect.height - 50)
                if card_rect.collidepoint(x, y):
                    selected_card = i
                    break

    draw_screen(player_hand)  # 화면 그리기

pygame.time.delay(2000)

pygame.quit()
sys.exit()