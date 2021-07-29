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

# user states
# {userid, int}
# 0 = Base state
# 1 = Into and Confirmation
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



class MyClient(discord.Client):

	#on ready
	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))
		
		#initialize session data for each user
		for guild in self.guilds:
			async for member in guild.fetch_members():
				if member.id not in sessionData:
					filepath = str(member.id) + '.json'
					if os.path.exists(filepath):
						sessionData[member.id] = dict()
						sessionData[member.id]['state'] = 13
						sessionData[member.id]['substate'] = 0
						sessionData[member.id]['race'] = '' #TODO: Load from file
						sessionData[member.id]['theme'] = '' #TODO
						sessionData[member.id]['class'] = '' #TODO
						sessionData[member.id]['str'] = 10 #TODO
						sessionData[member.id]['dex'] = 10 #TODO
						sessionData[member.id]['con'] = 10 #TODO
						sessionData[member.id]['int'] = 10 #TODO
						sessionData[member.id]['wis'] = 10 #TODO
						sessionData[member.id]['cha'] = 10 #TODO
						sessionData[member.id]['abilitypoints'] = 0
						sessionData[member.id]['maxresolve'] = 0 #TODO
						sessionData[member.id]['maxstamina'] = 0 #TODO
						sessionData[member.id]['maxhp'] = 0 #TODO
						
					else:
						sessionData[member.id] = dict()
						sessionData[member.id]['state'] = 0
						sessionData[member.id]['substate'] = 0
						sessionData[member.id]['race'] = ''
						sessionData[member.id]['theme'] = ''
						sessionData[member.id]['class'] = ''
						sessionData[member.id]['str'] = 10
						sessionData[member.id]['dex'] = 10
						sessionData[member.id]['con'] = 10
						sessionData[member.id]['int'] = 10
						sessionData[member.id]['wis'] = 10
						sessionData[member.id]['cha'] = 10
						sessionData[member.id]['abilitypoints'] = 10
						sessionData[member.id]['maxresolve'] = 0
						sessionData[member.id]['maxstamina'] = 0
						sessionData[member.id]['maxhp'] = 0

	#user sent a message
	async def on_message(self, message):
		#prevent acting on own messages
		if message.author == self.user:
			return
		
		#DEBUG
		if message.content == '!members':
			print(sessionData)
		if message.content == '!purge':
			await message.channel.purge()
			
		#List character options
		if message.content == '!list race':
			await message.channel.send(blocksOfText.listRaces())
		if message.content == '!list theme':
			await message.channel.send(blocksOfText.listThemes())
		if message.content == '!list class':
			await message.channel.send(blocksOfText.listClasses())
			
		
		#Create Character
		if sessionData[message.author.id]['state'] == 0:
			
			#Start character creation
			if message.content == '!create':
				#check if user already has a file
				filepath = str(message.author.id) + '.json'
				if os.path.exists(filepath):
					await message.channel.send('You already have a character!')
					sessionData[message.author.id]['state'] = 12
					return
				
				sessionData[message.author.id]['state'] = 1
				await message.channel.send(blocksOfText.introPt1(message.author.name))
				await message.channel.send(blocksOfText.introPt2())
				
		if sessionData[message.author.id]['state'] == 1:
			if message.content == '!next':
				sessionData[message.author.id]['state'] = 2
				await message.channel.send(blocksOfText.racePt1())
				await message.channel.send(blocksOfText.listRaces())
				await message.channel.send(blocksOfText.racePt2())
		
		if sessionData[message.author.id]['state'] == 2:
			if message.content.startswith('!race '):
				sessionData[message.author.id]['race'] = message.content[6:]
				race = message.content[6:]
				
				if not races.isValid(race):
					await message.channel.send('\'' + race + '\' is not a valid race. Please try again!')
					return
				
				await message.channel.send(races.getRaceOverview(race))
				await message.channel.send(blocksOfText.racePt3(race))
				
			if message.content == '!confirm':
				if not races.isValid(sessionData[message.author.id]['race']):
					await message.channel.send('You haven\'t chosen a proper race yet!')
				else:
					await message.channel.send('You\'ve chosen **\'' + sessionData[message.author.id]['race'] + '\'** as your race!\nIf your racial choice requires further specification for \'sub-race\' (like the different kinds of Lashunta or Gnomes), we\'ll take care of that after a couple more steps.')
					sessionData[message.author.id]['state'] = 3
					await message.channel.send(blocksOfText.themePt1())
					await message.channel.send(blocksOfText.listThemes())
					await message.channel.send(blocksOfText.themePt2())
					return
		
		if sessionData[message.author.id]['state'] == 3:
			if message.content.startswith('!theme '):
				sessionData[message.author.id]['theme'] = message.content[7:]
				theme = message.content[7:]
				
				if not themes.isValid(theme):
					await message.channel.send('\'' + theme + '\' is not a valid theme. Please try again!')
					return
					
				for part in themes.getThemeOverview(theme):
					await message.channel.send(part)
				await message.channel.send(blocksOfText.themePt3(theme))
				return
				
			if message.content == '!confirm':
				if not themes.isValid(sessionData[message.author.id]['theme']):
					await message.channel.send('You haven\'t chosen a proper theme yet!')
				else:
					await message.channel.send('You\'ve chosen **\'' + sessionData[message.author.id]['theme'] + '\'** as your theme!\nIf your choice requires further specification (like the specialization of a Scholar), we\'ll take care of that soon!')
					sessionData[message.author.id]['state'] = 4
					await message.channel.send(blocksOfText.classPt1())
					await message.channel.send(blocksOfText.listClasses())
					await message.channel.send(blocksOfText.classPt2())
					return
		
		if sessionData[message.author.id]['state'] == 4:
			if message.content.startswith('!class '):
				sessionData[message.author.id]['class'] = message.content[7:]
				classChoice = message.content[7:]
				
				if not classes.isValid(classChoice):
					await message.channel.send('\'' + classChoice + '\' is not a valid class. Please try again!')
					return
				for part in classes.getClassOverview(classChoice):
					await message.channel.send(part)
				await message.channel.send(blocksOfText.classPt3(classChoice))
				return
				
			if message.content == '!confirm':
				if not classes.isValid(sessionData[message.author.id]['class']):
					await message.channel.send('You haven\'t chosen a proper class yet!')
				else:
					await message.channel.send('You\'ve chosen**\'' + sessionData[message.author.id]['class'] + '\'** as your class!\nI might have to work with you individually to flesh out your class abilities, but we\'ll cross that bridge when we get there.')
					sessionData[message.author.id]['state'] = 5
					await message.channel.send(blocksOfText.abilityScore())
					#todo: this, finish filling out classes.py {mystic, operative, solarian, soldier, technomancer}
					raceBool = races.needsChoices(sessionData[message.author.id]['race'])
					themeBool = themes.needsChoices(sessionData[message.author.id]['theme'])
					classBool = classes.needsChoices(sessionData[message.author.id]['class'])
					
					# treat substate as bits -> RTC (RaceThemeClass) -> 000
					if not raceBool and not themeBool and not classBool:
						await message.channel.send('Alright, we should be good to move on ahead! When you\'re ready to move on, type **!next** please.')
						sessionData[message.author.id]['substate'] = -1
					else:
						await message.channel.send('Okay, we have to make some choices about some things yet. When you\'re ready to move on, type **!next** please.')
						if raceBool:
							sessionData[message.author.id]['substate'] += 4
						elif themeBool:
							sessionData[message.author.id]['substate'] += 2
						else:
							sessionData[message.author.id]['substate'] += 1
					return
		
		if sessionData[message.author.id]['state'] == 5:
			#TODO
			if sessionData[message.author.id]['substate'] >= 4:
				if message.content == '!next':
					await message.channel.send(races.getChoices(sessionData[message.author.id]['race']))
					return
				if message.content == '
					
			elif sessionData[message.author.id]['substate'] >= 2:
				return
			elif sessionData[message.author.id]['substate'] == 1:
				return
				
			elif sessionData[message.author.id]['substate'] == 0:
				return
			elif sessionData[message.author.id]['substate'] == -1:
				stats = races.getAbilityScoreAdjustments()
				for stat in stats:
					sessionData[message.author.id][stat] += stats[stat]
				#todo: theme adjustment
				
				sessionData[message.author.id]['state'] = 6:
			return
		
		if sessionData[message.author.id]['state'] == 6:
			#TODO
			return
		
		if sessionData[message.author.id]['state'] == 7:
			#TODO
			return
		
		if sessionData[message.author.id]['state'] == 8:
			#TODO
			return
		
		if sessionData[message.author.id]['state'] == 9:
			#TODO
			return
		
		if sessionData[message.author.id]['state'] == 10:
			#TODO
			return
		
		if sessionData[message.author.id]['state'] == 11:
			#TODO
			return
		
		if sessionData[message.author.id]['state'] == 12:
			#TODO
			return
		
					
		#Level up your character
		if message.content == '!levelup':
			if sessionData[message.author.id]['state'] != 13:
				await message.channel.send('You don\'t have a character yet, ' + message.author.name + '! Type **!create** to get started.')
			else:
				await message.channel.send('Under construction!')
		
		
		
#Initialize bot
client = MyClient(intents=discord.Intents.all())
client.run(os.environ.get('TOKEN'))