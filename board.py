import tkinter as tk

root = tk.Tk()

img_png = tk.PhotoImage(file='./img/bg.png')
label_img = tk.Label(root, image=img_png)
label_img.pack()
 
tk.mainloop()