import tkinter as tk
import sqlite3 as db
from tkinter import messagebox

bg_color = "RoyalBlue1"
def show_view_screen():
    global view_screen
    main_screen.destroy()
    view_screen = tk.Toplevel()
    view_screen.title("View Screen")
    view_screen.geometry('800x600')  # Set the size of the window to be much larger
    tk.Label(
       view_screen, 
        text = "View Menu",
        bg = "white",
        fg = "black",
        font =("TkMenuFont", 14)
        ).pack()
    # Create 3 buttons with commands and pack them in the window
    button1 = tk.Button(view_screen, text="Search by keyword", command=lambda: print("Button 1 Pressed"), bg = bg_color, fg = "white")
    button2 = tk.Button(view_screen, text="Search for exercise Instructions", command=lambda: print("Button 2 Pressed"), bg = bg_color, fg = "white")
    button3 = tk.Button(view_screen, text="Back", command=leave_view, bg = bg_color, fg = "white")


    # Arrange buttons in a grid or pack them
    buttons = [button1, button2, button3]
    for i, button in enumerate(buttons, start=1):
        button.pack(pady=10)

    view_screen.protocol("WM_DELETE_WINDOW", on_closing_main_screen)
def show_delete_screen():
    global delete_screen
    main_screen.destroy()
    delete_screen = tk.Toplevel()
    delete_screen.title("Delete Screen")
    delete_screen.geometry('800x600')  # Set the size of the window to be much larger
    tk.Label(
       delete_screen, 
        text = "Delete Menu",
        bg = "white",
        fg = "black",
        font =("TkMenuFont", 14)
        ).pack()
    # Create 7 buttons with commands and pack them in the window
    button1 = tk.Button(delete_screen, text="Delete User Equipment", command=lambda: print("Button 1 Pressed"), bg = bg_color, fg = "white")
    button2 = tk.Button(delete_screen, text="Delete Exercise", command=lambda: print("Button 2 Pressed"), bg = bg_color, fg = "white")
    button3 = tk.Button(delete_screen, text="Remove exercise from workout", command=lambda: print("Button 3 Pressed"), bg = bg_color, fg = "white")
    button4 = tk.Button(delete_screen, text="Delete Health Log", command=lambda: print("Button 4 Pressed"), bg = bg_color, fg = "white")
    button5 = tk.Button(delete_screen, text="Delete Lift Log", command=lambda: print("Button 5 Pressed"), bg = bg_color, fg = "white")
    button6 = tk.Button(delete_screen, text="Delete Account", command=lambda: print("Button 6 Pressed"), bg = bg_color, fg = "white")
    button7 = tk.Button(delete_screen, text="Back", command=leave_delete, bg = bg_color, fg = "white")

    # Arrange buttons in a grid or pack them
    buttons = [button1, button2, button3, button4, button5, button6, button7]
    for i, button in enumerate(buttons, start=1):
        button.pack(pady=10)

    delete_screen.protocol("WM_DELETE_WINDOW", on_closing_main_screen)

def show_add_screen():
    global add_screen
    main_screen.destroy()
    add_screen = tk.Toplevel()
    add_screen.title("Add Screen")
    add_screen.geometry('800x600')  # Set the size of the window to be much larger
    tk.Label(
       add_screen, 
        text = "Add Menu",
        bg = "white",
        fg = "black",
        font =("TkMenuFont", 14)
        ).pack()
    # Create 10 buttons with commands and pack them in the window
    button1 = tk.Button(add_screen, text="Update User Weight", command=lambda: print("Button 1 Pressed"), bg = bg_color, fg = "white")
    button2 = tk.Button(add_screen, text="Update User Goal Weight", command=lambda: print("Button 2 Pressed"), bg = bg_color, fg = "white")
    button3 = tk.Button(add_screen, text="Add Equipment", command=lambda: print("Button 3 Pressed"), bg = bg_color, fg = "white")
    button4 = tk.Button(add_screen, text="Add User Equipment", command=lambda: print("Button 4 Pressed"), bg = bg_color, fg = "white")
    button5 = tk.Button(add_screen, text="Add Exercise", command=lambda: print("Button 5 Pressed"), bg = bg_color, fg = "white")
    button6 = tk.Button(add_screen, text="Add Muscle", command=lambda: print("Button 6 Pressed"), bg = bg_color, fg = "white")
    button7 = tk.Button(add_screen, text="Create Workout", command=lambda: print("Button 7 Pressed"), bg = bg_color, fg = "white")
    button8 = tk.Button(add_screen, text="Create Health Log", command=lambda: print("Button 8 Pressed"), bg = bg_color, fg = "white")
    button9 = tk.Button(add_screen, text="Create Lift Log", command=lambda: print("Button 9 Pressed"), bg = bg_color, fg = "white")
    button10 = tk.Button(add_screen, text="Back", command=leave_add, bg = bg_color, fg = "white")

    # Arrange buttons in a grid or pack them
    buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9, button10]
    for i, button in enumerate(buttons, start=1):
        button.pack(pady=10)

    add_screen.protocol("WM_DELETE_WINDOW", on_closing_main_screen)

def show_main_screen():
    global main_screen
    app.withdraw()
    main_screen = tk.Toplevel()
    main_screen.title("Main Screen")
    main_screen.geometry('800x600')  # Set the size of the window to be much larger
    tk.Label(
        main_screen, 
        text = "Main Menu",
        bg = "white",
        fg = "black",
        font =("TkMenuFont", 14)
        ).pack()
    # Create 4 buttons with commands and pack them in the window
    button1 = tk.Button(main_screen, text="ADD STUFF", command= show_add_screen, bg = bg_color, fg = "white")
    button2 = tk.Button(main_screen, text="DELETE STUFF", command=show_delete_screen, bg = bg_color, fg = "white")
    button3 = tk.Button(main_screen, text="VIEW STUFF", command=show_view_screen, bg = bg_color, fg = "white")
    button4 = tk.Button(main_screen, text="Log out", command= logout, bg = bg_color, fg = "white")
    
    # Arrange buttons in a grid or pack them
    buttons = [button1, button2, button3, button4]
    for i, button in enumerate(buttons, start=1):
        button.pack(pady=10)

    main_screen.protocol("WM_DELETE_WINDOW", on_closing_main_screen)

def on_closing_main_screen():
    app.destroy()

def submit_login():
    con = db.connect("CS2300 PROJECT/tuple.db")
    cur = con.cursor()
    try:
        user_id = entry_username.get()
        password = entry_password.get()
        cur.execute("SELECT password FROM user WHERE user_id = ?", (user_id,))
        stored_password = cur.fetchone()
        if stored_password is None:
            messagebox.showwarning("Login Failed", "User is not found.")
        elif password == stored_password[0]:
            messagebox.showinfo("Login Successful", "Welcome!")
            show_main_screen()
        else:
            messagebox.showwarning("Login Failed", "Incorrect password.")
    except db.Error as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")
    finally:
        con.close()

def setup_account_creation():
    global create_account_window, entry_user_id, entry_password, entry_full_name, entry_weight, entry_goal_weight, entry_goal_macros

    create_account_window = tk.Toplevel(app)
    create_account_window.title("Create Account")

    # Labels and entries setup without using a loop
    tk.Label(create_account_window, text="User ID:").grid(row=0, column=0)
    entry_user_id = tk.Entry(create_account_window)
    entry_user_id.grid(row=0, column=1)

    tk.Label(create_account_window, text="Password:").grid(row=1, column=0)
    entry_password = tk.Entry(create_account_window, show="*")
    entry_password.grid(row=1, column=1)

    tk.Label(create_account_window, text="Full Name:").grid(row=2, column=0)
    entry_full_name = tk.Entry(create_account_window)
    entry_full_name.grid(row=2, column=1)

    tk.Label(create_account_window, text="Weight:").grid(row=3, column=0)
    entry_weight = tk.Entry(create_account_window)
    entry_weight.grid(row=3, column=1)

    tk.Label(create_account_window, text="Goal Weight:").grid(row=4, column=0)
    entry_goal_weight = tk.Entry(create_account_window)
    entry_goal_weight.grid(row=4, column=1)

    tk.Label(create_account_window, text="Goal Macros:").grid(row=5, column=0)
    entry_goal_macros = tk.Entry(create_account_window)
    entry_goal_macros.grid(row=5, column=1)

    submit_btn = tk.Button(create_account_window, text="Create Account", command=create_account)
    submit_btn.grid(row=6, column=1)

def create_account():
    # Extract values directly from entry widgets
    user_id = entry_user_id.get()
    password = entry_password.get()
    full_name = entry_full_name.get()
    weight = entry_weight.get()
    goal_weight = entry_goal_weight.get()
    goal_macros = entry_goal_macros.get()

    # Connect to the database and insert the new user
    con = db.connect("CS2300 PROJECT/tuple.db")
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO user (user_id, password, full_name, weight, g_weight, g_macros) VALUES (?, ?, ?, ?, ?, ?)",
                    (user_id, password, full_name, weight, goal_weight, goal_macros))
        con.commit()
        messagebox.showinfo("Account Created", "Your account was successfully created!")
        create_account_window.destroy()  # Close the creation window
        show_main_screen()  # Log in automatically
        create_account_window.destroy()  # Close the creation window upon success
    except db.Error as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")
    finally:
        con.close()

def setup_login_window():
    global app, entry_username, entry_password
    app = tk.Tk()
    app.title("Login Form")
    app.eval("tk::PlaceWindow . center")

    tk.Label(app, text="Username:").grid(row=0, column=0)
    tk.Label(app, text="Password:").grid(row=1, column=0)

    entry_username = tk.Entry(app)
    entry_password = tk.Entry(app, show="*")
    entry_username.grid(row=0, column=1)
    entry_password.grid(row=1, column=1)

    submit_button = tk.Button(app, text="Login", command=submit_login)
    submit_button.grid(row=2, column=1)

    create_account_button = tk.Button(app, text="Create Account", command=setup_account_creation)
    create_account_button.grid(row=3, column=1)

#go back to main 
def leave_view():
    view_screen.destroy()
    show_main_screen()
def leave_add():
    add_screen.destroy()
    show_main_screen()
def leave_delete():
    delete_screen.destroy()
    show_main_screen()
def logout():
    main_screen.destroy()
    setup_login_window()


setup_login_window()
app.mainloop()

#basically the program starts in a login/create user screen then the user is taken to a new window where the user can choose to add/delete/view data in the database the 
#the view page has things like view the instructions and the query to search exercises based on equipment and the add/delete would be like adding and deleting data from tables