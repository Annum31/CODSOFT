import tkinter as Tk
import tkinter 
import tkinter.messagebox

window = tkinter.Tk()
window.title("To_do_list_app")

def addtask():
    task = entry_task.get()
    if task:
        listbox_task.insert(Tk.END,task)
        entry_task.delete(0,Tk.END)

def delete_task():
    try:
        task_index = listbox_task.curselection()[0]
        listbox_task.delete(task_index)
    except IndexError:
        pass

def update_task():
    try:
        new_word = entry_task.get()
        task_index = listbox_task.curselection()[0]
        listbox_task.delete(task_index)
        listbox_task.insert(task_index, new_word)
        entry_task.delete(0,Tk.END)
    except IndexError:
        pass

#def save_task():
    #To_do_list_app = list_frame.cget(0, list_frame.size())
    #tkinter.dump(To_do_list_app,open("task.dat","wb"))
    

    

#root = tk.Tk()


list_frame= Tk.Frame(window)
list_frame.pack()

frame_tasks = Tk.Frame(window)
frame_tasks.pack()

listbox_task = Tk.Listbox(frame_tasks,height=10,width=50)
listbox_task.pack(side=Tk.LEFT)

scrollbar_tasks = Tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=Tk.RIGHT, fill=Tk.Y)

listbox_task.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_task.yview)

entry_task = Tk.Entry(window,width=50)
entry_task.pack()

button_add_task = Tk.Button(window,text="Add text",width=48,command=addtask)
button_add_task.pack()

button_delete_task = Tk.Button(window,text="delete text",width=48,command=delete_task)
button_delete_task.pack()

button_update_task = Tk.Button(window,text="update text",width=48,command=update_task)
button_update_task.pack()

#button_save_task = Tk.Button(window,text="save text",width=48,command=save_task)
#button_save_task.pack()

window.mainloop()