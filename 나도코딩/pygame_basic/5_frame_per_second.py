import pygame

pygame.init()   #초기화(반드시 필요)

#화면크기
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))  # 튜플형식

#화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임이름

#FPS
clock = pygame.time.Clock()

#배경이미지 불러오기
background = pygame.image.load("C:\\Users\\onesd\\Desktop\\python work\\나도코딩\\pygame_basic\\background.png")

# 캐릭터 (스프라이트)  불러오기
character = pygame.image.load("C:\\Users\\onesd\\Desktop\\python work\\나도코딩\\pygame_basic\\character.png")
character_size = character.get_rect().size  #이미지의 크기를 구해줌
character_width = character_size[0] #캐릭터의 가로크기
character_height = character_size[1] #캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) #화면가로의 절반크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면세로크기 가장 아래에 해당하는 곳에 위치


# 이동할 좌표

to_x = 0
to_y = 0

# 이동속도
character_speed = 0.6

# 이벤트 루프
running = True # 게임은 진행중인가
while running :
    dt = clock.tick(60)  # 게임화면의 초장 프레임 수를 설정

    print ("fps : ", str(clock.get_fps()))

    for event in pygame.event.get() :  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT :   # 창이 닫히는 에벤트가 발생하였는가?
            running = False  #게임진행중이 아님

        if event.type == pygame.KEYDOWN :  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT : 
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT :
                to_x += character_speed
            elif event.key == pygame.K_UP :
                to_y -= character_speed
            elif event.key == pygame.K_DOWN :
                to_y += character_speed

        if event.type == pygame.KEYUP : #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계갑 처리
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height :
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0))  #(0,0)은 시작좌표 배경그리기

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # 게임화면 다시 그리기 !!

#pygame 종료
pygame.quit()
 