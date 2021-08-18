themes = {'ace pilot', 'bounty hunter', 'icon', 'mercenary', 'outlaw', 'priest', 'scholar', 'spacefarer', 'xenoseeker', 'themeless'}
themesWithAbilityChoices = {'themeless'}
themeAbilityAdjustments = {
	'ace pilot': {'dexterity':1},
	'bounty hunter': {'constitution':1},
	'icon': {'charisma':1},
	'mercenary': {'strength':1},
	'outlaw': {'dexterity':1},
	'priest': {'wisdom':1},
	'scholar': {'intelligence':1},
	'spacefarer': {'constitution':1},
	'xenoseeker': {'charisma':1},
	'themeless': {
		'strength':1,
		'dexterity':1,
		'constitution':1,
		'wisdom':1,
		'intelligence':1,
		'charisma':1
	}
}



def getThemeOverview(theme):
	if theme.lower() == 'ace pilot':
		return ['''***==Ace Pilot==***
You are most comfortable at the controls of a vehicle, whether it's a starship racing through the inky void of space or a ground vehicle zooming between trees, around boulders, and across dusty badlands. You might be a member of an elite military force, the recipient of intense courses of training. Alternatively, you might be a total amateur with innate skills that make you a much-admired hotshot.

***==Ability Adjustments==***
    +1 Dexterity

***==Theme Features==***
**Theme Knowledge (1st Lvl)**
Reduce the DC of **Culture** checks to recall knowledge about starship and vehicle models and parts as well as famous hotshot pilots by 5. **Piloting** is a class skill for you, though if it is a class skill from the class you take at 1st level, you instead gain a +1 bonus to your Piloting checks.

**Lone Wolf (6th Lvl)**
Whenever you need to attempt a skill check either during starship combat or to directly repair or otherwise maintain you starship, you can treat half your ranks in **Piloting** as your ranks in the appropriate skill for the check, if that would be better. You are considered trained in the skill for the purposes of this check.

**Need for Speed (12th Lvl)**
Reduce any penalties to **Piloting** checks you make when on a vehicle by 1. When you take the double maneuver action during a vehicle chase, reduce the penalty for each action by 1. Whenever a **Piloting** check has a penalty for failing by 5 or more, you take that penalty only if you fail by 10 or more.

**Master Pilot (18th Lvl)**
Up to twice per day, when you defeat a significant foe in starship combat as a pilot or succeed in a vehicle chase (meaning that you've either escaped a pursuer or caught or defeated your opponent), you recover 1 **Resolve Point**.
		''']
	if theme.lower() == 'bounty hunter':
		return ['''***==Bounty Hunter==***
You track people down for money. It is a dangerous profession, as most of your targets understandably don't wish to be caught. You wouldn't have it any other way. You might have a code of ethics, never taking jobs that, say, target children or members of your own race. You might hunt down only escaped criminals. Or you might be completely amoral, taking any job that comes along - for the right price, of course.

***==Ability Adjustments==***
    +1 Constitution

***==Theme Features==***
**Theme Knowledge (1st Lvl)**
Choose a specific sentient creature that you can identify by name, alias, or specific identity to be your mark. Reduce the DC of **Culture** or **Profession(Bounty Hunter)** checks to recall knowledge about your mark, as well as to recall knowledge about law-enforcement individuals and practices, by 5. If you choose a mark that is known only by an alias or secred identity, this ability helps you learn facts only about the identity you know about, not any other unknown identities. Once you defeat your mark, as an action that takes 1 minute, you can study dossiers and database information about another individual to be your new mark. You can instead abandon your mark for a new one without defeating it, but if you do so, you take a -2 penalty to all skill checks for 1 week.
**Survival** is a class skill for you, though if it is a class skill from the class you take, you instead gain a +1 bonus to **Survival** checks.''','''

**Swift Hunter (6th Lvl)**
You can use **Diplomacy** to gather information about a specific individual in half the normal time, and you reduce the penalty for following tracks using **Survival** while moving at full speed to 0.

**Relentless (12th Lvl)**
You can walk or be otherwise active for 12 hours instead of 8 before needing to attempt Constitution checks for a forced march, and you can hustle for 2 hours a day during overland travel instead of 1 hour. Reduce the penalty for following tracks using **Survival** while moving at double speed to -10.

**Master Hunter (18th Lvl)**
Once per day while in pursuit of your mark, you can review current information about your mark for 10 minutes to regain 1 **Resolve Point**; this doesn't count as resting to regain **Stamina Points**. Additionally, once per day when you defeat your mark, you regain 1 **Resolve Point**.
		''']
	if theme.lower() == 'icon':
		return ['''***==Icon==***
Thanks to interstellar transmissions and Drift travel, the galaxy is smaller than ever, and this connectivity has facilitated your ascension to celebrity status. You might be a famous performer or a celebrated scientist, but either way, you get recognized on the Pact Worlds and in associated systems. Your reason for traveling to unknown worlds might be to further spread your acclaim or to escape the limelight.

***==Ability Adjustments==***
    +1 Charisma

***==Theme Features==***
**Theme Knowledge (1st Lvl)**
Choose a **Profession** skill. You are hooked deeply into the culture of your iconic profession. When attempting a **Profession** or **Culture** check to recall knowledge about other icons of your profession or details about your profession's cultural aspects, reduce the DC by 5. You gain a +1 bonus to checks with your chosen **Profession** skill. **Culture** also becomes a class skill for you, though if it is a class skill from the class you take, you instead gain a +1 bonus to **Culture** checks.''','''

**Celebrity (6th Lvl)**
You are famous enough that pretty much everyone has either heard of you or can quickly find information about you. If you're looking for a generic person like "a doctor who can treat this disease", you can almost always find one who's a fan and whose attitude starts as friendly or helpful to you; this takes 2d4 hours. At the GM's discretion, fans might even give you service (but not goods) for a discount or even for free.

**Megacelebrity (12th Lvl)**
The DC of **Culture** checks to recognize you is reduced to 5 (or 10 to recognize you out of context from appearance alone) and it takes only 1d4 hours to find a fan who meets a generic description. In addition, fans give you a 10% discount on goods.

**Master Icon (18th Lvl)**
Up to twice per day, you can interact with the public about your profession (usually during a performance, but sometimes in a press conference afterward if your profession requires no audience) for a total of at least 10 minutes to recover 1 **Resolve Point**. 
		''']
	if theme.lower() == 'mercenary':
		return ['''***==Mercenary==***
Whether you take jobs that match your ethical beliefs or you fight for anyone who can afford your services, you are a hired gun. You might take pride in your past accomplishments, proudly displaying trophies of your kills, or you might be laden with guilt over being the sole survivor of a mission gone terribly wrong. You most likely work with other mercenaries and are familiar with the methodologies of military actions all across the galaxy.

***==Ability Adjustments==***
    +1 Strength

***==Theme Features==***
**Theme Knowledge (1st Lvl)**
Reduce the DC of **Culture** checks and **Profession(Mercenary)** checks to recall knowledge abour hierarchies, practices, personnel, and so on in the military by 5. **Athletics** is a class skill for you, though if it is a class skill from the class you take, you instead gain a +1 bonus to **Athletics** checks.

**Grunt (6th Lvl)**
Treat your **Strength** as 1 higher for the purpose of determining your bulk limit. *TODO: Replace this with something else, I don't care about bulk*

**Squad Leader (12th Lvl)**
If you are able to attempt the check in question, you automatically succeed at a skill check to aid another person when assisting a squad member or other longtime ally.

**Commander (18th Lvl)**
After participating in at least three combats in a day in which you defeat distinct groups of significant foes, you recover 1 **Resolve Point**. After participating in six such combats in a day, you recover a second **Resolve Point**.
		''']
	if theme.lower() == 'outlaw':
		return ['''***==Outlaw==***
Due to the sins of your past or your current unlawful behavior, you are a wanted individual somewhere in the Pact Worlds. You might not even be guilty and are striving to clear your good name. Or you might fully admit to being a criminal but believe the laws you break are unjust. Whatever the case, boarding a starship headed to the Vast might be just the thing you need until the heat dies down - or until you're dragged off to prison.

***==Ability Adjustments==***
    +1 Dexterity

***==Theme Features==***
**Theme Knowledge (1st Lvl)**
Reduce the DC of **Culture** checks to recall knowledge about the criminal underworld by 5. **Sleight of Hand** is a class skill for you, though if it is a class skill from the class you take at 1st level, you instead gain a +1 bonus to **Sleight of Hand** checks.

**Legal Corruption (6th Lvl)**
Depending on the severity of the crime, you may be able to use your underworld contacts to get you out of legal trouble. This can cost anywhere between 500 credits x your level and 10,000 credits x your level.

**Black Market Connections (12th Lvl)**
You can sell goods in any city for their usual price, even if the goods are illegal or too luxurious for the locals to afford. Additionally, for 10% more than the usual price, you can purchase goods to be delivered to a remote drop-off point (possibly near an adventure location) in the same solar system as a familiar city. The delivery always takes at least as lon as the journey between the city and the drop-off point - and usually longer.

**Master Outlaw (18th Lvl)**
Up to twice per day, after you spend at least 10 minutes to plan a significant heist, caper, or other crime (this doesn't count as resting to regain **Stamina Points**) and successfully complete at least one action toward enacting that plan, you regain 1 **Resolve Point**.
		''']
	if theme.lower() == 'priest':
		return ['''***==Priest==***
You are a member of an organized religion or similar association. Your belief, whether it has been a part of you since childhood or it came to you later in life, is an integral part of your character. You m ight travel the stars proselytizing your deity, or your church might have sent you out on a specific holy (or unholy) mission. No matter what obstacles life puts in your way, you always have the conviction of your beliefs to fall back on.

***==Ability Adjustments==***
    +1 Wisdom

***==Theme Features==***
**Theme Knowledge (1st Lvl)**
Choose a deity or a philosophy whose alignment is within one step (on either the good-evil axis or the law-chaos axis) of your own. Reduce the DC of **Culture** and **Mysticism** checks to recall knowledge about religious traditions, religious symbols, and famous religious leaders by 5. **Mysticism** becomes a class skill for you, though if it's a class skill from the class you take, you instead gain a +1 bonus to **Mysticism** checks.''','''

**Mantle of the Clergy (6th Lvl)**
Typical laymen followers of your religion have a starting attitude of helpful toward you and will often provide you with simple assistance on request due to some combination of adoration, respect, or fear (depending on your religion), and even other clergy must give your opinions due consideration in matters of disagreement. You gain a +2 bonus to **Diplomacy** and **Intimidate** checks against said followers and clergy.

**Divine Boon (12th Lvl)**
Choose one 1st-level **Mystic** spell with some connection to your deity's portfolio (subject to GM's approval). If you have levels in the **Mystic** class, you gain 1 additional 1st-level spell per day, and add the chosen spell to your list of **Mystic** spells known. Otherwise, you can use the spell once per day as a spell-like ability.

**True Communion (18th Lvl)**
Up to twice per day, after performing a significant action strongly aligned with your faith's dogma (at GM's discretion), you can spend 10 minutes in deep meditation or prayer to regain 1 **Resolve Point**. This doesn't count as resting to regain **Stamina Points**.
		''']
	if theme.lower() == 'scholar':
		return ['''***==Scholar==***
You are an erudite intellectual, pitting your brain against problems and puzzles that others would find daunting. You might be an instructor of a specific topic at a large university or a dabbler in a number of fields of study. You could be exploring the galaxy in search of ancient artifacts or new scientific phenomena. Whatever your motivation, you are sure that the answers you seek are out there.

***==Ability Adjustments==***
    +1 Intelligence

***==Theme Features==***
**Theme Knowledge (1st Lvl)**
You are an expert in one particular field of study, and your passion for it shows. Choose either **Life Science** or **Physical Science**, and then choose a field of specialization. If you pick **Life Science**, you can specialize in:
Bioengineering, Biology, Botany, Ecology, Genetics, Xenobiology, Zoology, Another field (at GM's discretion)
If you pick **Physical Science**, you can specialize in:
Astronomy, Chemistry, Climatology, Geography, Geology, Meteorology, Oceanography, Physics, Another field (at GM's discretion)
The DC of skill checks to recall knowledge about your specialty is reduced by 5. Your chosen skill is a class skill for you, though if it is a class skill from the class you take, you instead gain a +1 bonus to checks with your chosen skill.''','''

**Tip of the Tongue (6th Lvl)**
Once per day, you can reroll any skill check to recall knowledge. You must decide to use this ability after rolling but before learning the information from your first roll. You must take the second result, even if it is worse.

**Research Maven (12th Lvl)**
You can research much faster than most other people, allowing you to collate information from databases, libraries, and other sources in one-quarter the normal time; with this ability, you can typically take 20 to recall knowledge in 5 rounds.

**Master Scholar (18th Lvl)**
Up to twice per day, when in a situation where information from your specialty field could be useful (at GM's discretion), you can spend 10 minutes in deep contemplation and research of your specialty field and recover 1 **Resolve Point**, in addition to using recall knowledge for the information you seek. This doesn't count as resting to regain **Stamina Points**.
		''']
	if theme.lower() == 'spacefarer':
		return ['''***==Spacefarer==***
Your longing to journey among the stars can't be sated. You yearn for the adventure of stepping onto a distant world and exploring its secrets. You tend to greet every new opportunity with bravery and fortitude, confident that your multitude of skills will pull you through. Perhaps you simply find joy in the act of traveling with your companions, or perhaps you are just out to line your pockets with all sorts of alien loot!

***==Ability Adjustments==***
    +1 Constitution

***==Theme Features==***
**Theme Knowledge (1st Lvl)**
Reduce the DC of **Physical Science** checks to recall knowledge about strange new worlds or features of space by 5. **Physical Science** is a class skill for you, though if it is a class skill from the class you take, you instead gain a +1 bonus to **Physical Science** checks.

**Eager Dabbler (6th Lvl)**
You gain a +2 bonus to skill checks if you don't have any ranks in that skill. This does not allow you to attempt checks for trained-only skills.

**Jack of all Trades (12th Lvl)**
You can use all skill untrained, even if you could not normally do so, and when you roll a natural 20 while attempting a skill check for a skill in which you don't have ranks, your bonus from eager dabbler increases to +4 for that skill permanently.

**Master Explorer (18th Lvl)**
Up to twice per day while on an unexplored planet (typically one that has had no contact with the Pact Worlds, though it doesn't need to be one you discovered yourself), you can spend 10 minutes exploring, mapping, and documenting a new geographical feature to recover 1 **Resolve Point**. This doesn't count as resting to regain **Stamina Points**.
		''']
	if theme.lower() == 'xenoseeker':
		return ['''***==Xenoseeker==***
The thought of meeting alien life-forms excites you. The more different their appearances and customs are from yours, the better! You either believe they have much to teach you or you want to prove you are better than them. Of course, the only way to accomplish your goal is to leave the Pact Worlds and travel to the Vast, where a virtually endless number of aliens await.

***==Ability Adjustments==***
    +1 Charisma

***==Theme Features==***
**Theme Knowledge (1st Lvl)**
Reduce the DC to identify a rare creature using **Life Science** by 5. **Life Science** is a class skill for you, though if it is a class skill from the class you take, you instead gain a +1 bonus to **Life Science** checks.

**Quick Pidgin (6th Lvl)**
If you don't share a language with creatures you encounter, you and the creatures can spend 10 minutes attempting to converse (if they are willing), after which you attempt a DC25 **Culture** check. If you succeed, you formulate a simple pidgin language that allows basic communication. You can use the pidgin language with those specific creatures only, but you gain a +2 bonus to **Culture** checks to create a pidgin language with similar creatures that speak the same language.

**First Contact (12th Lvl)**
When meeting a creature that has never seen your race or any of the races of your traveling companions, if it would normally be unfriendly to unknown races, treat it as indifferent instead. This has no effect if the creature would be hostile, indifferent, friendly, or helpful.

**Brilliant Discovery (18th Lvl)**
Up to twice per day, when you discover and document a new species of flora or fauna, you recover 1 **Resolve Point**. On an unexplored planet where every species is new, this process usually takes 10 minutes at most (and doesn't count as rest to regain **Stamina Points**), but even on known planets, you might be able to find a new species in 1d4 hours in a remote biome or one with a high variety of wildlife.
		''']
	if theme.lower() == 'themeless':
		return ['''***==Themeless==***
You don't fit neatly into any of the above categories, or you see yourself as a blank slate. A themeless character is considerably less powerful than a character with a theme, so take care if choosing this option!

***==Ability Adjustments==***
    +1 Your Choice

***==Theme Features==***
**General Knowledge (1st Lvl)**
You gain a class skill of your choice.

**Certainty (6th Lvl)**
Once per day before you roll a skill check, you can gain a +2 bonus to that skill for that check.

**Extensive Studies (12th Lvl)**
Choose a skill that is a class skill for you. Once per day, you can reroll one such skill check before learning the results of the roll. You must take the second result, even if it is worse.

**Steely Determination (18th Lvl)**
Increase your pool of **Resolve Points** by 1.
		''']
	
def isValid(theme):
	return theme.lower() in themes
	
def needsChoices(theme):
	return theme.lower() in themesWithAbilityChoices
	
def isValidChoice(theme, choice):
	return theme.lower() in themesWithAbilityChoices and choice.lower() in themeAbilityAdjustments[theme.lower()]

def getChoices(theme):
	if theme.lower() == 'themeless':
		return '''As a Themeless character, you may increase any ability score by 1.

To make your choice type ***!{Ability}*** (for example, ***!wisdom*** or ***!dexterity***)'''

#overload
#theme does not require further choice
#Returns: dict of stat adjustment
def getAbilityScoreAdjustments(theme):
	return themeAbilityAdjustments[theme.lower()]
	
#overload
#theme requires further choice
#Returns: singular stat adjustment
def getAbilityScoreAdjustmentsChoice(theme, choice):
	return themeAbilityAdjustments[theme.lower()][choice.lower()]