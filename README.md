```markdown
# CPU Scheduling Algorithms

This repository contains Python implementations of three common CPU scheduling algorithms:

* **First-Come, First-Served (FCFS)**
* **Shortest-Remaining-Time-First (SRT)**
* **Round Robin (RR)**

**Files**

* **process.py:** Defines the `Process` and `PCB` (Process Control Block) classes. 
    * `Process`: An abstract base class for process information (PID, burst time, arrival time).
    * `PCB`: Extends `Process` and includes additional information specific to the scheduling algorithms (start time, finish time, waiting time, turnaround time, etc.).
* **CPUScheduler.py:** Defines the abstract `Scheduler` class with abstract methods for fetching processes and scheduling them.
* **FCFS.py:** Implements the FCFS scheduling algorithm, including:
    * `fetchProcesses`: Reads process information from a file.
    * `Schedule`: Schedules processes using the FCFS algorithm.
    * `ResultViewer`: Displays scheduling results (table and Gantt chart).
* **SRT.py:** Implements the SRT scheduling algorithm, including:
    * `fetchProcesses`: Reads process information from a file.
    * `Schedule`: Schedules processes using the SRT algorithm.
    * `SRTDrawer`: Displays scheduling results (table and Gantt chart).
* **RR.py:** Implements the RR scheduling algorithm, including:
    * `fetchProcesses`: Reads process information from a file.
    * `Schedule`: Schedules processes using the RR algorithm with a specified quantum.
    * `RRDrawer`: Displays scheduling results (table and Gantt chart).

**How to Use**

1. Save the provided Python files in the same directory.
2. Create text files named `FCFS.txt`, `SRT.txt`, and `RR.txt` in the same directory. Each file should contain process information in the following format:

```
PID BurstTime ArrivalTime 
```

    * `PID`: The process ID (an integer).
    * `BurstTime`: The burst time of the process (an integer).
    * `ArrivalTime`: The arrival time of the process (an integer).

3. **To run FCFS:**
   ```bash
   python FCFS.py 
   ```

4. **To run SRT:**
   ```bash
   python SRT.py 
   ```

5. **To run RR (with a quantum of 4):**
   ```bash
   python RR.py 
   ```

**Output**

Each script will generate the following output:

* **Table:** Displays the waiting time, turnaround time, and CPU utilization for each process.
* **Gantt Chart:** Visualizes the process execution order using Matplotlib.

This implementation provides a basic framework for understanding and comparing different CPU scheduling algorithms. You can further enhance it by:

* Adding more scheduling algorithms (e.g., Priority Scheduling, Deadline Scheduling).
* Implementing more advanced features (e.g., context switching, process priorities).
* Improving the visualization and user interface.
```

This code effectively represents the readme file content in Markdown format, ready to be saved as `README.md`.
