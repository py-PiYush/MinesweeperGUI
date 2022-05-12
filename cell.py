from tkinter import Button
import random
import settings


class Cell:
    ALL = []

    def __init__(self, x, y, is_mine=False):
        self.x = x
        self.y = y
        self.is_mine = is_mine
        self.cell_btn_object = None

        # Append the objects in Cell.ALL
        Cell.ALL.append(self)

    def create_btn_object(self, location):
        btn = Button(location, width=6, height=2, text=f"({self.x}, {self.y})")
        btn.bind("<Button-1>", self.left_click_actions)  # Left click
        btn.bind("<Button-3>", self.right_click_actions)  # right click
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        print(event)
        print("I am left click")

    def right_click_actions(self, event):
        print("i'm right click")

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.ALL, settings.MINES)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self) -> str:
        return f"Cell({self.x}, {self.y})"
