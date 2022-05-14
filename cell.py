from tkinter import Button, Label
import random
import settings
import ctypes
import sys


class Cell:
    ALL = []
    cell_count_label_object = None
    cell_count = settings.GRID_SIZE ** 2
    mine_count = settings.MINES
    timer_object = None
    time = -1

    def __init__(self, x, y, is_mine=False):
        self.x = x
        self.y = y
        self.is_mine = is_mine
        self.is_mine_candidate = False
        self.is_open = False
        self.cell_btn_object = None

        # Append the objects in Cell.ALL
        Cell.ALL.append(self)

    def create_btn_object(self, location):
        btn = Button(location, width=6, height=2)
        btn.bind("<Button-1>", self.left_click_actions)  # Left click
        btn.bind("<Button-3>", self.right_click_actions)  # right click
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            text=f"Mines Left: {Cell.mine_count}",
            width=12,
            height=2,
            bg=settings.COLOR,
            fg="white",
            font=("Gill Sans MT", 14),
        )
        Cell.cell_count_label_object = lbl

    @staticmethod
    def create_timer_label(location):
        lbl = Label(
            location,
            text=f"Time: {Cell.time} sec",
            width=12,
            height=2,
            bg=settings.COLOR,
            fg="white",
            font=("Gill Sans MT", 14),
        )
        Cell.timer_object = lbl

    @staticmethod
    def update_time():
        Cell.time += 1
        Cell.timer_object.configure(text=f"Time: {Cell.time} sec")

        Cell.timer_object.after(1000, Cell.update_time)

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

    def mines_count_color(self, count):
        if count == 0:
            return "green"
        elif count <= 2:
            return "blue"
        elif count == 3:
            return "orange"
        else:
            return "red"

    def show_mine(self):
        """
        Interrupts the game, player lost
        """
        self.cell_btn_object.configure(bg="red")
        ctypes.windll.user32.MessageBoxW(0, "You clicked on mine", "Game Over", 0)
        sys.exit()

    def show_cell(self):
        """
        Display the number of surrounding mines
        """
        if not self.is_open:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(
                text=self.surrounded_cells_mines_count,
                fg=self.mines_count_color(self.surrounded_cells_mines_count),
            )
        self.is_open = True

    def left_click_actions(self, event):
        if self.is_mine_candidate:
            self.right_click_actions(event)
            return
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_count == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()

            # If total mines = cells left, player won
            if Cell.cell_count == settings.MINES:
                ctypes.windll.user32.MessageBoxW(
                    0,
                    f"Congratulations! You won the game in {Cell.time} seconds.",
                    "Yay!!!",
                    0,
                )

        # cancel left and right click events if cell is opened
        self.cell_btn_object.unbind("<Button-1>")
        self.cell_btn_object.unbind("<Button-3>")

    def right_click_actions(self, event):

        if not self.is_mine_candidate:
            self.cell_btn_object.configure(bg="orange", text="M")
            self.is_mine_candidate = True
            Cell.mine_count -= 1
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Mines Left: {Cell.mine_count}"
                )

        else:
            self.cell_btn_object.configure(bg="SystemButtonFace", text="")
            self.is_mine_candidate = False
            Cell.mine_count += 1
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Mines Left: {Cell.mine_count}"
                )

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.ALL, settings.MINES)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self) -> str:
        return f"Cell({self.x}, {self.y})"
