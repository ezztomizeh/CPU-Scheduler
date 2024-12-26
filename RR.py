from CPUScheduler import Scheduler
from process import PCB
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

class RR(Scheduler, ABC):
    def __init__(self, quantum):
        self.__processes = []
        self.__timeline = []
        self.quantum = quantum

    def addProcess(self, time, process=PCB):
        self.__timeline.append((time, process))

    def getTimeline(self):
        return self.__timeline

    def fetchProcesses(self, fileName=str):
        with open(fileName, 'r') as file:
            for line in file:
                pid, brustTime, arrivalTime = line.split()
                process = PCB(int(pid), int(brustTime), int(arrivalTime), -1, 0, -1)
                self.__processes.append(process)

    def getProcesses(self):
        return self.__processes

    def Schedule(self):
        completedProcesses = 0
        numOfProcesses = len(self.getProcesses())
        time = 0
        queue = []

        while completedProcesses < numOfProcesses:
            for process in self.getProcesses():
                if process.getArrivalTime() <= time and process.getRemainingTime() > 0 and process not in queue:
                    queue.append(process)

            if queue:
                currentProcess = queue.pop(0)  
                if currentProcess.getFirstResponseTime() == -1:
                    currentProcess.setFirstResponseTime(time)

                if currentProcess.getStartTime() == -1:
                    currentProcess.setStartTime(time)

                execution_time = min(currentProcess.getRemainingTime(), self.quantum)
                currentProcess.setRemainingTime(currentProcess.getRemainingTime() - execution_time)
                self.addProcess(time, currentProcess)

                time += execution_time  

                if currentProcess.getRemainingTime() == 0:
                    currentProcess.setFinishTime(time)
                    completedProcesses += 1
            else:
                time += 1  

    @abstractmethod
    def RRDrawer(self):
        pass

class RRDrawer(RR):
    def RRDrawer(self):
        totalWaitingTime = 0
        totalTurnArroundTime = 0

        print("PID\tWait Time\tTurn Arround Time")
        for process in self.getProcesses():
            waitTime = process.getFinishTime() - process.getArrivalTime() - process.getBrustTime()
            turnArroundTime = process.getFinishTime() - process.getArrivalTime()
            totalWaitingTime += waitTime
            totalTurnArroundTime += turnArroundTime
            print(process.getPID(), '\t', waitTime, '\t', turnArroundTime)

        totalBrustTime = sum(process.getBrustTime() for process in self.getProcesses())
        minArrive = min(self.getProcesses(), key=lambda pcb: pcb.getArrivalTime())
        maxFinish = max(self.getProcesses(), key=lambda pcb: pcb.getFinishTime())

        print(f"Avg. Waiting Time: {totalWaitingTime / len(self.getProcesses())}")
        print(f"Avg. TurnArroundTime: {totalTurnArroundTime / len(self.getProcesses())}")
        print(f"CPU utilization: {totalBrustTime / (maxFinish.getFinishTime() - minArrive.getArrivalTime())}")

        fig, ax = plt.subplots()
        colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple']
        
        pid_list = [process.getPID() for process in self.getProcesses()]
        
        for time, process in self.getTimeline():
            color = colors[pid_list.index(process.getPID()) % len(colors)]
            ax.broken_barh([(time, 1)], (pid_list.index(process.getPID()), 0.8), facecolors=color)

        ax.set_yticks([i + 0.4 for i in range(len(pid_list))])
        ax.set_yticklabels([f"P{pid}" for pid in pid_list])
        ax.set_xlabel('Time')
        ax.set_ylabel('Processes')
        ax.set_title('Round Robin Scheduling Gantt Chart')
        plt.show()


if __name__ == "__main__":
    quantum = 4  
    x = RRDrawer(quantum)
    x.fetchProcesses("RR.txt") 
    x.Schedule()
    x.RRDrawer()