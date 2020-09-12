""" Examples from class: classes! """


class Integer:

    def __init__(self, x):
        self.val = x


class Pet:
    full = -2

    def __init__(self, name, species,
                 parent1=None, parent2=None):
        self.name = name
        self.species = species
        self.hunger = 0
        self.parents = (parent1, parent2)

    def eat(self, amount):
        self.hunger -= amount
        if self.hunger < self.too_much_food:
            self.nap()

    def nap(self):
        self.hunger += 1

    def __repr__(self):
        return self.name + ", a " + self.species

    def __eq__(self, r):
        return self.name == r.name

    def __gt__(self, r):
        return self.name > r.name


def pet_example():
    m = Pet('mittens', 'cat')
    r = Pet('rover', 'dog')
    r.hunger = -10
    r.nap()
    print('{} is a {}'.format(m.name, m.species))


# Blob: example of a mutable class variable (shared)
class Blob:
    population = [0]

    def __init__(self, mass):
        self.mass = mass
        self.population[0] += 1


def blob_example():
    family = []
    for k in range(10):
        family.append(Blob(5))

    # show that each member sees the same pop. list
    for member in family:
        print(member.population)
