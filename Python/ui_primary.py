import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk

font_x = ("Segoe UI Light", 32)


class rss_core(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #icon changes here:
        tk.Tk.iconbitmap(self, 'iconbeta.png')
        #title changes here:
        tk.Tk.wm_title(self, 'Chronus')

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Add Frame list here:
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
        
        f = Figure(figsize = (5,5), dpi=120)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7],[9,3,3,3,2,2,2])
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        

app = rss_core()
app.mainloop()
