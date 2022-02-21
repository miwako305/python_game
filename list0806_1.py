import tkinter
import tkinter.messagebox

key=""

def key_down(e):
    global key
    key = e.keysym

def key_up(e):
    global key
    key = ""

mx=1
my=1
yuka = 0
def main_proc():
    global mx,my,key,yuka
    if key == "Shift_L" and yuka == 0:
        mx=1
        my=1
        canvas.delete("PAINT")
        for y in range(7):
            for x in range(11):
                if maze[y][x] == 2:
                    maze[y][x] = 0
                else:
                    yuka = yuka + 1
    if key == "Up" and maze[my-1][mx] == 0:
        my = my - 1
    if key == "Down" and maze[my+1][mx] ==0:
        my = my + 1
    if key == "Right" and maze[my][mx + 1] == 0:
        mx = mx + 1
    if key == "Left" and maze[my][mx -1] == 0:
        mx = mx - 1
    if maze[my][mx] == 0:
        maze[my][mx] = 2
        canvas.create_rectangle(mx*80,my*80,mx*80+80,my*80+80,fill="pink",width=0,tag="PAINT")
        canvas.delete("MYCHR")
        canvas.create_image(mx*80+40,my*80+40, image=img,tag="MYCHR")
        yuka = yuka - 1
        if yuka == 0:
            canvas.update()
            tkinter.messagebox.showinfo("おめでとう","全て塗った")
    canvas.coords("MYCHR",mx*80+40,my*80+40) #cordは新しい位置
    root.after(300, main_proc)

root = tkinter.Tk()
root.title("迷路をぬるにゃん")
root.bind("<KeyPress>",key_down)
root.bind("<KeyRelease>",key_up)

canvas = tkinter.Canvas(width=800, height=560, bg="white")
canvas.pack()

x=0
y=0
maze=[
[1,1,1,1,1,1,1,1,1,1,1],
[1,0,1,1,1,1,1,1,1,1,1],
[1,0,1,1,1,1,1,1,1,1,1],
[1,0,0,1,1,1,1,1,1,1,1],
[1,0,0,1,1,1,1,1,1,1,1],
[1,0,0,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1],
]
yuka=0
for y in range(7):
    for x in range(11):
        if maze[y][x] == 1:
            canvas.create_rectangle(x*80,y*80,x*80+80,y*80+80,fill="skyblue",width=0)
        else:
            yuka = yuka + 1
img =tkinter.PhotoImage(file="./img/mimi_s.png")
canvas.create_image(mx*80+40,my*80+40, image=img,tag="MYCHR")
main_proc()
root.mainloop()
