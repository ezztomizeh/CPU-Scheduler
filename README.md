# CPU Scheduling Algorithms

This project implements various CPU scheduling algorithms in Python, including First-Come, First-Served (FCFS), Shortest Remaining Time (SRT), and Round Robin (RR). Each algorithm is designed to manage the execution of processes based on their arrival times and burst times.

## Project Structure

The project consists of the following files:

- `process.py`: Contains the abstract base class `Process` and the `PCB` (Process Control Block) class, which represents a process in the system.
- `CPUScheduler.py`: Defines the abstract base class `Scheduler` that outlines the methods for fetching processes and scheduling them.
- `FCFS.py`: Implements the First-Come, First-Served scheduling algorithm.
- `SRT.py`: Implements the Shortest Remaining Time scheduling algorithm.
- `RR.py`: Implements the Round Robin scheduling algorithm.
- `processes.txt`: A sample input file for the FCFS algorithm.
- `SRT.txt`: A sample input file for the SRT algorithm.
- `RR.txt`: A sample input file for the RR algorithm.

## Classes Overview

### `Process` Class

- **Attributes**:
  - `pid`: Process ID
  - `brustTime`: Time required for the process to complete
  - `ArrivalTime`: Time at which the process arrives in the system

- **Methods**:
  - Getters and setters for the attributes.

### `PCB` Class

Inherits from `Process` and adds additional attributes and methods:

- **Attributes**:
  - `StartTime`: Time at which the process starts execution
  - `FinishTime`: Time at which the process completes execution
  - `RemainingTime`: Time remaining for the process to complete
  - `TurnAroundTime`: Total time taken from arrival to completion
  - `WaitingTime`: Time the process has been in the ready queue
  - `FirstResponseTime`: Time at which the process first gets CPU time

### `Scheduler` Class

An abstract base class for all scheduling algorithms. It defines the methods `fetchProcesses` and `Schedule`.

### `FCFS` Class

Implements the First-Come, First-Served scheduling algorithm.

- **Methods**:
  - `fetchProcesses`: Reads processes from a file and sorts them by arrival time.
  - `Schedule`: Schedules the processes based on FCFS logic.
  - `ResultViewer`: Displays the results and Gantt chart for the scheduled processes.

### `SRT` Class

Implements the Shortest Remaining Time scheduling algorithm.

- **Methods**:
  - `fetchProcesses`: Reads processes from a file.
  - `Schedule`: Schedules the processes based on SRT logic.
  - `SRTDrawer`: Displays the results and Gantt chart for the scheduled processes.

### `RR` Class

Implements the Round Robin scheduling algorithm.

- **Methods**:
  - `fetchProcesses`: Reads processes from a file.
  - `Schedule`: Schedules the processes based on RR logic.
  - `RRDrawer`: Displays the results and Gantt chart for the scheduled processes.

## Input Files

### `processes.txt`

This file is used for the FCFS algorithm. Each line contains three integers representing the process ID, burst time, and arrival time, respectively.


### `SRT.txt`

This file is used for the SRT algorithm. Each line contains three integers representing the process ID, burst time, and arrival time, respectively.


### `RR.txt`

This file is used for the RR algorithm. Each line contains three integers representing the process ID, burst time, and arrival time, respectively.


## Usage

1. Ensure you have Python installed on your machine.
2. Install the required libraries, if not already installed:
   ```bash
   pip install matplotlib
   python FCFS.py

### Saving the README

1. Open a text editor or an IDE of your choice.
2 . Create a new file and paste the above content into it.
3. Save the file as `README.md` in your project directory.

This README file will serve as a comprehensive guide for anyone looking to understand or use your CPU scheduling algorithms project.
