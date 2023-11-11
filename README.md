# AI-project
This is my project for the Artificial Intelligence course.

1. Introduction

1.1 Background
In the realm of artificial intelligence, maze-solving algorithms serve as fundamental tools with applications in various
domains, including robotics, pathfinding, and game development. The primary objective of such algorithms is to find
an optimal or near-optimal path from a predefined start point to a goal point while navigating through a maze. These
algorithms take advantage of search strategies to explore and traverse the maze efficiently. The use of heuristic functions in
informed search algorithms, such as A* and Greedy Best-First, further enhances their ability to discover the shortest
path. This project aims to explore and implement a suite of maze-solving algorithms, including Breadth-First Search
(BFS), Depth-First Search (DFS), Iterative Deepening Search (IDS), Greedy Best-First Search, and A* Search, to solve randomly generated mazes.
Through this project, we seek to analyze the effectiveness of each algorithm in finding the optimal path and compare
their performances.
1.2 Objectives
The primary objectives of this project are twofold: First, to implement and analyze the performance of four distinct
maze-solving algorithms - BFS, DFS, IDS, Greedy Best-First, and A* Search - in solving randomly generated mazes. Second,
to visualize and present the results, including the paths discovered by each algorithm, and to draw conclusions about
their efficiency and effectiveness in finding optimal solutions. By achieving these objectives, we aim to provide
insights into the strengths and weaknesses of different search algorithms when applied to maze-solving tasks.

2. Project Overview

2.1 Project Description
The project focuses on the development and evaluation of maze-solving algorithms, which are fundamental in
artificial intelligence. We aim to implement four diverse algorithms, namely Breadth-First Search (BFS), Depth-First
Search (DFS), Iterative Deepening Search (IDS), Greedy Best-First Search, and A* Search, and examine their performance in solving randomly
generated mazes. The mazes feature start and end points, as well as walls, and are created using a random maze
generation approach. The algorithms are then tasked with finding the optimal path from the start to the end while
navigating through the maze. The results, including the paths discovered by each algorithm, are presented and
analyzed to determine their efficiency and effectiveness in solving maze puzzles. This project offers valuable insights
into the comparative strengths and weaknesses of different search strategies for maze-solving tasks.

3. Methodology

3.1 Maze Generation
To facilitate the evaluation of the maze-solving algorithms, a random maze-generation approach is employed. The
mazes are created with a predefined number of rows and columns, and they feature a start point marked as 'S', an
endpoint marked as 'E', and walls represented by '#'. The maze generation process introduces an element of
randomness, ensuring that each test scenario presents a unique challenge to the algorithms. This randomization
adds an essential element of unpredictability and complexity to the project, enhancing its practical applicability.
3.2 Search Algorithms
This project uses five distinct search algorithms: Breadth-First Search (BFS), Depth-First Search (DFS), Iterative Deepening Search 
(IDS), Greedy Best-First Search, and A* Search. These algorithms utilize different search strategies and heuristics to traverse the
maze and find the optimal path from the start to the endpoint. BFS explores the maze layer by layer, DFS delves
deep into a branch before backtracking, Greedy Best-First prioritizes paths with the lowest heuristic values, and A*
Search combines both cost and heuristic information to make informed decisions. The project seeks to understand
the advantages and limitations of each algorithm and compare their performance in maze-solving tasks.

4. Implementation Details

4.1 Code Structure
The code is structured into distinct components for maze generation, search algorithms, and result visualization. It
features modular functions for each algorithm, enabling the easy addition of new algorithms if desired. The code
also incorporates data structures and logic specific to each search strategy. A clear and organized code structure
facilitates experimentation with different algorithms and the evaluation of their effectiveness.
4.2 Algorithm Details
Each search algorithm has been implemented with specific details tailored to its strategy. For instance, BFS and DFS
use data structures like queues and stacks, respectively, to manage node exploration. Greedy Best-First Search
employs a priority queue to choose nodes with the lowest heuristic values. A* Search combines cost tracking with
heuristic evaluation, utilizing a priority queue for optimal pathfinding. These algorithm-specific details enable each
search strategy to function as intended and provide insights into their unique characteristics.

5. Results
The project produces visual representations of the randomly generated mazes, highlighting the start, end, walls, and
discovered paths. Each algorithm's output, including the paths it found, is presented and analyzed. The results
showcase the effectiveness of each search algorithm in solving maze puzzles and provide a basis for comparative
evaluation.

6. Conclusion
In conclusion, this project explores and implements a suite of maze-solving algorithms, including BFS, DFS, Greedy
Best-First, and A* Search. The utilization of random maze generation ensures diversity in test scenarios, making it
possible to analyze and compare the performance of these algorithms under varying conditions. The project aims to
shed light on the strengths and limitations of different search strategies and their effectiveness in finding optimal
solutions to maze puzzles. By evaluating the results and considering the visual representations, this project
contributes insights into the practical applicability of search algorithms in maze-solving tasks and lays the foundation
for further explorations in artificial intelligence and pathfinding.
