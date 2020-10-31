import abc
from abc import ABCMeta


class Weapon(object):
    durability = 0
    name = ""
    def __init__(self):
        __metaclass__ = ABCMeta

    @abc.abstractmethod
    def Attack(self):
        pass

    def get_name(self):
       pass

    def set_name(self,name):
       pass

    name = abc.abstractproperty(get_name, set_name)

class Sword(Weapon):
    def __init__(self, name, durability, hability):
        self._name = name
        self._durability = durability
        self._hability = hability

    def get_hability(self):
        return self._hability

    def Attack(self):
        print("te han pegado un espadazo...")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

class Bow(Weapon):
    def __init__(self, name, durability, hability):
        self._name = name
        self._durability = durability
        self._hability = hability

    def get_hability(self):
        return self._hability

    def Attack(self):
        print("te han pegado un espadazo...")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name


sword = Sword("espada",100,"una mano")
sword.name = "chunchumaru"
print(sword.name)

bow = Bow("Arco",100,"larga distancia")
bow.name = "Arco santo"
print(bow.name)
