import pygame
import sys
import random

# Pygame 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("알파벳과 숫자/기호 게임")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 폰트 설정
font = pygame.font.Font(None, 40)

# 게임판 데이터 구조 정의
# 각 칸에는 알파벳, 숨겨진 내용(숫자/기호), 상태(공개됨/숨겨짐)을 저장
class Cell:
    def __init__(self, letter, hidden_content):
        self.letter = letter
        self.hidden_content = hidden_content
        self.revealed = False

# 랜덤한 영어 알파벳 생성 (중복 없음)
def generate_random_letters(num_letters=16):
    # 전체 알파벳 리스트에서 num_letters만큼 랜덤하게 선택
    letters = random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', num_letters)
    return letters

# 숫자와 연산기호를 포함한 숨겨진 내용 생성
def generate_hidden_contents():
    # 1부터 12까지의 숫자 중에서 중복 없이 12개 선택
    numbers = random.sample(range(1, 13), 12)
    # 연산기호 추가
    operators = ['+', '-', '*', '/']
    # 숫자와 연산기호 결합
    contents = numbers + operators
    # 전체 내용을 무작위로 섞음
    random.shuffle(contents)
    return contents

# 숨겨진 내용 초기화
hidden_contents = generate_hidden_contents()

# 게임판 초기화
letters = generate_random_letters()
board = [Cell(letter, hidden_contents[i]) for i, letter in enumerate(letters)]

# 클릭 이벤트 처리 함수
def handle_click(pos):
    cell_size = 100
    for index, cell in enumerate(board):
        col = index % 4
        row = index // 4
        x = col * cell_size + (screen_width - 4 * cell_size) / 2
        y = row * cell_size + (screen_height - 4 * cell_size) / 2
        if x <= pos[0] <= x + cell_size and y <= pos[1] <= y + cell_size:
            cell.revealed = True
            return True  # 칸이 공개됨
    return False  # 클릭된 칸이 없음

# 게임 시작 시간 기록
start_ticks = pygame.time.get_ticks()  # 시작 시간을 저장

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            handle_click(pos)
    
    # 현재 시간에서 게임 시작 시간을 빼서 경과 시간 계산
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # milliseconds to seconds

    screen.fill(BLACK)

    # 게임판 그리기
    cell_size = 100
    for index, cell in enumerate(board):
        col = index % 4
        row = index // 4
        x = col * cell_size + (screen_width - 4 * cell_size) / 2
        y = row * cell_size + (screen_height - 4 * cell_size) / 2
        pygame.draw.rect(screen, WHITE, (x, y, cell_size, cell_size), 1)
        
        # 첫 10초 동안 숨겨진 내용을 보여주고, 그 후에는 알파벳만 보여줌
        if seconds < 5:
            text_content = str(cell.hidden_content)  # 숨겨진 내용 보여주기
        else:
            if cell.revealed:
                text_content = str(cell.hidden_content)  # 공개된 칸은 숨겨진 내용 보여주기
            else:
                text_content = cell.letter  # 아직 공개되지 않은 칸은 알파벳 보여주기
        text = font.render(text_content, True, WHITE)
        text_rect = text.get_rect(center=(x + cell_size / 2, y + cell_size / 2))
        screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()