from tkinter import *
import backend


window=Tk()
window.wm_title("Sale_details")

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(customer_name_text.get(),vehicle_model_text.get(),chassis_no_text.get(),reg_no_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(customer_name_text.get(),vehicle_model_text.get(),chassis_no_text.get(),reg_no_text.get())
    list1.delete(0,END)
    list1.insert(END,(customer_name_text.get(),vehicle_model_text.get(),chassis_no_text.get(),reg_no_text.get()))

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def update_command():
    backend.update(selected_tuple[0],customer_name_text.get(),vehicle_model_text.get(),chassis_no_text.get(),reg_no_text.get())





def delete_command():
    backend.delete(selected_tuple[0])




l1=Label(window,text="customer_name")
l1.grid(row=0,column=0)


l2=Label(window,text="vehicle_model")
l2.grid(row=0,column=2)


l3=Label(window,text="chassis_no")
l3.grid(row=1,column=0)


l4=Label(window,text="reg_no")
l4.grid(row=1,column=2)

customer_name_text=StringVar()
e1=Entry(window,textvariable=customer_name_text,width=20)
e1.grid(row=0,column=1)


vehicle_model_text=StringVar()
e2=Entry(window,textvariable=vehicle_model_text,width=20)
e2.grid(row=0,column=3)


chassis_no_text=StringVar()
e3=Entry(window,textvariable=chassis_no_text,width=20)
e3.grid(row=1,column=1)


reg_no_text=StringVar()
e4=Entry(window,textvariable=reg_no_text,width=20)
e4.grid(row=1,column=3)


list1=Listbox(window,height=15,width=100)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

list1.bind('<<ListboxSelect>>',get_selected_row)


sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window,text="View all",width=12,command=view_command)
b1.grid(row=2,column=3)


b2=Button(window,text="Search Entry",width=12,command=search_command)
b2.grid(row=3,column=3)


b3=Button(window,text="Add Entry",width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update Selected",width=12,command=update_command)
b4.grid(row=5,column=3)


b5=Button(window,text="Delete Selected",width=12,command=delete_command)
b5.grid(row=6,column=3)


b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)





window.mainloop()
