from tkinter import *
from caden_marek_area import *


class GUI:
    """
    A class that uses tkinter to create a GUI for the user
    """
    def __init__(self, window):
        """
        A Constructor to create an initial window layout that has frames, label, entry, and button widgets within it
        :param window: Creates the window and allows objects to be placed within the window
        """
        self.window = window
        """
        There are 5 different frames in the window each are listed in order from top to bottom 
        :param frame_shape: The first frame that holds a label that has text
        :param frame_selection: The second frame that has 4 buttons each with a different shape
        :param frame_options: The third frame holds labels and entries for the corresponding shape selected
        :param frame_text: The fourth frame shows text saying the answer or error when the Compute button is pressed
        :param frame_compute: The last frame that contains the button Compute 
        """
        self.frame_shape = Frame(self.window, bg='black')
        self.frame_shape.pack(anchor='w', fill='both', expand=True)
        self.frame_selection = Frame(self.window, bg='black')
        self.frame_selection.pack(anchor='w', fill='both', expand=True)
        self.frame_options = Frame(self.window, bg='black')
        self.frame_options.pack(anchor='w', fill='both', expand=True)
        self.frame_text = Frame(self.window, bg='black')
        self.frame_text.pack(side='bottom', fill='both', expand=True)
        self.frame_compute = Frame(self.window, bg='black')
        self.frame_compute.pack(side='bottom', fill='both', expand=True)

        # This label is in frame_shape and displays text to the user saying 'Select a Shape'
        self.label_title = Label(self.frame_shape, text='Select a Shape', font=("Times New Roman", 40, 'bold'),
                                 fg='White', bg='Black')
        self.label_title.pack(side='top', pady=20)

        # Buttons below are selected to choose which area you want to compute
        self.button_circle = Button(self.frame_selection, text='Circle', command=self.press_button_circle, width=8)
        self.button_rectangle = Button(self.frame_selection, text='Rectangle', command=self.press_button_rectangle,
                                       width=8)
        self.button_square = Button(self.frame_selection, text='Square', command=self.press_button_square, width=8)
        self.button_triangle = Button(self.frame_selection, text='Triangle', command=self.press_button_triangle,
                                      width=8)
        self.button_circle.pack(side='left', padx=30)
        self.button_rectangle.pack(side='left', padx=30)
        self.button_square.pack(side='left', padx=30)
        self.button_triangle.pack(side='left', padx=30)

        # Label for circle where you enter the radius
        self.label_options_circle = Label(self.frame_options, text='Radius', bg='black', fg='white')
        self.label_options_circle.pack(side='left')
        self.entry_circle = Entry(self.frame_options, width=10)
        self.label_options_circle.pack_forget()
        self.entry_circle.pack_forget()

        # Label and entry for area of rectangles you can enter values
        self.label_options_length = Label(self.frame_options, text='length (top)', bg='black', fg='white')
        self.label_options_length.pack(side='left')
        self.entry_rectangle_length = Entry(self.frame_options, width=10)
        self.label_options_width = Label(self.frame_options, text='width (bottom)', bg='black', fg='white')
        self.label_options_width.pack(side='left')
        self.entry_rectangle_width = Entry(self.frame_options, width=10)
        self.label_options_length.pack_forget()
        self.label_options_width.pack_forget()
        self.entry_rectangle_length.pack_forget()
        self.entry_rectangle_width.pack_forget()

        # Label and entry for area of squares you can enter the side value
        self.label_options_side = Label(self.frame_options, text='Side', bg='black', fg='white')
        self.label_options_side.pack(side='top')
        self.entry_square = Entry(self.frame_options, width=10)
        self.frame_options.pack(anchor='w')
        self.label_options_side.pack_forget()
        self.entry_square.pack_forget()

        # Label and entry for area of triangles you can enter values
        self.label_options_base = Label(self.frame_options, text='Base (top)', bg='black', fg='white')
        self.label_options_base.pack(side='top')
        self.entry_triangle_base = Entry(self.frame_options, width=10)
        self.label_options_height = Label(self.frame_options, text='height (bottom)', bg='black', fg='white')
        self.label_options_height.pack(side='top')
        self.entry_triangle_height = Entry(self.frame_options, width=10)
        self.label_options_base.pack_forget()
        self.label_options_height.pack_forget()
        self.entry_triangle_base.pack_forget()
        self.entry_triangle_height.pack_forget()

        # Label where the answer is displayed
        self.label_answer = Label(self.frame_text, width=50, bg='black', fg='white')
        self.label_answer.pack(side='top')

        # Pressing the compute button gets you the answer
        self.button_answer = Button(self.frame_compute, text="Compute", command=self.press_button_compute)
        self.button_answer.pack(side='top')

    # When you click circle only the circle labels will appear
    def press_button_circle(self):
        self.label_options_circle.pack()
        self.entry_circle.pack()

        self.label_options_length.pack_forget()
        self.label_options_width.pack_forget()
        self.entry_rectangle_length.pack_forget()
        self.entry_rectangle_width.pack_forget()
        self.label_options_side.pack_forget()
        self.entry_square.pack_forget()
        self.label_options_base.pack_forget()
        self.label_options_height.pack_forget()
        self.entry_triangle_base.pack_forget()
        self.entry_triangle_height.pack_forget()

        # removes the input from other entries
        self.entry_rectangle_width.delete(0, END)
        self.entry_rectangle_length.delete(0, END)
        self.entry_square.delete(0, END)
        self.entry_triangle_height.delete(0, END)
        self.entry_triangle_base.delete(0, END)

    # When you click rectangle only the rectangle labels will appear
    def press_button_rectangle(self):
        self.label_options_length.pack()
        self.label_options_width.pack()
        self.entry_rectangle_length.pack()
        self.entry_rectangle_width.pack()

        self.label_options_circle.pack_forget()
        self.entry_circle.pack_forget()
        self.label_options_side.pack_forget()
        self.entry_square.pack_forget()
        self.label_options_base.pack_forget()
        self.label_options_height.pack_forget()
        self.entry_triangle_base.pack_forget()
        self.entry_triangle_height.pack_forget()

        # removes the input from other entries
        self.entry_circle.delete(0, END)
        self.entry_square.delete(0, END)
        self.entry_triangle_height.delete(0, END)
        self.entry_triangle_base.delete(0, END)

    # When you click square only the square labels will appear
    def press_button_square(self):
        self.label_options_side.pack()
        self.entry_square.pack()

        self.label_options_length.pack_forget()
        self.label_options_width.pack_forget()
        self.entry_rectangle_length.pack_forget()
        self.entry_rectangle_width.pack_forget()
        self.label_options_circle.pack_forget()
        self.entry_circle.pack_forget()
        self.label_options_base.pack_forget()
        self.label_options_height.pack_forget()
        self.entry_triangle_base.pack_forget()
        self.entry_triangle_height.pack_forget()

        # removes the input from other entries
        self.entry_rectangle_width.delete(0, END)
        self.entry_rectangle_length.delete(0, END)
        self.entry_circle.delete(0, END)
        self.entry_triangle_height.delete(0, END)
        self.entry_triangle_base.delete(0, END)

    # When you click triangle only the triangle labels will appear
    def press_button_triangle(self):
        self.label_options_base.pack()
        self.label_options_height.pack()
        self.entry_triangle_base.pack()
        self.entry_triangle_height.pack()

        self.label_options_side.pack_forget()
        self.entry_square.pack_forget()
        self.label_options_length.pack_forget()
        self.label_options_width.pack_forget()
        self.entry_rectangle_length.pack_forget()
        self.entry_rectangle_width.pack_forget()
        self.label_options_circle.pack_forget()
        self.entry_circle.pack_forget()

        # removes the input from other entries
        self.entry_rectangle_width.delete(0, END)
        self.entry_rectangle_length.delete(0, END)
        self.entry_square.delete(0, END)
        self.entry_circle.delete(0, END)

    # when pressed it gets the information from the entries and then gets the answer
    def press_button_compute(self):
        circle_compute = self.entry_circle.get()
        rectangle_compute = self.entry_rectangle_width.get()
        rectangle_compute1 = self.entry_rectangle_length.get()
        square_compute = self.entry_square.get()
        triangle_compute = self.entry_triangle_base.get()
        triangle_compute1 = self.entry_triangle_height.get()
        # determines which one to compute
        if circle_compute != '':
            answer_circle = area_circle(int(circle_compute))
            self.label_answer.configure(text=answer_circle)
        elif (rectangle_compute != '') and (rectangle_compute1 != ''):
            answer_rectangle = area_rectangle(int(rectangle_compute1), int(rectangle_compute))
            self.label_answer.configure(text=answer_rectangle)
        elif square_compute != '':
            answer_square = area_square(int(square_compute))
            self.label_answer.configure(text=answer_square)
        elif (triangle_compute != '') and (triangle_compute1 != ''):
            answer_triangle = area_triangle(int(triangle_compute), int(triangle_compute1))
            self.label_answer.configure(text=answer_triangle)
