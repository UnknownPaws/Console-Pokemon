from Pokemon import Pokemon
import random as ran
import time

enemyNames = ['Fred', 'Dan', 'Sara', 'Claire', 'LiterallyMe']
Pokemons = ['Pikachu', 'Charmander', 'Squirtle', 'Bulbasoar', 'Litten', 'Snorlax', 'Eevee', 'Diddo', 'Mew']
PokeObj = {
    'Pikachu': Pokemon(['Pikachu', 'electricity', 85, 30]),
    'Charmander': Pokemon(['Charmander', 'fire', 74, 35]),
    'Squirtle': Pokemon(['Squirtle', 'water', 56, 20]),
    'Bulbasoar': Pokemon(['Bulbasoar', 'leaf', 30, 90]),
    'Litten': Pokemon(['Litten', 'fire', 90, 20]),
    'Snorlax': Pokemon(['Snorlax', 'leaf', 49, 56]),
    'Eevee': Pokemon(['Eevee', 'leaf', 78, 56]),
    'Diddo': Pokemon(['Diddo', 'leaf', 13, 30]),
    'Mew': Pokemon(['Mew', 'legendary', 95, 80])
}


class Trainer:
    def __init__(self):
        self.Pokedex = []
        self.main = ''

    def __init__(self, pokemon_s):
        self.Pokedex = []
        for pkmn in [pokemon_s]:
            if pkmn in Pokemons:
                self.Pokedex.append(PokeObj[pkmn])
        if len(self.Pokedex) > 0:
            self.main = self.Pokedex[0]
            return
        print('The pokemon that you have entered is not valid\n')

    def findPokemon(self):
        if len(self.Pokedex) >= 7:
            print('Pokedex is full\n')
            return
        print('Searching for pokemon: ')
        loadStr = ''
        for i in range(10):
            loadStr += '.'
            print(loadStr)
            time.sleep(1)
            if i % 3 == 0:
                loadStr = ''
        poKey = ran.randint(0, len(Pokemons) - 1)
        pokemon = PokeObj[Pokemons[poKey]]
        for pkmon in self.Pokedex:
            if pkmon.name == pokemon.name:
                pokemon.pokeNum += 1
        self.Pokedex.append(pokemon)
        print('You have found a wild', pokemon.name, '\n')

    def healPokemon(self):
        if self.main == '':
            print('You have no pokemon')
            return
        self.main.heal()

    def switchMain(self, targetPk):  # Change the main pokemon to the target pokemon if it exists in the pokedex
        for pkmon in self.Pokedex:
            if targetPk == pkmon.name:
                if pkmon.name == self.main.name and pkmon.pokeNum != self.main.pokeNum:
                    self.main = pkmon
                    return True
                elif pkmon.name == self.main.name and pkmon.pokeNum == self.main.pokeNum:
                    continue
                else:
                    self.main = pkmon
                    return True
        print('This pokemon is not in your pokedex.\n')
        return False

    def attack(self, enemy):
        if self.main == '':
            print('You do not have a pokemon to attack with.\n')
            return
        if enemy.main == '':
            print('The enemy does not have a main pokemon that you can attack.\n')
            return
        if enemy.main != '':
            if self.main != '':
                self.main.hurt(enemy.main)

    def setFree(
            self):  # it is going to set the main pokemon free, by removing it from the pokedex and replace the main with another one
        if self.main != '':
            self.Pokedex.remove(self.main)
        if self.Pokedex != []:
            self.main = self.Pokedex[ran.randint(0, len(self.Pokedex))]
            return
        self.main = ''
        print('You have no main pokemon.')

    def setFree(self, Pkmon):  # check if pokemon exists in pokedex and if it does set it free
        if self.main == PokeObj[Pkmon]:
            self.Pokedex.remove(PokeObj[Pkmon])
            if self.Pokedex != []:
                self.main = self.Pokedex[ran.randint(0, len(self.Pokedex) - 1)]
                return
            else:
                self.main = ''
                print('You do not have any pokemon now.\n')
                return
        if PokeObj[Pkmon] in self.Pokedex:
            self.Pokedex.remove(Pkmon)
            return
        print('This pokemon is not in your pokedex.\n')

    def getTotalHP(self):
        totalHP = 0
        for Pokemon in self.Pokedex:
            totalHP += Pokemon.hp
        return totalHP

    def main_has_health(self):
        # print('INSIDE OF CAN ATTACK')
        return self.main.hp != 0

    def set_healthy_pokemon(self):
        if len(self.Pokedex) <= 1:
            print('No pokemon to switch too.\n')
            return False
        # print('INSIDE OF SET_HEALTHY_POKEMON')
        for Pokemon in self.Pokedex:
            # print('IN FOR LOOP')
            if Pokemon.hp > 0 and Pokemon != self.main:
                # print('SWITCHING POKEMON')
                self.main = Pokemon
                return True
        print('No healthy pokemon to switch to.\n')
        return False

    def printPokedex(self):
        for pokemon in self.Pokedex:
            pokemon.printStats()


print('Welcome to Pokemon!')
name = input('Type your name here: ')
print('Welcome ', name, '. Choose your starting pokemon: ', Pokemons[1:4])
startPk = input()
player = Trainer(startPk)
print('Good choice!', player.main.name, 'is happy to see you!\n')

while True:
    print(
        'Choose an action:\n1 - Battle\n2 - Search for a pokemon\n3 - Free a pokemon\n4 - Heal a pokemon\n5 - Open pokedex\n6 - Exit game\n')
    userChoice = int(input())
    if userChoice == 1:
        mytotalHP = player.getTotalHP()
        if mytotalHP == 0:
            print('You either have no pokemon or all your pokemon are at 0 hp.\n')
            continue  # Restarts the current loop
        if player.main_has_health() == False:
            print('Your main pokemon has no health, switching main pokemon.\n')
            player.set_healthy_pokemon()

        # Enters battle
        enemy_name = enemyNames[ran.randint(0, len(enemyNames) - 1)]
        print(enemy_name, 'is ready for battle!\n')
        enemy_dex_len = ran.randint(1, 7)
        enemy_str_dex = [Pokemons[ran.randint(0, len(Pokemons) - 1)] for _ in range(
            enemy_dex_len)]  # takes a random pokemon from the Pokemons list and repeat the process the amount of times the enemy pokedex length is
        enemyObj = Trainer(enemy_str_dex[0])
        for Pokemon in enemy_str_dex[1:]:
            # print('INSIDE OF ENEMY POKEDEX', Pokemon)
            enemyObj.Pokedex.append(PokeObj[Pokemon])

        while True:
            mytotalHP = player.getTotalHP()
            enemytotalHP = enemyObj.getTotalHP()
            print(name, 'HP:', mytotalHP)
            print(enemy_name, 'HP:', enemytotalHP)
            main_has_health = player.main_has_health()
            if mytotalHP == 0:
                print('You either have no pokemon or all your pokemon are at 0 hp.\n')
                break  # leaves loop
            if main_has_health == False:
                print('Your main pokemon has no health, switching main pokemon.\n')
                player.set_healthy_pokemon()
            action = int(input('Choose an action\n1 - Attack\n2 - Switch pokemon\n3 - Leave battle\n'))

            if action == 1:
                main_has_health = enemyObj.main_has_health()
                if main_has_health == False:
                    # print('INSIDE OF IF STATEMENT')
                    enemyObj.set_healthy_pokemon()
                player.attack(enemyObj)
                enemytotalHP = enemyObj.getTotalHP()
                if enemytotalHP == 0:
                    print(enemy_name, 'ran out of health.')
                    break  # Leaves the battle
                if player.main.hp > 0:
                    enemyObj.attack(player)
                else:
                    print('Players main has no hp\n')

            elif action == 2:
                target = input('Which pokemon would you like to switch to?\n')
                player.switchMain(target)

            elif action == 3:
                print('Leaving battle.')
                break
            else:
                print('Invalid input.')


    elif userChoice == 2:
        player.findPokemon()
    elif userChoice == 3:
        freePokemon = input('Choose which pokemon you would like to set free: ')
        player.setFree(freePokemon)
    elif userChoice == 4:
        print('Healing main pokemon')
        player.healPokemon()
    elif userChoice == 5:
        print(
            'Choose what to do in your pokedex:\n1 - Look at pokemon statistics\n2 - Switch main pokemon\n3 - Go back\n')
        dex_choice = int(input())
        if dex_choice == 1:
            player.printPokedex()
        elif dex_choice == 2:
            target = input('Which pokemon would you like to switch to?\n')
            if player.switchMain(target):
                print('Main pokemon has been switched')
        elif dex_choice == 3:
            continue
        else:
            print('This command is not valid.\n')
            continue
    elif userChoice == 6:
        print('Thank you for playing!')
        break
    else:
        print('This is not a valid command.\n')
        continue
