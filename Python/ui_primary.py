import tkinter as tk

LARGE_FONT = ("Segoe UI Light", 42)


class rss_core(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne):
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
        tk.Frame.__init__(self, parent, bg='Grey')
        label = tk.Label(self, text="Hi!", font=LARGE_FONT, bg='Grey')
        label.pack(pady=10, padx=10)
        entry1 = tk.Entry(self)
        entry1.pack()

        s = entry1.get()

        button1 = tk.Button(self, text='Confirm', command=lambda: controller.show_frame(PageOne))
        button1.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Hi!, user", font=LARGE_FONT, bg='Grey')
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text='Back', command=lambda: controller.show_frame(StartPage))

        button1.pack()

app = rss_core()
app.mainloop()
