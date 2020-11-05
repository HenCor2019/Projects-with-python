from abc import abstractmethod, ABCMeta


class Operation(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def Operacion(self):
        pass

class Add(Operation):

    def __init__(self, value1, value2):
        Operation.__init__(self)
        self.__value1 = value1
        self.__value2 = value2

    def Operacion(self):
        return self.__value1 + self.__value2

class Subs(Operation):

    def __init__(self, value1, value2):
        Operation.__init__(self)
        self.__value1 = value1
        self.__value2 = value2

    def Operacion(self):
        return self.__value1 - self.__value2

suma = Add(5,3)
resultado = suma.Operacion()
print(resultado)

resta = Subs(5,3)
resultado = resta.Operacion()
print(resultado)

