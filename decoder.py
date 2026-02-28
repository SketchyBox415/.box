import tkinter as tk

#==========Just-The-Tkinter-Stuf============
root = tk.Tk()
root.title("Page")
root.state("zoomed")

#======Calculate-Screen-Dimensions======
scr_width = root.winfo_screenwidth()
scr_height = root.winfo_screenheight()

#=======Scroll-Wheel========
scrollbar = tk.Scrollbar(
    master = root,
    orient = "vertical"
)
scrollbar.pack(side="right", fill="y")

#==============Main-Canvas=============
canvas = tk.Canvas(root, width=scr_width, height=scr_height, bg="#f8f8f8", yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.config(command = canvas.yview)

#=============Main-Page==============
root.update()  # Force window to render
page = canvas.create_rectangle(scr_width/2-450, 10, scr_width/2+450, 1273, fill="#ffffff", outline="#cbcbcb", width=1)

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
    y = 60
    for line in raw_lines:
        center = scr_width/2 - len(line)/2
        left = 300 # Adjust this value based on your needs
        if line[0] == "3":
            if line[1] == "^":
                canvas.create_text(center, y, text=line[2:], anchor="center", font=("Space Mono", 34 , "bold"))
            else:
                canvas.create_text(left, y, text=line[2:], anchor="nw", font=("Space Mono", 34, "bold"))
            y += 52
        elif line[0] == "2":
            if line[1] == "^":
                canvas.create_text(center, y, text=line[2:], anchor="center", font=("Space Mono", 20, "bold"))
            else:
                canvas.create_text(left, y, text=line[2:], anchor="nw", font=("Space Mono", 20, "bold"))
            y += 30
        else:
            if line[1] == "^":
                canvas.create_text(center, y, text=line[2:], anchor="center", font=("Space Mono", 13))
            else:
                canvas.create_text(left, y, text=line[2:], anchor="nw", font=("Space Mono", 13))
            y += 10
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
