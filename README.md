# AERO60492 - AMR Path Planning Coursework

## Overview

This project implements the A\* path planning algorithm for a generalized robotic system within a predefined GUI framework. It enables autonomous planning of safe routes avoiding obstacles, restricted to vertical and horizontal movements (no diagonals).

## Objectives

- Implement the A\* algorithm.
- Navigate efficiently from a start point to an end point.
- Ensure robustness, speed, and adherence to good coding practices.

## Requirements

- **Language**: Python 3 (no external libraries allowed).
- Movement: Only vertical/horizontal cell transitions allowed.
- Return the path as a list of (col, row) coordinates from start to goal.

## Files

- `gui.py`: Prebuilt graphical interface (DO NOT EDIT).
- `pathPlanner.py`: Implemented the A\* algorithm here

## Running the Project

1. Ensure Python3 is installed.
2. Install required package (`QT5`) in a virtual environment:
   ```bash
   python -m venv myenv
   source myenv/bin/activate
   pip install PyQt5
   ```

````
3. Run the project:
```bash
python gui.py
````



