import tkinter
root = tkinter.Tk()
root.title("チェックボックスを扱う")
root.geometry("400x200")
cval=tkinter.BooleanVar()
cval.set(True)
cbtn=tkinter.Checkbutton(text="チェックボタン",variable=cval)
cbtn.pack()
root.mainloop()
