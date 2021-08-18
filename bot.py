from dotenv import load_dotenv
import discord
import json
import os

import blocksOfText
import classes
import races
import themes

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

	#on ready
	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))
		print('Self ID: {0}'.format(self.user.id))
		
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
			await message.channel.send(blocksOfText.listRaces())
			return
		if message.content == '!list theme':
			await message.channel.send(blocksOfText.listThemes())
			return
		if message.content == '!list class':
			await message.channel.send(blocksOfText.listClasses())
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
				
				if not races.isValid(race):
					await message.channel.send('\'' + race + '\' is not a valid race. Please try again!')
					return
				
				await message.channel.send(races.getRaceOverview(race))
				await message.channel.send(blocksOfText.racePt3(race))
				
			if message.content == '!confirm':
				if not races.isValid(sessionData[userID]['race']):
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
			if message.content.startswith('!theme '):
				sessionData[userID]['theme'] = message.content[7:]
				theme = message.content[7:]
				
				if not themes.isValid(theme):
					await message.channel.send('\'' + theme + '\' is not a valid theme. Please try again!')
					return
					
				for part in themes.getThemeOverview(theme):
					await message.channel.send(part)
				await message.channel.send(blocksOfText.themePt3(theme))
				return
				
			elif message.content == '!confirm':
				if not themes.isValid(sessionData[userID]['theme']):
					await message.channel.send('You haven\'t chosen a proper theme yet!')
				else:
					await message.channel.send('You\'ve chosen **\'' + sessionData[userID]['theme'] + '\'** as your theme!\nIf your choice requires further specification (like the specialization of a Scholar), we\'ll take care of that soon!')
					sessionData[userID]['state'] = 4
					await message.channel.send(blocksOfText.classPt1())
					await message.channel.send(blocksOfText.listClasses())
					await message.channel.send(blocksOfText.classPt2())
					return
		#Choose Class
		if sessionData[userID]['state'] == 4:
			if message.content.startswith('!class '):
				sessionData[userID]['class'] = message.content[7:]
				classChoice = message.content[7:]
				
				if not classes.isValid(classChoice):
					await message.channel.send('\'' + classChoice + '\' is not a valid class. Please try again!')
					return
				for part in classes.getClassOverview(classChoice):
					await message.channel.send(part)
				await message.channel.send(blocksOfText.classPt3(classChoice))
				return
				
			if message.content == '!confirm':
				if not classes.isValid(sessionData[userID]['class']):
					await message.channel.send('You haven\'t chosen a proper class yet!')
				else:
					await message.channel.send('You\'ve chosen**\'' + sessionData[userID]['class'] + '\'** as your class!\nI might have to work with you individually to flesh out your class abilities, but we\'ll cross that bridge when we get there.')
					sessionData[userID]['state'] = 5
					await message.channel.send(blocksOfText.abilityScore())
					#todo: finish filling out classes.py {mystic, operative, solarian, soldier, technomancer}
					raceBool = races.needsChoices(sessionData[userID]['race'])
					themeBool = themes.needsChoices(sessionData[userID]['theme'])
					classBool = classes.needsChoices(sessionData[userID]['class'])
					
					# treat substate as bits -> RTC (RaceThemeClass) -> 000
					if not raceBool and not themeBool and not classBool:
						await message.channel.send('Alright, we should be good to move on ahead! When you\'re ready to move on, type **!next** please.')
						sessionData[userID]['substate'] = -1
					else:
						await message.channel.send('Okay, we have to make some choices about some things yet. When you\'re ready to move on, type **!next** please.')
						if raceBool:
							sessionData[userID]['substate'] += 4
						if themeBool:
							sessionData[userID]['substate'] += 2
						if classBool:
							sessionData[userID]['substate'] += 1
					return
		#RTC sub-choices
		if sessionData[userID]['state'] == 5:
			if sessionData[userID]['substate'] >= 4: #Race
				if message.content == '!next':
					await message.channel.send(races.getChoices(sessionData[userID]['race']))
					return
				elif message.content.startswith('!'):
					if races.isValidChoice(sessionData[userID]['race'], message.content[1:]):
						stats = races.getAbilityScoreAdjustmentsChoice(sessionData[userID]['race'], message.content[1:])
						for stat in stats:
							sessionData[userID][stat] += stats[stat]
						
						sessionData[userID]['substate'] -= 4
						if sessionData[userID]['substate'] >= 2:
							await message.channel.send('Cool, on to your Theme!')
							await message.channel.send(themes.getChoices(sessionData[userID]['theme']))
							return
						elif sessionData[userID]['substate'] == 1:
							await message.channel.send('Cool, now we just need to choose your Key Ability Score for your class!')
							await message.channel.send(classes.getChoices(sessionData[userID]['class']))
							return
						else: #TODO: Done with choices
							return
						return
					else:
						await message.channel.send('Sorry, ' + message.content[1:] + ' is an invalid choice. Please try again!')
					
			elif sessionData[userID]['substate'] >= 2: #Theme
				if message.content == '!next':
					await message.channel.send(themes.getChoices(sessionData[userID]['theme']))
					return
				elif message.content.startswith('!'):
					if themes.isValidChoice(sessionData[userID]['theme'], message.content[1:]):
						stat = themes.getAbilityScoreAdjustmentsChoice(sessionData[userID]['theme'], message.content[1:])
						sessionData[userID][message.content[1:]] += stat
						sessionData[userID]['substate'] -= 2

						if sessionData[userID]['substate'] == 1:
							await message.channel.send('Cool, now we just need to choose your Key Ability Score for your class!')
							await message.channel.send(classes.getChoices(sessionData[userID]['class']))
						else:
							return #TODO: Done with choices
						return
					else:
						await message.channel.send('Sorry, ' + message.content[1:] + ' is an invalid choice. Please try again!')
			elif sessionData[userID]['substate'] == 1: #Class
				if message.content == '!next':
					await message.channel.send(classes.getChoices(sessionData[userID]['class']))
					return
				elif message.content.startswith('!'):
					return #TODO
				return
				
			elif sessionData[userID]['substate'] == 0:
				return
			elif sessionData[userID]['substate'] == -1:
				if message.content == '!next':
					stats = races.getAbilityScoreAdjustments(sessionData[userID]['race'])
					for stat in stats:
						sessionData[userID][stat] += stats[stat]
						
					stats = themes.getAbilityScoreAdjustments(sessionData[userID]['theme'])
					for stat in stats:
						sessionData[userID][stat] += stats[stat]
					
					sessionData[userID]['state'] = 6
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