from dotenv import load_dotenv
import discord
import json
import os
import random
import string

import blocksOfText

from packages.squirrel3 import squirrel3

MSG_CHAR_LIMIT = 2000
MSG_CHAR_THRESHOLD = 1750

load_dotenv()
sessionData = dict()

'''
# user states
# {userid, int}
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



class MyClient(discord.Client):

	#list available races
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
	#list available themes
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
	#list available classes
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

	def rollDie(self, die):
		return [(self.rng.random() % die) + 1]

	def rollDice(self, numDice, die):
		results = []
		for x in range(numDice):
			results.append((self.rng.random() % die) + 1)
		return results

	def getRaceOverview(self, race):
		pass

	def getClassOverview(self, classChoice):
		pass

	def getThemeOverview(self, theme):
		pass

	#on ready
	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))
		print('Self ID: {0}'.format(self.user.id))
		

		self.rng = squirrel3.Squirrel3Random(random.Random(self.user.id))
		self.rng.seed(self.user.id)

		#initialize session data for each user
		for guild in self.guilds:
			print('Logged into guildID: {0}'.format(guild.id))
			async for member in guild.fetch_members():
				if member.id not in sessionData:
					print('Loading session data for memberID ' + str(member.id) + ' in guildID ' + str(guild.id) + '...')
					filepath = str(member.id) + '.json'
					if os.path.exists(filepath):
						sessionData[member.id] = dict()
						sessionData[member.id]['state'] = 13
						sessionData[member.id]['substate'] = 0
						sessionData[member.id]['race'] = '' #TODO: Load from file
						sessionData[member.id]['theme'] = '' #TODO
						sessionData[member.id]['class'] = '' #TODO
						sessionData[member.id]['strength'] = 10 #TODO
						sessionData[member.id]['dexterity'] = 10 #TODO
						sessionData[member.id]['constitution'] = 10 #TODO
						sessionData[member.id]['intelligence'] = 10 #TODO
						sessionData[member.id]['wisdom'] = 10 #TODO
						sessionData[member.id]['charisma'] = 10 #TODO
						sessionData[member.id]['abilitypoints'] = 0
						sessionData[member.id]['maxresolve'] = 0 #TODO
						sessionData[member.id]['maxstamina'] = 0 #TODO
						sessionData[member.id]['maxhp'] = 0 #TODO
						sessionData[member.id]['keyabilityscore'] = ''
						
					else:
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
		self.races = json.load(open('characterCreation/races.json', 'r'))
		self.themes = json.load(open('characterCreation/themes.json', 'r'))
		self.classes = json.load(open('characterCreation/classes.json', 'r'))

	#user sent a message
	async def on_message(self, message):
		#prevent acting on own messages
		if message.author == self.user:
			return
		
		#Message vars
		userID = message.author.id

		#DEBUG
		if message.content == '!members':
			print(sessionData)
			return
		if message.content == '!purge':
			await message.channel.purge()
			return
			
		#List character options
		if message.content == '!list race':
			messages = self.listRaces()
			for msg in messages:
				await message.channel.send(msg)
			return
		if message.content == '!list theme':
			messages = self.listThemes()
			for msg in messages:
				await message.channel.send(msg)
			return
		if message.content == '!list class':
			messages = self.listClasses()
			for msg in messages:
				await message.channel.send(msg)
			return
			
		
		#Create Character
		if sessionData[userID]['state'] == 0:
			
			#Start character creation
			if message.content == '!create':
				#check if user already has a file
				filepath = str(userID) + '.json'
				if os.path.exists(filepath):
					await message.channel.send('You already have a character!')
					sessionData[userID]['state'] = 13
					return
				
				sessionData[userID]['state'] = 1
				await message.channel.send(blocksOfText.introPt1(message.author.name))
				await message.channel.send(blocksOfText.introPt2())
		#Intro
		if sessionData[userID]['state'] == 1:
			if message.content == '!next':
				sessionData[userID]['state'] = 2
				await message.channel.send(blocksOfText.racePt1())
				await message.channel.send(blocksOfText.listRaces())
				await message.channel.send(blocksOfText.racePt2())
		#Choose Race
		if sessionData[userID]['state'] == 2:
			if message.content.startswith('!race '):
				sessionData[userID]['race'] = message.content[6:]
				race = message.content[6:]
				
				if not race in self.races:
					await message.channel.send('\'' + race + '\' is not a valid race. Please try again!')
					return
				
				await message.channel.send(self.getRaceOverview(race))
				await message.channel.send(blocksOfText.racePt3(race))
				
			if message.content == '!confirm':
				if not sessionData[userID]['race'] in self.races:
					await message.channel.send('You haven\'t chosen a proper race yet!')
				else:
					await message.channel.send('You\'ve chosen **\'' + sessionData[userID]['race'] + '\'** as your race!\nIf your racial choice requires further specification for \'sub-race\' (like the different kinds of Lashunta or Gnomes), we\'ll take care of that after a couple more steps.')
					sessionData[userID]['state'] = 3
					await message.channel.send(blocksOfText.themePt1())
					await message.channel.send(blocksOfText.listThemes())
					await message.channel.send(blocksOfText.themePt2())
					return
		#Choose Theme
		if sessionData[userID]['state'] == 3:
			#TODO
			return
		#Choose Class
		if sessionData[userID]['state'] == 4:
			#TODO
			return
		#RTC sub-choices
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