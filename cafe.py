from tkinter import *
window = Tk()
window.title("커피 자동 주문기")

e=Entry(window, width=40, bg="white", fg="black", bd=5)
e.grid(row=0, column=0, columnspan=5)

buttons = [
'아메리카노(Hot)','카페라떼(Hot)','카푸치노(Hot)',
'아메리카노(Ice)','카페라떼(Ice)','카푸치노(Ice)',
'카라멜마끼아또','핫초코','레모네이드',
'자몽에이드','주문','지움']

def click(key):
    if e.get() == "":
        if key == '핫초코':
            e.insert(END,"3000")
        else:
            e.insert(END,"4000")
    elif key == '주문':
        result=eval(e.get())
        s=str(result) + '원을 결제하세요.'
        e.delete(0,END)
        e.insert(0,s)
    elif key == '지움':
        e.delete(0,END)
    else:
        if key == '핫초코':
            e.insert(END,"+3000")
        else:
            e.insert(END,"+4000")

row=1
col=0
for text in buttons:
    def process(t=text):
        click(t)

    b=Button(window, text=text, width=12, height=3, command=process)
    b.grid(row=row, column=col)
    col += 1
    if col > 2:
        row += 1
        col = 0

window.mainloop()
