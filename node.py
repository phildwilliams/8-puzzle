import copy
import random
import os
from png_processing import tile_image, combine_tiles

class Node:

    def __init__(self, puzzle=None, image_path=None, g=0, function="brute_force"):
        if image_path == None:
            self.image_path = os.path.join("images", random.choice(os.listdir("images")))
        else: self.image_path = image_path
        if puzzle == None:
            self.puzzle = [1,2,3,4,5,6,7,8,0]
            random.shuffle(self.puzzle)
            while not self.is_solvable():
                random.shuffle(self.puzzle)
        else: self.puzzle = puzzle
        self.blank_index = self.find_blank()
        self.g = g
        self.h = 0
        if function == "manhattan_distance": self.h = self.manhattan_distance()
        if function == "misplaced_tiles": self.h = self.misplaced_tiles()
        self.cost = self.g + self.h

    def is_solvable(self):
        inv_count = 0
        for i in range(0, 9):
            for j in range(i + 1, 9):
                if self.puzzle[j] != 0 and self.puzzle[i] != 0 and self.puzzle[i] > self.puzzle[j]:
                    inv_count += 1
        return inv_count%2 == 0

    def find_blank(self):
        return self.puzzle.index(0)

    def is_goal(self):
        return self.misplaced_tiles() == 0

    def misplaced_tiles(self):
        misplaced_tiles = 0
        for i in range(0,8):
            if self.puzzle[i] != i + 1: misplaced_tiles += 1
        return misplaced_tiles

    def manhattan_distance(self):
        return sum(abs((val-1)%3 - i%3) + abs((val-1)//3 - i//3) for i, val in enumerate(self.puzzle) if val) 

    def print_puzzle(self):
        print(self.puzzle[:3])
        print(self.puzzle[3:6])
        print(self.puzzle[6:])

    def get_image(self):
        tiles, size = tile_image(self.image_path)
        return combine_tiles(tiles, self.puzzle, size)

    def move_up(self):
        temp = copy.deepcopy(self.puzzle)
        temp[self.blank_index], temp[self.blank_index - 3] = temp[self.blank_index - 3], temp[self.blank_index]
        return temp

    def move_down(self):
        temp = copy.deepcopy(self.puzzle)
        temp[self.blank_index], temp[self.blank_index + 3] = temp[self.blank_index + 3], temp[self.blank_index]
        return temp

    def move_left(self):
        temp = copy.deepcopy(self.puzzle)
        temp[self.blank_index], temp[self.blank_index - 1] = temp[self.blank_index - 1], temp[self.blank_index]
        return temp

    def move_right(self):
        temp = copy.deepcopy(self.puzzle)
        temp[self.blank_index], temp[self.blank_index + 1] = temp[self.blank_index + 1], temp[self.blank_index]
        return temp