# PathFinder
The robot that finds path to it's goal.

## Overview

**PathFinder** is a robotics project aimed at designing and building a robot capable of autonomously solving mazes using intelligent search algorithms. Initiated by members of the [MESL](#abbreviation), this project offers a valuable hands-on opportunity to integrate algorithm design, embedded systems, and robotics.

Though maze-solving competitions are currently rare in domestic university contests, the landscape is evolving. In 2023, TechnoXian Bangladesh introduced a maze-solving segment, followed by events like [BDRO](#abbreviation), Makers Mania at [IUB](#abbreviation), and Techkriti Bangladesh Zonal by [IARC](#abbreviation). This project not only prepares us for such emerging opportunities but also deepens our understanding of graph algorithms in practical applications.


## Objectives

- Learn and implement classical graph traversal algorithms (e.g., BFS, DFS, A*).
- Visualize algorithm performance in software.
- Build a physical robot capable of navigating and solving mazes autonomously.


## Scope of Work

**Included**
- Visualization of different search methods (BFS, DFS, etc.).
- Integration of selected algorithm into a moving robot.

**Excluded**
- Transport robotics (e.g., Wall-E-style robots carrying objects).


## Implementation Plan

### Phase 1: Software Simulation
- Study different search algorithms.
- Build a visualizer to simulate and compare performances.
#### Searching algorithms
1. [DFS](search-algorithms/DFS.md)
2. [BFS](search-algorithms/DFS.md)
3. [Flood Fill](search-algorithms/Flood-fill.md)
4. [Dijkstra’s Algorithm](search-algorithms/Dijkstra.md)
5. [A* (A-Star) Algorithm](search-algorithms/A-star.md)
6. [Greedy Best-First Search](search-algorithms/GBFS.md)

### Phase 2: Hardware Development
- Select optimal algorithm based on simulation results.
- Integrate algorithm with microcontroler.
- Test robot in physical maze environments and refine as needed.


## Project Timeline

| Task                                      | Start Date | End Date   |
|-------------------------------------------|------------|------------|
| Study graph algorithms                    | Day 1      | Day 3      |
| Implement visual simulations              | Day 2      | Day 5      |
| Finalize maze-solving algorithm           | Day 5      | Day 6      |
| Hardware integration and testing          | Day 6      | Day 10     |
| Performance tuning and final evaluation   | Day 10     | Day 12     |


## Hardware and Software Requirements

### Hardware
- IR sensors (for edge detection)
- Ultrasonic sensors (for wall distance)
- Microcontroler (Arduino or ESP32)
- Lightweight chassis and frame
- Accurate motor driver circuit (≥95% fidelity)
- Rechargeable compact battery (sufficient capacity)

### Software
- Python 3.x
- Pygame / matplotlib (for visualizer)
- Arduino IDE or PlatformIO
- Git (version control)


### System Overview
- **Perception Unit**: IR & ultrasonic sensor for maze detection
- **Processing Unit**: Arduino / ESP32 (Be aware of the GPIO voltage)
- **Control Logic**: Pathfinding algorithm running in real-time
- **Mobility Unit**: Dual motor system with feedback. (360 servo seems promising)


### Evaluation Criteria
- **Accuracy**: Robot reaches the goal with minimum errors
- **Speed**: Important, but, after accuracy
- **Path Optimality**: Algorithm chooses shortest or best path
- **Noise Immunity**: Resilience to sensor error or signal noise


### Error Handling
- **Sensor failures**: Use redundancy or fallback logic.
- **Off-path recovery**: Reset algorithm to reevaluate route.
- **Battery monitoring**: Pre-check voltage levels before mission.


### Future Plans
- Host an introductory workshop for juniors on robotics and algorithms.
- Expand into multi-robot coordination systems.
- Implement Wall-E style object transport as a future module.


### Project Log
Progress and notes are maintained in the /reports directory:

- [Daily acknowledgements](reports/Daily-acknowledgements.md)
- [Weekly meeting logs](reports/Weekly-meeting-logs.md)
- [Testing observations](reports/Testing-bservations.md)
- [Algorithm comparison data](reports/Algorithm-comparison-data.md)


### Abbreviation

| Acronym | Full Form                                   |
|---------|---------------------------------------------|
| MESL    | Mechatronics and Embedded System Lab        | 
| BDRO    | Bangladesh Robot Olympiad                   |
| IUB     | Independent University, Bangladesh          |
| IARC    | International Autonomous Robotics Challenge |
| BFS     | Breadth first search                        |
| DFS     | Depth first search                          |

