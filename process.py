from abc import ABC, abstractmethod

class Process(ABC):

    def __init__(self,pid,brustTime,ArrivalTime):
        self.setPID(pid)
        self.setBrustTime(brustTime)
        self.setArrivalTime(ArrivalTime)

    def getPID(self):
        return self.__pid
    
    def getBrustTime(self):
        return self.__brustTime
    
    def getArrivalTime(self):
        return self.__ArrivalTime
    
    def setPID(self,pid=int):
        self.__pid = pid
    
    def setBrustTime(self,brustTime=int):
        self.__brustTime = brustTime

    def setArrivalTime(self,ArrivalTime=int):
        self.__ArrivalTime = ArrivalTime


class PCB(Process):
    def __init__(self,pid,brustTime,ArrivalTime,StartTime,FinishTime,firstResponse=-1):
        self.setPID(pid)
        self.setBrustTime(brustTime)
        self.setArrivalTime(ArrivalTime)
        self.setStartTime(StartTime)
        self.setFinishTime(FinishTime)
        self.setFirstResponseTime(firstResponse)
        self.__RemainingTime = brustTime

    def setRemainingTime(self,time=int):
        self.__RemainingTime = time

    def setStartTime(self,time=int):
        self.__startTime = time

    def setFinishTime(self,time=int):
        self.__finishTime = time

    def setTurnArroundTime(self,time=int):
        self.__turnArroundTime = time

    def setWaitingTime(self,time=int):
        self.__waitingTime = time

    def getTurnArroundTime(self):
        return self.__turnArroundTime
    
    def getWaitingTime(self):
        return self.__waitingTime

    def getStartTime(self):
        return self.__startTime
    
    def getFinishTime(self):
        return self.__finishTime
    
    def getFirstResponseTime(self):
        return self.__firstResponse
    
    def setFirstResponseTime(self,time):
        self.__firstResponse = time

    def getRemainingTime(self):
        return self.__RemainingTime