from tkinter import *

root = Tk()
root.title("나도 gui")
root.geometry("604x480") #가로 세로 크기


# ------------------------------------

txt = Text(root, width=30, height=5) 
txt.pack()
txt.insert(END,"글자를 입력하세요")


e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력해요")

        
        
        
    #내용 입력
def btncmd():
    print(txt.get('1.0',END)) 
                # 1 : 첫번째 라인, 0: 0번째 column 위치
    print(e.get())

    txt.delete("1.0",END)
    e.delete(0,END)
    #내용 텍스트 삭제
    
    
    
    
btn = Button(root, text="클릭", command=btncmd)
btn.pack()




# -------------------------------------------

root.mainloop()
