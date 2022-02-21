import tkinter
root = tkinter.Tk()
KEKKA=[
"特別、おかしなところはありません",
"ややねこっぽいです。",
"猫に近い性格のようです",
"猫にかなり近い性格です",
"前世は猫だったかもしれません",
"見た目は人間、中身は猫の可能性があります",
"夜元気になる"
]
def click_btn():
    pts=0
    for i in range(7):
        if bvar[i].get() == True:
            pts = pts + 1
    nekodo = int(100*pts/7)
    text.delete("1.0",tkinter.END)
    text.insert("1.0","チェックの数は" + str(nekodo) + "%です\n" + KEKKA[pts])


root.resizable(False,False)
canvas=tkinter.Canvas(root,width=800,height=600)
canvas.pack()
gazou=tkinter.PhotoImage(file="./img/sumire.png")
canvas.create_image(400,300,image=gazou)
button=tkinter.Button(text="診断する",font=("Times New Roman",32), bg="Lightgreen", command=click_btn)
button.place(x=400,y=480)
text=tkinter.Text(width=40,height=5,font=("Times New Roman",16))
text.place(x=320,y=30)

bvar=[None]*7
cbtn=[None]*7
ITEM=[
"高いところが好き",
"ボールを見ると転がしたくなる",
"びっくりすると髪の毛がたつ",
"ネズミの玩具が気になる",
"匂いに敏感",
"魚の骨をしゃぶりたくなる",
"夜元気になる"
]
for i in range(7):
    bvar[i]= tkinter.BooleanVar()
    bvar[i].set(False)
    cbtn[i]=tkinter.Checkbutton(text=ITEM[i],font=("Times New Roman",6), variable=bvar[i],bg="#dfe")
    cbtn[i].place(x=400,y=160+40*i)

root.mainloop()
