from pet import Pet

class Ninja:
    def __init__(self, firstName, lastName, pet, treats, petFood):
        self.firstName = firstName
        self.lastName = lastName
        self.pet = pet
        self.treats = treats
        self.petFood = petFood

    def walk(self):
        self.pet.play()
        print(f'{self.firstName} took {self.pet.name} on a nice walk! 🏡')
        return self

    def feedTreat(self, treats):
        if len(self.treats) > 0:
            treats = self.treats.pop()
            print(f'{self.pet.name} ate some {treats}!')
            self.pet.eat()
        else:
            print(f'Oh no! You ran out of Treats! 🤯 Don\'t let {self.pet.name} know!')
        return self

    def feedFood(self, food):
        if len(self.petFood) > 0:
            food = self.petFood.pop()
            print(f'{self.pet.name} ate some {food}!')
            self.pet.eat()
        else:
            print('Oh no! You ran out of food! You should visit the store soon.')
        return self

    def bathe(self):
        self.pet.makeNoise()
        return self