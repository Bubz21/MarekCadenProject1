from Area_Gui import *


def main():
    window = Tk()
    window.title('Area Solver')
    window.geometry('500x500')
    window.resizable(False, False)

    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
