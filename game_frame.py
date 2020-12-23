__author__ = "Lenka Skanderova"
__copyright__ = "(c)2020 VSB-TUO, FEECS, Dept. of Computer Science"
__email__ = "lenka.skanderova@vsb.cz"
__version__ = "0.1.0"


import pygame
import tkinter as tk
from tkinter import *
import os
from playground import PygamePlayground


class GameFrame:
    """
    Main frame for the application
    """
    def __init__(self):
        self.btn_checked = None
        self.selected_type = None
        self.dict_objects = self.make_list()

    def make_list(self):
        """
        Create a list of tuples:
            file_name, pygame.image, type
        :return: list of tuples (for buttons)
        """
        main_dir = 'winter_tile_set/PNG'
        sub_dirs = ['road', 'building', 'decor']
        lst = []

        order = 0

        for sub_dir in sub_dirs:
            path = main_dir+'/'+sub_dir+'/icons'

            files = os.listdir(path)

            for i in range(len(files)):
                img = pygame.image.load(path+'/'+files[i])
                lst.append((files[i], img, order, sub_dir))
                order += 1

        return lst

    def my_function_game(self, event):
        self.game_canvas.configure(scrollregion=self.game_canvas.bbox("all"), width=250, height=0)

    def my_function_options(self, event):
        self.options_canvas.configure(scrollregion=self.options_canvas.bbox("all"), width=70, height=0)

    def create_tk_components(self, grid_size):
        """
        Main method for components creation:
        - Canvases
        - Scrollbars
        - Toggle buttons
        - Playground

        Connection tkinter and pygame
        """

        self.root = tk.Tk()
        self.root.geometry("1280x800")
        self.main_frame = tk.Frame(self.root, bg="red")  # creates main_frame frame for pygame window
        self.main_frame.pack(side = LEFT, expand=1, fill=BOTH)  # packs window to the left

        # ---
        self.game_frame = tk.LabelFrame(self.main_frame, text='Game', relief="sunken", border = 1)
        self.game_frame.pack(side=LEFT, expand=1, fill=BOTH)
        self.game_canvas = tk.Canvas(self.game_frame)
        self.game_scrollbar_vertical = tk.Scrollbar(self.game_frame, orient="vertical", command=self.game_canvas.yview)
        self.game_scrollbar_vertical.pack(side='right', fill='y')
        self.game_canvas.configure(yscrollcommand=self.game_scrollbar_vertical.set)
        self.game_scrollbar_horizontal = tk.Scrollbar(self.game_frame, orient="horizontal", command=self.game_canvas.xview)
        self.game_scrollbar_horizontal.pack(side='bottom', fill='x')
        self.game_canvas.configure(xscrollcommand=self.game_scrollbar_horizontal.set)
        self.game_canvas.pack(side=LEFT, expand=1, fill=BOTH)
        self.game_frame_scrollable = tk.Frame(self.game_canvas)
        self.game_frame_scrollable.pack(side='top', fill=BOTH, expand=1)
        self.game_canvas.create_window((0,0),window=self.game_frame_scrollable, anchor='nw')
        self.game_frame.bind("<Configure>", self.my_function_game)
        # ---

        # ---
        self.options_frame = tk.LabelFrame(self.main_frame, text='Options', relief="sunken", border=1)
        self.options_frame.pack(side=RIGHT, fill=Y)
        self.options_canvas = tk.Canvas(self.options_frame)
        self.options_canvas.pack(side=LEFT, fill=Y)
        self.options_scrollbar = tk.Scrollbar(self.options_frame, orient="vertical", command=self.options_canvas.yview)
        self.options_scrollbar.pack(side='left', fill=Y)
        self.options_canvas.configure(yscrollcommand=self.options_scrollbar.set)
        self.options_frame_scrollable = tk.Frame(self.options_canvas)
        self.options_frame_scrollable.pack(side='top', fill=BOTH, expand=YES)
        self.options_canvas.create_window((0,0), window=self.options_frame_scrollable, anchor='nw')
        self.options_frame.bind("<Configure>", self.my_function_options)

        self.create_set_of_buttons(self.dict_objects)

        os.environ['SDL_WINDOWID'] = str(self.game_canvas.winfo_id())
        os.environ['SDL_VIDEODRIVER'] = 'windib'

        self.pygame_playground = PygamePlayground(grid_size)

    def get_object_type(self, file_name):
        """
        Returns type of object
        :param file_name: name of file
        :return: type of object
        """
        for dic_item in self.dict_objects:
            if file_name == dic_item[0]:
                return dic_item[3]
        return None

    def printit(self, file_name):
        """
        Print the name of file (image) used for the selected button
        :param file_name:
        :return:
        """
        self.btn_checked = file_name
        print(self.btn_checked)

    def create_set_of_buttons(self, lst_name):
        """
        Toggle buttons are created using RadioButtons
        :param lst_name: list of tuples
        :return:
        """
        self.images = []
        main_dir = 'winter_tile_set/PNG'
        sub_dirs = ['road', 'building', 'decor']

        v2 = tk.IntVar()
        v2.set(0)
        for sub_dir in sub_dirs:
            path = main_dir+'/'+sub_dir+'/icons'
            for file_name, image, order, type in lst_name:
                if type == sub_dir:
                    img = PhotoImage(file=path+'/'+file_name)
                    self.images.append(img)
                    tk.Radiobutton(self.options_frame_scrollable, variable=v2, image=img, indicatoron=0, value=order, command=lambda x=file_name: self.printit(x)).pack(fill="x", padx=5)

    def run(self, grid_size):
        """
        Main method for application running
        :param grid_size: size of a grid tile
        :return:
        """
        self.create_tk_components(grid_size)
        while True:
            selected_object_type = self.get_object_type(self.btn_checked)
            self.pygame_playground.process_event(self.btn_checked, selected_object_type)
            self.pygame_playground.update()
            self.root.update()


if __name__ == '__main__':
    gs = 36
    gf = GameFrame()
    gf.run(gs)


