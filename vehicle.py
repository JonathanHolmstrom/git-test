from abc import abstractmethod

class Vehicle :
    def __init__(self) :
        self._name = "Vehicle"

    @abstractmethod # decorator
    def drive(self) :
        """ Drives the vehicle forwards """

    def getName(self) :
        return self._name