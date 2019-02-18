import tkinter as tk
import re

window = tk.Tk()
window.title('my window')
window.geometry('400x400')
# e = tk.Entry(window, show="*")
text_entry = tk.Entry(window)
reg_entry = tk.Entry(window)
text_entry.pack()
reg_entry.pack()
t = tk.Text(window, height=2)
t.pack()

def reg():
    key = text_entry.get()
    p1 = re.compile(reg_entry.get())
    pattern = re.compile(p1)
    matcher = re.search(pattern, key)
    t.insert(1.0,matcher.group(0))



button = tk.Button(window, text='R!', width=15,
              height=2,command=reg)
button.pack()



window.mainloop()