#L.A. #27
#Mark J. Rullan

from abc import ABC, abstractmethod

class NinjaTurtle(ABC):
    pass
    @property
    @abstractmethod
    def alias(self):
        pass


class Leonardo(NinjaTurtle):
    def __init__(self, name, alias):
        self.name = name
        self.__alias = alias
    @property
    def alias (self):
        return self.__alias
        
class MichaelAngelo(NinjaTurtle):
    def __init__(self, name, alias):
        self.name = name
        self.__alias = alias
    @property
    def alias (self):
        return self.__alias 
       
class Donatello(NinjaTurtle):
    def __init__(self, name, alias):
        self.name = name
        self.__alias = alias
    @property
    def alias (self):
        return self.__alias 
    
class Raphael(NinjaTurtle):
    def __init__(self, name, alias):
        self.name = name
        self.__alias = alias
    @property
    def alias (self):
        return self.__alias

if __name__ == "__main__":
    Leonardo = Leonardo("Leornardo", "1")
    Michaelangelo = Michaelangelo("Michaelangelo", "2")
    Donatello = Donatello("Donatello", "3")
    Raphael = Raphael("Raphael", "4")

    print(Leonardo.alias)
    print(Michaelangelo.alias)
    print(Donatello.alias)
    print(Raphael.alias)
