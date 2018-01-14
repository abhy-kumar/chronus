import tkinter as tk

window = tk.Tk()
window.title('Readle')
window.geometry('1000x1000')
title = tk.Label(text = "Welcome, user")
title.grid()
button1 = tk.Button(text = "Please enter your name")
button1.grid()
window.mainloop()