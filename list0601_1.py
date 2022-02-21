import tkinter
def click_btn():
    button["text"]="クリックしました。"

root=tkinter.Tk()
root.title("初めてのウィンドウ")
root.geometry("800x600")
#ラベル
label =tkinter.Label(root,text="text system24",font=("System",24))
# bボタn
button = tkinter.Button(root,text="ボタン",font=("Times New Roman",24),command=click_btn)
label.place(x=40,y=500)
button.place(x=50,y=400)
root.mainloop()
