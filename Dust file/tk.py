import tkinter as tk
root = tk.Tk()
root.title("My First Tkinter App")
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

list = [2, 4, 5, 6]

button = tk.Button(root, text=f"Click Me,", command=lambda: print(f" is Clicked!"))
button.pack()
root.mainloop()