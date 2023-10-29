import tkinter

class Gui:
    def __init__(self):
        self.root = tkinter.Tk()
        self.frm = ttk.Frame(root, padding=10)
        self.frm.grid()
        ttk.Label(self.frm, text="Hello World!").grid(column=0, row=0)
        ttk.Button(frm, text="Quit", command=self.root.destroy).grid(column=1, row=0)
        self.root.mainloop()

if __name__ == '__main__':
    gui = Gui()