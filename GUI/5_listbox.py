from tkinter import *

root = Tk()
root.title("나도 gui")
root.geometry("604x480") #가로 세로 크기


# ------------------------------------


                            #     extended = 복수 선택 가능
                            #       single = 하나만 선택가능
listbox = Listbox(root, selectmode="extended", height=0) 
#                                             height 보여지는 개수를 표시 0일때 모두 3이라면 3개만 표시
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(3,"바나나")
listbox.insert(END,"수박")
listbox.insert(END,"포도")
listbox.pack()




    #내용 입력
def btncmd():
    #리스트 박스 삭제
    # listbox.delete(0)
    
    #갯수 확인
    # print("리스트에는", listbox.size(), "개가 있어요")
    
                                        #항목확인(시작 인덱스 , 끝인덱스)
    # print("1번째부터 3번째까지의 항목 : ", listbox.get(0,2))
    
    #선택항목 확인                  클릭한 항목이 인덱스 값(위치로 반환)으로 나타남
    print("선택된 항목: ", listbox.curselection())
    
    
    
    
    
btn = Button(root, text="클릭", command=btncmd)
btn.pack()


# -------------------------------------------

root.mainloop()
