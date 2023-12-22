from tkinter import *

root = Tk()
root.title('OKi')
root.geometry('500x500')

Label(root, text = 'ứng dụng test', fg='green', font=('cambria',16), width= 25).grid(row=0)
Listbox(root, width=85, height=10).grid(row=1,columnspan=2)
Label(root, text = 'tên hàng:').grid(row=2, colomn=0)
Entry(root, width=40).grid(row=2, column=1)
Label(root, text = 'sô lượng:').grid(row=3, colomn=0)
Entry(root, width=40).grid(row=3, column=1)
Label(root, text = 'đơn vị tính:').grid(row=4, colomn=0)
Entry(root, width=40).grid(row=4, column=1)


root.mainloop()