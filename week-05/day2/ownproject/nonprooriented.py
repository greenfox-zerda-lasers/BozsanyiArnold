thief = {'strength': 5, 'luck': 7, 'speed':5, 'inteligence':3}
warrior = {'strength': 5, 'luck': 7, 'speed':5, 'inteligence':3}
mage = {'strength': 5, 'luck': 7, 'speed':5, 'inteligence':3}
classes = [thief, mage, warrior]
strength = 0
luck = 0
speed = 0
inteligence = 0
distributable = 0
player_name = ''
def get_name_and_class():
    player_name = input('Yo Player. Please enter a name for yourself:')
    print ('----press T + enter for thief ---- Press W+ enter for warrior ---- Press M+enter for mage ----\n'
    'The Thief has luck at most but see for yourself:\n {} \n The Warrior has strength at most but see for yourself:\n {} \n The Mage has inteligence at most but see for yourself:\n {}'.format(thief, warrior, mage))
    playerclass = input ('Good Job {}, now choose a class for yourself:'.format(player_name)).lower()
    #if playerclass in 'twm' and len(playerclass) == 1:
print(get_name_and_class())
