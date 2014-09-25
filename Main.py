print 'Welcome to DotaBase Alpha 0.11.'

print 'Main menu,'
print '1. Mana Cost Calculator'

import re
import os
import math
def cls(): print "\n" * 100

class spells(object):
    spellname = ''
    manacost = 0
    cooldown = 0
    
    def __init__(self, spellname, manacost, cooldown):
        self.spellname = spellname
        self.manacost = manacost
        self.cooldown = cooldown

class hero(object):
    health = 0
    mana = 0
    int = 0
    str = 0
    intgain = 0
    strgain = 0
    lvl = 0
    name = ''
    def __init__(self, health, mana, int, str, intgain, strgain, lvl, name, spells):
        self.health = health
        self.mana = mana
        self.int = int
        self.str = str
        self.intgain = intgain
        self.strgain = strgain
        self.lvl = lvl
        self.name = name
        self.spell = spells
heros = {}
# sort out the spells tonight
heros['Axe' : hero(625, 234, 18, 25, 1.6, 2.5, 1, 'Axe', [spells('BESERKERS CALL',110, 10),spells('BATTLE HUNGER', 105, 5),spells('CULLING BLADE', 180, 55)]),
    'Bane': hero(568, 286, 22, 22, 2.1, 2.1, 1, 'Bane',[spells('ENFEEBLE',125,10), spells('BRAIN SAP',200,14), spells('NIGHTMARE',165,15), spells('FIENDS GRIP',400,100)]),
    'Bristleback': hero(568, 182, 14, 22, 2.8, 2.2, 1, 'Bristleback',[spells('NASAL GOO',30,2), spells('QUILL SPRAY',35,3)]), 
    'Crystal_Maiden': hero(454, 208, 16, 16, 2.9, 1.7, 1, 'Crystal Maiden',[spells('CRYSTAL NOVA',160,15), spells('FROSTBITE',150,10), spells('FREEZING FIELD',600,90)]) ,
    'Death_Prophet': hero(511, 260, 20, 19, 3, 2.2, 1, 'Death Prophet',[spells('CRYPT SWARM',165,8), spells('SILENCE',80,15), spells('EXORCISM',400,135)]) ,
    'Jakiro': hero(606, 364, 28, 24, 2.8, 2.3, 1, 'Jakiro',[spells('DUAL BREATH',170,10), spells('ICE PATH',90,9), spells('LIQUID FIRE',0,4), spells('MACROPYRE',440,60)]) ,
    'Lich': hero(492, 234, 18, 18, 3.25, 1.55, 1, 'Lich',[spells('FROST BLAST',190,8), spells('ICE ARMOUR',50,5), spells('SACRIFICE',0,20), spells('CHAIN FROST',500,60)]) ,
    'Omniknight': hero(530, 221, 17, 20, 1.8, 2.65, 1, 'Omniknight',[spells('PURIFICATION',160,10), spells('REPEL',50,14), spells('GUARDIAN ANGEL',250,150)]) ,
    'Riki': hero(473, 182, 14, 17, 1.3, 2, 1, 'Riki',[spells('SMOKE SCREEN',90,11), spells('BLINK STRIKE',40,5)]) ,
    'Vengeful_Spirit': hero(492, 195, 15, 18, 1.75, 2.6, 1, 'Vengeful Spirit',[spells('MAGIC MISSILE',140,10), spells('WAVE OF TERROR',40,15), spells('NETHER SWAP',200,45)]), 
    'Viper': hero(530, 195, 15, 20, 1.8, 1.9, 1, 'Viper',[spells('POISON ATTACK',20,0), spells('VIPER STRIKE',250,30)]) ,
    'Zeus': hero(511, 260, 20, 19, 2.7, 2.3, 1, 'Zeus',[spells('ARC LIGHTNING',80,2), spells('LIGHTNING BOLT',135,6), spells('THUNDERGODS WRATH',450,90)]




with open('heroes.txt', 'r') as f:
    herolist = re.split('[^\w_]*', f.read())

def levelselection():
    while True:
        level = raw_input('Select a level between 1 and 25 ')
        if 1<= int(level) <= 25:
            
            return int(level)
        print 'invalid level'

def manacalc():
    print 'Here is the list of heroes to choose from'
    print herolist
    userSelection = userchoice('What hero would you like to select? ','Invalid hero, please reselect your hero ')

    
    while True:
        print 'You have selected ' + userSelection
        userinput = raw_input('Is this the correct hero? ')
        if userinput == 'no':
            cls()
            userSelection = userchoice('What hero would you like to select? ','Invalid hero, please reselect your hero ')
            continue
        break

    print heros[userSelection].name + " has been selected"
    print
    print heros[userSelection].name + " has these base stats at level 1"
    print '{} base strength'.format(heros[userSelection].str)
    print '{} base intelligence'.format(heros[userSelection].int)
    level = levelselection()
    
    currentint = (level * heros[userSelection].intgain) + heros[userSelection].int
    currentstr = (level * heros[userSelection].strgain) + heros[userSelection].str
    
    print heros[userSelection].name +  ' has {} intelligence at '.format(currentint) + 'level {}'.format(level)
    print heros[userSelection].name + ' has {} strength at '.format(currentstr) + 'level {}'.format(level)
    
    print
    print 'What spells would you like to cast?'
    print ', '.join(i.spellname for i in heros[userSelection].spells)
    
    
def userchoice(question, check):
    while True:
        userInput = raw_input(question)
        if userInput in herolist:
            return userInput
        print check

def main():
    while True:
        userinput = raw_input('Select an option ')
        if userinput.lower== "quit" :
            break
        elif userinput== "1":
            manacalc()
        cls()

if __name__ == '__main__'
    main()

