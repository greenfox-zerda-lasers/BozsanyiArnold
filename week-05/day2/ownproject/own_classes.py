import random

class Player:
    def __init__(self, playername,finalclass):
        self.playername = playername
        self.finalclass = finalclass
    def self_inspect(self):
        print (' -Your name:{playername}\t\t\t -Your class:{finalclass}\n ')
class Character:
    hp = 150
    def __init__(self,strength,luck,inteligence,speed):
        self.strength = strength
        self.luck = luck
        self.inteligence = inteligence
        self.speed = speed
        self.hp = 150
        self.currency = 30
    def __str__(self):
        return '-strength:{}\n -luck:{}\n -inteligence:{}\n -speed:{}'.format(self.strength,self.luck,self.inteligence,self.speed)
class Warrior(Character):
    def __init__(self):
        super().__init__(7,5,3,5)
class Mage(Character):
    def __init__(self):
        super().__init__(3,5,7,5)
class Thief(Character):
    def __init__(self):
        super().__init__(5,7,3,5)
class GameZones:
    zones = [[1,2,3],[4,5,6],[7,8,9]]
class GamePlay:
    pass

import os
os.system('cls' if os.name == 'nt' else 'clear')

playername = input(' -Yo player. Please pick a name for yourself:\n -(should be between 5-10 characters)\n')
while len(playername) == 0:
    print('Please give me a name.')
    playername = input(' -Yo player. Please pick a name for yourself:\n -(should be between 5-10 characters)\n')

os.system('cls' if os.name == 'nt' else 'clear')

warrior = Warrior()
mage = Mage()
thief = Thief()
print('Choose your class wisely. See the class descriptions below.')
print('The Warrior has strength at most but see for yourself:\n', warrior, '\n')
print('The Mage has inteligence at most but see for yourself:\n', mage, '\n')
print('The Thief has luck at most but see for yourself:\n', thief, '\n')
playerclass = input(' ----Press T + enter for Thief\n ----Press W + enter for Warrior\n ----Press M + enter for Mage\n Aaaaand you are gona be a:').lower()
if playerclass in 'twm' and len(playerclass) == 1:
    if playerclass == 't':
        player = {'{}\nThief\n{}'.format(playername,{thief})}
        print('I hope you are going to be a hardcore Thief!!!')
        choosenclass = 'Thief'
    elif playerclass == 'w':
        player = {'{}\nWarrior\n{}'.format(playername,{warrior})}
        print ('I hope you are going to be a hardcore Warrior!!!')
        choosenclass = 'Warrior'
    else:
        player = {'{}\nMage\n{}'.format(playername,{mage})}
        print ('I hope you are going to be a hardcore Mage!!!')
        choosenclass = 'Mage'
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Please insert one of the following letters:T,W or M')
while playerclass not in 'twm' or len(playerclass) != 1:
    playerclass = input(' ----Press T + enter for Thief\n ----Press W + enter for Warrior\n ----Press M + enter for Mage\n Aaaaand you are gona be a:').lower()

os.system('cls' if os.name == 'nt' else 'clear')

play_or_read = input('Ayo {}{}, if you want to read about function key biddings just press R + enter. If you already played and know the instructions, then just go for it with pressing P + enter.'.format(playername[0].upper(),playername[1:]))
print(len(play_or_read))
while len(play_or_read) == 0 or play_or_read not in 'pr':
    os.system('cls' if os.name == 'nt' else 'clear')
    print ('It is P or R you should press enter after. Nothing less... nothing more.')
    play_or_read = input('Ayo {}{}, if you want to read about function key biddings just press R + enter. If you already played and know the instructions, then just go for it with pressing P + enter.'.format(playername[0].upper(),playername[1:]).lower())

os.system('cls' if os.name == 'nt' else 'clear')

if play_or_read == 'p':
    print (' -Arnold the great king of the kings , the lord of the dragons and also local PIMP welcomes you.\n -Good luck on your journey.\n\n')


if play_or_read == 'r':
    print(' ---Movement keys:\n - UP arrow key + ENTER --> Move to NORTH\n - DOWN arrow key + ENTER ---> SOUTH\n - LEFT arrow key + ENTER --> Move to WEST\n - RIGHT arrow key + ENTER --> Move to EAST\n\n ---Function keys:\n - Type SI + ENTER --> Self Inspection\n - Type V + ENTER --> Enter the Vendor\'s shop\n - Tyoe A + ENTER --> Enter the Armory\n - Type MT + ENTER --> Enter the Mage\'s tower\n - Type C + ENTER --> Enter the Castle')
    back = input('For stepping back press B + Enter\n')
    os.system('cls' if os.name == 'nt' else 'clear')
    if back == 'b':
        play_or_read = input('Ayo {}{}, if you want to read about function key biddings just press R + enter. If you already played and know the instructions, then just go for it with pressing P + enter.'.format(playername[0].upper(),playername[1:]))
actual_zone = GameZones.zones[1][1]



if actual_zone == 5:
    todo = input(' You find yourself in the inner city , you wish you weren\'t this poor bastard and could live a high life like the people from here.\n Places you could go:\t\t\tVendor (buy regular stuff)\t\t\tArmory (buy equipments)\t\t\tCastle (accept/turn in QUESTS)')
    if todo == 'si':
        print('{}\t\t\t{}')
