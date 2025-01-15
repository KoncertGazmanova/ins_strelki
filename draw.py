# draw.py
# Интерфейс для рисования
import tkinter as tk

def launch_drawing_app():
    window = tk.Tk()
    window.title("Рисование")
    canvas = tk.Canvas(window, width=300, height=300, bg="white")
    canvas.pack()

    def draw(event):
        x, y = event.x, event.y
        canvas.create_oval(x, y, x+2, y+2, fill="black")

    canvas.bind("<B1-Motion>", draw)
    window.mainloop()
