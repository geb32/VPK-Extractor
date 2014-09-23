print 'Welcome to DotaBase Alpha 0.11.'

print 'Main menu,'
print '1. Mana Cost Calculator'

import re
import os
import math
def cls(): print "\n" * 100

class hero(object):
    health = 0
    mana = 0
    int = 0
    str = 0
    intgain = 0
    strgain = 0
    lvl = 0
    name = ''
    def __init__(self, health, mana, int, str, intgain, strgain, lvl, name):
        self.health = health
        self.mana = mana
        self.int = int
        self.str = str
        self.intgain = intgain
        self.strgain = strgain
        self.lvl = lvl
        self.name = name
        
heros = {}

heros['Axe'] = hero(625, 234, 18, 25, 1.6, 2.5, 1, 'Axe') 
heros['Bane'] = hero(568, 286, 22, 22, 2.1, 2.1, 1, 'Bane') 
heros['Bristleback'] = hero(568, 182, 14, 22, 2.8, 2.2, 1, 'Bristleback') 
heros['Crystal_Maiden'] = hero(454, 208, 16, 16, 2.9, 1.7, 1, 'Crystal Maiden') 
heros['Death_Prophet'] = hero(511, 260, 20, 19, 3, 2.2, 1, 'Death Prophet') 
heros['Jakiro'] = hero(606, 364, 28, 24, 2.8, 2.3, 1, 'Jakiro') 
heros['Lich'] = hero(492, 234, 18, 18, 3.25, 1.55, 1, 'Lich') 
heros['Omniknight'] = hero(530, 221, 17, 20, 1.8, 2.65, 1, 'Omniknight') 
heros['Riki'] = hero(473, 182, 14, 17, 1.3, 2, 1, 'Riki') 
heros['Vengeful_Spirit'] = hero(492, 195, 15, 18, 1.75, 2.6, 1, 'Vengeful Spirit') 
heros['Viper'] = hero(530, 195, 15, 20, 1.8, 1.9, 1, 'Viper') 
heros['Zeus'] = hero(511, 260, 20, 19, 2.7, 2.3, 1, 'Zeus')
      
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
    print heros[userSelection].name +  ' has {} intelligence'.format(currentint)
  
def userchoice(question, check):
    while True:
        userInput = raw_input(question)
        if userInput in herolist:
            return userInput
        print check


userinput = raw_input('Select an option ')
while True:
    if userinput.lower== "quit" :
        break
    elif userinput== "1":
        manacalc()


