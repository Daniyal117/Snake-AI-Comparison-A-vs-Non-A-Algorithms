# A* vs Non-A* Snake Pathfinding

## Overview
This project implements a playable Snake game that compares the performance of two pathfinding algorithms: A* and non-A* strategies. The game allows for real-time comparison of algorithmic efficiency, accuracy, and speed in reaching the food while avoiding obstacles.

## Table of Contents
- [Features](#features)
- [Gameplay](#gameplay)
- [Comparison](#comparison)
- [How It Works](#how-it-works)
- [Running the Game](#running-the-game)
- [Cloning the Repository](#cloning-the-repository)

## Getting Started
To get started with this repository, follow the instructions below.
### Clone the Repository
First, clone this repository to your local machine using the following command:
```
git clone https://github.com/Daniyal117/XOR_Net.git
```
## Running the Game
To run the game, use the following command:
```bash
python3 main.py

## Features
- **A* Algorithm**: Implements an optimal pathfinding algorithm that dynamically calculates the best path to the food while avoiding obstacles.
- **Non-A* Algorithms**: Includes random and heuristic-based movement strategies for the snake, offering simpler, non-optimal alternatives.
- **Pathfinding Comparison**: Compares the efficiency, speed, and accuracy of A* and non-A* algorithms in reaching the food and avoiding obstacles.
- **Interactive Gameplay**: Provides a playable Snake game where users can choose between A* and non-A* algorithms to visually compare their performance in real-time.

## Gameplay
- The player can control the snake’s movement using arrow keys.
- Choose between A* or non-A* algorithm to navigate the snake.
- The objective is to reach the food while avoiding obstacles and the snake’s body.
- The game dynamically compares the two algorithms, showcasing their differences in terms of efficiency and performance.

## Comparison
- **A* Algorithm**: Known for its optimal pathfinding, the A* algorithm calculates the most efficient path to reach the food, avoiding all obstacles.
- **Non-A* Algorithms**: Includes simpler strategies like random movement or heuristic-based approaches that are less efficient but offer faster calculations.

## How It Works
- **A* Algorithm**: Uses a priority queue to explore the most promising paths first, ensuring an optimal solution.
- **Non-A* Algorithms**: These algorithms may use simpler methods like random or greedy search for navigation, providing faster but non-optimal solutions.
- **Game Loop**: The game continually updates the snake’s position and algorithm choice in real-time, displaying the performance of each strategy.


