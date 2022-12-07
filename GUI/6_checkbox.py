from tkinter import  *

root = Tk()
root.title("나도 gui")
root.geometry("604x480") #가로 세로 크기


# ------------------------------------



chkvar = IntVar()
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
#채크박스 선택
# chkbox.select() # 자동선택 처리
# chkbox.deselect()     # 선택 해제 처리
chkbox.pack()


chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기",variable=chkvar2)
chkbox2.pack()




def btncmd():
    print(chkvar.get()) 
    print(chkvar2.get())# 0: 체크헤제 , 1:체크



    
btn = Button(root, text="클릭", command=btncmd)
btn.pack()



# -------------------------------------------

root.mainloop()
