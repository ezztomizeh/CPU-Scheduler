from CPUScheduler import Scheduler
from process import PCB
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

class FCFS(Scheduler,ABC):

    def __init__(self):
        self.__processes = []

    def getProcesses(self):
        return self.__processes

    def addProcess(self,process=PCB):
        self.__processes.append(process)

    def fetchProcesses(self, fileName=str):
        with open(fileName,'r') as file:
            for line in file:
                pid,BrustTime,ArivalTime = line.split()
                process = PCB(int(pid),int(BrustTime),int(ArivalTime),0,0)
                self.addProcess(process)
        self.__processes.sort(key=lambda pcb:pcb.getArrivalTime()) 

    def Schedule(self):
        currentTime = 0
        for process in self.__processes:
            if currentTime < process.getArrivalTime():
                currentTime = process.getArrivalTime()
            process.setStartTime(currentTime)
            process.setFinishTime(currentTime+process.getBrustTime())
            process.setTurnArroundTime(process.getFinishTime()-process.getArrivalTime())
            process.setWaitingTime(process.getTurnArroundTime()-process.getBrustTime())
            currentTime = process.getFinishTime()

    @abstractmethod
    def ResultViewer(self):
        pass

class FCFSDrawer(FCFS):
    def ResultViewer(self):
        totalWaitTime = 0
        totalTurnArroundTime = 0
        CPUtime = sum(process.getBrustTime() for process in self.getProcesses())

        print("PID\tWait Time\tTurn Arround Time")
        for process in self.getProcesses():
            totalWaitTime += process.getWaitingTime()
            totalTurnArroundTime += process.getTurnArroundTime()
            print(process.getPID(),'\t',process.getWaitingTime(),'\t',process.getTurnArroundTime())

        print(f"CPU Utilization: {CPUtime/self.getProcesses()[-1].getFinishTime()}")
        print(f"Avg. Waiting Time: {totalWaitTime/len(self.getProcesses())}")
        print(f"Avg. TurnArroundTime: {totalTurnArroundTime/len(self.getProcesses())}")

        for i, process in enumerate(self.getProcesses()):
            plt.barh(y=i, width=process.getBrustTime(), left=process.getStartTime(), align='center',
                    label=f'P{process.getPID()} (Burst: {process.getBrustTime()})',color = 'blue')
            plt.text(process.getStartTime() + process.getBrustTime() / 2, i,
                    f'P{process.getPID()}', color='white', va='center', ha='center')
            
        plt.grid(True)
        plt.show()

X = FCFSDrawer()
X.fetchProcesses("processes.txt")
X.Schedule()
X.ResultViewer()
