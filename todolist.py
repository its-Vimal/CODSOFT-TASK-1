import tkinter
from tkinter import *
root=Tk()
root.title("-- TO DO LIST --")
root.geometry("400x650")
root.resizable(False,False)
task_list= []
def addtask():
    task=task_entry.get()
    task_entry.delete(0,END)
    if task:
        with open("todolist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        todolist.insert(END,task)
def deltask():
    global task_list
    task=str(todolist.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("todolist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        todolist.delete(ANCHOR)

def opentodolist():
    try:
        global todo_list
        with open("todolist.txt","r") as taskfile:
            tasks=taskfile.readlines()
        for task in tasks:
            if task !='\n':
                task_list.append(task)
                todolist.insert(END,task)
    except:
        file=open("todolist.txt","w")
        file.close()

head=PhotoImage(file="bar.png")
Label(root,image=head).pack()
heading=Label(root,text="TASK",font="arial 20 bold",fg="white",bg="#32405b")
heading.place(x=160,y=20)
frame=Frame(root,height=40,width=400,bg="white")
frame.place(x=0,y=130)

task=StringVar()
task_entry=Entry(frame,width=30,font="arial 15",bd=0)
task_entry.place(x=10,y=10)
addbutton=Button(frame,text="ADD",font="arial 17 bold",width=7,height=1,bg="#5a95ff",fg="#fff",bd=0,command=addtask)
addbutton.place(x=300,y=0)

todoframe=Frame(root,bd=3,width=650,height=300,bg="black")
todoframe.pack(pady=(150,0))

todolist=Listbox(todoframe,font=("arial",15),width=33,height=15,bg="black",fg="green",cursor="hand2",selectbackground="#5a95ff")
todolist.pack(side=LEFT,fill=BOTH,padx=0)
scrollbar=Scrollbar(todoframe)
scrollbar.pack(side=RIGHT,fill=BOTH)
todolist.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=todolist.yview)
opentodolist()
delbutton=Button(root,text="DELETE",font="arial 17 bold",width=7,height=1,bg="red",fg="white",bd=0,command=deltask)
delbutton.place(x=150,y=605)

root.mainloop()