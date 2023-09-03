class Pokemon:
    def __init__(self, stats): #stats is a list, the list takes in name, type, attack and defence
        self.name = stats[0]
        self.type = stats[1]
        self.attack = stats[2]
        self.defence = stats[3]
        self.hp = 100
        self.dMax = stats[3]
        self.pokeNum = 1

    def takeDamage(self, fromPk):
        percentEffective = (100-self.defence)/100 #finding percentage of how effective an attack is going to be   e.g. a defence of 80 makes attacks 20% effective
        self.hp -= fromPk.attack*percentEffective #attacking calculation
        if self.hp < 0:
            self.hp = 0
        self.hp = int(self.hp)
        self.defence -= int(0.2*self.defence) #making defence lower when attacked
        if self.defence < 0:
            self.defence = 0
        print(fromPk.name, "'s attack was", percentEffective*100, 'percent effective!\n')
        self.printStats()

    def hurt(self, pokemon):
        if self.hp == 0:
            print(self.name, 'has no health. No damage is done to', pokemon.name, '\n')
            return
        pokemon.takeDamage(self)

    def heal(self):
        self.hp = 100
        self.defence = self.dMax
        print(self.name, ' is healed.\n')
        self.printStats()

    def printStats(self):
        print('Name: ', self.name)
        print('Type: ', self.type)
        print('Attack: ', self.attack)
        print('Defence: ', self.defence)
        print('Health Points: ', self.hp)
        print()
