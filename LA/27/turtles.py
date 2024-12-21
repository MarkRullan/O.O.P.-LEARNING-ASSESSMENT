#L.A. #26
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
