import pygame
import random 
import os

verdict = True
try:
	os.mkdir("./.myfolder")
except:
	pass

while verdict:
	pygame.init()

	screen_width = 800
	screen_height = 600
	snake_block_width = 20
	food_block_width = snake_block_width
	blue = (0 , 0 , 255)
	red = (255 , 0 , 0)
	green = (0 , 255 , 0)
	black = (0 , 0 , 0 )
	white = (255 , 255, 255)
	blue = (0 , 0 , 255)
	brown = (219 , 84 , 6)
	font  = pygame.font.SysFont(None , 25)
	msg = 'Ohh!! Snake Crashed.. Press "P" to Play More and "Q" to Quit'
	crashed = False
	exit = False

	filename = open('./.myfolder/highscore.txt' , 'a+')

	snake_lead_x = screen_width * 0.45
	snake_lead_y = screen_height * 0.8
	snake_x_change = 0
	snake_y_change = 0
	snake_lead_x+=snake_x_change
	snake_lead_y+=snake_y_change
	score = 0
	speed = 40
	FPS = speed + score
	snakelist = []
	snakeinitiallength = 3
	snakelength = snakeinitiallength
	food_x = random.randint(0 , screen_width - food_block_width)
	food_y = random.randrange(0 , screen_height - food_block_width)
	highscore = filename.read()
	filename.close()
	
	if os.stat('./.myfolder/highscore.txt').st_size == 0:
		highscore = 0

	gameDisplay = pygame.display.set_mode((screen_width , screen_height))
	pygame.display.set_caption('My_Game')
	clock = pygame.time.Clock()

	for i in range(snakeinitiallength):
		snakeheadinitial = []
		snakeheadinitial.append(snake_lead_x + snake_block_width * i)
		snakeheadinitial.append(snake_lead_y)
		snakelist.append(snakeheadinitial)

	snake_lead_x = snake_lead_x + snake_block_width * (snakeinitiallength - 1)   

	def snake(snake_block_width , snakelist):
		i = 0
		for XY in snakelist:
			i = i + 1
			if i == len(snakelist):
				pygame.draw.rect(gameDisplay , brown , [XY[0] , XY[1] , snake_block_width , snake_block_width])	 
			else:
				pygame.draw.rect(gameDisplay , green , [XY[0] , XY[1] , snake_block_width , snake_block_width])

	def food_pos(food_x , food_y):
			food_x = round(food_x / 10.0) * 10.0
			food_y = round(food_y / 10.0) * 10.0

			pygame.draw.rect(gameDisplay , red , [food_x , food_y , food_block_width , food_block_width])

	def check_collision(snake_x , snake_y , snakelist):
		x_pos = screen_width / 4
		y_pos = screen_height / 2
		if snake_x < 0 or snake_x > screen_width - snake_block_width or snake_y < 0 or snake_y > screen_height - snake_block_width:
			color = red
			message_to_screen(msg , color , x_pos , y_pos)
			return True
		else:
			return self_collided(snake_lead_x , snake_lead_y , snakelist , x_pos , y_pos)

	def self_collided(snake_lead_x , snake_lead_y , snakelist , x_pos , y_pos):
		flag = 0
		for XY in snakelist:
			if snake_lead_x == XY[0] and snake_lead_y == XY[1]:
				flag = flag + 1
		if flag > snakeinitiallength:
			color = red
			message_to_screen(msg , color , x_pos , y_pos)
			return 	True
		else:
			return False

	def check_update(snake_x , snake_y , food_x , food_y , score , snakelength):
		if (snake_x >= food_x and snake_x <= food_x + food_block_width and snake_y >= food_y and snake_y <= food_y + food_block_width) or (snake_x >= food_x - snake_block_width and snake_x <= food_x + food_block_width - snake_block_width and snake_y >= food_y - snake_block_width and snake_y <= food_y + food_block_width - snake_block_width):
			score = score + 1
			snakelength = snakelength + 1
			food_x = random.randrange(0 , screen_width - snake_block_width)
			food_y = random.randrange(0 , screen_height - snake_block_width)

		return food_x , food_y , score , snakelength

	def message_to_screen(msg , color , x_pos , y_pos):
		screen_text = font.render(msg , True , color)
		gameDisplay.blit(screen_text , [x_pos , y_pos])

	def update_score(score):
		scoreboard = 'SCORE  ' + str(score)
		color = blue
		x_pos = (screen_width / 2) - 50
		y_pos = screen_height / 8
		message_to_screen(scoreboard , color , x_pos , y_pos)

	def update_highscore(highscore):
		highscoreboard = 'HIGHSCORE  ' + str(highscore)
		color = blue
		x_pos = (screen_width / 2) - 70
		y_pos = (screen_height / 8) + 30
		message_to_screen(highscoreboard , color , x_pos , y_pos)

	gameDisplay.fill(black)
	snake(snake_block_width , snakelist)
	print(snakelist)
	pygame.display.update()	
	get = False
	
	while not exit and not crashed:

		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:			
				exit = True
			
			if event.type == pygame.KEYDOWN:
				get = True
				if event.key == pygame.K_UP:
					snake_y_change = -snake_block_width
					snake_x_change = 0
				if event.key == pygame.K_DOWN:
					snake_y_change = snake_block_width
					snake_x_change = 0
				if event.key == pygame.K_LEFT:
					snake_x_change = -snake_block_width
					snake_y_change = 0
				if event.key == pygame.K_RIGHT:
					snake_x_change = snake_block_width
					snake_y_change = 0		
			
		if get:
			gameDisplay.fill(black)

		snake_lead_y+=snake_y_change	
		snake_lead_x+=snake_x_change	
		snakehead = []
		snakehead.append(snake_lead_x)
		snakehead.append(snake_lead_y)
		snakelist.append(snakehead)
		if len(snakelist) > snakelength:
			del snakelist[0]	
		
		food_pos(food_x , food_y)
		snake(snake_block_width , snakelist)
		print(snakelist)
		food_x , food_y , score , snakelength =  check_update(snake_lead_x , snake_lead_y , food_x , food_y , score , snakelength)
		
		if get:
			crashed = check_collision(snake_lead_x , snake_lead_y , snakelist)
		if int(score) > int(highscore):
			highscore = score
			filename = open('./.myfolder/highscore.txt' , 'w+')
			filename.write(str(highscore)) 
			filename.close()
		update_score(score) 
		update_highscore(highscore)
		pygame.display.update()
		clock.tick(FPS)

	if crashed:
		flag = False
		while not flag:
			for check_verdict in pygame.event.get():
				if check_verdict.type == pygame.KEYDOWN:
					if check_verdict.key == pygame.K_p:
						flag = True
						verdict = True
						break;
					elif check_verdict.key == pygame.K_q:
						flag = True
						verdict = False		
						break;
					else:
						flag = False			

pygame.quit()
quit()	 