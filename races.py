races = {'android', 'dwarf', 'elf', 'gnome', 'half-elf', 'half-orc', 'halfling', 'human', 'kasatha', 'lashunta', 'shirren', 'vesk', 'ysoki'}
racesWithAbilityChoices = {'gnome', 'half-elf', 'half-orc', 'human', 'lashunta'}
raceAbilityAdjustments = {
	'android': {
		'maxhp':4,
		'dexterity':2,
		'intelligence':2,
		'charisma':-2},
	'dwarf': {
		'maxhp':6,
		'constitution':2,
		'wisdom':2,
		'charisma':-2},
	'elf': {
		'maxhp':4,
		'dexterity':2,
		'intelligence':2,
		'constitution':-2},
	'gnome': {
		'maxhp':4,
		'wisdom':2,
		'strength':-2}
	

}

#Params
#	string: character's race
#Returns 
#	string: bot's message text describing the race's stat adjustments and traits
def getRaceOverview(race):
	if race.lower() == 'android':
		return '''***==Android==***
Complex technological creations crafted to resemble humans, androids were originally a servitor race, but they have since broken free to form their own society. Unlike ordinary robots or ship AIs, androids do not simply respond according to their programming; rather, they have independent consciousnesses and are animated by souls—a distinction crucial to their generally accepted status as people rather than property.

***==Stats==***
**Hit points:** 4
**Ability adjustments**
    +2 Dexterity
	+2 Intelligence
	-2 Charisma
**Size and type:** Medium Humanoid(Android)

***==Racial Traits==***
**Constructed**
For effects targeting creatures by type, androids count as both humanoids and constructs (whichever effect is worse). They receive a +2 racial bonus to saving throws against disease, mind-affecting effects, poison, and sleep, unless those effects specifically target constructs. In addition, androids do not breathe or suffer the normal environmental effects of being in a vacuum.
**Exceptional Vision**
Androids have low-light vision and darkvision. As a result, they can see in dim light as if it were normal light, and they can see with no light source at all to a range of 60 feet in black and white only.
**Flat Affect**
Androids find emotions confusing and keep them bottled up. They take a –2 penalty to Sense Motive checks, but the DCs of Sense Motive checks attempted against them increase by 2.
**Upgrade Slot**
Androids have a single armor upgrade slot in their bodies. Regardless of whether androids are wearing physical armor, they can use this slot to install any one armor upgrade that could be installed into light armor.
		'''
	elif race.lower() == 'dwarf':
		return '''***==Dwarf==***
Dwarves are a stocky race, roughly a foot shorter than humans, with broad, heavy frames. Dwarves trace their heritage to the furnaces of subterranean passages, and many dwarves born long after the planet’s disappearance still feel the sting of its loss, kept alive in dwarven song and legend. Dwarven history also claims that they once had a different racial god.
Dwarves are most commonly found where their guilds and clans wield significant power, or on city-sized starships. Significant dwarven communities on other worlds are rare, though small groups can be found throughout extrasolar colonies. Many dwarves are attracted to asteroid mining, with Star Citadels common in the Diaspora.

***==Stats==***
**Hit points:** 6
**Ability adjustments**
    +2 Constitution
	+2 Wisdom
	-2 Charisma
**Size and type:** Medium Humanoid(Dwarf)

***==Racial Traits==***
**Darkvision**
Dwarves can see up to 60 feet in the dark.
**Slow but Steady**
Dwarves have a land speed of 20 feet, which is never modified when they are encumbered or wearing heavy armor. They also gain a +2 racial bonus to saving throws against poisons, spells, and spell-like abilities, and when standing on the ground they gain a +4 racial bonus to their KAC against bull rush and trip combat maneuvers.
**Stonecunning**
Dwarves gain a +2 bonus to Perception checks to notice unusual stonework, such as traps and hidden doors located in stone walls or floors. They receive a check to notice such features whenever they pass within 10 feet of them, whether or not they are actively looking.
**Traditional Enemies**
Dwarves still train to fight their ancient enemies. A dwarf gains a +1 racial bonus to attack rolls against a creature with the goblinoid or orc subtype and a +4 racial bonus to AC against an attack from a creature with the giant subtype.
**Weapon Familiarity**
Dwarves are proficient with basic and advanced melee weapons and gain specialization with those weapons at 3rd level.
		'''
	elif race.lower() == 'elf':
		return '''***==Elf==***
Lithe, long-lived humanoids, elves are easily recognized by their pointed ears and pupils so large that their eyes seem to be all one color. Possessed of an inherent bond with the natural world, they tend to subtly take on the coloration of their surroundings over the course of many years and have a deep spiritual regard for nature.
Of all the races common to the solar system, elves were perhaps the hardest-hit, and the slowest to adapt and recover. Where shorter-lived races quickly gave birth to children who had never known any other way of life and thus were personally unaffected by the loss of history, the elven generation continued on, broken and confused by the blank centuries in their own lives and memories. What’s more, those leaders charged with trying to piece together their social history from scraps soon came to a grim conclusion: their race had been betrayed by another—yet exactly which race was involved remains unclear, all suggestions of the answer scrubbed.

***==Stats==***
**Hit points:** 4
**Ability adjustments**
    +2 Dexterity
	+2 Intelligence
	-2 Constitution
**Size and type:** Medium Humanoid(Elf)

***==Racial Traits==***
**Elven Immunities**
Elves are immune to magic sleep effects and receive a +2 racial bonus to saving throws against enchantment spells and effects.
**Elven Magic**
Elves receive a +2 racial bonus to caster level checks to overcome spell resistance. In addition, elves receive a +2 racial bonus to Mysticism skill checks.
**Keen Senses**
Elves receive a +2 racial bonus to Perception skill checks.
**Low-Light Vision**
Elves can see in dim light as if it were normal light.
		'''
	elif race.lower() == 'gnome':
		return '''***==Gnome==***
Gnomes are a vivacious people who have adapted to their tumultuous heritage in curious ways, and evolved significantly from accounts found in records.

***==Stats==***
**Hit points:** 4
**Ability adjustments**
    +2 Wisdom
	-2 Strength
   Feychild
	+2 Charisma
   Bleachling
	+2 Intelligence
**Size and type:** Small Humanoid(Gnome)

***==Racial Traits==***
**Curious**
Gnomes receive a +2 racial bonus to Culture checks.
**Eternal Hope**
Gnomes receive a +2 racial bonus to saving throws against fear and despair effects. Once per day, after rolling a 1 on a d20, the gnome can reroll and use the second result.
**Gnome Magic**
Gnomes gain the following spell-like abilities:
    1/day—dancing lights, ghost sound, and token spell.
The caster level for these effects is equal to the gnome’s character level. In addition, gnomes get a +2 racial saving throw bonus against illusion spells and effects.
**Low-Light Vision**
Gnomes can see in dim light as if it were normal light.
		'''
	elif race.lower() == 'half-elf':
		return '''***==Half-Elf==***
Half-elves are the interracial children of human and elven parents or the descendants of such children. While they can often pass for human by hiding their Modestly pointed ears, they nevertheless tend toward the tall, slim physiques of their elven parents, with life spans twice as long as those of their human kin. Despite being seen as generally attractive by both races, half-elves often feel like outsiders in both societies, always exoticized and never quite accepted as part of either group. This leads many half-elves to band together with others of their kind or else abandon both their parent races in favor of new friends and families among aliens who lack those preconceptions. Since half-elves breed true, many second- or third-generation half-elves have no firsthand knowledge of their parent cultures.

***==Stats==***
**Hit points:** 4
**Ability adjustments**
    +2 Your Choice
**Size and type:** Medium Humanoid(Elf/Human)

***==Racial Traits==***
**Adaptability**
Half-elves receive Skill Focus as a bonus feat at 1st level.
**Elven Blood**
Half-elves are immune to magic sleep effects and receive a +2 racial bonus to saving throws against enchantment Spells and effects.
**Keen Senses**
Half-elves receive a +2 racial bonus to Perception skill checks.
**Low-Light Vision**
Half-elves can see dim light as if it were normal light.
		'''
	elif race.lower() == 'half-orc':
		return '''***==Half-Orc==***
Half-orcs have both human and orc ancestry. Though these individuals sometimes result from the union of orcs and humans, the relative rarity of pure-blooded orcs means that most half-orcs are the children of other half-orcs. They usually stand a bit taller than humans and have strong, muscular builds, with green or gray skin. Many half-orcs have tusk-like canines protruding from their lower jaws, as well as slightly pointed ears and large brows that give them a brooding appearance.

***==Stats==***
**Hit points:** 6
**Ability adjustments**
    +2 Your Choice
**Size and type:** Medium Humanoid(Human/Orc)

***==Racial Traits==***
**Darkvision**
Half-orcs can see up to 60 feet in the dark.
**Intimidating**
Half-orcs receive a +2 racial bonus to Intimidate skill checks.
**Orc Ferocity**
Once per day, a half-orc brought to 0 Hit Points but not killed can fight on for 1 more round. The half-orc drops to 0 HP and is dying (following the normal rules for death and dying) but can continue to act normally until the end of his next turn, when he becomes unconscious as normal. If he takes additional damage before this, he ceases to be able to act and falls unconscious.
**Self-Sufficient**
Half-orcs receive a +2 racial bonus to Survival skill checks.
		'''
	elif race.lower() == 'halfling':
		return '''***==Halfling==***
Gifted with quick reflexes, charming confidence, and an apparent lack of fear, halflings are known across the galaxy as athletes, celebrities, and explorers. Of course, this dramatic public image hardly defines the race as a whole. While most halflings experience a period of daredevil bravado in early adulthood, most settle out of it again just as quickly to become happy and loving homebodies, content with a hard day’s work and an evening spent with friends. Boasting a wide variety of eye, hair, and skin colors mirroring the human range, halflings usually have slight builds and large hands and feet. They make fast friends wherever they travel, preferring negotiation or clever wordplay to combat. Despite this accommodating nature, they have few permanent allies; halfling history is littered with long eras of domination and abuse, making them gregarious but wary of placing themselves in situations they can’t get out of again. While they share much in common with the ysoki—a love of travel and trade especially—they lack the ratfolk’s mechanical inclinations, and the two races often compete for markets, salvage rights, and trade lanes. If halflings truly ally with any race, it is humans, whose history is intimately entwined with their own, for better or worse.

***==Stats==***
**Hit points:** 2
**Ability adjustments**
    +2 Dexterity
	+2 Charisma
	-2 Strength
**Size and type:** Small Humanoid(Halfling)

***==Racial Traits==***
**Halfling Luck**
Halflings receive a +1 racial bonus to all saving throws. This bonus increases to +3 against fear effects.
**Keen Senses**
Halflings receive a +2 racial bonus to Perception skill checks.
**Sneaky**
Halflings receive a +2 racial bonus to Stealth checks. In addition, halflings reduce the penalty for using Stealth while moving by 5, and reduce the Stealth check penalty for sniping by 10.
**Sure-Footed**
Halflings receive a +2 racial bonus to Acrobatics and Athletics skill checks.
		'''
	elif race.lower() == 'human':
		return '''***==Human==***
Ambitious, creative, and endlessly curious, humans have shown more drive to explore their system and the universe beyond than any of their neighbor races—for better and for worse. They’ve helped usher in a new era of system-wide communication and organization and are admired for their passion and tenacity, but their tendency to shoot first and think about the consequences later can make them a liability for those races otherwise inclined to work with them.
Humans born and raised in isolated or unusual locations sometimes develop different physical and mental traits than those widely considered to be the norm for their species. Whether through decades of interaction with other species or adaptation to harsh environments, these differing traits represent humanity’s constant drive to change and progress.

***==Stats==***
**Hit points:** 4
**Ability adjustments**
    +2 Your Choice
**Size and type:** Medium Humanoid(Human)

***==Racial Traits==***
**Bonus Feat**
Humans select one extra feat at 1st level.
**Skilled**
Humans gain an additional skill rank at 1st level and each level thereafter.
		'''
	elif race.lower() == 'kasatha':
		return '''***==Kasatha==***
Originally from a planet orbiting a dying star, the four-armed kasathas maintain a reputation as a noble and mysterious people. They are famous for their anachronistic warriors, ancient wisdom, and strange traditions.

***==Stats==***
**Hit points:** 4
**Ability adjustments**
    +2 Strength
	+2 Wisdom
	-2 Intelligence
**Size and type:** Medium Humanoid(Kasatha)

***==Racial Traits==***
**Desert Stride**
Kasathas can move through nonmagical difficult terrain in deserts, hills, and mountains at their normal speed.
**Four-Armed**
Kasathas have four arms, which allows them to wield and hold up to four hands’ worth of weapons and equipment. While their multiple arms increase the number of items they can have at the ready, it doesn’t increase the number of attacks they can make during combat.
**Historian**
Due to their in-depth historical training and the wide-ranging academic background knowledge they possess, kasathas receive a +2 racial bonus to Culture checks.
**Natural Grace**
Kasathas receive a +2 racial bonus to Acrobatics and Athletics checks.
		'''
	elif race.lower() == 'lashunta':
		return '''***==Lashunta==***
Idealized by many other humanoid races and gifted with innate psychic abilities, lashuntas are at once consummate scholars and enlightened warriors, naturally divided into two specialized subraces with different abilities and societal roles.

***==Stats==***
**Hit points:** 4
**Ability adjustments**
    +2 Charisma
   Korasha (Muscular)
	+2 Strength
	-2 Wisdom
   Damaya (Tall/Clever)
    +2 Intelligence
	-2 Constitution
**Size and type:** Medium Humanoid(Lashunta)

***==Racial Traits==***
**Lashunta Magic**
Lashuntas gain the following spell-like abilities:
At will: daze, psychokinetic hand
1/day: detect thoughts
The caster level for these effects is equal to the lashunta’s level.
**Limited Telepathy**
Lashuntas can mentally communicate with any creatures within 30 feet with whom they share a language. Conversing telepathically with multiple creatures simultaneously is just as difficult as listening to multiple people speaking.
**Student**
Lashuntas love to learn, and they receive a +2 racial bonus to any two skills of their choice.
		'''
	elif race.lower() == 'shirren':
		return '''***==Shirren==***
Once part of a ravenous hive of locust-like predators, the insectile shirrens only recently broke with their hive mind to become a race of telepaths physically addicted to their own individualism, yet dedicated to the idea of community and harmony with other races.

***==Stats==***
**Hit points:** 6
**Ability adjustments**
    +2 Constitution
	+2 Wisdom
	-2 Charisma
**Size and type:** Medium Humanoid(Shirren)

***==Racial Traits==***
**Blindsense**
Shirrens’ sensitive antennae grant them blindsense (vibration)—the ability to sense vibrations in the air—out to 30 feet. A shirren ignores the Stealth bonuses from any form of visual camouflage, invisibility, and the like when attempting a Perception check opposed by a creature’s Stealth check. Even on a successful Perception check, any foe that can’t be seen still has total concealment (50% miss chance) against a shirren, and the shirren still has the normal miss chance when attacking foes that have concealment. A shirren is still flat-footed against attacks from creatures it can’t see.
**Communalism**
Shirrens are used to working with others as part of a team. Once per day, as long as an ally is within 10 feet, a shirren can roll a single attack roll or skill check twice and take the higher result.
**Cultural Fascination**
Shirrens are eager to learn about new cultures and societies. Shirrens receive a +2 racial bonus to Culture and Diplomacy checks.
**Limited Telepathy**
Shirrens can communicate telepathically with any creatures within 30 feet with whom they share a language. Conversing telepathically with multiple creatures simultaneously is just as difficult as listening to multiple people speak.
		'''
	elif race.lower() == 'vesk':
		return '''***==Vesk==***
Heavily muscled and covered with thick scales and short, sharp horns, the reptilian vesk are exactly as predatory and warlike as they appear. Vesk originally sought to conquer and subdue their stellar neighbors, as they had all the other intelligent races in their own system, until an overwhelming threat forced them into a grudging alliance.

***==Stats==***
**Hit points:** 6
**Ability adjustments**
    +2 Strength
	+2 Constitution
	-2 Intelligence
**Size and type:** Medium Humanoid(Vesk)

***==Racial Traits==***
**Armor Savant**
Vesk use armor in a way that complements their uniquely sturdy physiology. When wearing armor, they gain a +1 racial bonus to AC. When they’re wearing heavy armor, their armor check penalty is 1 less severe than normal.
**Fearless**
Vesk receive a +2 racial bonus to saving throws against fear effects.
**Low-Light Vision**
Vesk can see in dim light as if it were normal light.
**Natural Weapons**
Vesk are always considered armed. They can deal 1d3 lethal damage with unarmed strikes and the attack doesn’t count as archaic. Vesk gain a unique weapon specialization with their natural weapons at 3rd level, allowing them to add 1–1/2 × their character level to their damage rolls for their natural weapons (instead of just adding their character level, as usual).
		'''
	elif race.lower() == 'ysoki':
		return '''***==Ysoki==***
Small and furtive, the ysoki are often overlooked by larger races. Yet through wit and technological prowess, they’ve spread throughout the Solar system, giving truth to the old adage that every starship needs a few rats.

***==Stats==***
**Hit points:** 2
**Ability adjustments**
    +2 Dexterity
	+2 Intelligence
	-2 Strength
**Size and type:** Small Humanoid(Ysoki)

***==Racial Traits==***
**Cheek Pouches**
Ysoki can store up to 1 cubic foot of items weighing up to 1 bulk in total in their cheek pouches, and they can transfer a single object between hand and cheek as a swift action. A ysoki can disgorge the entire contents of his pouch onto the ground in his square as a move action that does not provoke an attack of opportunity.
**Darkvision**
Ysoki can see up to 60 feet in the dark.
**Moxie**
Ysoki are scrappy and nimble even when the odds are against them. A ysoki can stand from prone as a swift action. Additionally, when off-kilter, a ysoki does not take the normal penalties to attacks or gain the flat-footed condition. When attempting an Acrobatics check to tumble through the space of an opponent at least one size category larger than himself, a ysoki receive a +5 racial bonus to the check.
**Scrounger**
Ysoki receive a +2 racial bonus to Engineering, Stealth, and Survival checks.
		'''
	else:
		return 'Invalid race'


#Params
#	string: player's race selection
#Returns
#	bool: true if the race selection is valid/in the list of races
def isValid(race):
	return race.lower() in races
	
#Params
#	string: character's race
#Returns
#	bool: true if the race selected requires further choices to determine ability scores
def needsChoices(race):
	return race.lower() in racesWithAbilityChoices

#Params
#	string: character's race 
#Returns
#	string: bot's message text describing the available choices for racial ability score adjustments and how to proceed
def getChoices(race):
	if race.lower() == 'gnome':
		return '''As a Gnome, you have two choices:

**Feychild**
    +2 Charisma
	Sporting brightly colored skin and hair, feychildren cling to their pre-Gap heritage and are abound with wild whimsy and a ravenous, reckless appetite for adventure.
	
**Bleachling**
	+2 Intelligence
	Believed to be the descendants of those who survived the plague known as the Bleaching, a Bleachling's features are typically monochromatic, ranging from black and white to brown and gray. They have a reputation of being even-tempered and rather dour.
	
To make your choice, type ***!feychild*** or ***!bleachling***
	'''
	elif race.lower() == 'half-elf':
		return '''As a Half-Elf, you may increase any ability score by 2.

To make your choice type ***!{Ability}*** (for example, ***!wisdom*** or ***!dexterity***)		
		'''
	elif race.lower() == 'half-orc':
		return '''As a Half-Orc, you may increase any ability score by 2.

To make your choice type ***!{Ability}*** (for example, ***!wisdom*** or ***!dexterity***)		
		'''
	elif race.lower() == 'human':
		return '''As a Human, you may increase any ability score by 2.

To make your choice type ***!{Ability}*** (for example, ***!wisdom*** or ***!dexterity***)		
		'''
	elif race.lower() == 'lashunta':
		return '''As a Lashunta, you have two choices:
		
**Korasha**
	+2 Strength
	-2 Wisdom
	Korasha Lashuntas are muscular, but often brash and unobservant.

**Damaya**
	+2 Intelligence
	-2 Constitution
	Damaya Lashuntas are typically clever and well-spoken, but somewhat delicate.

To make your choice, type ***!korasha*** or ***!damaya***
		'''
	else:
		return race + ' does not require any ability score choices'
		
#Overload: Race does not need choices for ability scores
def getAbilityScoreAdjustments(race):
	return raceAbilityAdjustments[race.lower()]
#Overload: Race does need a choice for ability scores
def getAbilityScoreAdjustments(race, choice):
	return
		
	
	
	
	