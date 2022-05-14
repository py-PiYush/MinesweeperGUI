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
        btn = Button(location, width=6, height=2)
        btn.bind("<Button-1>", self.left_click_actions)  # Left click
        btn.bind("<Button-3>", self.right_click_actions)  # right click
        self.cell_btn_object = btn

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x + i, self.y + j)
            for i, j in [
                (1, 1),
                (1, 0),
                (0, 1),
                (-1, -1),
                (-1, 0),
                (0, -1),
                (1, -1),
                (-1, 1),
            ]
            if (
                0 <= self.x + i < settings.GRID_SIZE
                and 0 <= self.y + j < settings.GRID_SIZE
            )
        ]
        return cells

    def get_cell_by_axis(self, x, y):
        """
        Return cell object based on x,y value
        """
        for cell in Cell.ALL:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells_mines_count(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_mine(self):
        """
        Interrupts the game, player lost
        """
        self.cell_btn_object.configure(bg="red")

    def show_cell(self):
        """
        Display the number of surrounding mines
        """
        self.cell_btn_object.configure(text=self.surrounded_cells_mines_count)

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()

    def right_click_actions(self, event):
        print("i'm right click")

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.ALL, settings.MINES)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self) -> str:
        return f"Cell({self.x}, {self.y})"
