###########
# IMPORTS #
###########
from email import message
from dotenv import load_dotenv
import asyncio
import datetime
import discord
import json
import logging
import math
import os
import random
import re
import string
import sys

#########
# LOCAL #
#########
import block_of_text
from packages.squirrel3 import squirrel3

#############
# CONSTANTS #
#############
logging.basicConfig(filename='output.log', encoding='utf-8', level=logging.INFO)
log = logging.getLogger()

BLANK = '<:blank:894263650825670698>'
BLANK_ID = 894263650825670698
GAMEMASTER = 187346007837638657
ROLL_CHANNEL = 864933210265616404
LOG_CHANNEL = 1015611632136753274
MSG_CHAR_LIMIT = 2000
MSG_CHAR_THRESHOLD = 1500
PERSONAL_CHANNEL = 'personal_channel'
STR_EMOTE = '💪'
DEX_EMOTE = '💃'
CON_EMOTE = '❤️'
WIS_EMOTE = '🧐'
INT_EMOTE = '🤓'
CHA_EMOTE = '😎'
DIE_EMOTE = '🎲'
ACROBATICS_EMOTE = '🤸'
ATHLETICS_EMOTE = '🏃'
BLUFF_EMOTE = '😏'
COMPUTERS_EMOTE = '💻'
CULTURE_EMOTE = '🛐'
DIPLOMACY_EMOTE = '🤝'
DISGUISE_EMOTE = '🕵️'
ENGINEERING_EMOTE = '🔧'
INTIMIDATE_EMOTE = '😡'
LIFE_SCIENCE_EMOTE = '🌿'
MEDICINE_EMOTE = '🩺'
MYSTICISM_EMOTE = '🧙'
PERCEPTION_EMOTE = '👁️'
PHYSICAL_SCIENCE_EMOTE = '🌦️'
PILOTING_EMOTE = '✈️'
PROFESSION_EMOTE = '✍️'
SENSE_MOTIVE_EMOTE = '🤨'
SLEIGHT_OF_HAND_EMOTE = '🤹'
STEALTH_EMOTE = '🤫'
SURVIVAL_EMOTE = '⛺'
EMOTE_MAP = {
	STR_EMOTE: 'strength',
	DEX_EMOTE: 'dexterity',
	CON_EMOTE: 'constitution',
	WIS_EMOTE: 'wisdom',
	INT_EMOTE: 'intelligence',
	CHA_EMOTE: 'charisma',
	ACROBATICS_EMOTE: 'acrobatics',
	ATHLETICS_EMOTE: 'athletics',
	BLUFF_EMOTE: 'bluff',
	COMPUTERS_EMOTE: 'computers',
	CULTURE_EMOTE: 'culture',
	DIPLOMACY_EMOTE: 'diplomacy',
	DISGUISE_EMOTE: 'disguise',
	ENGINEERING_EMOTE: 'engineering',
	INTIMIDATE_EMOTE: 'intimidate',
	LIFE_SCIENCE_EMOTE: 'life science',
	MEDICINE_EMOTE: 'medicine',
	MYSTICISM_EMOTE: 'mysticism',
	PERCEPTION_EMOTE: 'perception',
	PHYSICAL_SCIENCE_EMOTE: 'physical science',
	PILOTING_EMOTE: 'piloting',
	PROFESSION_EMOTE: 'profession',
	SENSE_MOTIVE_EMOTE: 'sense motive',
	SLEIGHT_OF_HAND_EMOTE: 'sleight of hand',
	STEALTH_EMOTE: 'stealth',
	SURVIVAL_EMOTE: 'survival',
}
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
ALL_SKILLS = {
	'acrobatics': 'dexterity',
	'athletics': 'strength',
	'bluff': 'charisma',
	'computers': 'intelligence',
	'culture': 'intelligence',
	'diplomacy': 'charisma',
	'disguise': 'charisma',
	'engineering': 'intelligence',
	'intimidate': 'charisma',
	'life science': 'intelligence',
	'medicine': 'intelligence',
	'mysticism': 'wisdom',
	'perception': 'wisdom',
	'physical science': 'intelligence',
	'piloting': 'dexterity',
	'profession': 'wisdom',
	'sense motive': 'wisdom',
	'sleight of hand': 'dexterity',
	'stealth': 'dexterity',
	'survival': 'wisdom'
}

patterns = {}
patterns['r xdy'] = re.compile(r'\d+d\d+', re.IGNORECASE)
patterns['r dy'] = re.compile(r'd\d+', re.IGNORECASE)
patterns['+'] = re.compile(r'\+')
patterns['-'] = re.compile(r'\-')
patterns['numbers'] = re.compile(r'\d+')
load_dotenv()
user_data_dir = 'users/'
session_data = {}


'''
# {user_id, int}
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

def get_modifier(score):
	return (score - 10) // 2

def save_session_data():
	for user in session_data:
		data = json.dumps(session_data[user], indent=4)
		user_file_name = f'{user_data_dir}{user}.json'
		try:
			user_file = open(user_file_name, 'w')
			user_file.write(data)
			user_file.close()
			log.info(f'User data {user_file_name} saved successfully!')
		except Exception as e:
			log.info(f'ERROR: User data {user_file_name} failed to save: {e}')

def load_session_data():
	user_files = os.listdir(user_data_dir)
	for file in user_files:
		user_id = file.removesuffix('.json')
		user_file_name = user_data_dir+file
		try:
			user_file = open(user_file_name, 'r')
			session_data[int(user_id)] = json.loads(user_file.read())
			user_file.close()
			log.info(f'User data {user_data_dir+file} loaded successfully!')
		except Exception as e:
			log.info(f'ERROR: User data {user_file_name} failed to load: {e}')

async def init_session_data(guilds):
	for guild in guilds:
		log.info('Logged into guildID: {0}'.format(guild.id))
		async for member in guild.fetch_members():
			if member.id not in session_data:
				session_data[member.id] = dict()
				session_data[member.id]['player_name'] = member.display_name
				session_data[member.id]['name'] = 'N/A'
				session_data[member.id]['level'] = 0
				session_data[member.id]['alignment'] = 'N'
				session_data[member.id]['state'] = 0
				session_data[member.id]['substate'] = 0
				session_data[member.id]['race'] = 'r'
				session_data[member.id]['theme'] = 't'
				session_data[member.id]['class'] = 'c'
				session_data[member.id]['strength'] = 10
				session_data[member.id]['dexterity'] = 10
				session_data[member.id]['constitution'] = 10
				session_data[member.id]['intelligence'] = 10
				session_data[member.id]['wisdom'] = 10
				session_data[member.id]['charisma'] = 10
				session_data[member.id]['size'] = ''
				session_data[member.id]['type'] = ''
				session_data[member.id]['ability points'] = 10
				session_data[member.id]['max resolve'] = 0
				session_data[member.id]['max stamina'] = 0
				session_data[member.id]['max hp'] = 0
				session_data[member.id]['current stamina'] = 0
				session_data[member.id]['current hp'] = 0
				session_data[member.id]['current resolve'] = 0
				session_data[member.id]['key ability score'] = 'n'
				session_data[member.id]['eac'] = 10
				session_data[member.id]['kac'] = 10
				session_data[member.id]['needs race choice'] = False
				session_data[member.id]['needs theme choice'] = False
				session_data[member.id]['needs class choice'] = False
				session_data[member.id]['skills'] = {}
				session_data[member.id]['saving throws'] = {
					'will': {
						'ability': 'wisdom',
						'misc modifiers': 0
					},
					'reflex': {
						'ability': 'dexterity',
						'misc modifiers': 0
					},
					'fortitude': {
						'ability': 'constitution',
						'misc modifiers': 0
					}
				}
				session_data[member.id]['proficiencies'] = []
				session_data[member.id]['ranks per level'] = 0
				session_data[member.id]['base attack bonus'] = 0
				session_data[member.id]['feats'] = {}
				session_data[member.id]['traits'] = {}
				session_data[member.id]['triggered traits'] = {}
				session_data[member.id]['speed'] = 0

				
				for skill in ALL_SKILLS:
					session_data[member.id]['skills'][skill] = {
						'ranks': 0,
						'class skill': False,
						'ability': ALL_SKILLS[skill],
						'misc modifiers': 0
					}
			elif 'player_name' not in session_data[member.id]:
				session_data[member.id]['player_name'] = member.display_name

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

def extract_rolls(content):
	rolls = content.split(DIE_EMOTE)
	if len(rolls) == 1:
		return []
	else:
		for x in range(len(rolls)):
			rolls[x] = rolls[x].strip()
		return rolls[1:]


#------------------------#
#---  Discord Client  ---#
#------------------------#
class MyClient(discord.Client):

	#-----------------#
	#---  Logging  ---#
	#-----------------#
	async def logMessage(self, message):
		log.info(message)
		await self.log_channel.send(message)

	#----------------------------------#
	#---  List Information methods  ---#
	#----------------------------------#
	def list_races(self):
		messages = []
		builder = 'Here\'s a list of all the playable **Races** for our campaign:\n\n'

		for race in self.races:
			builder += '**' + string.capwords(race, '-') + '**: ' + self.races[race]['short_desc'] + '\n\n'
			if len(builder) >= MSG_CHAR_THRESHOLD:
				messages.append(builder)
				builder = ""
		
		if builder != "":
			messages.append(builder)

		return messages
	def list_themes(self):
		messages = []
		builder = 'Here\'s a list of all the **Themes** for our campaign:\n\n'

		for theme in self.themes:
			builder += '**' + string.capwords(theme, '-') + '**: ' + self.themes[theme]['short_desc'] + '\n\n'
			if len(builder) >= MSG_CHAR_THRESHOLD:
				messages.append(builder)
				builder = ""
		
		if builder != "":
			messages.append(builder)

		return messages
	def list_classes(self):
		messages = []
		builder = 'Here\'s a list of all the **Classes** you can choose from:\n\n'

		for charClass in self.classes:
			builder += '**' + string.capwords(charClass, '-') + '**: ' + self.classes[charClass]['short_desc'] + '\n\n'
			if len(builder) >= MSG_CHAR_THRESHOLD:
				messages.append(builder)
				builder = ""

		if builder != "":
			messages.append(builder)
		
		return messages

	#TODO
	def build_character_sheet(self, id):
		builder = ''
		messages = []
		data = session_data[id]

		builder += f"**{data['name']}** - {string.capwords(data['race'])} {string.capwords(data['theme'])}\nLvl {data['level']} {string.capwords(data['class'])}\n"
		builder += f":yellow_heart: **Stamina:** {data['current stamina']} / {data['max stamina']}\n:heart: **HP:** {data['current hp']} / {data['max hp']}\n:zap: **Resolve:** {data['current resolve']} / {data['max resolve']}\n:shield: **KAC**: {data['kac']} {BLANK} **EAC**: {data['eac']}\n{string.capwords(data['size'])} {string.capwords(data['type'])}\n\n"
		builder += f":muscle: Strength: {data['strength']}\n"
		builder += f":cartwheel: Dexterity: {data['dexterity']}\n"
		builder += f":anatomical_heart: Constitution: {data['constitution']}\n"
		builder += f":brain: Intelligence: {data['intelligence']}\n"
		builder += f":mag: Wisdom: {data['wisdom']}\n"
		builder += f":sunglasses: Charisma: {data['charisma']}\n"
		messages.append(builder)
		builder = ''

		

		return messages

	#------------------------------#
	#---  Get Overview methods  ---#
	#------------------------------#
	def get_race_overview(self, race):
		messages = []
		builder = f"**{string.capwords(race, '-')}**\n{self.races[race]['long_desc']}\n\n"

		builder += "**Stats**\n========================================\n"
		for stat in self.races[race]['stats']:
			builder += f"**{string.capwords(stat)}**: {'+' if str(self.races[race]['stats'][stat]).isdigit() else ''}{self.races[race]['stats'][stat]}\n"
			if len(builder) >= MSG_CHAR_THRESHOLD:
				messages.append(builder)
				builder = ""
		
		builder += "\n**Racial Traits**\n========================================\n"
		for trait in self.races[race]['traits']:
			builder += f"**{string.capwords(trait)}**: {self.races[race]['traits'][trait]['desc']}\n"
			if len(builder) >= MSG_CHAR_THRESHOLD:
				messages.append(builder)
				builder = ""
		
		if 'choices' in self.races[race]:
			builder += "\n**Additional Choices**\n========================================\n"
			for choice in self.races[race]['choices']:
				for option in self.races[race]['choices'][choice]:
					log.info(f'choice: {choice}\n|--option: {option}')
					builder += f"**{string.capwords(option)}**\n{self.races[race]['choices'][choice][option]['description']}\n"
					if len(builder) >= MSG_CHAR_THRESHOLD:
						messages.append(builder)
						builder = ""

		if builder != "":
			messages.append(builder)
		return messages
	def get_class_overview(self, class_choice):
		messages = []
		builder = f"**{string.capwords(class_choice)}** (<{self.classes[class_choice]['link']}>)\n========================================\n{self.classes[class_choice]['long_desc']}\n\n"

		builder += "**Stats**\n========================================\n"
		for stat in self.classes[class_choice]['stats']:
			builder += f"**{string.capwords(stat)}**: +{self.classes[class_choice]['stats'][stat]}\n"
			if len(builder) >= MSG_CHAR_THRESHOLD:
				messages.append(builder)
				builder = ""

		builder += f"**Key Ability Score**: {string.capwords(self.classes[class_choice]['key ability score'])}\n"
		if len(builder) >= MSG_CHAR_THRESHOLD:
				messages.append(builder)
				builder = ""
		
		builder += f"\n**Skill Ranks per Level**: {self.classes[class_choice]['ranks per level']} + Intelligence modifier"
		builder += "\n**Class Skills**\n========================================\n"
		for skill in self.classes[class_choice]['class skills']:
			builder += f"{string.capwords(skill)}"
			if skill in TRAINED_SKILLS: builder += " :star:"
			builder += "\n"
			if len(builder) >= MSG_CHAR_THRESHOLD:
				messages.append(builder)
				builder = ""
		
		builder += "\n**Proficiencies**\n========================================\n"
		for prof in self.classes[class_choice]['proficiencies']:
			builder += f"{string.capwords(prof)}\n"
			if len(builder) >= MSG_CHAR_THRESHOLD:
				messages.append(builder)
				builder = ""

		builder += f"\n**Base Attack Bonus**: +{self.classes[class_choice]['base attack bonus']}"
		builder += "\n**==Saving Throws==**\n"
		for save in self.classes[class_choice]['saving throws']:
			builder += f"{string.capwords(save)}: +{self.classes[class_choice]['saving throws'][save]}\n"
			if len(builder) >= MSG_CHAR_THRESHOLD:
				messages.append(builder)
				builder = ""

		builder += "\n**Class Features**\n========================================\n"
		messages.append(builder)
		builder = ""
		for feature in self.classes[class_choice]['features']:
			builder += f"**{feature}**\n"
			builder += f"{self.classes[class_choice]['features'][feature]}\n"
			
			messages.append(builder)
			builder = ""

		if builder != "":
			messages.append(builder)
		return messages
	def get_theme_overview(self, theme):
		messages = []
		builder = f"**{string.capwords(theme)}**\n{self.themes[theme]['long_desc']}\n\n"

		if 'stats' in self.themes[theme]:
			builder += "**Stats**\n========================================\n"
			for stat in self.themes[theme]['stats']:
				builder += f"**{string.capwords(stat)}**: +{self.themes[theme]['stats'][stat]}\n"
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
		log.info('Logged on as {0}!'.format(self.user))
		log.info('Self ID: {0}'.format(self.user.id))
		self.roll_channel = await self.fetch_channel(ROLL_CHANNEL)
		self.log_channel = await self.fetch_channel(LOG_CHANNEL)
		
		self.rng = squirrel3.Squirrel3Random(random.Random(datetime.datetime.now(datetime.timezone.utc).timestamp()))
		self.rng.seed(int(datetime.datetime.now(datetime.timezone.utc).timestamp()))
		load_session_data()

		#initialize session data for each user
		await init_session_data(self.guilds)
					
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
		user_id = message.author.id
		command = message.content[1:]

		#
		# DEBUG
		#
		if command == 'members':
			await self.logMessage(session_data)
			return
		if command == 'purge':
			await message.channel.purge()
			return
		if command == 'save':
			await init_session_data(self.guilds)
			save_session_data()
			return
		if command == 'quit':
			sys.exit()

		#--------------------------------#
		#---  List character options  ---#
		#--------------------------------#
		if command == 'list race':
			messages = self.list_races()
			for msg in messages:
				await message.channel.send(msg)
			return
		if command == 'list theme':
			messages = self.list_themes()
			for msg in messages:
				await message.channel.send(msg)
			return
		if command == 'list class':
			messages = self.list_classes()
			for msg in messages:
				await message.channel.send(msg)
			return
			
		if command == 'character':
			for msg in self.build_character_sheet(user_id):
				await message.channel.send(msg)
			return
		
		if command == 'register':
			channel = message.channel.id
			user = message.author.id
			if user in session_data and PERSONAL_CHANNEL not in session_data[user]:
				session_data[user][PERSONAL_CHANNEL] = channel
				await message.channel.send("Channel registered for "+message.author.display_name)
			elif user not in session_data:
				await init_session_data(self.guilds)
				session_data[user][PERSONAL_CHANNEL] = channel
				await message.channel.send("Channel registered for "+message.author.display_name)
			else:
				await self.logMessage(f'@= user {message.author.display_name} already has channel {message.channel.name} registered.')			
			save_session_data()


		#--------------------------#
		#---  Rolling Commands  ---#
		#--------------------------#
		if command.startswith('r ') or command.startswith('roll '):
			try:
				outcome = roll_dice(command, self.rng)
				await self.logMessage(outcome)
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
				await self.logMessage(f'invalid roll: {command} - {e}')
				await message.channel.send(f"That's not a valid roll!\n"
									f"Attempted: {command}\n"
									f"Error: {e}")

		#----------------------------#
		#---  Character Creation  ---#
		#----------------------------#
		if session_data[user_id]['state'] != 13:
			#Create Character
			if session_data[user_id]['state'] == 0:
				
				#Start character creation
				if command == 'create':
					#check if user already has a file
					filepath = str(user_id) + '.json'
					if os.path.exists(filepath):
						await message.channel.send('You already have a character!')
						session_data[user_id]['state'] = 13
						#TODO: Load character file
						return
					
					session_data[user_id]['state'] = 1
					await message.channel.send(block_of_text.introPt1(message.author.name))
					await message.channel.send(block_of_text.introPt2())
					return
			#Intro
			if session_data[user_id]['state'] == 1:
				if command == 'next':
					session_data[user_id]['state'] = 2
					await message.channel.send(block_of_text.racePt1())
					for msg in self.list_races():
						await message.channel.send(msg)
					await message.channel.send(block_of_text.racePt2())
					return
			#Choose Race
			if session_data[user_id]['state'] == 2:
				if command.startswith('race '):
					session_data[user_id]['race'] = command[5:].lower()
					race = command[5:].lower()
					
					if not race in self.races:
						await message.channel.send('\'' + race + '\' is not a valid race. Please try again!')
						return
					
					for msg in self.get_race_overview(race):
						await message.channel.send(msg)
					await message.channel.send(block_of_text.racePt3(race))
					
				if command == 'confirm':
					if not session_data[user_id]['race'] in self.races:
						await message.channel.send('You haven\'t chosen a proper race yet!')
					else:
						await message.channel.send('You\'ve chosen **\'' + session_data[user_id]['race'] + '\'** as your race!\nIf your racial choice requires further specification for \'sub-race\' (like the different kinds of Lashunta or Gnomes), we\'ll take care of that after a couple more steps.')
						session_data[user_id]['state'] = 3
						await message.channel.send(block_of_text.themePt1())
						for msg in self.list_themes():
							await message.channel.send(msg)
						await message.channel.send(block_of_text.themePt2())
				return
			#Choose Theme
			if session_data[user_id]['state'] == 3:
				if command.startswith('theme'):
					session_data[user_id]['theme'] = command[6:].lower()
					theme = command[6:].lower()

					if not theme in self.themes:
						await message.channel.send(f"'{theme}' is not a valid theme. Please try again!")
						return
					
					for msg in self.get_theme_overview(theme):
						await message.channel.send(msg)
					await message.channel.send(block_of_text.themePt3(theme))

				if command == 'confirm':
					if not session_data[user_id]['theme'] in self.themes:
						await message.channel.send("You haven't chosen a proper theme yet!")
					else:
						await message.channel.send(f"You've chosen **{session_data[user_id]['theme']}** as your theme!\nIf your theme choice requires further choices at level 1 (the 'Themeless' theme), we'll take care of that soon.")
						session_data[user_id]['state'] = 4
						await message.channel.send(block_of_text.classPt1())
						for msg in self.list_classes():
							await message.channel.send(msg)
						await message.channel.send(block_of_text.classPt2())
				return
			#Choose Class #TODO
			if session_data[user_id]['state'] == 4:
				if command.startswith('class'):
					session_data[user_id]['class'] = command[6:].lower()
					class_choice = command[6:].lower()
					
					if not class_choice in self.classes:
						await message.channel.send(f"'{class_choice}' is not a valid class. Please try again!")
						return

					for msg in self.get_class_overview(class_choice):
						await message.channel.send(msg)
					await message.channel.send(block_of_text.classPt3(class_choice))

				if command == 'confirm':
					if not session_data[user_id]['class'] in self.classes:
						await message.channel.send("You haven't chosen a proper class yet!")
					else:
						await message.channel.send(f"You've chosen **{session_data[user_id]['class']}** as your class!\nIf your class choice requires further choices at level 1 (most do), we'll take care of that soon.")
						session_data[user_id]['state'] = 5
						#Determine what needs choices
						race_data = self.races[session_data[user_id]['race']]
						theme_data = self.themes[session_data[user_id]['theme']]
						class_data = self.classes[session_data[user_id]['class']]
						if 'choices' in race_data:
							session_data[user_id]['needsracechoice'] = True
						if 'choices' in theme_data:
							session_data[user_id]['needsthemechoice'] = True
						if 'choices' in class_data: #TODO: implement in classes.json
							session_data[user_id]['needsclasschoice'] = True
						
						#Apply stats - Race
						for stat in race_data['stats']:
							session_data[user_id][stat] += race_data['stats'][stat]
						for trait in race_data['traits']:
							session_data[user_id]['traits'][trait] = race_data['traits'][trait]
							for entry in race_data['traits'][trait]:
								valid = not race_data['traits'][trait]['manual'] and (entry != 'desc' and entry != 'manual')

								if isinstance(race_data['traits'][trait][entry], dict) and valid:
									for modification in race_data['traits'][trait][entry]:
										session_data[user_id][entry][modification]['misc modifiers'] += race_data['traits'][trait][entry][modification]
								elif valid:
									session_data[user_id][entry] += race_data['traits'][trait][entry]
						
						#Apply stats - Theme #TODO: Refactor
						for stat in theme_data['stats']:
							session_data[user_id][stat] += theme_data['stats'][stat]
						#TODO:
						#	- features

						#Apply stats - Class #TODO: Refactor
						for stat in class_data['stats']:
							session_data[user_id][stat] += class_data['stats'][stat]
						#TODO:
						#	- Key Ability Score
						#	- Class skills
						#	- Proficiencies
						#	- Skill ranks
						#	- saving throws
						#	- base attack bonus
						#	- features
				return
			#Race-Theme-Class sub-choices
			if session_data[user_id]['state'] == 5:
				#TODO
				return
			#Ability score buys
			if session_data[user_id]['state'] == 6:
				#TODO
				return
			#Class abilities 
			if session_data[user_id]['state'] == 7:
				#TODO
				return
			#Skill Ranks
			if session_data[user_id]['state'] == 8:
				#TODO
				return
			#Feats
			if session_data[user_id]['state'] == 9:
				#TODO
				return
			#Gear/Equipment
			if session_data[user_id]['state'] == 10:
				#TODO
				return
			#Finishing touches
			if session_data[user_id]['state'] == 11:
				#TODO
				return
			#Overview and confirmation
			if session_data[user_id]['state'] == 12:
				#TODO
				return
			
		#Level up your character
		if message.content == '!levelup':
			if session_data[user_id]['state'] != 13:
				await message.channel.send('You don\'t have a character yet, ' + message.author.name + '! Type **!create** to get started.')
			else:
				await message.channel.send('Under construction!')
		
	#---------------------------#
	#---  Reaction Handling  ---#
	#---------------------------#
	async def on_raw_reaction_add(self, payload):
		try:
			emoji = payload.emoji
			# Check emote
			if emoji.name != DIE_EMOTE:
				return

			get_msg = self.get_channel(payload.channel_id).fetch_message(payload.message_id)
			msg = await get_msg
			user = msg.author.id
		
			rolls = []
			# if user reacted to own post
			if user == payload.user_id:
				#handle rolls
				player_rolls = extract_rolls(msg.content)
				await self.logMessage('@===@ ROLLS', player_rolls)
				await self.react_rolls(msg, player_rolls)
				return
			# if GM reacted to post
			elif payload.user_id == GAMEMASTER:
				reacts = msg.reactions
				for react in reacts:
					if react.emoji in EMOTE_MAP:
						raw_users = await react.users().flatten()
						users = []
						for raw in raw_users:
							users.append(raw.id)
						if GAMEMASTER in users:
							rolls.append(EMOTE_MAP[react.emoji])

			roll_string = ''
			for r in rolls:
				roll_string += (', '+r.capitalize()) if roll_string != '' else r.capitalize() 
			if user in session_data and PERSONAL_CHANNEL in session_data[user]:
				user_channel = self.get_channel(session_data[user][PERSONAL_CHANNEL])
				embed = discord.Embed(
					title = 'Post',
					type = 'rich',
					url = msg.jump_url
				)
				embed.add_field(
					name='The GM requests the following rolls...', 
					value='{' + roll_string + '}', inline=True
				)
				embed.add_field(
					name='To perform these rolls...', 
					value='1. Edit your message (click `Post` above)\n2. Add a new line to the end (hold `shift` and press `enter`)\n'+
						'3. Add '+DIE_EMOTE+', the name of the roll, and then your roll\n'+
						'Format: '+DIE_EMOTE+' {name of roll} r {dice} + {modifiiers}\n'
						'(Example: '+DIE_EMOTE+' Str r d20 + 2)\n'+
						'4. Repeat steps `2-3` for each roll requested above\n'+
						'5. When finished, react to your own message with '+DIE_EMOTE, 
					inline=False
				)
				await user_channel.send(embed=embed)
		except Exception as e:
			self.logMessage(f"{payload} failed: {e}")
	
	async def react_rolls(self, msg, rolls):
		try:
			content = ''
			cleansed_rolls = {}
			for r in rolls:
				unpacked = r.split()
				raw_roll = ''
				for x in unpacked[1:]:
					raw_roll += x if raw_roll == '' else ' '+x
				cleansed_rolls[unpacked[0]] = roll_dice(raw_roll, self.rng)
			for name,r in cleansed_rolls.items():
				total = 0
				message_text = ''
				for roll in r:
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
				content += name.capitalize()+': '+message_text +'\n'
			content = '**'+msg.author.display_name+'** rolled:\n' + content
			embed = discord.Embed(
				title='Rolls for post by '+msg.author.display_name,
				type='rich',
				url=msg.jump_url,
			)
			embed.add_field(
				name='Post preview', 
				value=(msg.content if len(msg.content) < 100 else msg.content[:100]+'...'),
				inline=False
			)
			await self.roll_channel.send(content=content, embed=embed)
		except Exception as e:
			self.logMessage(f"{msg} failed: {e}")
			user = msg.author.id
			if user in session_data and PERSONAL_CHANNEL in session_data[user]:
				user_channel = self.get_channel(session_data[user][PERSONAL_CHANNEL])
				embed = discord.Embed(
					title = 'Post',
					type = 'rich',
					rl = msg.jump_url
				)
				embed.add_field(
					name='Your roll was not valid',
					value='Please re-edit your message and redo the roll.\n'+
					'Remember to follow the format:\n'+
					DIE_EMOTE+' {name of roll} r {dice} + {modifiiers}\n'+
					'When you are ready to re-roll, redo your '+DIE_EMOTE+' reaction on your message.'
				)
				await user_channel.send(embed=embed)


##################
# Initialize bot #
##################
client = MyClient(intents=discord.Intents.all())
client.run(os.environ.get('TOKEN'))