import tkinter
import random
def click_btn():
    label["text"]=random.choice(["大吉","中吉","小吉","凶"])
    label.update()

root = tkinter.Tk()
root.title("omikuji")
root.resizable(False,False)
canvas=tkinter.Canvas(root,width=800, height=600)
canvas.pack()
path = ra
gazou=tkinter.PhotoImage(file="./img/miko.png")
canvas.create_image(400,300,image=gazou)
label=tkinter.Label(root,text="? ?",font=("Times NEW Roman",120), bg="white")
label.place(x=380,y=60)
button=tkinter.Button(root,text="おみくじを引く",font=("Times New Roman",36),command=click_btn,fg="skyblue")
button.place(x=360,y=400)
root.mainloop()
