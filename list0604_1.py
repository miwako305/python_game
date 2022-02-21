import tkinter
root=tkinter.Tk()
root.title("hogehoge")
canvas=tkinter.Canvas(root,width=400,height=600,bg="skyblue")
canvas.pack()
gazou=tkinter.PhotoImage(file="./img/iroha.png")
canvas.create_image(200,300,image=gazou)
root.mainloop()
