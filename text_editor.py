from tkinter import Menu, Scrollbar, Text, Tk
from tkinter import *

class TextEditor():

    """
    This Class is where we will build our text editor app
    """

    def __init__(self,window):
        self.window = window        #store our window object
        window.title("Text Editor") #give out editor a title
        window.minsize(500,500)     #give dimensions to our editor
        menu_bar = Menu(self.window)
        menu_bar.add_command(label='File',command=None)
        menu_bar.add_command(label = 'Edit', command = window.quit())
        menu_bar.add_command(label = 'Format',command = None)
        menu_bar.add_command(label = 'View',command = None)
        menu_bar.add_command(label = 'Help', command = window.quit())
        menu_bar.add_command(label = 'Web Search',command = None)

        self.scrollbar = Scrollbar(window)
        self.scrollbar.pack(side=RIGHT,fill=Y) 
        text_area = Text(window,yscrollcommand=self.scrollbar.set)
        text_area.pack(expand=True,fill=BOTH)

        self.window.config(menu = menu_bar)
        self.scrollbar.config(command=text_area.yview)

    def run(self):
        """
        This method deals with the main loop to run our app
        """
        self.window.mainloop()


if __name__ == '__main__':
    window = Tk()
    text_editor = TextEditor(window) #instanciate the text editor
    text_editor.run()          #run the main loop for the editor
