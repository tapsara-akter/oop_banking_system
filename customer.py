
# abstraction
from abc import ABC, abstractmethod, abstractproperty


class Customer(ABC):

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def setName(self, name):
        pass

    @abstractmethod
    def getId(self):
        pass

    @abstractmethod
    def setId(self, id):
        pass