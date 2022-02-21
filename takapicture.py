import tkinter
import random
img_path="2"
no=""
GONE=["1","11","3","5","20","21","7","18","27","26"]
NOMEN="2"
def click_btn():
    button.place(x=-80,y=-50)
    anser_gone_button.place(x=160,y=700)
    anser_goto_button.place(x=650,y=700)
    anser_gone_button["text"]="行ったね❤️"
    anser_goto_button["text"]="行こうね❤️"
    global img_path
    global no
    no = str(random.randint(1,21)+random.randint(0,2)+random.randint(0,1))

    img_path = "./img/meshi/ramen" + no + ".png"
    print(img_path)
    gazou=tkinter.PhotoImage(file=img_path)
    canvas.create_image(400,400,image=gazou)
    #gazou["file"]=img_path
    anser_gone_button.update()
    anser_goto_button.update()
    gazou.update()
    button.update()


def click_anser_btn_no():
    anser_gone_button.place(x=160,y=-700)
    anser_goto_button.place(x=650,y=-700)
    button.place(x=220,y=300)
    global no
    global img_path
    for i in GONE:
        if i == no:
            result="....はい？私に興味ないんだ。。。。？"
            break
        else:
            result="そうだね❤️次のラー写真見て見て❤️？"
        if no == "":
            result="....始めます ここ押してください"
    button["text"]=result
    anser_gone_button.update()
    anser_goto_button.update()
    button.update()

def click_anser_btn_yes():
    global no
    global img_path
    anser_gone_button.place(x=160,y=-700)
    anser_goto_button.place(x=650,y=-700)
    button.place(x=220,y=300)
    for i in GONE:
        if i == no:
            result="そうだね❤️次のラーメン写真覚えてる？"
            break
        else:
            result="....はい？誰と？。。。。次のラーメン写真覚えてる？"
    if no == NOMEN:
        result="....うどんだよ！！！！！次のラーメンは？"
    if no == "":
        result="自信まんまんね！！！！もう！"
    button["text"]=result
    button.update()
    anser_gone_button.update()
    anser_goto_button.update()


root = tkinter.Tk()
root.title("行ったラーメン店かどうかを思い出すだけのクイズ")
root.resizable(False,False)
canvas=tkinter.Canvas(root,width=1180, height=900)
canvas.pack()
anna=tkinter.PhotoImage(file="./img/meshi/donokurai.png")
canvas.create_image(550,450,image=anna)
label=tkinter.Label(root,text="一緒に行ったラーメン屋さんを覚えてますか！！",font=("Times NEW Roman",50), bg="white")
label.place(x=80,y=50)
button=tkinter.Button(root,text="",font=("Times New Roman",36),command=click_btn)
button.place(x=-500,y=450)
anser_gone_button=tkinter.Button(root,text="A.もちろんだよ",font=("Times New Roman",36),command=click_anser_btn_yes,fg="skyblue")
anser_gone_button.place(x=160,y=700)
anser_goto_button=tkinter.Button(root,text="A.忙しいんだけど",font=("Times New Roman",36),command=click_anser_btn_no,fg="skyblue")
anser_goto_button.place(x=650,y=700)

root.mainloop()
