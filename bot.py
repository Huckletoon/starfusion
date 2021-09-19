from dotenv import load_dotenv
import discord
import json
import math
import os
import random
import re
import string

import blocksOfText

from packages.squirrel3 import squirrel3

MSG_CHAR_LIMIT = 2000
MSG_CHAR_THRESHOLD = 1500
TRAINED_SKILLS = [
	'computers',
	'culture',
	'engineering',
	'life science',
	'medicine',
	'mysticism',
	'physical science',
	'profession',
	'sleight of hand'
]

patterns = {}
patterns['r xdy'] = re.compile(r'\d+d\d+', re.IGNORECASE)
patterns['r dy'] = re.compile(r'd\d+', re.IGNORECASE)
patterns['+'] = re.compile(r'\+')
patterns['-'] = re.compile(r'\-')
patterns['numbers'] = re.compile(r'\d+')
load_dotenv()
user_data_dir = 'users/'
sessionData = {}


'''
# {userid, int}
# user states
# 0 = Base state
# 1 = Intro and Confirmation
# 2 = Race
# 3 = Theme
# 4 = Class
# 5 = Ability Score initial adjustments
# 6 = Ability Score buying
# 7 = Class stats/features
# 8 = Skill Ranks
# 9 = Feats
# 10 = Gear/Equipment
# 11 = Finishing details/touches
# 12 = Overview and confirm character creation
# 13 = Character exists
'''

def save_session_data():
	for user in sessionData:
		data = json.dumps(sessionData[user])
		user_file_name = f'{user_data_dir}{user}.json'
		try:
			user_file = open(user_file_name, 'w')
			user_file.write(data)
			user_file.close()
			print(f'User data {user_file_name} saved successfully!')
		except Exception as e:
			print(f'ERROR: User data {user_file_name} failed to save: {e}')

def load_session_data():
	user_files = os.listdir(user_data_dir)
	for file in user_files:
		user_id = file.removesuffix('.json')
		user_file_name = user_data_dir+file
		try:
			user_file = open(user_file_name, 'r')
			sessionData[int(user_id)] = json.loads(user_file.read())
			user_file.close()
			print(f'User data {user_data_dir+file} loaded successfully!')
		except Exception as e:
			print(f'ERROR: User data {user_file_name} failed to load: {e}')

def validate_token(token):
	for pattern in patterns:
		match = patterns[pattern].match(token)
		if match:
			return pattern
	raise Exception(f'token {token} not matched to any patterns')

def roll_dice(command, rng):
	tokens = command.split(' ')
	del tokens[0]

	plus = True
	components = []
	for token in tokens:
		token_type = validate_token(token)
		if token_type == '+':
			plus = True
			continue
		if token_type == '-':
			plus = False
			continue
		if token_type == 'numbers':
			components.append([plus, int(token)])
			continue
		if token_type == 'r dy':
			die = int(token[1:])
			roll = (math.trunc(rng.random() * die)) + 1
			components.append([plus, token, die, roll])
			continue
		if token_type == 'r xdy':
			numbers = patterns['numbers'].findall(token)
			number_of_dice = int(numbers[0])
			die = int(numbers[1])
			component = [plus, token, die]
			for x in range(number_of_dice):
				roll = (math.trunc(rng.random() * die)) + 1
				component.append(roll)
			components.append(component)
			continue

	return components


#------------------------#
#---  Discord Client  ---#
#------------------------#
class MyClient(discord.Client):

	#----------------------------------#
	#---  List Information methods  ---#
	#----------------------------------#
	def listRaces(self):
		messages = []
		builder = 'Here\'s a list of all the playable **Races** for our campaign:\n\n'

		for race in self.races:
			builder += '**' + string.capwords(race, '-') + '**: ' + self.races[race]['shortDesc'] + '\n\n'
			if len(builder) >= MSG_CHAR_THRESHOLD:
				messages.append(builder)
				builder = ""
		
		if builder != "":
			messages.append(builder)

		return messages
	def listThemes(self):
		messages = []
		builder = 'Here\'s a list of all the **Themes** for our campaign:\n\n'

		for theme in self.themes:
			builder += '**' + string.capwords(theme, '-') + '**: ' + self.themes[theme]['shortDesc'] + '\n\n'
			if len(builder) >= MSG_CHAR_THRESHOLD:
				messages.append(builder)
				builder = ""
		
		if builder != "":
			messages.append(builder)

		return messages
	def listClasses(self):
		messages = []
		builder = 'Here\'s a list of all the **Classes** you can choose from:\n\n'

		for charClass in self.classes:
			builder += '**' + string.capwords(charClass, '-') + '**: ' + self.classes[charClass]['shortDesc'] + '\n\n'
			if len(builder) >= MSG_CHAR_THRESHOLD:
				messages.append(builder)
				builder = ""

		if builder != "":
			messages.append(builder)
		
		return messages

	#------------------------------#
	#---  Get Overview methods  ---#
	#------------------------------#
	def getRaceOverview(self, race):
		messages = []
		builder = f"**{string.capwords(race, '-')}**\n{self.races[race]['longDesc']}\n\n"

		builder += "**Stats**\n========================================\n"
		for stat in self.races[race]['stats']:
			builder += f"**{string.capwords(stat)}**: {self.races[race]['stats'][stat]}\n"
			if len(builder) >= MSG_CHAR_THRESHOLD:
				messages.append(builder)
				builder = ""
		
		builder += "\n**Racial Traits**\n========================================\n"
		for trait in self.races[race]['traits']:
			builder += f"**{string.capwords(trait)}**: {self.races[race]['traits'][trait]}\n"
			if len(builder) >= MSG_CHAR_THRESHOLD:
				messages.append(builder)
				builder = ""
		
		if 'choices' in self.races[race]:
			builder += "\n**Additional Choices**\n========================================\n"
			for choice in self.races[race]['choices']:
				for option in self.races[race]['choices'][choice]:
					builder += f"**{string.capwords(option)}**\n{self.races[race]['choices'][choice][option]['description']}\n"
					if len(builder) >= MSG_CHAR_THRESHOLD:
						messages.append(builder)
						builder = ""

		if builder != "":
			messages.append(builder)
		return messages
	def getClassOverview(self, classChoice):
		messages = []
		builder = f"**{string.capwords(classChoice)}** (<{self.classes[classChoice]['link']}>)\n========================================\n{self.classes[classChoice]['longDesc']}\n\n"

		builder += "**Stats**\n========================================\n"
		for stat in self.classes[classChoice]['stats']:
			builder += f"**{string.capwords(stat)}**: {self.classes[classChoice]['stats'][stat]}\n"
			if len(builder) >= MSG_CHAR_THRESHOLD:
				messages.append(builder)
				builder = ""

		builder += f"**Key Ability Score**: {string.capwords(self.classes[classChoice]['keyAbilityScore'])}\n"
		if len(builder) >= MSG_CHAR_THRESHOLD:
				messages.append(builder)
				builder = ""
		
		builder += f"\n**Skill Ranks per Level**: {self.classes[classChoice]['ranksPerLevel']} + Intelligence modifier"
		builder += "\n**Class Skills**\n========================================\n"
		for skill in self.classes[classChoice]['classSkills']:
			builder += f"{string.capwords(skill)}"
			if skill in TRAINED_SKILLS: builder += " :star:"
			builder += "\n"
			if len(builder) >= MSG_CHAR_THRESHOLD:
				messages.append(builder)
				builder = ""
		
		builder += "\n**Proficiencies**\n========================================\n"
		for prof in self.classes[classChoice]['proficiencies']:
			builder += f"{string.capwords(prof)}\n"
			if len(builder) >= MSG_CHAR_THRESHOLD:
				messages.append(builder)
				builder = ""

		builder += f"\n**Base Attack Bonus**: {self.classes[classChoice]['baseAttackBonus']}"
		builder += "\n**==Saving Throws==**\n"
		for save in self.classes[classChoice]['savingThrows']:
			builder += f"{string.capwords(save)}: +{self.classes[classChoice]['savingThrows'][save]}\n"
			if len(builder) >= MSG_CHAR_THRESHOLD:
				messages.append(builder)
				builder = ""

		builder += "\n**Class Features**\n========================================\n"
		messages.append(builder)
		builder = ""
		for feature in self.classes[classChoice]['features']:
			builder += f"**{feature}**\n"
			builder += f"{self.classes[classChoice]['features'][feature]}\n"
			
			messages.append(builder)
			builder = ""

		if builder != "":
			messages.append(builder)
		return messages
	def getThemeOverview(self, theme):
		messages = []
		builder = f"**{string.capwords(theme)}**\n{self.themes[theme]['longDesc']}\n\n"

		if 'stats' in self.themes[theme]:
			builder += "**Stats**\n========================================\n"
			for stat in self.themes[theme]['stats']:
				builder += f"**{string.capwords(stat)}**: {self.themes[theme]['stats'][stat]}\n"
				if len(builder) >= MSG_CHAR_THRESHOLD:
					messages.append(builder)
					builder = ""

		builder += '\n**Theme Features**\n========================================\n'
		for feature in self.themes[theme]['features']:
			builder += f"**{feature}** - Level {self.themes[theme]['features'][feature]['level']}\n{self.themes[theme]['features'][feature]['description']}\n"
			if len(builder) >= MSG_CHAR_THRESHOLD:
				messages.append(builder)
				builder = ""
		
		if builder != "":
			messages.append(builder)
		return messages

	#------------------#
	#---  On Ready  ---#
	#------------------#
	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))
		print('Self ID: {0}'.format(self.user.id))
		

		self.rng = squirrel3.Squirrel3Random(random.Random(self.user.id))
		self.rng.seed(self.user.id)
		load_session_data()

		#initialize session data for each user
		for guild in self.guilds:
			print('Logged into guildID: {0}'.format(guild.id))
			async for member in guild.fetch_members():
				if member.id not in sessionData:
					sessionData[member.id] = dict()
					sessionData[member.id]['state'] = 0
					sessionData[member.id]['substate'] = 0
					sessionData[member.id]['race'] = ''
					sessionData[member.id]['theme'] = ''
					sessionData[member.id]['class'] = ''
					sessionData[member.id]['strength'] = 10
					sessionData[member.id]['dexterity'] = 10
					sessionData[member.id]['constitution'] = 10
					sessionData[member.id]['intelligence'] = 10
					sessionData[member.id]['wisdom'] = 10
					sessionData[member.id]['charisma'] = 10
					sessionData[member.id]['abilitypoints'] = 10
					sessionData[member.id]['maxresolve'] = 0
					sessionData[member.id]['maxstamina'] = 0
					sessionData[member.id]['maxhp'] = 0
					sessionData[member.id]['keyabilityscore'] = ''
		#initialize character option data
		self.races = json.load(open('characterCreation/races.json', 'r', encoding='utf-8'))
		self.themes = json.load(open('characterCreation/themes.json', 'r', encoding='utf-8'))
		self.classes = json.load(open('characterCreation/classes.json', 'r', encoding='utf-8'))

	#--------------------------#
	#---  Command Handling  ---#
	#--------------------------#
	async def on_message(self, message):
		#prevent acting on own messages
		if message.author == self.user:
			return
		elif not message.content.startswith('!'):
			return
		#Message vars
		userID = message.author.id
		command = message.content[1:]

		#
		# DEBUG
		#
		if command == 'members':
			print(sessionData)
			return
		if command == 'purge':
			await message.channel.purge()
			return
		if command == 'save':
			save_session_data()

		#--------------------------------#
		#---  List character options  ---#
		#--------------------------------#
		if command == 'list race':
			messages = self.listRaces()
			for msg in messages:
				await message.channel.send(msg)
			return
		if command == 'list theme':
			messages = self.listThemes()
			for msg in messages:
				await message.channel.send(msg)
			return
		if command == 'list class':
			messages = self.listClasses()
			for msg in messages:
				await message.channel.send(msg)
			return
			
		#--------------------------#
		#---  Rolling Commands  ---#
		#--------------------------#
		if command.startswith('r ') or command.startswith('roll '):
			try:
				outcome = roll_dice(command, self.rng)
				print(outcome)
				total = 0
				message_text = ''
				for roll in outcome:
					if len(roll) > 2:
						if roll[0]:
							temp_text = f'[{roll[1]} ='
							temp_total = 0
							for x in range(len(roll) - 3):
								total += roll[x+3]
								temp_total += roll[x+3]
								if roll[x+3] == roll[2] or roll[x+3] == 1:
									temp_text = temp_text + f'  ***{roll[x+3]}***'
								else:
									temp_text = temp_text + f'  *{roll[x+3]}*'
							temp_text = f' **+ {temp_total}** ' + temp_text + ']'
							message_text = message_text + temp_text
						else:
							temp_text = f'[{roll[1]} ='
							temp_total = 0
							for x in range(len(roll) - 3):
								total -= roll[x+3]
								temp_total += roll[x+3]
								if roll[x+3] == roll[2] or roll[x+3] == 1:
									temp_text = temp_text + f'  ***{roll[x+3]}***'
								else:
									temp_text = temp_text + f'  *{roll[x+3]}*'
							temp_text = f' **- {temp_total}** ' + temp_text + ']'
							message_text = message_text + temp_text
					elif len(roll) == 2:
						if roll[0]: 
							total += roll[1]
							message_text = message_text + f' **+ {roll[1]}**'
						else: 
							total -= roll[1]
							message_text = message_text + f' **- {roll[1]}**'
				message_text = f'**{total}** ||= (' + message_text + ')||'
				await message.channel.send(message_text)
			except Exception as e:
				print(f'invalid roll: {command} - {e}')
				await message.channel.send(f"That's not a valid roll!\n"
									f"Attempted: {command}\n"
									f"Error: {e}")

		#----------------------------#
		#---  Character Creation  ---#
		#----------------------------#
		if sessionData[userID]['state'] != 13:
			#Create Character
			if sessionData[userID]['state'] == 0:
				
				#Start character creation
				if command == 'create':
					#check if user already has a file
					filepath = str(userID) + '.json'
					if os.path.exists(filepath):
						await message.channel.send('You already have a character!')
						sessionData[userID]['state'] = 13
						#TODO: Load character file
						return
					
					sessionData[userID]['state'] = 1
					await message.channel.send(blocksOfText.introPt1(message.author.name))
					await message.channel.send(blocksOfText.introPt2())
					return
			#Intro
			if sessionData[userID]['state'] == 1:
				if command == 'next':
					sessionData[userID]['state'] = 2
					await message.channel.send(blocksOfText.racePt1())
					for msg in self.listRaces():
						await message.channel.send(msg)
					await message.channel.send(blocksOfText.racePt2())
					return
			#Choose Race
			if sessionData[userID]['state'] == 2:
				if command.startswith('race '):
					sessionData[userID]['race'] = command[5:].lower()
					race = command[5:].lower()
					
					if not race in self.races:
						await message.channel.send('\'' + race + '\' is not a valid race. Please try again!')
						return
					
					for msg in self.getRaceOverview(race):
						await message.channel.send(msg)
					await message.channel.send(blocksOfText.racePt3(race))
					
				if command == 'confirm':
					if not sessionData[userID]['race'] in self.races:
						await message.channel.send('You haven\'t chosen a proper race yet!')
					else:
						await message.channel.send('You\'ve chosen **\'' + sessionData[userID]['race'] + '\'** as your race!\nIf your racial choice requires further specification for \'sub-race\' (like the different kinds of Lashunta or Gnomes), we\'ll take care of that after a couple more steps.')
						sessionData[userID]['state'] = 3
						await message.channel.send(blocksOfText.themePt1())
						for msg in self.listThemes():
							await message.channel.send(msg)
						await message.channel.send(blocksOfText.themePt2())
				return
			#Choose Theme
			if sessionData[userID]['state'] == 3:
				if command.startswith('theme'):
					sessionData[userID]['theme'] = command[6:].lower()
					theme = command[6:].lower()

					if not theme in self.themes:
						await message.channel.send(f"'{theme}' is not a valid theme. Please try again!")
						return
					
					for msg in self.getThemeOverview(theme):
						await message.channel.send(msg)
					await message.channel.send(blocksOfText.themePt3(theme))

				if command == 'confirm':
					if not sessionData[userID]['theme'] in self.themes:
						await message.channel.send("You haven't chosen a proper theme yet!")
					else:
						await message.channel.send(f"You've chosen **{sessionData[userID]['theme']}** as your theme!\nIf your theme choice requires further choices at level 1 (the 'Themeless' theme), we'll take care of that soon.")
						sessionData[userID]['state'] = 4
						await message.channel.send(blocksOfText.classPt1())
						for msg in self.listClasses():
							await message.channel.send(msg)
						await message.channel.send(blocksOfText.classPt2())
				return
			#Choose Class #TODO
			if sessionData[userID]['state'] == 4:
				if command.startswith('class'):
					sessionData[userID]['class'] = command[6:].lower()
					classChoice = command[6:].lower()
					
					if not classChoice in self.classes:
						await message.channel.send(f"'{classChoice}' is not a valid class. Please try again!")
						return

					for msg in self.getClassOverview(classChoice):
						await message.channel.send(msg)
					await message.channel.send(blocksOfText.classPt3(classChoice))

				if command == 'confirm':
					if not sessionData[userID]['class'] in self.classes:
						await message.channel.send("You haven't chosen a proper class yet!")
					else:
						await message.channel.send(f"You've chosen **{sessionData[userID]['class']}** as your class!\nIf your class choice requires further choices at level 1 (most do), we'll take care of that soon.")
						sessionData[userID]['state'] = 5
						#TODO

				return
			#Race-Theme-Class sub-choices
			if sessionData[userID]['state'] == 5:
				#TODO
				return
			#Ability score buys
			if sessionData[userID]['state'] == 6:
				#TODO
				return
			#Class abilities 
			if sessionData[userID]['state'] == 7:
				#TODO
				return
			#Skill Ranks
			if sessionData[userID]['state'] == 8:
				#TODO
				return
			#Feats
			if sessionData[userID]['state'] == 9:
				#TODO
				return
			#Gear/Equipment
			if sessionData[userID]['state'] == 10:
				#TODO
				return
			#Finishing touches
			if sessionData[userID]['state'] == 11:
				#TODO
				return
			#Overview and confirmation
			if sessionData[userID]['state'] == 12:
				#TODO
				return
			
		#Level up your character
		if message.content == '!levelup':
			if sessionData[userID]['state'] != 13:
				await message.channel.send('You don\'t have a character yet, ' + message.author.name + '! Type **!create** to get started.')
			else:
				await message.channel.send('Under construction!')
		
		
		
#Initialize bot
client = MyClient(intents=discord.Intents.all())
client.run(os.environ.get('TOKEN'))