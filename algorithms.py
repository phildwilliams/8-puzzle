from node import Node
from png_processing import setup_canvas, add_image
import time

def search(initial_node, function):
    queue = [initial_node]
    visited_states = []
    win, canvas = setup_canvas()
    while queue:
        current = queue.pop()
        visited_states.append(current.puzzle)
        add_image(win, canvas, current.get_image())
        if current.is_goal():
            print("Solution found!")
            print(f"The search algorithm expanded {len(visited_states)} nodes.")
            print(f"The depth of the goal node is {current.g}.")
            time.sleep(5)
            return current
        
        # print(f"The best state to expand with g(n) = {current.g} and h(n) = {current.h}")


        if current.blank_index%3 > 0 and current.move_left() not in visited_states: queue.append(Node(puzzle=current.move_left(), image_path=current.image_path, g=current.g + 1, function=function))
        if current.blank_index%3 < 2 and current.move_right() not in visited_states: queue.append(Node(puzzle=current.move_right(), image_path=current.image_path, g=current.g + 1, function=function))
        if current.blank_index//3 > 0 and current.move_up() not in visited_states: queue.append(Node(puzzle=current.move_up(), image_path=current.image_path, g=current.g + 1, function=function))
        if current.blank_index//3 < 2 and current.move_down() not in visited_states: queue.append(Node(puzzle=current.move_down(), image_path=current.image_path, g=current.g + 1, function=function))

        queue.sort(key=lambda x: x.cost, reverse=True)

    print("No solution found")
    return -1


def uniform_cost_search(initial_node):
    search(initial_node=initial_node, function="brute_force")

def manhattan_distance_search(initial_node):
    search(initial_node=initial_node, function="manhattan_distance")

def misplaced_tiles_search(initial_node):
    search(initial_node=initial_node, function="misplaced_tiles")