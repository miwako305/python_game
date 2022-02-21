import tkinter
import tkinter.messagebox
import random

key=""

def key_down(e):
    global key
    key = e.keysym

def key_up(e):
    global key
    key = ""

mx=1
my=2
yuka = 0
GOAL =(8,16)
def is_GOAL(py,px):
    if py == GOAL[0] and px == GOAL[1]:
        return True

def is_touch(py,px):
    if py == my and px == mx:
        anna=tkinter.PhotoImage(file="./img/date/gameover.png")
        canvas.create_image(500,400,image=anna)
        label=tkinter.Label(root,text="感極まって、敬之を脱がした！！！",font=("Times NEW Roman",50), bg="white")
        label.place(x=80,y=50)
        anna.update()
        #tkinter.messagebox.showinfo("おめでとう","全て塗った")
        return True
def has_hanami(ey,ex):
    if maze[ey+1][ex] == 3 or maze[ey-1][ex] == 3 or maze[ey][ex-1] == 3 or maze[ey][ex+1] == 3 :
        return True
    else:
        return False
def main_proc():
    global mx,my,key,yuka
    if key == "Shift_L" and yuka == 0:
        mx=1
        my=1
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
    if is_GOAL(my, mx):
        canvas.delete("MYCHR")
        anna=tkinter.PhotoImage(file="./img/date/cofee_now.png")
        canvas.create_image(500,400,image=anna)
        label=tkinter.Label(root,text="コーヒうまい！！！",font=("Times NEW Roman",50), bg="white")
        label.place(x=80,y=50)
        canvas.update()
        tkinter.messagebox.showinfo("おめでとう","愛してる")

    if maze[my][mx] == 0:
        canvas.coords("MYCHR",mx*80+40,my*80+40)
    root.after(300, main_proc)
ex1=5
ey1=7
ex2=6
ey2=0
ex3=10
ey3=5
ex4=15
ey4=0
ex5=15
ey5=4
def enemy_proc1():
    global ey1,ex1
    (ey1,ex1)= goto("ENCHR1",ey1,ex1)
    if has_hanami(ey1,ex1):
        root.after(1200, enemy_proc1)
    else:
        root.after(1000, enemy_proc1)

def enemy_proc2():
    global ey2,ex2
    (ey2,ex2)= goto("ENCHR2",ey2,ex2)
    if has_hanami(ey2,ex2):
        root.after(1100, enemy_proc2)
    else:
        root.after(900, enemy_proc2)

def enemy_proc3():
    global ey3,ex3
    (ey3,ex3)= goto("ENCHR3",ey3,ex3)
    if has_hanami(ey3,ex3):
        root.after(900, enemy_proc3)
    else:
        root.after(700, enemy_proc3)
def enemy_proc4():
    global ey4,ex4
    (ey4,ex4)= goto("ENCHR4",ey4,ex4)
    if has_hanami(ey4,ex4):
        root.after(800, enemy_proc4)
    else:
        root.after(600, enemy_proc4)
def enemy_proc5():
    global ey5,ex5
    (ey5,ex5)= goto("ENCHR5",ey5,ex5)
    if has_hanami(ey5,ex5):
        root.after(700, enemy_proc5)
    else:
        root.after(500, enemy_proc5)

def touch_proc():
    is_touch(ey1,ex1)
    is_touch(ey2,ex2)
    is_touch(ey3,ex3)
    is_touch(ey4,ex4)
    is_touch(ey5,ex5)
    root.after(100, touch_proc)

def goto(tagtype,ey,ex):
    while True:
        x_pos= random.randint(-1,1)
        y_pos= random.randint(-1,1)
        if maze[ey + y_pos][ex + x_pos] == 0 :
            ey = ey + y_pos
            ex = ex + x_pos
            break
    canvas.coords(tagtype,ex*80+40,ey*80+40)
    return ey,ex



root = tkinter.Tk()
root.title("お花見散歩ー")
root.bind("<KeyPress>",key_down)
root.bind("<KeyRelease>",key_up)

canvas = tkinter.Canvas(width=1620, height=860, bg="beige")
canvas.pack()

x=0
y=0
maze=[
[1,1,1,1,3,1,1,1,1,1,1,3,1,1,1,1,1,1],
[1,3,0,0,1,3,0,0,1,0,0,0,0,0,0,1,3,1],
[1,0,0,0,0,3,0,0,0,0,0,0,0,3,3,0,1,1],
[1,0,0,0,0,0,0,0,0,0,1,3,0,0,0,0,0,1],
[3,0,3,0,0,0,0,0,0,0,0,1,3,0,0,0,3,1],
[3,0,1,0,0,3,3,3,0,0,0,3,3,1,0,0,3,1],
[1,0,3,0,0,1,3,0,0,3,0,3,1,0,0,0,0,1],
[1,0,3,3,0,0,0,0,0,1,0,0,0,0,1,0,0,1],
[1,1,1,3,3,0,3,1,3,1,3,0,1,1,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,3,1,3,1,1,1],
]
yuka=0
tree = tkinter.PhotoImage(file="./img/date/s_tree.png").subsample(4, 4)
goal = tkinter.PhotoImage(file="./img/date/tatemono_cafe.png").subsample(4, 4)
picnic_img = tkinter.PhotoImage(file="./img/date/picnic_couple.png").subsample(8, 8)
enemy_img =tkinter.PhotoImage(file="./img/date/couple_nakaii_hug.png").subsample(8, 8)
player_img =tkinter.PhotoImage(file="./img/date/datetaka.png").subsample(4, 4)


for y in range(10):
    for x in range(18):
        if maze[y][x] == 1 or maze[y][x] == 3:
            canvas.create_rectangle(x*80,y*80,x*80+80,y*80+80,fill="lightgreen",width=0)
            if maze[y][x] == 3:
                canvas.create_image(x*80+40,y*80+40, image=tree,tag="TREE")
canvas.create_image(mx*80+40,my*80+40, image=player_img,tag="MYCHR")
canvas.create_image(ex1*80+40,ey1*80+40, image=enemy_img,tag="ENCHR1")
canvas.create_image(ex2*80+40,ey2*80+40, image=enemy_img,tag="ENCHR2")
canvas.create_image(ex3*80+40,ey3*80+40, image=enemy_img,tag="ENCHR3")
canvas.create_image(ex4*80+40,ey4*80+40, image=enemy_img,tag="ENCHR4")
canvas.create_image(ex4*80+40,ey4*80+40, image=enemy_img,tag="ENCHR5")
canvas.create_image(GOAL[1]*80+50,GOAL[0]*80+50, image=goal,tag="GOAL")
canvas.create_image(1*80+50,8*80+50, image=picnic_img,tag="GOAL")
main_proc()
enemy_proc1()
enemy_proc2()
enemy_proc3()
enemy_proc4()
enemy_proc5()
touch_proc()
root.mainloop()
