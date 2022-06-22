from tkinter import *
from math import *  
from time import *
from random import *
from DecimalToHex import *


root = Tk()
root.title("Social Media Marketing Simulator")
screen = Canvas(root, width=1000, height=600, background="black")


#Creates an array of 3000 most common words in english
a_file = open("assets/3000commonWords.txt", "r")

easyWords = []
for line in a_file:
  commonWord = line.strip()
  easyWords.append(commonWord)

a_file.close()


def setInitialValues():
	global health, score, totalWords, timeTillNextWord, teslaHealthImg, teslaHealthDrawing1, teslaHealthDrawing2, teslaHealthDrawing3
	global xTesla, yTesla, xMusk, yMusk, teslaSpeed, muskSpeed, elonMusk, tesla, teslaDrawing, elonDrawing
	global wordSpeed, xWord, yWord, colours, wordDrawings, word, currentWords, easyWordList
	global typeWordDrawing, scoreDrawing, typeWordHereDrawing
	global startTime, teslaRed, wordColors, scoreColor, socialMediaDrawings, twitter, discord, instagram, logoDrawings
	global end, teslaRed, username , blackPaper, blackPaperBackground, leaderBoardScreen, normalButton 
	global hoverButton, menuScreen, playButtonDrawing, restartButtonDrawing, xMouse, yMouse, helpButtonDrawing, helpScreen
	global difficultyScreen, easyButtonDrawing, hardButtonDrawing, mediumButtonDrawing, easyExplaination, mediumExplaination, hardExplaination
	global easy, medium, hard, wordLengthMax, wordLengthMin, pointsEarned, warningText, bitcoin, bitcoinDrawing, elonSmile, elonSmileDrawing
	global elonSmileRotate, elonSmileRotateDrawing, elonNeutral, elonNeutralDrawing, elonNeutralRotate, elonNeutralRotateDrawing
	global elonFrown, elonFrownDrawing, elonFrownRotate, elonFrownRotateDrawing, socialBackground, social, story
	global objective, objectiveText, menuButtonDrawing


	word = ""
	xWord = []
	yWord = []
	colours = []
	wordColors = []
	wordDrawings = []
	wordSpeed = 3
	currentWords = []
	easyWordList = ['Dogecoin', 'Tesla', 'SpaceX', 'Elon Musk', 'Cryptocurrency']
	teslaRed = '#cc0000'
	username = 'Elon Musk'
	pointsEarned = 0

	#Adds the 3000 common words to the custom words I've added
	easyWordList.extend(easyWords)

	score = 0
	health = 3
	totalWords = 0
	xMouse = 0
	yMouse = 0 
	story = 0
	objective = 0

	typeWordDrawing = 0
	scoreDrawing = 0
	teslaDrawing = 0
	elonDrawing = 0
	typeWordHereDrawing = 0
	timeTillNextWord = 0
	teslaHealthDrawing1 = 0
	teslaHealthDrawing2 = 0
	teslaHealthDrawing3 = 0
	blackPaperBackground = 0
	playButtonDrawing = 0
	restartButtonDrawing = 0
	helpButtonDrawing = 0
	easyButtonDrawing = 0
	mediumButtonDrawing = 0
	hardButtonDrawing = 0
	easyExplaination = 0
	mediumExplaination = 0
	hardExplaination = 0
	warningText = 0
	bitcoinDrawing = 0
	elonSmileDrawing = 0 
	elonSmileRotateDrawing = 0
	elonNeutralDrawing = 0
	elonNeutralRotateDrawing = 0
	elonFrownRotateDrawing = 0
	elonFrownDrawing = 0
	socialBackground = 0
	objectiveText = 0
	menuButtonDrawing = 0
	socialMediaDrawings = []
	logoDrawings = []

	scoreColor = '#B0FC38'

	elonMusk = PhotoImage(file = "assets/elon.png")
	tesla = PhotoImage(file = "assets/tesla.png")
	teslaHealthImg = PhotoImage(file = "assets/tesla model x.png")
	twitter = PhotoImage(file = "assets/twitter.png")
	discord = PhotoImage(file = "assets/discord.png")
	instagram = PhotoImage(file = "assets/instagram.png")
	blackPaper = PhotoImage(file = "assets/black paper.png")
	normalButton = PhotoImage(file = "assets/Normal Button.png")
	hoverButton = PhotoImage(file = "assets/Hover Button.png")
	bitcoin = PhotoImage(file = "assets/bitcoin.png")
	elonSmile = PhotoImage(file = "assets/elonSmile.png")
	elonSmileRotate = PhotoImage(file = "assets/elonSmile Rotate.png")
	elonNeutral = PhotoImage(file = "assets/elonNeutral.png")
	elonNeutralRotate = PhotoImage(file = "assets/elonNeutral Rotate.png")
	elonFrown = PhotoImage(file = "assets/elonFrown.png")
	elonFrownRotate = PhotoImage(file = "assets/elonFrown Rotate.png")
	social = PhotoImage(file = "assets/social.png")


	teslaSpeed = 0
	muskSpeed = 0
	xTesla = 900
	yTesla = 300
	xMusk = 75
	yMusk = 50

	wordLengthMax = 0
	wordLengthMin = 0

	end = False
	leaderBoardScreen = False
	menuScreen = True
	helpScreen = False
	difficultyScreen = False
	easy = False
	medium = False
	hard = False


#Function that changes the color of the text as it runs across the screen
def getColor(xPos):
	green = floor((xPos-1)/999*256)
	redHexVal = getHexValue( green )
	greenHexVal = getHexValue( 255 - green )

	wordColor = "#" + redHexVal + greenHexVal +"00" 

	return wordColor



#Changes the score color everytime the user presses enter
def netWorthColor(currentColor):
	global scoreColor

	if currentColor == '#B0FC38':
		scoreColor = '#AEF359'
	
	elif currentColor == '#AEF359':
		scoreColor = '#74B72E'

	elif currentColor == '#74B72E':
		scoreColor = '#028A0F'

	elif currentColor == '#028A0F':
		scoreColor = '#B0FC38'
	


#Draws initial drawings that do not change throughout the game 
def initialDrawings():
	global textBoxDrawing, typeWordHereDrawing, teslaHealthDrawing1, teslaHealthDrawing2,teslaHealthDrawing3, healthDrawing

	screen.create_image( 500, 300, image = blackPaper)

	textBoxDrawing = screen.create_rectangle(200, 500, 700,550, fill='white')

	typeWordHereDrawing = screen.create_text(225, 525, anchor='w', text='Type words here...', fill='gray')

	#Health Bar
	teslaHealthDrawing1 = screen.create_image( 950, 35, image = teslaHealthImg)

	teslaHealthDrawing2 = screen.create_image( 900, 35, image = teslaHealthImg)

	teslaHealthDrawing3 = screen.create_image( 850, 35, image = teslaHealthImg)

	healthDrawing = screen.create_text(820, 35, anchor = 'e', text='Health:', fill=teslaRed, font='Helvletica 16')


#Draws the changing objects onto the screen
def drawObjects():
	global elonDrawing, teslaDrawing, typeWordDrawing, scoreDrawing, typeWordHereDrawing, wordDrawings, socialMediaDrawings


	elonDrawing = screen.create_image(xMusk, yMusk, image = elonMusk)

	typeWordDrawing = screen.create_text(225, 525, text=word, font = 'Helvetica 16', fill='black', anchor = 'w')

	scoreDrawing = screen.create_text(125, 50, text=f'Net Worth: ${score}', font = 'Times 16', fill=scoreColor, anchor = 'w')
	
	
	#Determines the color of the text
	for x in range(len(currentWords)):
		wordColors[x-1] = getColor(xWord[x-1])


	#Draws the words on the canvas
	for x in range(len(currentWords)):
		wordDrawings[x-1] = screen.create_text(xWord[x-1], yWord[x-1], font='Times 16', fill=wordColors[x-1], text=currentWords[x-1], anchor = 'e')

		socialMediaDrawings[x-1] = screen.create_image( xWord[x-1]+20, yWord[x-1], image = logoDrawings[x-1])
		

#Chooses a random social media logo for each text
def chooseRandomImage():
	global twitter, instagram, discord

	listOfSocialMedia = []
	listOfSocialMedia.append(twitter)
	listOfSocialMedia.append(instagram)
	listOfSocialMedia.append(discord)

	return choice(listOfSocialMedia)


#Draws all objects on the screen again with updated positions/values
def updateObjects():
	global xTesla, yTelsa, xMusk, yMusk, timeTillNextWord, elapsedTime, currentWords, xWord, yWord, wordDrawings, currentWords, health, logoDrawings, secondsUntilNextWord, wordSpeed, wpmSpeedUp


	#Generates a new word every certain amount of seconds
	if timeTillNextWord < elapsedTime:

		randomWord = choice(easyWordList)

		#Keep choosing a random word until one that works is chosen
		if easy == True:
			while len(randomWord) > wordLengthMax:
				randomWord = choice(easyWordList)
		

		elif medium == True or hard == True:
			while len(randomWord) < wordLengthMin:
				randomWord = choice(easyWordList)

		currentWords.append(randomWord)

		#The time until the next word appears gradually gets lower
		
		secondsUntilNextWord = 60/startWPM - elapsedTime/wpmSpeedUp


		#If the current WPM is greater than the max WPM
		if 60/secondsUntilNextWord > maxWPM or 60/secondsUntilNextWord < 0:
			secondsUntilNextWord = 60/maxWPM
		
		timeTillNextWord += secondsUntilNextWord


		#Generates a random y coordinate for the word to spawn on 
		yPos = randint(100, 475)

		xWord.append(0)
		yWord.append(yPos)

		#If the words overlap generate a new coordinate
		if len(yWord) > 1:
			while yPos+35 >= yWord[-2] and yPos-35 <= yWord[-2]:
				yPos = randint(100, 475)
				
			
		yWord.pop(-1)
		yWord.append(yPos)

		wordDrawings.append(0)
		wordColors.append(0)
		socialMediaDrawings.append(0)
		logoDrawings.append(chooseRandomImage())


	#Moves the words to the right of the screen
	for i in range(len(currentWords)):
		xWord[i-1] += wordSpeed


	#Removes words that are too far right
	for x in range(len(currentWords)):
		if (xWord[x-1] > 1000):
			xWord.pop(x-1)
			yWord.pop(x-1)
			wordDrawings.pop(x-1) 
			currentWords.pop(x-1)
			wordColors.pop(x-1)
			socialMediaDrawings.pop(x-1)
			logoDrawings.pop(x-1)

			health -= 1
		

	#Don't even think of putting an animation loop here.  No update(), no sleep(), no delete(), 


#Mouse click binding  
def mouseClickHandler(event):
	global leaderBoardScreen, menuScreen, easy, medium, hard, difficultyScreen, clicks, storyText, helpScreen, screen2, mButtonX

	#If the game has ended, a mouse click on the restart button will restart the game
	if leaderBoardScreen == True:

		#Ensures the mouse is on the restart button
		if xMouse < 500 + 100 and xMouse > 500 - 100 and yMouse < 510 + 38 and yMouse > 510 - 38:
			leaderBoardScreen == False
			screen.delete('all')
			runGame()
	

	#On the menu screen
	if menuScreen == True:

		#Ensures the mouse is on the play button
		if xMouse < pButtonX + 100 and xMouse > pButtonX - 100 and yMouse < 300 + 38 and yMouse > 300 - 38:
			menuScreen = False
			screen.delete('all')
			chooseDifficulty()

		#Ensures the mouse is on the help button
		if xMouse < hButtonX + 100 and xMouse > hButtonX - 100 and yMouse < 400 + 38 and yMouse > 400 - 38:
			menuScreen = False
			screen.delete('all')
			help()

		#Ensures the mouse is on the rankings button
		if xMouse < hButtonX + 100 and xMouse > hButtonX - 100 and yMouse < 500 + 38 and yMouse > 500 - 38:
			menuScreen = False
			screen.delete('all')
			draw_end_screen()
	

	#On the choose difficulty screen
	if difficultyScreen == True:

		#Ensures the mouse is on the EASY button
		if xMouse < eButtonX + 100 and xMouse > eButtonX - 100 and yMouse < 200 + 38 and yMouse > 200 - 38:
			easy = True
			difficultyScreen = False
			screen.delete('all')
		

		#Ensures the mouse is on the MEDIUM button
		if xMouse < eButtonX + 100 and xMouse > eButtonX - 100 and yMouse < 300 + 38 and yMouse > 300 - 38:
			medium = True
			difficultyScreen = False
			screen.delete('all')

		
		#Ensures the mouse is on the HARD button
		if xMouse < eButtonX + 100 and xMouse > eButtonX - 100 and yMouse < 400 + 38 and yMouse > 400 - 38:
			hard = True
			difficultyScreen = False
			screen.delete('all')


		#Ensures the mouse is on the MENU button
		if xMouse < mButtonX + 100 and xMouse > mButtonX - 100 and yMouse < 530 + 38 and yMouse > 530 - 38:
			screen.delete('all')
			difficultyScreen = False
			menuScreen = True
			menu()

	
	#Clicking on the help screen
	if helpScreen == True:

		#Story screen
		if clicks == 0:
			screen.delete(storyText,story)
			clicks += 1

		#Objective screen
		elif clicks == 1 and screen2 == True:
			screen.delete('all')
			helpScreen = False

			#Return to menu screen
			menuScreen = True
			menu() 
			
		

#Choose a difficulty after pressing play
def chooseDifficulty():
	global easyDifficulty, mediumDifficulty, hardDifficulty, difficultyScreen, easyButtonDrawing, mediumButtonDrawing, hardButtonDrawing, easyExplaination, mediumExplaination, hardExplaination, eButtonX, word, username, warningText, elonSmileDrawing, elonSmileRotateDrawing, elonNeutralDrawing, elonNeutralRotateDrawing, elonFrownDrawing, elonFrownRotateDrawing, menuButtonDrawing, mButtonX

	difficultyScreen = True
	eButtonX = 300
	word = ''
	mButtonX = 800

	#Paper background
	screen.create_image( 500, 300, image = blackPaper)

	#Choose your difficulty text 
	screen.create_text(eButtonX, 100, text='Choose Difficulty', fill='red', font='Times 35', anchor = 'c')

	#Username Textbox
	screen.create_rectangle(200, 500, 475,550, fill='white')

	#Username Drawing (Text)
	screen.create_text(190, 525, text='Username:', fill='red', font='Times 20', anchor = 'e')

	unnamedText = screen.create_text(215, 525, text='Type username here', font = 'Helvetica 16', fill='gray', anchor = 'w')


	while difficultyScreen == True:

		#Easy Button no Hover
		if xMouse > eButtonX + 100 or xMouse < eButtonX - 100 or yMouse > 200 + 38 or yMouse < 200 - 38:
			easyButtonDrawing = screen.create_image( eButtonX, 200, image = normalButton)

			#Picture of elon smiling next to easy difficulty
			elonSmileDrawing = screen.create_image( 150, 200, image = elonSmile)


		#Easy Button with Hover / Explaination
		elif xMouse < eButtonX + 100 and xMouse > eButtonX - 100 and yMouse < 200 + 38 and yMouse > 200 - 38:
			easyButtonDrawing = screen.create_image( eButtonX, 200, image = hoverButton)

			easyExplaination = screen.create_text(500, 250, text='Easy:\n- Words are no longer than 6 letters\n- +100 points for each word typed\n- Maximum 50 wpm\n- Starts at 30 wpm\n- Words start speeding up\n  after reaching 50 wpm', fill='yellow', font='Times 20', anchor = 'w')

			#Picture of elon smiling next to easy difficulty
			elonSmileRotateDrawing = screen.create_image( 150, 200, image = elonSmileRotate)

		#Easy text 
		easyText = screen.create_text(eButtonX, 200, text='Easy', fill='yellow', font='Times 20', anchor = 'c')



		#Medium Button no Hover
		if xMouse > eButtonX + 100 or xMouse < eButtonX - 100 or yMouse > 300 + 38 or yMouse < 300 - 38:
			mediumButtonDrawing = screen.create_image( eButtonX, 300, image = normalButton)

			#Picture of elon neutral next to medium difficulty
			elonNeutralDrawing = screen.create_image( 150, 300, image = elonNeutral)


		#Medium Button with Hover / Explaination
		elif xMouse < eButtonX + 100 and xMouse > eButtonX - 100 and yMouse < 300 + 38 and yMouse > 300 - 38:
			mediumButtonDrawing = screen.create_image( eButtonX, 300, image = hoverButton)

			mediumExplaination = screen.create_text(500, 250, text='Medium:\n- Words are no shorter\n  than 5 letters\n- +300 points for each word typed\n- Starts at 30 wpm\n- Maximum 60 wpm\n- Words start speeding up\n  after reaching 60 wpm', fill='yellow', font='Times 20', anchor = 'w')

			#Picture of elon neutral next to medium difficulty
			elonNeutralRotateDrawing = screen.create_image( 150, 300, image = elonNeutralRotate)


		#Medium text 
		mediumText = screen.create_text(eButtonX, 300, text='Medium', fill='yellow', font='Times 20', anchor = 'c')

	

		#Hard Button no Hover
		if xMouse > eButtonX + 100 or xMouse < eButtonX - 100 or yMouse > 400 + 38 or yMouse < 400 - 38:
			hardButtonDrawing = screen.create_image( eButtonX, 400, image = normalButton)

			#Picture of elon sunglasses next to hard difficulty
			elonFrownDrawing = screen.create_image( 150, 400, image = elonFrown)


		#Hard Button with Hover / Explaination
		elif xMouse < eButtonX + 100 and xMouse > eButtonX - 100 and yMouse < 400 + 38 and yMouse > 400 - 38:
			hardButtonDrawing = screen.create_image( eButtonX, 400, image = hoverButton)

			hardExplaination = screen.create_text(500, 250, text='Hard:\n- Words are no shorter\n  than 6 letters\n- +500 points for each word typed\n- Starts at 40 wpm\n- Maximum 80 wpm\n- Words start speeding up\n  after reaching 80 wpm', fill='yellow', font='Times 20', anchor = 'w')

			#Picture of elon sunglasses next to hard difficulty
			elonFrownRotateDrawing = screen.create_image( 150, 400, image = elonFrownRotate)


		#Hard text 
		hardText = screen.create_text(eButtonX, 400, text='Hard', fill='yellow', font='Times 20', anchor = 'c')


		#Username typed in shows up on screen
		typeWordDrawing = screen.create_text(215, 525, text=word, font = 'Helvetica 16', fill='black', anchor = 'w')



		#Menu button no hover
		if xMouse > mButtonX + 100 or xMouse < mButtonX - 100 or yMouse > 400 + 38 or yMouse < 400 - 38:
			menuButtonDrawing = screen.create_image( mButtonX, 530, image = normalButton)

		
		#Menu button with hover
		if xMouse < mButtonX + 100 and xMouse > mButtonX - 100 and yMouse < 530 + 38 and yMouse > 530 - 38:
			menuButtonDrawing = screen.create_image( mButtonX, 530, image = hoverButton)


		#Menu Text
		menuText = screen.create_text(mButtonX, 530, text='Menu', fill='yellow', font='Times 20', anchor = 'c')


		#Username is too long warning 
		if len(word) >= 13:
			warningText = screen.create_text(500, 525, text='Your Username is too long!', font = 'Times 20', fill='yellow', anchor = 'w')
			word = word[:-1]

		
		screen.update()
		sleep(0.03)
		screen.delete(easyButtonDrawing, easyText, easyExplaination, hardText, mediumText, mediumExplaination, hardExplaination, hardButtonDrawing, mediumButtonDrawing, typeWordDrawing, warningText, elonSmileDrawing, elonSmileRotateDrawing, elonNeutralDrawing, elonNeutralRotateDrawing, elonFrownDrawing, elonFrownRotateDrawing, menuButtonDrawing, menuText)

		if word != '':
			screen.delete(unnamedText)
	
	#If the username is not too long
	if len(word) < 13 and len(word) != 0:
		username = word


	else:
		username = 'Unnamed Musk'


	word = ''
	set_difficulty_values()


#Sets game values based on the difficulty
def set_difficulty_values():
	global easy, medium, hard, wordLengthMax, wordLengthMin, pointsEarned, maxWPM, startWPM, wpmSpeedUp

	#Easy difficulty
	if easy == True:
		pointsEarned = 100
		maxWPM = 50
		wordLengthMax = 6
		startWPM = 30
		wpmSpeedUp = 60


	#Medium difficulty
	elif medium == True:
		pointsEarned = 300
		maxWPM = 60
		wordLengthMin = 5
		startWPM = 30
		wpmSpeedUp = 90


	#Hard difficulty
	elif hard == True:
		pointsEarned = 500
		maxWPM = 80
		wordLengthMin = 6
		startWPM = 40
		wpmSpeedUp = 120



#The menu screen
def menu():
	global playButtonDrawing, helpButtonDrawing, pButtonX, hButtonX, rankingDrawing

	x = 0
	pButtonX = 500
	hButtonX = 500

	#Paper background
	screen.create_image( 500, 300, image = blackPaper)
	

	while menuScreen == True:
		adjY = 0
		adjX = 0

		# sin(x/45)*10
		# cos(x/90)*15

		#Background for title text
		titleBackground = screen.create_rectangle(100+adjX, 40+adjY,900+adjX, 200+adjY, fill='#d3d3d3', outline='')

		#Title/Logo Text 
		socialMedia = screen.create_text(500+adjX, 80+adjY, text='Social Media', fill='red', font='Times 50', anchor = 'c')

		marketingSim = screen.create_text(500+adjX, 150+adjY, text='Marketing Simulator', fill='red', font='Times 50', anchor = 'c')


		#Play button no hover
		if xMouse > pButtonX + 100 or xMouse < pButtonX - 100 or yMouse > 300 + 38 or yMouse < 300 - 38:
			playButtonDrawing = screen.create_image( pButtonX, 300, image = normalButton)

		#Play button with mouse hover
		if xMouse < pButtonX + 100 and xMouse > pButtonX - 100 and yMouse < 300 + 38 and yMouse > 300 - 38:
			playButtonDrawing = screen.create_image( pButtonX, 300, image = hoverButton)

		#Play Text
		playText = screen.create_text(pButtonX, 300, text='Play', fill='yellow', font='Times 20', anchor = 'c')


		#Help button no hover
		if xMouse > hButtonX + 100 or xMouse < hButtonX - 100 or yMouse > 400 + 38 or yMouse < 400 - 38:
			helpButtonDrawing = screen.create_image( pButtonX, 400, image = normalButton)

		#Help button with mouse hover
		if xMouse < hButtonX + 100 and xMouse > hButtonX - 100 and yMouse < 400 + 38 and yMouse > 400 - 38:
			helpButtonDrawing = screen.create_image( pButtonX, 400, image = hoverButton)

		#Help Text
		helpText = screen.create_text(hButtonX, 400, text='Help', fill='yellow', font='Times 20', anchor = 'c')



		#Ranking button no hover
		if xMouse > hButtonX + 100 or xMouse < hButtonX - 100 or yMouse > 500 + 38 or yMouse < 500 - 38:
			rankingDrawing = screen.create_image( pButtonX, 500, image = normalButton)


		#Ranking button with hover
		if xMouse < hButtonX + 100 and xMouse > hButtonX - 100 and yMouse < 500 + 38 and yMouse > 500 - 38:
			rankingDrawing = screen.create_image( pButtonX, 500, image = hoverButton)


		#Rankings Text
		rankingsText = screen.create_text(hButtonX, 500, text='Rankings', fill='yellow', font='Times 20', anchor = 'c')


		screen.update()
		sleep(0.03)
		screen.delete(socialMedia, marketingSim, titleBackground, playButtonDrawing, playText, helpText, helpButtonDrawing, rankingDrawing, rankingsText)
		x += 1
		

#Help screen with instructions on how to play the game
def help():
	global helpScreen, socialBackground, clicks, storyText, story, objective, objectiveText, screen2

	clicks = 0
	helpScreen = True
	screen2 = False

	#Background
	socialBackground = screen.create_image( 500, 300, image = social)

	#Story text 
	story = screen.create_text(100, 50, text='Story', fill='red', font='Times 25', anchor = 'w')

	storyText = screen.create_text(50, 250, text='Growing up, you were surrounded by computers and technology.\nYou spent most of your time indoors on social media and video\ngames. As a result, you are very proficient in using computers\nand your typing speed exceeds the speed of sound. However, you\njust turned 18 and you needed a job to finance yourself.\n\nYour job application to Starbucks has caught the attention of\nElon Musk and he has hired you to be TESLA\'s social media\nmarketer.', fill='yellow', font='Times 20', anchor = 'w')

	#Click to Continue text
	screen.create_text(500, 550, text='Click to continue...', fill='white', font='Times 14', anchor = 'c')

	while True:

		#Objective block of text
		if clicks == 1:
			objective = screen.create_text(100, 50, text='Objective', fill='red', font='Times 25', anchor = 'w')

			objectiveText = screen.create_text(50, 300, text='As TESLA\'s Social Media Marketer, you must increase Elon Musk\'s\nsphere of inflence on social media and repel those who try and ruin\nhis reputation. Manage Elon Musk\'s social media accounts by\ntyping the words that come onto the screen. If a word reaches the\nright side of the screen before you type it, you lose a life and are\none step closer to being fired.\n\nBecause Elon is so generous, you have 3 lives/chances to screw\nup before being fired. Each word you successfully type increases\nyour score and Elon\'s net worth. After typing, press enter to\nclear the word.\n\nWill you be able to impress Elon Musk?', fill='yellow', font='Times 20', anchor = 'w')

		screen2 = True
		screen.update()
		screen.delete(objective, objectiveText)



#Function that starts the entire game 
def runGame():  
	global word, teslaHealthDrawing1, teslaHealthDrawing2, teslaHealthDrawing3, elapsedTime, socialMediaDrawings


	setInitialValues()
	menu()
	initialDrawings()
	startTime = time()

	while True:   
		drawObjects()  
		elapsedTime = time() - startTime

		#When health is lost
		if health == 2:
			screen.delete(teslaHealthDrawing1)

		elif health == 1:
			screen.delete(teslaHealthDrawing2)

		elif health == 0:
			screen.delete(teslaHealthDrawing3)

		screen.update()
		sleep(0.03)
		screen.delete( teslaDrawing, elonDrawing, typeWordDrawing, scoreDrawing)


		#Deletes all the current word drawings
		for x in range(len(currentWords)):
			screen.delete(wordDrawings[x-1])
			screen.delete(socialMediaDrawings[x-1])


		#Delete the temporary text on the typing area
		if len(word) != 0:
			screen.delete(typeWordHereDrawing)
		
	
		updateObjects()  #This should adjust all the objects' positions and speeds

		#Once there are no more lives left
		if health == 0:
			endGame()


#What happens at the end of the game
def endGame():

	screen.delete('all')

	#Writes your score and name in the list of high scores 
	if score > 0:
		with open('assets/highScore.txt', 'a') as file:
			file.write(f'{str(score)} {username}\n')
	
	draw_end_screen()
	

#END SCREEN AFTER LOSING THE GAME 
def draw_end_screen():
	global colors, background, teslaRed, blackPaperBackground, blackPaper, leaderBoardScreen, restartButtonDrawing, bitcoinDrawing


	topFiveScores = []
	topFiveUsernames = []
	scoreDrawings = [0, 0, 0, 0, 0]
	usernameDrawings = [0, 0, 0, 0, 0]

	leaderBoardScreen = True
	

	#Finds the highscores
	with open("assets/highScore.txt", 'r') as file:
		lines = []

		#Reads every line of the file and puts it into the lines array
		lines = file.readlines()


		#Finds the top five highscores of all time
		for x in range(5):
			highscore = 0
			index = 0
			highscoreIndex = 0
			highusername = ''

			#For each line in the array 
			for hscore in lines:
				username = ''

				#Find the score number
				l = hscore.split(" ")
				currentScore = int(l[0])
				
				#Find the username
				for x in range(1, len(l)):
					if username != '':
						username += " " + l[x]
					
					else:
						username += l[x]

				username = username[:-1]

				#If the current score is higher than the highscore
				if currentScore > highscore:
					highscore = currentScore
					highscoreIndex = index
					highusername = username

				index += 1

			#Adds the highscore to the top five scores and the username
			topFiveScores.append(highscore)

			topFiveUsernames.append(highusername)

			#Removes the highscore found from the topscores array
			lines.pop(highscoreIndex)
		
		
	#Draws in the leaderboard and background
	blackPaper = PhotoImage(file = "assets/black paper.png")

	blackPaperBackground = screen.create_image( 500, 300, image = blackPaper)

	screen.create_rectangle(265,65, 825, 425, fill='gray')

	screen.create_text((265+825)/2, 100, text='LEADERBOARDS', fill='red', font='Times 26')

	screen.create_text(350, 150, text='Username', fill='red', font='Times 20', anchor = 'w')

	screen.create_text(700, 150, text='Score', fill='red', font='Times 20', anchor = 'w')


	#Draws in the bitcoin symbol
	bitcoinDrawing = screen.create_image( 365, 100, image = bitcoin)

	bitcoinDrawing = screen.create_image( 725, 100, image = bitcoin)


	#Draws in all the rankings 
	for i in range(5):
		usernameDrawings[i] = screen.create_text(280, 190+i*50, text=f'#{i+1}.   {topFiveUsernames[i]}', fill='white', font='Times 20', anchor = 'w')

		scoreDrawings[i] = screen.create_text(700, 190+i*50, text=f'{topFiveScores[i]}',  fill='white', anchor='w', font='Times 20')
	

	#Draws in your score 
	screen.create_text(500, 450, text=f'Your Score: {score}',  fill='red', anchor='c', font='Times 20')

	while True:

		#Restart Button while not hovering
		if xMouse > 500 + 100 or xMouse < 500 - 100 or yMouse > 510 + 38 or yMouse < 510 - 38:
			restartButtonDrawing = screen.create_image( 500, 510, image = normalButton)


		#While hovering
		if xMouse < 500 + 100 and xMouse > 500 - 100 and yMouse < 510 + 38 and yMouse > 510 - 38:
			restartButtonDrawing = screen.create_image( 500, 510, image = hoverButton)


		#Restart Text on Button
		restartText = screen.create_text(500, 510, text=f'Restart',  fill='Yellow', anchor='c', font='Times 20')
		


		screen.update()
		sleep(0.03)
		screen.delete(restartText, restartButtonDrawing)
		


#All of the typing bindings 
def aBind( event ) :
	global word
	word += 'a'

def bBind( event ) :
	global word
	word += 'b'

def cBind( event ) :
	global word
	word += 'c'

def dBind( event ) :
	global word
	word += 'd'

def eBind( event ) :
	global word
	word += 'e'

def fBind( event ) :
	global word
	word += 'f'

def gBind( event ) :
	global word
	word += 'g'

def hBind( event ) :
	global word
	word += 'h'

def iBind( event ) :
	global word
	word += 'i'

def jBind( event ) :
	global word
	word += 'j'

def kBind( event ) :
	global word
	word += 'k'

def lBind( event ) :
	global word
	word += 'l'

def mBind( event ) :
	global word
	word += 'm'

def nBind( event ) :
	global word
	word += 'n'

def oBind( event ) :
	global word
	word += 'o'

def pBind( event ) :
	global word
	word += 'p'

def qBind( event ) :
	global word
	word += 'q'

def rBind( event ) :
	global word
	word += 'r'

def sBind( event ) :
	global word
	word += 's'

def tBind( event ) :
	global word
	word += 't'

def uBind( event ) :
	global word
	word += 'u'

def vBind( event ) :
	global word
	word += 'v'

def wBind( event ) :
	global word
	word += 'w'

def xBind( event ) :
	global word
	word += 'x'

def yBind( event ) :
	global word
	word += 'y'

def zBind( event ) :
	global word
	word += 'z'

#Capital letters keybind
def capAbind (event):
	global word
	word += 'A'

def capBbind (event):
	global word
	word += 'B'

def capCbind (event):
	global word
	word += 'C'

def capDbind (event):
	global word
	word += 'D'

def capEbind (event):
	global word
	word += 'E'

def capFbind (event):
	global word
	word += 'F'

def capGbind (event):
	global word
	word += 'G'

def capHbind (event):
	global word
	word += 'H'

def capIbind (event):
	global word
	word += 'I'

def capJbind (event):
	global word
	word += 'J'

def capKbind (event):
	global word
	word += 'K'

def capLbind (event):
	global word
	word += 'L'

def capMbind (event):
	global word
	word += 'M'

def capNbind (event):
	global word
	word += 'N'

def capObind (event):
	global word
	word += 'O'

def capPbind (event):
	global word
	word += 'P'

def capQbind (event):
	global word
	word += 'Q'

def capRbind (event):
	global word
	word += 'R'

def capSbind (event):
	global word
	word += 'S'

def capTbind (event):
	global word
	word += 'T'

def capUbind (event):
	global word
	word += 'U'

def capVbind (event):
	global word
	word += 'V'

def capWbind (event):
	global word
	word += 'W'

def capXbind (event):
	global word
	word += 'X'

def capYbind (event):
	global word
	word += 'Y'

def capZbind (event):
	global word
	word += 'Z'


#Backspace
def backspace( event ):
	global word
	word = word[:-1]

#Spacebar
def space( event ) :
	global word
	word += ' '

#Apostrophe 
def apostrophe ( event ) :
	global word
	word += "'"

#Enter button
def enter (event):
	global currentWords, word, score, xWord, yWord, logoDrawings, socialMediaDrawings, wordSpeed, secondsUntilNextWord

	#Goes through all the words on the screen and finds the word the user typed
	for x in range(len(currentWords)):
		if currentWords[x] == word:
			word = ""

			#Deletes the word and image from the screen and removes all the values from the proper arrays. 
			screen.delete(wordDrawings[x])

			currentWords.pop(x) 
			xWord.pop(x)
			yWord.pop(x)
			wordDrawings.pop(x)
	
			screen.delete(socialMediaDrawings[x])
			socialMediaDrawings.pop(x)
			logoDrawings.pop(x)
			
			#Adds score and changes the text color
			score += pointsEarned
			netWorthColor(scoreColor)
	

			#If the current WPM is capped
			if 60/secondsUntilNextWord == maxWPM:
				wordSpeed += 0.025

			break

	word = ''


#Tracks where the mouse is
def mouseMotionHandler(event):
	global xMouse, yMouse
	
	xMouse = event.x
	yMouse = event.y


#Binds any mouse motion to mouseMotionHander()
screen.bind("<Motion>", mouseMotionHandler)


#Once the program is ready, run the game
root.after( 0, runGame )

#Binds clicking to mouseClickHander()
screen.bind( "<Button-1>", mouseClickHandler )

#Binds all mouse motion to mouseMotionHandler()
screen.bind("<Motion>", mouseMotionHandler)


#Binds all keys to its respective function
screen.bind("a", aBind)
screen.bind("b", bBind)
screen.bind("c", cBind)
screen.bind("d", dBind)
screen.bind("e", eBind)
screen.bind("f", fBind)
screen.bind("g", gBind)
screen.bind("h", hBind)
screen.bind("i", iBind)
screen.bind("j", jBind)
screen.bind("k", kBind)
screen.bind("l", lBind)
screen.bind("m", mBind)
screen.bind("n", nBind)
screen.bind("o", oBind)
screen.bind("p", pBind)
screen.bind("q", qBind)
screen.bind("r", rBind)
screen.bind("s", sBind)
screen.bind("t", tBind)
screen.bind("u", uBind)
screen.bind("v", vBind)
screen.bind("w", wBind)
screen.bind("x", xBind)
screen.bind("y", yBind)
screen.bind("z", zBind)

#Binding capital letters 
screen.bind("A", capAbind)
screen.bind("B", capBbind)
screen.bind("C", capCbind)
screen.bind("D", capDbind)
screen.bind("E", capEbind)
screen.bind("F", capFbind)
screen.bind("G", capGbind)
screen.bind("H", capHbind)
screen.bind("I", capIbind)
screen.bind("J", capJbind)
screen.bind("K", capKbind)
screen.bind("L", capLbind)
screen.bind("M", capMbind)
screen.bind("N", capNbind)
screen.bind("O", capObind)
screen.bind("P", capPbind)
screen.bind("Q", capQbind)
screen.bind("R", capRbind)
screen.bind("S", capSbind)
screen.bind("T", capTbind)
screen.bind("U", capUbind)
screen.bind("V", capVbind)
screen.bind("W", capWbind)
screen.bind("X", capXbind)
screen.bind("Y", capYbind)
screen.bind("Z", capZbind)


#Apostrophe button bind
screen.bind("<apostrophe>", apostrophe)

#Binds backspace button 
screen.bind("<BackSpace>", backspace)

#Binds Spacebar button
screen.bind("<space>", space)

#Binds the enter button
screen.bind("<Return>", enter)

screen.pack()
screen.focus_set()
root.mainloop()