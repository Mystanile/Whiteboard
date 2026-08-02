import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter import ttk

BG = "#1e1e24" #toolbar
SURFACE = "#2c2c35" #buttons, one step above the toolbar
HOVER = "#3a3a46" #one step above that
FG = "#e8e8ec" #text
ACCENT = "#5b8def"
ACCENT_HOVER = "#6f9bf2"
ACCENT_PRESSED = "#4a76c9"
FONT = ("Segoe UI", 10)

def start_drawing(event):
    global is_drawing, prev_x, prev_y
    is_drawing = True
    prev_x, prev_y = event.x, event.y
def draw(event):
    global is_drawing, prev_x, prev_y
    if is_drawing:
        current_x, current_y = event.x, event.y
        canvas.create_line(prev_x, prev_y, current_x, current_y, fill=drawing_color, width=line_width, capstyle=tk.ROUND)
        prev_x, prev_y = current_x, current_y
def stop_drawing(event):
    global is_drawing
    is_drawing = False
def change_pen_color():
    global drawing_color
    color = askcolor()[1]
    if color:
        drawing_color = color
def change_line_width(value):
    global line_width
    line_width = int(float(value))

root = tk.Tk()
root.title("Mystanile's Whiteboard")
root.geometry("800x600")

style = ttk.Style()
style.theme_use("clam")
style.configure("Tool.TButton", background=SURFACE, foreground=FG, borderwidth=0, focuscolor=SURFACE,
                lightcolor=SURFACE, darkcolor=SURFACE, bordercolor=SURFACE, padding=(14,8), font=FONT)
style.map("Tool.TButton",
          background=[("active", HOVER), ("pressed", ACCENT)],
          lightcolor=[("active", HOVER), ("pressed", ACCENT)],
          darkcolor=[("active", HOVER), ("pressed", ACCENT)])

style.configure("Accent.TButton", background=ACCENT, foreground="#ffffff", borderwidth=0, focuscolor=ACCENT,
                lightcolor=ACCENT, darkcolor=ACCENT, bordercolor=ACCENT, padding=(14,8), font=FONT)
style.map("Accent.TButton",
          background=[("active", ACCENT_HOVER), ("pressed", ACCENT_PRESSED)],
          lightcolor=[("active", ACCENT_HOVER), ("pressed", ACCENT_PRESSED)],
          darkcolor=[("active", ACCENT_HOVER), ("pressed", ACCENT_PRESSED)])

is_drawing = False
drawing_color = "black"
line_width = 2

controls_frame = tk.Frame(root, bg=BG, padx=12, pady=8)
controls_frame.pack(side="top", fill="x")
color_button = ttk.Button(controls_frame, text="Color", style="Accent.TButton", command=change_pen_color)
clear_button = ttk.Button(controls_frame, text="Clear Canvas", style="Tool.TButton",  command=lambda: canvas.delete("all"))
color_button.pack(side="left", padx=5, pady=5)
clear_button.pack(side="left", padx=5, pady=5)

line_width_label = tk.Label(controls_frame, bg=BG, fg=FG, font=FONT, text="Line Width:")
line_width_label.pack(side="left", padx=5, pady=5)
line_width_slider = tk.Scale(controls_frame,bg=BG, fg=FG, troughcolor=HOVER, highlightthickness=0, bd=0, font=FONT, from_=1, to=10, orient="horizontal", command=change_line_width)
line_width_slider.set(line_width)
line_width_slider.pack(side="left", padx=5, pady=5)

tk.Frame(root, height=1, bg="#33333d").pack(side="top", fill="x")

canvas = tk.Canvas(root, bg="white", highlightthickness=0)
canvas.pack(fill="both", expand=True)

canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stop_drawing)

root.mainloop()

