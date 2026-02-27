import tkinter as tk

#==========Just-The-Tkinter-Stuf============
root = tk.Tk()
root.title("Page")
root.state("zoomed")
root.geometry("850x500")

#======Calculate-Screen-Dementions======
root.update_idletasks()
scr_width = root.winfo_width()
scr_height = root.winfo_height()

#==============Main-Canvas=============
canvas = tk.Canvas(root, width=scr_width, height=scr_height, bg="#f8f8f8")
canvas.pack(side="left", fill="both", expand=True)

#=============Main-Page==============
page = canvas.create_rectangle(scr_width/2-450, 5, scr_width/2+450, 1273, fill="#ffffff", outline="#cbcbcb", width=1)

#=======Scroll-Wheel========
scrollbar = tk.Scrollbar(
    master = root,
    orient = "vertical"
)
canvas.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = canvas.yview)
scrollbar.pack(side="right", fill="y")

input_path = r"C:\Rupanuga\Code\Python\Custom File ext\output.box"

raw_lines = None
num_of_lines = None
def decode():
    #open file
    global raw_lines, num_of_lines
    try:
        with open(input_path, 'r') as f:
            raw_lines = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("Error: Input file not found.")
        return

def cout_lines():
    global raw_lines, num_of_lines
    #legth of file
    num_of_lines = len(raw_lines)

def print_on_page():
    #print on page
    global raw_lines, num_of_lines
    if raw_lines is None or len(raw_lines) == 0:
        return
    y = 30
    for line in raw_lines:
        if line.startswith("3^"):
            canvas.create_text(300, y, text=line[2:], anchor="nw", font=("Arial", 34, "bold"))
            y += 52
        elif line.startswith("2<"):
            canvas.create_text(300, y, text=line[2:], anchor="nw", font=("Arial", 20, "bold"))
            y += 30
        else:
            canvas.create_text(300, y, text=line[2:], anchor="nw", font=("Arial", 12))
            y += 4
        y += 20

decode()
cout_lines()
print_on_page()

#===========Scroll=========
canvas.configure(scrollregion=canvas.bbox("all"))

# Bind mousewheel for scrolling
def _on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", _on_mousewheel)

root.mainloop()
