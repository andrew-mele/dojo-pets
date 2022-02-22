class Pet:
    def __init__(self, name, tricks, noise):
        self.name = name
        self.tricks = tricks
        self.noise = noise
        self.health = 100
        self.energy = 80

    def sleep(self):
        self.energy += 25
        print(f'{self.name} seems to be sleeping...hopefully they will have more energy later!')
        return self

    def eat(self):
        self.energy += 5
        self.health +=10
        return self
    
    def trick(self):
        if self.energy > 20:
            self.energy -=10
            print(f'Wow! {self.name} just performed {self.tricks}!...ow...')
        else: 
            print(f'Hmm...{self.name} seems too tired to do tricks, maybe they need to rest?')
            self.energy <= 20
        return self

    def play(self):
        if self.energy >= 20:
            self.energy -= 15
            print(f'Wow! {self.name} loves playing with their toy!')
            self.health += 5 
        else: 
            print(f'Hmmm..{self.name} looks to be worn out...maybe a good time for a nap.')
            self.energy <= 20
        return self

    def makeNoise(self):
        print(self.noise)
    
    def checkPetStats(self):
        print(f'Health is: {self.health}' )
        print(f'Energy is: {self.energy}' )
