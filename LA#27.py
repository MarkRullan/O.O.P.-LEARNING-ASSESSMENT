#L.A. #27
#Mark J. Rullan

from abc import ABC, abstractmethod
class NinjaTurtle(ABC):
    @property
    @abstractmethod
    def alias(self):
        pass
    
class Leonardo(NinjaTurtle):
    def  __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias
    
    @property
    def alias(self):
        return f"{self.__alias}"

class Michelangelo(NinjaTurtle):
    def  __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias
    
    @property
    def alias(self):
        return f"{self.__alias}"

class Donatello(NinjaTurtle):
    def  __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias
    
    @property
    def alias(self):
        return f"{self.__alias}"

class Raphael(NinjaTurtle):
    def  __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias
    
    @property
    def alias(self):
        return f"{self.__alias}"

if __name__ =="__main__":
    
    leonardo = Leonardo("Leonardo", "blue")
    michalagelo = Michelangelo("Michelangelo", "orange")
    donatello = Donatello("Donatello", "violet")
    raphael = Raphael("Raphael", "red")

    print(leonardo.alias)
    print(michalagelo.alias)
    print(donatello.alias)
    print(raphael.alias)