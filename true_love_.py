from tkinter import *
import tkinter
root=Tk()
root.title('True Love Application')
root.geometry('500x300')
label1=Label(root,text='Your Name')
label2=Label(root,text='Your Partner Name')
entry1=Entry(root,width=40)
entry2=Entry(root,width=40)
labelframe=LabelFrame(root,text='result')
labelframe.grid(column=1,row=3)
#function for button1
def true_love():
    name1=entry1.get()
    name2=entry2.get()
    name3=name1+name2
    list4=[]
    for i in 'truelove':
        list4.append(name3.count(i))
    while True:
        a=[]
        for i in range(len(list4)-1):
            if list4[i]+list4[i+1] >=10:
                a.append(list4[i]+list4[i+1]-10)
            else:
                a.append(list4[i]+list4[i+1])
        list4=a
        if len(list4)<3:
            break
    e3=Label(labelframe,text='Tingkat Kecocokan %d%d'%(list4[0],list4[1])+'%')
    e3.grid(column=1,row=2)
    print('Tingkat Kecocokan %d%d'%(list4[0],list4[1])+'%')
    #function for button2
    def try_again():
        for i in [entry1,entry2]:
            i.delete('0','end')
        e3.destroy()
    button2=Button(root,text='try again',command=try_again)
    button2.grid(column=1,row=2,padx=4,pady=30)

label1.grid(column=0,row=0)
label2.grid(column=0,row=1)
entry1.grid(column=1,row=0,padx=20,pady=40)
entry2.grid(column=1,row=1)
button1=Button(root,text='check it out!!',command=true_love)
button1.grid(column=2,row=2,padx=20,pady=30)
root.mainloop()