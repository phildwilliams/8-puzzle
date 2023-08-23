import algorithms
from node import Node
from png_processing import *

def main():
    initial_state = Node()
    print("Welcome to Phillip's 8-Puzzle Solver! \n\nWhich algorithm you would like to use?")
    print("\t1.    Uniform Cost Search (Brute Force)")
    print("\t2.    A* with Manhattan Distance Heuristic")
    print("\t3.    A* with Misplaced Tiles Heuristic")
    response = None
    while response not in ["1", "2", "3"]:
        response = input("Please select 1, 2, or 3: ")
    if response == "1": algorithms.uniform_cost_search(initial_state)
    if response == "2": algorithms.manhattan_distance_search(initial_state)
    if response == "3": algorithms.misplaced_tiles_search(initial_state)

if __name__ == "__main__":
    main()