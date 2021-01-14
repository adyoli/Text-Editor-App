import tkinter.filedialog as fd
from tkinter import Menu, Scrollbar, Text, Tk
import tkinter as tk

class TextEditor():

    """
    This Class is where we will build our text editor app
    """

    def __init__(self,window):
        self.window = window        #store our window object
        window.title("Text Editor") #give out editor a title
        window.minsize(500,500)     #give dimensions to our editor
        menu_bar = Menu(self.window)
        menu_bar.add_command(label='Open',command=self.open_file)
        menu_bar.add_command(label = 'Edit', command = window.quit())
        menu_bar.add_command(label = 'Format',command = None)
        menu_bar.add_command(label = 'View',command = None)
        menu_bar.add_command(label = 'Help', command = window.quit())
        menu_bar.add_command(label = 'Web Search',command = None)

        self.scrollbar = Scrollbar(window)
        self.scrollbar.pack(side=tk.RIGHT,fill=tk.Y) 
        self.text_area = Text(window,yscrollcommand=self.scrollbar.set)
        self.text_area.pack(expand=True,fill=tk.BOTH)

        self.window.config(menu = menu_bar)
        self.scrollbar.config(command=self.text_area.yview)
    
        
    def open_file(self):
        """
        Opening a file to edit.
        """
        filepath =fd.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not filepath:
            return
        self.text_area.delete(1.0, tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            self.text_area.insert(tk.END, text)
        window.title(f"Text Editor - {filepath}")

    def save_file(self):
        pass


    def run(self):
        """
        This method deals with the main loop to run our app
        """
        self.window.mainloop()


if __name__ == '__main__':
    window = Tk()
    text_editor = TextEditor(window) #instanciate the text editor
    text_editor.run()          #run the main loop for the editor
