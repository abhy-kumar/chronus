import tkinter as tk
from tkinter import ttk

font_x = ("Segoe UI Light", 42)


class rss_core(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Hi!", font=font_x)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Page One', command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button1 = ttk.Button(self, text='Page Two', command=lambda: controller.show_frame(PageTwo))
        button1.pack()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Hi!, user", font=font_x)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Home', command=lambda: controller.show_frame(StartPage))
        button1.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is PageTwo", font=font_x)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Home', command=lambda: controller.show_frame(StartPage))
        button1.pack()

        

app = rss_core()
app.mainloop()
