from cefpython3 import cefpython as cef
import platform
import sys
from tkinter import *
import tkinter as tk
class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.widgets()
        master.minsize(600,400)

    def file_menu(self):
        pass

    def widgets(self):
        #label.grid(row=0)
        entry = Entry(self.master)

        # Menu items
        menubar = Menu(self.master)
        menubar.add_command(label = 'File',command = self.file_menu())
        menubar.add_command(label = 'Edit', command = window.quit())
        menubar.add_command(label = 'Format',command = self.file_menu())
        menubar.add_command(label = 'View',command = self.file_menu())
        menubar.add_command(label = 'Help', command = window.quit())
        menubar.add_command(label = 'Web Search',command = self.file_menu())
        #self.main()
        #window.config(menu = menubar)

        ###############################
        #self.scrollbar = Scrollbar(self.master)
        #self.scrollbar.grid(row=0, column=1, sticky='ns')
        #self.text_area = Text(self.master,yscrollcommand=self.scrollbar.set)
        #self.text_area.grid()


        ######
        vsb = tk.Scrollbar(self.master, orient="vertical")
        self.text_area = Text(self.master,yscrollcommand=vsb.set)

        self.text_area.grid()
        vsb.grid(row=0, column=1, sticky='ns')
        self.text_area.configure(yscrollcommand=vsb.set)
        ########
        vsb.config(command=self.text_area.yview)

        window.config(menu = menubar)
        ###############################
        self.main()
    
    ###########################################################################

    def open_link(self,url):
        print(url)
        root = self.master
        root.destroy()
        sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
        cef.Initialize()
        cef.CreateBrowserSync(url=url,
        window_title=url)
        cef.MessageLoop()
        self.main()

    def main(self):
        root = self.master
        root.geometry("400x100")
        l = tk.Label(root, text="Press Enter to browse Internet", fg="blue", font="Arial 20")
        l.grid()
        v = tk.StringVar()
        e = tk.Entry(root, textvariable=v, font="Arial 14")
        e.grid()
        v.set("https://www.google.com/")
        e.focus()
        e.bind("<Return>", lambda x: self.open_link(e.get()))
        root.mainloop()
        cef.Shutdown()


    ##############################################

if __name__ == '__main__':
    window = Tk()
    window.title('Text Editor')
    app = App(window)
    window.mainloop()
