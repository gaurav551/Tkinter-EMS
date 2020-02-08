from tkinter import *

import os

def add_employee():
    global add_screen
    add_screen = Tk()

    add_screen.title("Add Employee Section")
    add_screen.configure(background='pink')

    add_screen.geometry("650x550")

    Label(add_screen, text="Adding New Employee", bg="black",
          foreground="white", width="300", height="2", font=("Calibri", 13)).pack()

    global Id
    global Name
    global Age
    global Address
    global Contact
    global Department
    Id = StringVar()
    Name = StringVar()
    Age = StringVar()
    Address = StringVar()
    Contact = StringVar()
    Department = StringVar()

    Label(add_screen, height="1", text="Employee Id *").pack()
    Id = Entry(add_screen, width=100, textvariable=Id)
    Id.pack()
    Label(add_screen, text="").pack()

    Label(add_screen, text="Name").pack()

    Name = Entry(add_screen, width=100, textvariable=Name)
    Name.pack()

    Label(add_screen, text="").pack()

    Label(add_screen, text="Age").pack()
    Age = Entry(add_screen, width=100, textvariable=Age)
    Age.pack()
    Label(add_screen, text="").pack()

    Label(add_screen, text="Address").pack()
    Address = Entry(add_screen, width=100, textvariable=Address)
    Address.pack()
    Label(add_screen, text="").pack()

    Label(add_screen, text="Contact").pack()
    Contact = Entry(add_screen, width=100)
    Contact.pack()
    Label(add_screen, text="").pack()

    Label(add_screen, text="Department").pack()
    Department = Entry(add_screen, width=100)
    Department.pack()
    Label(add_screen, text="").pack()

    Button(add_screen, text="Submit", bg='green', width=10,
           height=1, command=save_add_employee).pack()
    Button(add_screen, text="Reset", bg='red', fg='black',
           width=10, height=1, command=clear_text).pack()
    Button(add_screen, text="Back", bg='blue', width=10,
           height=1, command=close_window).pack()


#  def view_employee():

#  def add_department():

#  def view_department():

def close_window():
    add_screen.destroy()
def close_window2():
 department_screen.destroy()
    


def clear_text():
    Id.delete(0, 'end')
    Name.delete(0, 'end')
    Age.delete(0, 'end')
    Address.delete(0, 'end')
    Contact.delete(0, 'end')
    Department.delete(0, 'end')


def save_add_employee():
    id_info = Id.get()
    name_info = Name.get()
    age_info = Age.get()
    address_info = Address.get()
    contact_info = Contact.get()
    department_info = Department.get()

    file = open("employeerecords.txt", "w")
    file.write(id_info + "\n")
    file.write(name_info + "\n")
    file.write(age_info + "\n")
    file.write(address_info + "\n")
    file.write(contact_info + "\n")
    file.write(department_info)

    file.close()
    Id.delete(0, 'end')
    Name.delete(0, 'end')
    Age.delete(0, 'end')
    Address.delete(0, 'end')
    Contact.delete(0, 'end')
    Department.delete(0, 'end')

    Label(add_screen, text="Employee Record Has Been Successfully Saved",
          fg="green", font=("calibri", 11)).pack()


def view_employee():
    global view_screen
    view_screen = Tk()

    view_screen.title("Viewing Employee Records")
    view_screen.configure(background='pink')

    view_screen.geometry("600x500")

    Label(view_screen, text="List of Employee", bg="black",
          foreground="white", width="300", height="2", font=("Calibri", 13)).pack()
    
    with open("employeerecords.txt", "r") as f:
    
     Label(view_screen, text=f.read()).pack()
    
def add_department():
    global department_screen
    department_screen = Tk()

    department_screen.title("Add Department Section")
    department_screen.configure(background='pink')

    department_screen.geometry("400x400")

    Label(department_screen, text="Adding New Department", bg="black",
          foreground="white", width="300", height="2", font=("Calibri", 13)).pack()

    global DepId
    global DepName
   
    Id = StringVar()
    Name = StringVar()
   

    Label(department_screen, height="1", text="DepartmentId *").pack()
    DepId = Entry(department_screen, width=100, textvariable=Id)
    DepId.pack()
    Label(department_screen, text="").pack()

    Label(department_screen, text="Department Name").pack()

    DepName = Entry(department_screen, width=100, textvariable=Name)
    DepName.pack()

    Label(department_screen, text="").pack()

    

    Button(department_screen, text="Submit", bg='green', width=10,
           height=1, command=save_add_department).pack()
   
    Button(department_screen, text="Back", bg='blue', width=10,
           height=1, command=close_window2).pack()


def save_add_department():
   id_info = DepId.get()
   name_info = DepName.get()
   file = open("departmentrecords.txt", "w")
   file.write(id_info + "\n")
   file.write(name_info)
  

   file.close()
   DepId.delete(0, 'end')
   DepName.delete(0, 'end')
  

   Label(department_screen, text= " {} Has Been Successfully Saved".format(name_info),
          fg="green", font=("calibri", 11)).pack()

def view_department():
    global view_department_screen
    view_department_screen = Tk()

    view_department_screen.title("Viewing Departments Records")
    view_department_screen.configure(background='pink')

    view_department_screen.geometry("600x500")

    Label(view_department_screen, text="List of Departments", bg="black",
          foreground="white", width="300", height="2", font=("Calibri", 13)).pack()
    
    with open("departmentrecords.txt", "r") as f:
    
     Label(view_department_screen, text=f.read()).pack()

def dashboard():
    global dash_screen
    dash_screen = Toplevel(main_screen)
    dash_screen.configure(background='pink')

    dash_screen.geometry("500x450")
    dash_screen.title("Employee Management System")
    Label(text="Employee Management System", bg="black", foreground="white",
          width="300", height="2", font=("verdana bold", 15)).pack()
    Label(text="Employee Section", bg="blue", foreground="white",
          width="100", height="2", font=("verdana bold", 15)).pack()

    Label(text="").pack()
    Button(text="Add Employee", height="2",
           width="30", command=add_employee).pack()
    Label(text="").pack()
    Button(text="View Employee", height="2",
           width="30", command=view_employee).pack()

    Label(text="Department Section", bg="blue", foreground="white",
          width="100", height="2", font=("verdana bold", 15)).pack()

    Label(text="").pack()
    Button(text="Add Department", height="2", width="30", command=add_department).pack()
    Label(text="").pack()
    Button(text="View Department", height="2",
           width="30", command=view_department).pack()
# Designing window for registration
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10,
           height=1, bg="blue", command=register_user).pack()
    # Implementing event on register button


def register_user():

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="You have been registered, Please Login Now",
          fg="green", font=("calibri", 11)).pack()


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(
        login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10,
           height=1, command=login_verify).pack()



# Implementing event on login button


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()

# Designing popup for login success


def login_sucess():
    global login_success_screen
    login_success_screen = Tk()
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK",
           command=delete_login_success).pack()
    
    
    
           
    

# Designing popup for login invalid password


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK",
           command=delete_password_not_recognised).pack()

# Designing popup for user not found


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK",
           command=delete_user_not_found_screen).pack()

# Deleting popups


def delete_login_success():
    
    login_success_screen.destroy()
    login_screen.destroy()
    dashboard()
   
    
   
    


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()

# Employee Section




# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Employee Management System")
    Label(text="Select Your Choice", bg="black", foreground="white",
          width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()




    # display when closing account screen


