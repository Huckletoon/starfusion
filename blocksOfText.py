def test():
	return 'test successful'
	
def introPt1(name):
	return '''Let\'s make your character, ''' + name + '''!
There's a lot that goes into making a character for an RPG, so I recommend setting aside a good chunk of time to do this: 30-60 minutes should be good. I know, that's a long time, but hang in there!

***If you don't have the time right now and need to come back to this later***, type **!cancel**.

So, welcome to Starfinder! In this Fantasy Sci-fi Role Playing Game, you and your party members will embark on a grand journey through the galaxy. If you haven't already, please read through the introductory post in the #📕rules channel.

Your character is your manifestation in the world. This character is comprised of not only their abilities in the game, but also their personality and goals! Both one's abilities and their personality are what make this a *role-playing* game. Your character doesn't have to be like you in real life, but they can be if you want!'''

def introPt2():
	return '''Now, start thinking about what kind of character you want to play as. If you don't know where to start, maybe think of some characters from fictional tales that you enjoy, like Spike from Cowboy Bebop, Rocket from the Guardians of the Galaxy, or even Mickey Mouse. You'll be choosing 3 main things that will outline your character:

  - **Race**: The species that your character is. Can range from a **Human** to classic fantasy races like **Elf** or **Dwarf** to an **Android** or even a 4-armed **Kasatha**!
  - **Theme**: The core of your character's motivations. Are you a **Bounty Hunter** or **Mercenary** just looking for the next paycheck, or maybe a **Scholar** or **Priest**? Perhaps you're an **Icon**, a celebrity streaming their adventures to the entertainment channels of the solar system!
  - **Class**: Your character's basis for their heroic abilities. As you gain experience, your abilities granted here will improve, and you will earn more unique abilities as well. Is your character a master **Mechanic**, or perhaps they've channeled the magics of the universe as a **Mystic**?

We're going to go through the available options one step at a time. While some races may be more comfortable playing as certain classes, it's entirely possible to mix and match your choices in any way you'd like!

If you want to see a list of the options ahead of time to help you decide, type **!list race**, **!list theme**, or **!list class** to see those. When you're ready to get started, go ahead and type **!next** please!
'''

def listRaces():
	return '''Here's a list of all the playable **Races** for our campaign:
			
**Android**: Artificial people with mechanical components, formerly built as servants but now recognized as citizens.

**Dwarf**: A stocky race with broad, heavy frames. Forged in the furnace of the lost planet Golarion, they strive to keep their traditions alive.

**Elf**: Lithe, long lived humanoids with pointed ears from the lost planet Golarion, still trying to find the truth behind the Gap.

**Gnome**: Descendants of the Fey with two striking ethnicities: the whimsical Feychildren and the dour Bleachlings.

**Half-Elf**: Children of mixed race, their blood is that of both Human and Elf; if they hide their pointed ears, they can pass as tall Humans.

**Half-Orc**: Descendants of both Humans and Orcs, they sport muscular builds with green or gray skin and larger tusk-like canines.

**Halfling**: A short, nimble, and charming people capable of just as much as everyone twice their size.

**Human**: Extremely versatile and adaptable race that's constantly expanding and exploring.

**Kasatha**: Four-armed race from a distant desert world with a highly traditional culture.

**Lashunta**: Charismatic and telepathic race of scholars with two subspecies: one tall and lean, the other short and muscular.

**Shirren**: Insectile race that broke away from a locustlike hive, community-minded b ut addicted to individual choice.

**Vesk**: Warlike reptilian race that recently declared a truce with the others - for now.

**Ysoki**: Also called "ratfolk", these short, furry scavengeres make up for their short size with big personalities.
	'''

def listThemes():
	return '''Here's a list of all the **Themes** available:
			
**Ace Pilot**: Skillful operator of starships and other vehicles who is obsessed with all related knowledge and lore.

**Bounty Hunter**: Unstoppable tracker who knows how to stay hot on the trail of those who flee.

**Icon**: Popular and respected celebrity who can leverage the public's adoration for specific needs.

**Mercenary**: Well-trained soldier of fortune who can work equally well as a combat grunt or a squad leader.

**Outlaw**: Wanted criminal with back-alley connections to black markets and associates who can fend off legal trouble.

**Priest**: Dedicated and knowledgeable adherent to a philosophy or religion who commands clout among other followers.

**Scholar**: Skilled researcher and cutting-edge thinker with a broad base of knowledge and a thirst to expand it.

**Spacefarer**: Restless explorer who has a strong intuition and has collected deep knowledge about alien biology and topology.

**Xenoseeker**: Guru of alien life-forms who finds that meeting them is one of life's most rewarding accomplishments.

**Themeless**: One who doesn't fit into any niche above but forges a personal path of determination and training.
	'''
	
def listClasses():
	return '''Here's a list of the classes you may choose:

**Envoy**: Charismatic people person good at a wide range of skills who inspires allies to accomplish great heroic feats.

**Mechanic**: Master of machines and technology whose tinkering produces a drone companion or a powerful brain implant.

**Mystic**: Magic user whose mysterious connection to a powerful force grants abilities that break the laws of the universe.

**Operative**: Stealthy combatant with wide-ranging know-how who is adept at taking advantage of unprepared foes.

**Solarian**: Disciplined warrior whose mastery of the stars grants either a weapon or armor made of stellar power.

**Soldier**: Expert with a huge range of armor, guns, and melee weapons who specializes in certain types of gear.

**Technomancer**: Magic user who is preternaturally attuned to technology and can use it to unlock powerful effects.
	'''
	
def racePt1():
	return '''Alright, let's get started! First up is your character's race.'''
	
def racePt2():
	return '''To select a race and learn more about what that entails, type **!race** ***{insert race name here}*** without the curly braces (e.g. **!race Elf**).
You may also view everything online here: https://www.starjammersrd.com/'''
	
def racePt3(race):
	return '''If you want to choose **''' + race + '''**, type **!confirm** please! Otherwise, feel free to keep browsing the options with **!race** ***{insert race name here}***'''

def themePt1():
	return '''Now it's time for your character's **theme**! As a reminder, a **Theme** is the core of your character's motivations - their ambitions, goals, and dreams. Another way to think of this could be the favored career path of the character, though this isn't necessarily the case.
	'''

def themePt2():
	return '''To select a **theme** and learn more about what that entails, type **!theme** ***{insert theme name here}*** without the curly braces, just like before. Again, you may also view everything online at https://www.starjammersrd.com/'''
	
def themePt3(theme):
	return '''If you want to choose **''' + theme + '''**, type **!confirm** please! Otherwise, feel free to keep browsing the options with **!theme** ***{insert theme name here}***'''
	
def classPt1():
	return '''Alright, on to your **class**! This will determine most of your heroic abilities as you progress through your adventure. As such, there's a lot that goes into these classes - more than I can fit into Discord messages. As such, the overviews here will provide you with the bare minimum of what you need to know to get started, but I'll also provide a link to the reference page for the class if you want to look ahead and see what cool abilities you get as you level up!'''
	
def classPt2():
	return '''To select a **class** and learn more, type **!class** ***{insert class name here}*** - you know the drill.'''
	
def classPt3(classChoice):
	return '''If you want to choose **''' + classChoice + '''**, type **!confirm** please! Otherwise, feel free to look around with **!class** ***{insert class name here}***'''
	
def abilityScore():
	return '''Time to get into some actual numbers - your Ability Scores! Except, not quite yet; we still need to go through any choices that still need to be made about your character that might impact your Ability Scores, like racial dimorphism, the themeless character theme, or the Soldier's key ability score.
	
I've just gotta check to see if you even need to make any of these choices, so hang tight just a second...'''

		
		