import re
import os
import math
def cls(): print "\n" * 50

with open('heroes.txt', 'r') as f:
    herolist = re.split('[^\w_]*', f.read())

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
    inte = 0
    stre = 0
    intgain = 0
    strgain = 0
    lvl = 0
    name = ''
    def __init__(self, health, mana, inte, stre, intgain, strgain, lvl, name, spells):
        self.health = health
        self.mana = mana
        self.inte = inte
        self.stre = stre
        self.intgain = intgain
        self.strgain = strgain
        self.lvl = lvl
        self.name = name
        self.spell = spells

heros= {
    'axe': hero(625, 234, 18, 25, 1.6, 2.5, 1, 'Axe', [
    spells('BESERKERS CALL',110, 10),
    spells('BATTLE HUNGER', 105, 5),
    spells('CULLING BLADE', 180, 55)]),
    'bane': hero(568, 286, 22, 22, 2.1, 2.1, 1, 'Bane',[
        spells('ENFEEBLE',125,10),
        spells('BRAIN SAP',200,14),
        spells('NIGHTMARE',165,15),
        spells('FIENDS GRIP',400,100)]),
    'bristleback': hero(568, 182, 14, 22, 2.8, 2.2, 1, 'Bristleback',[
        spells('NASAL GOO',30,2),
        spells('QUILL SPRAY',35,3)]), 
    'crystal_maiden': hero(454, 208, 16, 16, 2.9, 1.7, 1, 'Crystal Maiden',[
        spells('CRYSTAL NOVA',160,15),
        spells('FROSTBITE',150,10),
        spells('FREEZING FIELD',600,90)]) ,
    'death_prophet': hero(511, 260, 20, 19, 3, 2.2, 1, 'Death Prophet',[
        spells('CRYPT SWARM',165,8),
        spells('SILENCE',80,15),
        spells('EXORCISM',400,135)]) ,
    'jakiro': hero(606, 364, 28, 24, 2.8, 2.3, 1, 'Jakiro',[
        spells('DUAL BREATH',170,10),
        spells('ICE PATH',90,9),
        spells('LIQUID FIRE',0,4),
        spells('MACROPYRE',440,60)]) ,
    'lich': hero(492, 234, 18, 18, 3.25, 1.55, 1, 'Lich',[
        spells('FROST BLAST',190,8),
        spells('ICE ARMOUR',50,5),
        spells('SACRIFICE',0,20),
        spells('CHAIN FROST',500,60)]) ,
    'omniknight': hero(530, 221, 17, 20, 1.8, 2.65, 1, 'Omniknight',[
        spells('PURIFICATION',160,10),
        spells('REPEL',50,14),
        spells('GUARDIAN ANGEL',250,150)]) ,
    'riki': hero(473, 182, 14, 17, 1.3, 2, 1, 'Riki',[
        spells('SMOKE SCREEN',90,11),
        spells('BLINK STRIKE',40,5)]) ,
    'vengeful_spirit': hero(492, 195, 15, 18, 1.75, 2.6, 1, 'Vengeful Spirit',[
        spells('MAGIC MISSILE',140,10),
        spells('WAVE OF TERROR',40,15),
        spells('NETHER SWAP',200,45)]), 
    'viper': hero(530, 195, 15, 20, 1.8, 1.9, 1, 'Viper',[
        spells('POISON ATTACK',20,0),
        spells('VIPER STRIKE',250,30)]) ,
    'zeus': hero(511, 260, 20, 19, 2.7, 2.3, 1, 'Zeus',[
        spells('ARC LIGHTNING',80,2),
        spells('LIGHTNING BOLT',135,6),
        spells('THUNDERGODS WRATH',450,90)]),
    }

herosnames = {}
for i in list(heros):
    herosnames[i.lower()] = i
    if '_' in i:
        try:
            herosnames[''.join(j[0] for j in i.split('_'))] = i
        except:
            e = ''.join(j[0] for j in i.split('_'))
            print i
            print e
            print herosname[e]
print list(herosnames)

def main():
    print 'Welcome to DotaBase Alpha 0.15.'

    print 'Main menu,'
    print '1. Mana Cost Calculator'


    while True:
        userinput = raw_input('Select an option ')
        if userinput.lower== "quit" :
            break
        elif userinput== "1":
            manacalc()
        cls()
        print 'Main menu,'
        print '1. Mana Cost Calculator'

def levelselection():
    while True:
        level = raw_input('Select a level between 1 and 25 ')
        try:
            if 1<= int(level) <= 25:
                return int(level)
        except:
            print 'invalid level'

def manacalc():
    cls()
    print 'Here is the list of heroes to choose from'
    print herolist
    userSelection = userchoice('What hero would you like to select? ','Invalid hero, please reselect your hero ')
    totalcost = 0
    totalcooldown = 0
    
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
    print '{} base strength'.format(heros[userSelection].stre)
    print '{} base intelligence'.format(heros[userSelection].inte)
    level = levelselection()
    
    currentint = (level * heros[userSelection].intgain) + heros[userSelection].inte
    currentstr = (level * heros[userSelection].strgain) + heros[userSelection].stre
    
    print heros[userSelection].name +  ' has {} intelligence at '.format(currentint) + 'level {}'.format(level)
    print heros[userSelection].name + ' has {} strength at '.format(currentstr) + 'level {}'.format(level)
    
    print
    print 'Here is a list of {} spells;'.format(heros[userSelection].name)
    print ', '.join(i.spellname for i in heros[userSelection].spell)

    spellcasting(userSelection,totalcost,totalcooldown)
    while True:
        userInput = raw_input('Do you wish to cast another spell? ')
        if userInput == 'yes':
            spellcasting(userSelection,totalcost,totalcooldown)
        else:
            print 'Returning to main menu'
            main()           
    
def spellcasting(userSelection,totalcost,totalcooldown):

    while True:
        userInput = raw_input('Select a spell to cast ')
        userInput = userInput.upper()
    
        if userInput in(i.spellname for i in heros[userSelection].spell):

                for i in heros[userSelection].spell:
                    if i.spellname == userInput:
                        currentcost = i.manacost
                        currentcooldown = i.cooldown
                        totalcost = totalcost + currentcost
                        totalcooldown = totalcooldown + currentcooldown

                
                
                break
        elif userInput == 'Q':
                main()

       
                
    
    
def userchoice(question, check):
    while True:
        userInput = raw_input(question).lower()
        if userInput in herosnames:
            return herosnames[userInput]
        print check


main()
