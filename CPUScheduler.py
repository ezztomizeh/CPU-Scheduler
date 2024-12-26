from abc import ABC, abstractmethod
from process import PCB
import matplotlib.pyplot as plt

class Scheduler(ABC):

    @abstractmethod
    def fetchProcesses(self,fileName=str):
        pass

    @abstractmethod
    def Schedule(self):
        pass

