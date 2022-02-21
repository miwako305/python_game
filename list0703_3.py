import tkinter

def check():
    if cval.get()==True:
        print("チックされています")
    else:
        print("チェックされていません")

root=tkinter.Tk()
root.title("チェックボックスの状態をしる")
root.geometry("400x200")
cval=tkinter.BooleanVar()
cval.set(False)
cbtn=tkinter.Checkbutton(text="チェックボタ",variable=cval,command=check)
cbtn.pack()
root.mainloop()
