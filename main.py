from pet import Pet
from ninja import Ninja

petFood = ['Bacon🥓', 'Croissant🥐', 'Tacos🌮', 'Shrimp🍤', 'Banana🍌']

treats = ['CatNip🧆', 'Temptations Chicken Bites🍗']

pet1 = Pet('Yarn', 'Scratch', 'Meow!')
user1 = Ninja('Andrew', 'Mele', pet1, treats, petFood)

user1.bathe()
user1.feedTreat(treats)
pet1.play()
pet1.trick()
user1.feedTreat(treats)
user1.feedFood(petFood)
user1.walk()
user1.feedFood(petFood)
pet1.sleep()
user1.feedFood(petFood)
user1.feedTreat(treats)
user1.feedFood(petFood)
pet1.checkPetStats()
pet1.trick()
user1.feedFood(petFood)
pet1.trick()
pet1.sleep()
pet1.trick()
pet1.play()
pet1.play()
user1.feedTreat(treats)
pet1.sleep()
user1.walk()
user1.feedFood(petFood)
pet1.sleep()
pet1.checkPetStats()
user1.walk()
