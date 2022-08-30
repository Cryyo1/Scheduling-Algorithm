# Scheduling Algorithm
simulation of process management system 
## Setup
```
python scheduler.py
``` 
## Process

1. we have five process  , each one have its own priority  and a quantum 
    - white (priority=9548)
    - red (priority=3121)
    - green (priority=1024)
    - blue (priority=335)
    - yellow (priority=110)

2. the quantum of each process is calculated using its priority
```
Quantum of process (i)=  latency *  process priority(i) / sum of all priorities.

with latency=6ms
```

3. at each clock tick (each 1 sec) ,execution  value of each process is calculated :
```
execution value of process (i)= time spent in the cpu * 1024 / process priority(i).
```

4. the next elected process is the oen with the smaller execution value and takes the cpu for its quantum

5. at the start all processes are execution value is  0

## requirements

- python
- tkinter




