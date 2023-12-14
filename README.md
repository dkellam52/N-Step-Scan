# N-Step-Look Disk Scheduling Algorithm

## Overview
This project implements the N-Step-Look disk scheduling algorithm in Python. It's designed to simulate the way a disk head moves to fulfill requests for reading or writing data to disk tracks. The algorithm processes requests in groups of size N, moving the disk head in one direction until all requests in the group are fulfilled or there are no more requests in that direction. After each group, the direction of the disk head movement reverses.

## Features
- **Random Request Generation**: Generates 1000 random disk requests, simulating a real-world scenario for disk access.
- **N-Step Group Processing**: Processes disk requests in groups of N, where N is user-defined.
- **Directional Switching**: After processing each group, the direction of disk head movement switches, enhancing efficiency and reducing seek time.
- **Detailed Output**: Outputs each processed group of requests along with the direction of processing and the total number of tracks traversed.

## How to Run
1. **Set Up Your Environment**:
   Ensure that you have Python 3.x installed on your system.

2. **Running the Program**:
   - Open your terminal or command prompt.
   - Navigate to the directory containing the `disk_scheduling.py` file.
   - Run the program using Python:
     ```
     python disk_scheduling.py
     ```
   - Enter the value of N when prompted.
   - The program will display the generated disk requests, the order of processing for each group, and the total tracks traversed.

## Algorithm Explanation
The N-Step-Look algorithm is a variant of the LOOK disk scheduling algorithm. It groups requests into sets of N and processes each group in a single direction before reversing. This approach balances the time-efficient processing of LOOK with the fairness and bounded wait times of more segmented approaches.

## Project Structure
- `disk_scheduling.py`: Contains the main logic for the N-Step-Look disk scheduling algorithm.


---

Created as part of a computer science project on disk scheduling algorithms.
