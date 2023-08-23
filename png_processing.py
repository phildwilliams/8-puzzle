import PIL.Image, PIL.ImageTk
from itertools import product
from tkinter import *

def tile_image(image_path):
    tiles = []
    img = PIL.Image.open(image_path)
    w, h = img.size
    size = w // 3
    
    grid = product(range(0, size * 3, size), range(0, size * 3, size))
    for i, j in grid:
        box = (j, i, j+size, i+size)
        new = PIL.Image.new('RGB', (size + 8, size + 8), "Black")
        new.paste(img.crop(box), (4,4))
        tiles.append(new)
    return (tiles, size)

def combine_tiles(tiles, puzzle, size):
    image = PIL.Image.new('RGB', ((size+8)*3, (size+8)*3), (250,250,250))
    counter = 0
    for index in puzzle:
        if index == 0:
            image.paste(PIL.Image.new('RGB', (size + 8, size + 8), "Black"), ((counter%3)*size, (counter//3)*size))
        else: image.paste(tiles[index - 1], ((counter%3)*size, (counter//3)*size))
        counter += 1
    return image

def setup_canvas():
    win = Tk()
    win.geometry("400x400")
    win.attributes("-topmost", True)
    canvas= Canvas(win, width= 400, height= 400)
    canvas.pack()
    return (win, canvas)

def add_image(win, canvas, image):
    ph = PIL.ImageTk.PhotoImage(image)
    canvas.create_image(20,20,anchor=NW,image=ph)
    win.update_idletasks()
    win.update()