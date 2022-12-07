from tkinter import *

root = Tk()
root.title("sungbin GUI")
root.geometry("604x480") 


# --------------------------------------------


label1 = Label(root, text= "안녕하세요")
label1.pack()


photo = PhotoImage(file="GUI/c.png")
label2 = Label(root, image=photo)
label2.pack()


def change():
    label1.config(text="또 만나요")

    global photo2
    photo2 = PhotoImage(file="GUI/x.png")
    label2.config(image=photo2)    
    #가비지 컬렉션: 불필요한 메모리 공간 해제
    
    
btn = Button(root, text="클릭", command=change)
btn.pack()









# ---------------------------------------------------

root.mainloop()