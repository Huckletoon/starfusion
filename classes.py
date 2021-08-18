classes = {'envoy', 'mechanic', 'mystic', 'operative', 'solarian', 'soldier', 'technomancer'}
classesWithAbilityChoices = {'soldier'}
classChoices = {
	'soldier': [
		'strength',
		'dexterity'
	]
}

def getClassOverview(classChoice):
	if classChoice.lower() == 'envoy':
		return ['''***==Envoy==*** https://www.starjammersrd.com/classes/envoy/
You make your way in the universe with a charming smile, quick wit, and keen sense of self-preservation, and excel at getting others to do what you want. You might be a trickster, hustler, or con artist, or you might serve as an actor, ambassador, or businessperson, paving the way for negotiation through kind words or the occasional dirty trick. You are often the group’s strategist, using your quick wit and tactical acumen to push your friends to greater heights. You may also be skilled in diplomacy, serving as the face for a starship crew, talking your way into restricted systems or gaining audiences with local politicians or warlords.

***==Stats==***
**Hit Points:** 6
**Stamina Points:** 6 + Constitution modifier

**Key Ability Score:** Charisma
**Class Skills:** Acrobatics (Dex), Athletics (Str), Bluff (Cha), Computers (Int), Culture (Int), Diplomacy (Cha), Disguise (Cha), Engineering (Int), Intimidate (Cha), Medicine (Int), Perception (Wis), Piloting (Dex), Profession (Cha, Int, or Wis), Sense Motive (Wis), Sleight of Hand (Dex), Stealth (Dex)
**Skill Ranks per Level:** 8 + Intelligence modifier
**Proficiencies:** Light armor; Basic melee weapons, grenades, small arms
**Saving Throws:** +0 Fortitude, +2 Reflex, +2 Will
**Base Attack Bonus:** +0''',
'''***==Class Features==***
**Envoy Improvisation**
As you gain experience, you learn envoy improvisations—little tricks that bolster allies, confound enemies, or change the ebb and flow of battle using guile, inspiration, or luck. See the site for a list of improvisations.
You learn your first envoy improvisation at 1st level, and you learn an additional improvisation at 2nd level and every 2 levels thereafter.
If an improvisation allows you to grant an effect to an ally, you cannot grant yourself that effect unless the improvisation states otherwise. If an envoy improvisation allows a saving throw to resist its effects or requires an enemy to attempt a skill check, the DC is equal to 10 + half your envoy level + your Charisma modifier.
Some envoy improvisations are language-dependent, mind-affecting, sense-dependent, or some combination of any or all of these.
You learn your first envoy improvisation at 1st level and an additional improvisation at 2nd level and every 2 levels thereafter. Many improvisations require you to have a minimum envoy level, and they are organized accordingly. Some improvisations have additional prerequisites, such as other improvisations.

**Expertise**
You are an expert at dealing with challenges that test your skills, be the challenges social or otherwise. At 1st level, when attempting a **Sense Motive** check, you can roll 1d6 (your expertise die) and add the result of the roll to your check as an insight bonus. You can use this and other expertise abilities as long as you have at least 1 Resolve Point remaining.

**Skill Expertise**
At 1st level and every 4 levels thereafter, you can use expertise with one additional class skill. You must have at least 1 rank in a skill to select it, and it must come from the following list: Bluff (Cha), Computers (Int), Culture (Int), Diplomacy (Cha), Disguise (Cha), Engineering (Int), Intimidate (Cha), and Medicine (Int).
''']
	if classChoice.lower() == 'mechanic':
		return ['''***==Mechanic==*** https://www.starjammersrd.com/classes/mechanic/
You are a master of machines, from advanced supercomputers to simple magnetic engines. Understanding how these devices work gives you insight into the world around you, allowing you to make the most of your gear, circumvent hardened defenses, and even take over remote systems. Your programming skill also gives you the ability to create a powerful ally, in the form of either an implanted Artificial intelligence or a robotic drone, which can assist you with a variety of tasks.

***==Stats==***
**Hit Points:** 6 
**Stamina Points:** 6 + Constitution modifier

**Key Ability Score:** Intelligence
**Class Skills:** Athletics (Str), Computers (Int), Engineering (Int), Medicine (Int), Perception (Wis), Physical Science (Int), Piloting (Dex), Profession (Cha, Int, or Wis)
**Skill Ranks per Level:** 4 + Intelligence modifier
**Proficiencies:** Light armor; Basic melee weapons, grenades, small arms
**Saving Throws:** +2 Fortitude, +2 Reflex, +0 Will
**Base Attack Bonus:** +0''',
'''***==Class Features==***
**Artificial Intelligence**
You construct an Artificial intelligence (or AI), a sophisticated program of self-motivated code that you can access for help in a variety of endeavors. This AI is the product of your own genius, far more advanced and complicated than any available for sale to consumers (though it falls short of being truly self-aware), and only you know the secrets of its creation and operation. Your AI can take one of two forms: a drone or an exocortex. You must pick one of these forms upon taking your first level of mechanic, and once this choice is made, it cannot be changed. These choices are detailed below.

**Drone**
You begin play with a powerful robotic drone to house your AI. You build and control this drone, which accompanies you on your adventures and is capable of combat, espionage, and other specialized tasks. As you gain levels, your drone advances in sophistication and gain additional abilities. While the value of your drone is immense, only you, with your extensive knowledge of its quirks and security measures, can ever hope to operate or repair it.

**Exocortex**
You begin play with an exocortex, an Artificial processor that interacts with and augments your biological brain’s cognitive functions, which can aid you in a variety of tasks, from combat to digital infiltration. Your exocortex is implanted within your physical body or brain, similar to a piece of cybernetic hardware, allowing your AI to access your mind and feed you information. As you gain levels, your exocortex advances in sophistication and processing power—see Exocortex. Only you can access or interact with your exocortex.

''','''**Bypass**
You are skilled at getting inside computer systems and electronic devices. At 1st level, you gain a +1 insight bonus to **Computers** and **Engineering** skill checks. At 5th level, every 4 levels thereafter, and at 20th level, this bonus increases by 1.

**Custom Rig**
You have created a customized toolkit you can use to hack systems and items. Your custom rig can be configured to take up an upgrade slot on your armor or can be installed as a cybernetic augmentation system in your brain (though it can be combined with a datajack for the same price as installing a datajack normally), your eyes, or an arm. Alternatively, you can configure it to be a handheld device, meaning that you must retrieve it and hold it to use it effectively. While using this rig, you always count as having the appropriate tool or basic kit for any **Computers** or **Engineering** skill check you attempt. Some mechanic tricks and drone mods require the use of a custom rig. In addition, you can use your custom rig as a Mk I comm unit. Finally, if you have a drone, you can use your custom rig to communicate over an encrypted channel with your drone to issue commands to its AI or directly control it at a range of 2,500 feet.

If your custom rig is damaged, destroyed, lost, or stolen, you can kitbash a new one from any engineering kit, hacking kit, or other technological toolkit, reconfiguring the materials into a new custom rig with 1 hour of work. You can have only one custom rig at a time. If you create a new custom rig, your old one functions as a normal toolkit of whatever type you made it from and can no longer be used with your mechanic tricks.
''']
	if classChoice.lower() == 'mystic':
		return ['''***==Mystic==*** https://www.starjammersrd.com/classes/mystic/
You understand that what most people call magic is simply an expression of the innate connection between all things, and you intuitively tap into this unseen power to create strange effects. You may conceptualize the source of your magic as divine grace, a manipulation of fundamental energy, or an unlocking of psychic potential, but always with the knowledge that you are a conduit channeling forces greater than yourself.

***==Stats==***
**Hit Points:** 6
**Stamina Points:** 6 + Constitution modifier

**Key Ability Score:** Wisdom
**Class Skills:** Bluff (Cha), Culture (Int), Diplomacy (Cha), Disguise (Cha), Intimidate (Cha), Life Science (Int), Medicine (Int), Mysticism (Wis), Perception (Wis), Profession (Cha, Int, or Wis), Sense Motive (Wis), Survival (Wis)
**Skill Ranks per Level:** 6 + Intelligence modifier
**Proficiencies:** Light armor; Basic melee weapons, small arms
**Saving Throws:** +0 Fortitude, +0 Reflex, +2 Will
**Base Attack Bonus:** +0''',
'''***==Class Features==***

''']
	if classChoice.lower() == 'operative':
		return ['''***==Operative==*** https://www.starjammersrd.com/classes/operative/
You’re a shadow. You move swiftly, strike suddenly, and always have an escape plan. You’re a consummate professional, and you always get the job done, whether it’s scouting enemy lines, hunting down criminals, stealing and smuggling items, or assassinating key figures. As an operative, you’re skilled in a wide variety of disciplines and specialties, and use speed, mobility, and your quick wits rather than relying on heavy weapons. You excel at the art of surprise, whether it’s sniping targets from cover or striking while their backs are turned.

***==Stats==***
**Hit Points:** 6
**Stamina Points:** 6 + Constitution modifier

**Key Ability Score:** Dexterity
**Class Skills:** Acrobatics (Dex), Athletics ( Str), Bluff (Cha), Computers ( Int), Culture (Int), Disguise ( Cha), Engineering (Int), Intimidate ( Cha), Medicine (Int), Perception ( Wis), Piloting (Dex), Profession ( Cha, Int, or Wis), Sense Motive ( Wis), Sleight of Hand (Dex), Stealth ( Dex), Survival (Wis)
**Skill Ranks per Level:** 8 + Intelligence modifier
**Proficiencies:** Light armor; Basic melee weapons, small arms, sniper weapons
**Saving Throws:** +0 Fortitude, +2 Reflex, +2 Will
**Base Attack Bonus:** +0''',
'''***==Class Features==***

''']
	if classChoice.lower() == 'solarian':
		return ['''***==Solarian==*** https://www.starjammersrd.com/classes/solarian/
The stars guide the planets with gravity, create life with light and heat, and utterly consume worlds in supernovas and black holes. You understand that these acts of creation and destruction are not opposites, but rather two parts of a natural, dualistic cycle. You seek to be an agent of that cycle, an enlightened warrior with the ability to manipulate the forces of the stars themselves. Constantly accompanied by a mote of fundamental energy or entropy, you can shape this essence in combat to create weapons and armor of gleaming stellar light or pure, devouring darkness.

***==Stats==***
**Hit Points:** 7
**Stamina Points:** 7 + Constitution modifier

**Key Ability Score:** Charisma
**Class Skills:** Acrobatics (Dex), Athletics (Str), Diplomacy (Cha), Intimidate (Cha), Mysticism (Wis), Perception (Wis), Physical Science (Int), Profession (Cha, Int, or Wis), Sense Motive (Wis), Stealth (Dex)
**Skill Ranks per Level:** 4 + Intelligence modifier
**Proficiencies:** Light armor, shields; Basic melee weapons, Advanced melee weapons, small arms
**Saving Throws:** +2 Fortitude, +0 Reflex, +2 Will
**Base Attack Bonus:** +1''',
'''***==Class Features==***

''']
	if classChoice.lower() == 'soldier':
		return ['''***==Soldier==*** https://www.starjammersrd.com/classes/soldier/
Conflict is an inevitable result of life. On every world that harbors complex living organisms, creatures battle one another for dominance, resources, territory, or ideals. Whether you’ve taken up arms to protect others, win glory, exact revenge, or simply earn a living, you are the perfect embodiment of this truth. You’re an expert at combat of all types but tend to prefer heavy armor and weapons—the bigger, the better.

***==Stats==***
**Hit Points:** 7
**Stamina Points:** 7 + Constitution modifier

**Key Ability Score:** Strength or Dexterity
**Class Skills:** Acrobatics (Dex), Athletics (Str), Engineering (Int), Intimidate (Cha), Medicine (Int), Piloting (Dex), Profession (Cha, Int, or Wis), Survival (Wis)
**Skill Ranks per Level:** 4 + Intelligence modifier
**Proficiencies:** Light armor, Heavy armor, shields; basic and advanced melee weapons, small arms, longarms, heavy weapons, sniper weapons, and grenades
**Saving Throws:** +2 Fortitude, +0 Reflex, +2 Will
**Base Attack Bonus:** +1''',
'''***==Class Features==***

''']
	if classChoice.lower() == 'technomancer':
		return ['''***==Technomancer==*** https://www.starjammersrd.com/classes/technomancer/
To the uninitiated, magic and technology are completely unrelated, but you know there are more correlations between the two than most suspect. Magic and technology are just tools, and when combined into one discipline, called technomancy, they can be far more powerful than one or the other on its own. You utilize tech to empower, harness, and manipulate magic, and you wield magic to augment, control, and modify technology. You are an expert at hacking the underlying structure of the universe itself, bending the laws of science and nature to your will. Your technomancy—which is gained from scientific study and experimentation—manipulates the physical world, weaves illusions, allows you to peer through time and space, and if necessary, can blast a foe into atoms.

***==Stats==***
**Hit Points:** 5
**Stamina Points:** 5 + Constitution modifier

**Key Ability Score:** Intelligence
**Class Skills:** Computers (Int), Engineering (Int), Life Science (Int), Mysticism (Wis), Physical Science (Int), Piloting (Dex), Profession (Cha, Int, or Wis), Sleight of Hand (Dex)
**Skill Ranks per Level:** 4 + Intelligence modifier
**Proficiencies:** Light armor; Basic melee weapons, small arms
**Saving Throws:** +0 Fortitude, +2 Reflex, +2 Will
**Base Attack Bonus:** +0''',
'''***==Class Features==***

''']
	
	
def isValid(classChoice):
	return classChoice.lower() in classes
	
def needsChoices(classChoice):
	return classChoice.lower() in classesWithAbilityChoices

def isValidChoice(classChoice, choice):
	return classChoice.lower() in classesWithAbilityChoices and choice in classChoices[classChoice.lower()]

def getChoices(classChoice):
	if classChoice.lower() == 'soldier':
		return '''As a Soldier, you have the choice of your Key Ability Score being either Strength or Dexterity. This should be the ability you plan to have the most points in.
		
To make your choice type ***!strength*** or ***!dexterity***'''
