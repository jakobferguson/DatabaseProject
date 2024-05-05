import tkinter as tk
import sqlite3 as db
from tkinter import messagebox, scrolledtext
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk)

bg_color = "RoyalBlue1"
#delete a lift log
def deleteliftLog():
    # Create the delete lifting log window
    delete_window = tk.Toplevel()
    delete_window.title("Delete Lifting Log")
    delete_window.geometry("300x150")

    # Label and Entry for Log ID
    tk.Label(delete_window, text="Enter the log number of the lift log you want to delete:").pack(pady=(10, 0))
    log_id_entry = tk.Entry(delete_window, width=30)
    log_id_entry.pack(pady=(0, 10))

    # Function to handle the deletion of the lifting log
    def submit_deletion():
        log_id = log_id_entry.get()
        con = db.connect("tuple.db")
        cur = con.cursor()

        # First, verify that the log entry exists
        cur.execute("SELECT log_id FROM lift_log WHERE log_id = ?", (log_id,))
        if cur.fetchone() is None:
            messagebox.showerror("Error", "No such lift log found.")
            con.close()
            return

        # Perform the deletion
        try:
            cur.execute("DELETE FROM lift_log WHERE log_id = ?", (log_id,))
            con.commit()
            messagebox.showinfo("Success", "Lift log deleted successfully.")
        except db.Error as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            con.close()
            delete_window.destroy()

    # Button to submit the deletion
    delete_btn = tk.Button(delete_window, text="Delete Log", command=submit_deletion)
    delete_btn.pack(pady=20)
#add a lift log
def addLiftingLog():
    # Create the add lifting log window
    add_window = tk.Toplevel()
    add_window.title("Add Lifting Log")
    add_window.geometry("400x300")

    # Label and Entry for Log ID
    tk.Label(add_window, text="Enter the Log number:").pack(pady=(10, 0))
    log_id_entry = tk.Entry(add_window, width=50)
    log_id_entry.pack(pady=(0, 10))

    # Label and Entry for User ID
    tk.Label(add_window, text="Enter your user ID:").pack(pady=(10, 0))
    user_id_entry = tk.Entry(add_window, width=50)
    user_id_entry.pack(pady=(0, 10))

    # Label and Entry for Weight Lifted
    tk.Label(add_window, text="Enter the weight lifted (in lbs or kg):").pack(pady=(10, 0))
    weight_entry = tk.Entry(add_window, width=50)
    weight_entry.pack(pady=(0, 10))

    # Label and Entry for Reps
    tk.Label(add_window, text="Enter the number of reps:").pack(pady=(10, 0))
    reps_entry = tk.Entry(add_window, width=50)
    reps_entry.pack(pady=(0, 10))

    # Label and Entry for Sets
    tk.Label(add_window, text="Enter the number of sets:").pack(pady=(10, 0))
    sets_entry = tk.Entry(add_window, width=50)
    sets_entry.pack(pady=(0, 10))

    # Function to handle the insertion of lifting log data
    def submit_log():
        log_id = log_id_entry.get()
        user_id = user_id_entry.get()
        weight = weight_entry.get()
        reps = reps_entry.get()
        sets = sets_entry.get()

        con = db.connect("tuple.db")
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO lift_log (log_id, user_id, weight, reps, sets) VALUES (?, ?, ?, ?, ?)",
                        (log_id, user_id, weight, reps, sets))
            con.commit()
            messagebox.showinfo("Success", "Lifting log added successfully.")
        except db.IntegrityError:
            messagebox.showerror("Error", "There was an issue adding the lifting log. Make sure the user ID exists and data is correct.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            con.close()
            add_window.destroy()

    # Button to submit the new lifting log
    submit_btn = tk.Button(add_window, text="Add Log", command=submit_log)
    submit_btn.pack(pady=20)
#delete a health log entry
def deleteHealthLog():
    # Create the delete health log window
    delete_window = tk.Toplevel()
    delete_window.title("Delete Health Log")
    delete_window.geometry("300x150")

    # Label and Entry for Log ID
    tk.Label(delete_window, text="Enter the log number of the health log you want to delete:").pack(pady=(10, 0))
    log_id_entry = tk.Entry(delete_window, width=30)
    log_id_entry.pack(pady=(0, 10))

    # Function to handle the deletion of the health log
    def submit_deletion():
        log_id = log_id_entry.get()
        con = db.connect("tuple.db")
        cur = con.cursor()

        # First, verify that the log entry exists
        cur.execute("SELECT log_id FROM health_log WHERE log_id = ?", (log_id,))
        if cur.fetchone() is None:
            messagebox.showerror("Error", "No such health log found.")
            con.close()
            return

        # Perform the deletion
        try:
            cur.execute("DELETE FROM health_log WHERE log_id = ?", (log_id,))
            con.commit()
            messagebox.showinfo("Success", "Health log deleted successfully.")
        except db.Error as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            con.close()
            delete_window.destroy()

    # Button to submit the deletion
    delete_btn = tk.Button(delete_window, text="Delete Log", command=submit_deletion)
    delete_btn.pack(pady=20)
#add a health log entry 
def addHealthLog():
    # Create the add health log window
    add_log_window = tk.Toplevel()
    add_log_window.title("Add Health Log")
    add_log_window.geometry("300x200")

    # Label and Entry for Log ID
    tk.Label(add_log_window, text="Enter this log's number:").pack(pady=(10, 0))
    log_id_entry = tk.Entry(add_log_window, width=30)
    log_id_entry.pack(pady=(0, 10))

    # Label and Entry for User ID
    tk.Label(add_log_window, text="Enter your user ID:").pack(pady=(10, 0))
    user_id_entry = tk.Entry(add_log_window, width=30)
    user_id_entry.pack(pady=(0, 10))

    # Label and Entry for Weight
    tk.Label(add_log_window, text="Enter your weight:").pack(pady=(10, 0))
    weight_entry = tk.Entry(add_log_window, width=30)
    weight_entry.pack(pady=(0, 10))

    # Function to handle the insertion of health log data
    def submit_log():
        log_id = log_id_entry.get()
        user_id = user_id_entry.get()
        weight = weight_entry.get()

        con = db.connect("tuple.db")
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO health_log (log_id, user_id, weight) VALUES (?, ?, ?)", 
                        (log_id, user_id, weight))
            con.commit()
            messagebox.showinfo("Success", "Health log added successfully.")
        except db.IntegrityError:
            messagebox.showerror("Error", "There was an issue adding the health log. Make sure the user ID exists.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            con.close()
            add_log_window.destroy()

    # Button to submit the new health log
    submit_btn = tk.Button(add_log_window, text="Add Log", command=submit_log)
    submit_btn.pack(pady=20)
#remove exercise from a workout
def removeExcFromWorkout():
    # Create the remove exercise from workout window
    remove_window = tk.Toplevel()
    remove_window.title("Remove Exercise from Workout")
    remove_window.geometry("400x200")

    # Label and Entry for Workout ID
    tk.Label(remove_window, text="Enter the number of the workout to remove from:").pack(pady=(10, 0))
    wid_entry = tk.Entry(remove_window, width=50)
    wid_entry.pack(pady=(0, 10))

    # Label and Entry for Exercise Name
    tk.Label(remove_window, text="Enter the name of the exercise to remove:").pack(pady=(10, 0))
    exc_name_entry = tk.Entry(remove_window, width=50)
    exc_name_entry.pack(pady=(0, 10))

    # Function to handle the removal of exercise from workout
    def submit_removal():
        wid = wid_entry.get()
        exc_name = exc_name_entry.get()
        con = db.connect("tuple.db")
        cur = con.cursor()

        # First, verify that the exercise exists within the specified workout
        cur.execute("SELECT * FROM exc_included WHERE wid = ? AND exc_name = ?", (wid, exc_name))
        if cur.fetchone() is None:
            messagebox.showerror("Error", "No such exercise found in the specified workout.")
            con.close()
            return

        # Perform the deletion
        try:
            cur.execute("DELETE FROM exc_included WHERE wid = ? AND exc_name = ?", (wid, exc_name))
            con.commit()
            messagebox.showinfo("Success", "Exercise successfully removed from the workout.")
        except db.Error as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            con.close()
        remove_window.destroy()

    # Button to submit the removal
    remove_btn = tk.Button(remove_window, text="Remove Exercise", command=submit_removal)
    remove_btn.pack(pady=20)
#add an exercise to a workout
def addExcToWorkout():
    # Create the add exercise to workout window
    add_window = tk.Toplevel()
    add_window.title("Add Exercise to Workout")
    add_window.geometry("400x250")

    # Label and Entry for Workout ID
    tk.Label(add_window, text="Enter the workout number to add to:").pack(pady=(10, 0))
    wid_entry = tk.Entry(add_window, width=50)
    wid_entry.pack(pady=(0, 10))

    # Label and Entry for Exercise Name
    tk.Label(add_window, text="Enter the name of the exercise to add:").pack(pady=(10, 0))
    exc_name_entry = tk.Entry(add_window, width=50)
    exc_name_entry.pack(pady=(0, 10))

    # Label and Entry for Reps
    tk.Label(add_window, text="How many reps?:").pack(pady=(10, 0))
    reps_entry = tk.Entry(add_window, width=50)
    reps_entry.pack(pady=(0, 10))

    # Label and Entry for Sets
    tk.Label(add_window, text="How many sets?:").pack(pady=(10, 0))
    sets_entry = tk.Entry(add_window, width=50)
    sets_entry.pack(pady=(0, 10))

    # Function to handle the addition of exercise to workout
    def submit_addition():
        wid = wid_entry.get()
        exc_name = exc_name_entry.get()
        reps = reps_entry.get()
        sets = sets_entry.get()

        con = db.connect("tuple.db")
        cur = con.cursor()

        # Verify that the exercise and workout exists
        try:
            cur.execute("SELECT exc_name FROM exercise WHERE exc_name = ?", (exc_name,))
            if cur.fetchone() is None:
                messagebox.showerror("Error", "The exercise you have listed cannot be found")
                return
            cur.execute("SELECT wid FROM workout WHERE wid = ?", (wid,))
            if cur.fetchone() is None:
                messagebox.showerror("Error", "The workout you have listed cannot be found")
                return

            # Insert the exercise into the workout
            cur.execute("INSERT INTO exc_included(wid, exc_name, exc_reps, exc_sets) VALUES (?,?,?,?)", (wid, exc_name, reps, sets))
            con.commit()
            messagebox.showinfo("Success", "Exercise added to the workout successfully.")
        except db.IntegrityError:
            messagebox.showerror("Error", "This exercise is already included in the workout.")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
        finally:
            con.close()

    # Button to submit the new workout
    submit_btn = tk.Button(add_window, text="Add Exercise", command=submit_addition)
    submit_btn.pack(pady=20)
#create a workout
def createWorkout():
    # Create the create workout window
    create_window = tk.Toplevel()
    create_window.title("Create Workout")
    create_window.geometry("400x300")

    # Label and Entry for Workout Name
    tk.Label(create_window, text="Name the workout:").pack(pady=(10, 0))
    w_name_entry = tk.Entry(create_window, width=50)
    w_name_entry.pack(pady=(0, 10))

    # Label and Entry for Workout ID
    tk.Label(create_window, text="Give your workout a number:").pack(pady=(10, 0))
    wid_entry = tk.Entry(create_window, width=50)
    wid_entry.pack(pady=(0, 10))

    # Label and Entry for Workout Type
    tk.Label(create_window, text="Enter the type of workout (e.g., Upper Body, Lower Body):").pack(pady=(10, 0))
    w_type_entry = tk.Entry(create_window, width=50)
    w_type_entry.pack(pady=(0, 10))

    # Label and Entry for User ID
    tk.Label(create_window, text="Enter your user ID:").pack(pady=(10, 0))
    user_id_entry = tk.Entry(create_window, width=50)
    user_id_entry.pack(pady=(0, 10))

    # Function to handle the insertion of workout data
    def submit_workout():
        w_name = w_name_entry.get()
        wid = wid_entry.get()
        w_type = w_type_entry.get()
        user_id = user_id_entry.get()
        modifiable = 'no'  # User-created workouts aren't modifiable

        con = db.connect("tuple.db")
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO workout (w_name, type, wid, modifiable, user_id) VALUES(?,?,?,?,?)",
                        (w_name, w_type, wid, modifiable, user_id))
            con.commit()
            messagebox.showinfo("Success", "New workout created successfully.")
        except db.IntegrityError as e:
            messagebox.showerror("Error", "A workout with this ID already exists.")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
        finally:
            con.close()
            create_window.destroy()

    # Button to submit the new workout
    submit_btn = tk.Button(create_window, text="Create Workout", command=submit_workout)
    submit_btn.pack(pady=20)

#query instructions
def viewExcInstructions():
    # Create the view exercise instructions window
    view_inst_window = tk.Toplevel()
    view_inst_window.title("View Exercise Instructions")
    view_inst_window.geometry("400x300")

    # Label and Entry for Exercise Name
    tk.Label(view_inst_window, text="Enter the name of the exercise:").pack(pady=(10, 0))
    exercise_entry = tk.Entry(view_inst_window, width=50)
    exercise_entry.pack(pady=(0, 10))

    # Text widget to display instructions
    instruction_display = scrolledtext.ScrolledText(view_inst_window, height=10, width=45)
    instruction_display.pack(pady=(5, 10))
    instruction_display.config(state='disabled')  # Disable editing of the widget

    # Function to handle the fetching and display of instructions
    def get_instructions():
        exercise = exercise_entry.get()
        con = db.connect("tuple.db")
        cur = con.cursor()
        query = "SELECT instruction FROM exercise WHERE exc_name = ?"
        cur.execute(query, (exercise,))
        result = cur.fetchone()
        instruction_display.config(state='normal')
        instruction_display.delete('1.0', tk.END)  # Clear previous content
        if result:
            instruction_display.insert(tk.END, f"Instructions for {exercise}: {result[0]}")
        else:
            instruction_display.insert(tk.END, f"No instructions found for {exercise}")
        instruction_display.config(state='disabled')
        con.close()

    # Button to submit the request for instructions
    get_inst_btn = tk.Button(view_inst_window, text="Get Instructions", command=get_instructions)
    get_inst_btn.pack(pady=20)
#add a muscle 
def addMuscle():
    # Create the add muscle to exercise window
    add_muscle_window = tk.Toplevel()
    add_muscle_window.title("Add Muscle Usage")
    add_muscle_window.geometry("400x200")

    # Label and Entry for Exercise Name
    tk.Label(add_muscle_window, text="Enter the name of the exercise:").pack(pady=(10, 0))
    exc_name_entry = tk.Entry(add_muscle_window, width=50)
    exc_name_entry.pack(pady=(0, 10))

    # Label and Entry for Muscle Targeted
    tk.Label(add_muscle_window, text="Enter the name of the muscle targeted:").pack(pady=(10, 0))
    muscle_entry = tk.Entry(add_muscle_window, width=50)
    muscle_entry.pack(pady=(0, 10))

    # Function to handle the addition of muscle usage
    def submit_muscle_usage():
        exc_name = exc_name_entry.get()
        muscle = muscle_entry.get()
        con = db.connect("tuple.db")
        cur = con.cursor()

        # First, check if the exercise exists in the 'exercise' table
        cur.execute("SELECT exc_name FROM exercise WHERE exc_name = ?", (exc_name,))
        if cur.fetchone() is None:
            messagebox.showerror("Error", "The exercise you have listed cannot be found. Please add the exercise first.")
            con.close()
            return
        
        try:
            cur.execute("INSERT INTO m_used (exc_name, muscle) VALUES (?, ?)", (exc_name, muscle))
            con.commit()
            messagebox.showinfo("Success", "Muscle usage added successfully.")
        except db.IntegrityError:
            messagebox.showerror("Error", "An error occurred while trying to add the muscle usage.")
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")
        finally:
            con.close()
            add_muscle_window.destroy()

    # Button to submit the new muscle usage
    submit_btn = tk.Button(add_muscle_window, text="Add Muscle", command=submit_muscle_usage)
    submit_btn.pack(pady=20)
#query database for exercises
def viewExcByType():
    # Create the view exercise by type window
    view_window = tk.Toplevel()
    view_window.title("View Exercises")
    view_window.geometry("600x400")

    # Label and Entry for Keyword
    tk.Label(view_window, text="Enter the keyword to search by (muscle, equipment, or type):").pack(pady=(10, 0))
    keyword_entry = tk.Entry(view_window, width=50)
    keyword_entry.pack(pady=(0, 10))

    # ScrolledText widget to display results
    results_display = scrolledtext.ScrolledText(view_window, height=15, width=70)
    results_display.pack(pady=(5, 10))
    results_display.config(state='disabled')  # Disable editing of the widget

    # Function to handle the search and display results
    def search_exercises():
        keyword = keyword_entry.get()
        con = db.connect("tuple.db")
        cur = con.cursor()
        query = """
        SELECT e.exc_name, e.instruction, e.type, e.eqp_name, m.muscle
        FROM exercise e
        LEFT JOIN m_used m ON e.exc_name = m.exc_name
        WHERE e.type LIKE ? OR e.eqp_name LIKE ? OR m.muscle LIKE ?
        """
        cur.execute(query, ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))
        results = cur.fetchall()
        con.close()
        
        results_display.config(state='normal')
        results_display.delete('1.0', tk.END)
        if results:
            results_display.insert(tk.END, f"Found {len(results)} exercises matching '{keyword}':\n\n")
            for exc in results:
                results_display.insert(tk.END, f"Name: {exc[0]}, Instructions: {exc[1]}, Type: {exc[2]}, Equipment: {exc[3]}, Muscle: {exc[4]}\n")
        else:
            results_display.insert(tk.END, "No exercises were found containing that keyword\n")
        results_display.config(state='disabled')

    # Button to initiate search
    search_btn = tk.Button(view_window, text="Search Exercises", command=search_exercises)
    search_btn.pack(pady=20)

#Delete Exercises
def deleteExc():
    # Create the delete exercise window
    delete_exc_window = tk.Toplevel()
    delete_exc_window.title("Delete Exercise")
    delete_exc_window.geometry("350x150")

    # Label and Entry for Exercise Name
    tk.Label(delete_exc_window, text="Enter the name of the exercise you want to delete:").pack(pady=(10, 0))
    exc_name_entry = tk.Entry(delete_exc_window, width=50)
    exc_name_entry.pack(pady=(0, 10))

    # Function to handle the deletion of exercise
    def submit_delete():
        exc_name = exc_name_entry.get()
        con = db.connect("tuple.db")
        cur = con.cursor()
        try:
            # Verify the exercise exists
            cur.execute("SELECT exc_name FROM exercise WHERE exc_name = ?", (exc_name,))
            if cur.fetchone() is None:
                messagebox.showinfo("Error", "The exercise you have listed cannot be found.")
            else:
                cur.execute("DELETE FROM exercise WHERE exc_name = ?", (exc_name,))
                con.commit()
                messagebox.showinfo("Success", "Deletion successful")
        except db.Error as e:
            messagebox.showerror("Error", f"An Error has occurred: {e}")
        finally:
            con.close()
            delete_exc_window.destroy()

    # Button to submit the deletion
    delete_btn = tk.Button(delete_exc_window, text="Delete Exercise", command=submit_delete)
    delete_btn.pack(pady=20)
#Add exercises
def addExc():
    # Create the add exercise window
    add_exc_window = tk.Toplevel()
    add_exc_window.title("Add Exercise")
    add_exc_window.geometry("400x300")

    # Entry for Exercise Name
    tk.Label(add_exc_window, text="Enter the name of the exercise:").pack(pady=(5, 0))
    exc_name_entry = tk.Entry(add_exc_window, width=50)
    exc_name_entry.pack(pady=(0, 5))

    # Entry for Description
    tk.Label(add_exc_window, text="Enter the description of the exercise:").pack(pady=(5, 0))
    desc_entry = tk.Text(add_exc_window, height=3, width=38)
    desc_entry.pack(pady=(0, 5))

    # Entry for Exercise Type
    tk.Label(add_exc_window, text="Enter the type of exercise (e.g., cardio, strength):").pack(pady=(5, 0))
    xType_entry = tk.Entry(add_exc_window, width=50)
    xType_entry.pack(pady=(0, 5))

    # Entry for Equipment Name
    tk.Label(add_exc_window, text="Enter the name of the equipment (leave blank if none):").pack(pady=(5, 0))
    eqp_name_entry = tk.Entry(add_exc_window, width=50)
    eqp_name_entry.pack(pady=(0, 10))

    # Function to handle exercise addition
    def submit_exc():
        exc_name = exc_name_entry.get()
        desc = desc_entry.get("1.0", "end-1c")  # Get text from Text widget
        xType = xType_entry.get()
        eqp_name = eqp_name_entry.get()

        con = db.connect("tuple.db")
        cur = con.cursor()

        # Check if the equipment exists if not empty
        if eqp_name:
            cur.execute("SELECT eqp_name FROM eqp WHERE eqp_name = ?", (eqp_name,))
            if cur.fetchone() is None:
                messagebox.showerror("Error", "Equipment not found. Please add the equipment first.")
                return

        # Insert the data into the db
        try:
            cur.execute("INSERT INTO exercise (exc_name, instruction, Type, eqp_name) VALUES (?, ?, ?, ?)",
                        (exc_name, desc, xType, eqp_name or None))
            con.commit()
            messagebox.showinfo("Success", "The exercise has been added successfully")
        except db.IntegrityError:
            messagebox.showerror("Error", "An exercise with this name already exists")
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")
        finally:
            con.close()
            add_exc_window.destroy()  # Close the window after adding

    # Button to submit the new exercise
    submit_btn = tk.Button(add_exc_window, text="Add Exercise", command=submit_exc)
    submit_btn.pack(pady=20)
#Delete User equipment 
def deleteUserEqp():
    # Create the delete user equipment window
    delete_window = tk.Toplevel()
    delete_window.title("Delete Equipment from User")
    delete_window.geometry("350x200")

    # Label and Entry for User ID
    tk.Label(delete_window, text="Enter your user ID:").pack(pady=(10, 0))
    user_id_entry = tk.Entry(delete_window)
    user_id_entry.pack(pady=(0, 10))

    # Label and Entry for Equipment Name
    tk.Label(delete_window, text="Enter the name of the equipment:").pack(pady=(10, 0))
    eqp_name_entry = tk.Entry(delete_window)
    eqp_name_entry.pack(pady=(0, 10))

    # Function to handle the deletion of equipment
    def delete_eqp():
        user_id = user_id_entry.get()
        eqp_name = eqp_name_entry.get()
        con = db.connect("tuple.db")
        cur = con.cursor()
        try:
            # Check if the equipment exists for the user
            cur.execute("SELECT * FROM eqp_owned WHERE user_id = ? AND eqp_name = ?", (user_id, eqp_name))
            if cur.fetchone() is None:
                messagebox.showinfo("Error", "No equipment found")
            else:
                cur.execute("DELETE FROM eqp_owned WHERE user_id = ? AND eqp_name = ?", (user_id, eqp_name))
                con.commit()
                messagebox.showinfo("Success", "Equipment removed from your account successfully")
        except db.Error as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            con.close()
        delete_window.destroy()

    # Button to submit the deletion
    delete_btn = tk.Button(delete_window, text="Delete Equipment", command=delete_eqp)
    delete_btn.pack(pady=20)
#add user equipment
def addUserEqp():
    # Create the add user equipment window
    add_user_eqp_window = tk.Toplevel()
    add_user_eqp_window.title("Add User Equipment")
    add_user_eqp_window.geometry("350x200")

    # Label and Entry for User ID
    tk.Label(add_user_eqp_window, text="Enter the user ID:").pack(pady=(10, 0))
    user_id_entry = tk.Entry(add_user_eqp_window)
    user_id_entry.pack(pady=(0, 10))

    # Label and Entry for Equipment Name
    tk.Label(add_user_eqp_window, text="Enter the name of the equipment:").pack(pady=(10, 0))
    eqp_name_entry = tk.Entry(add_user_eqp_window)
    eqp_name_entry.pack(pady=(0, 10))

    # Function to handle user equipment addition
    def submit_user_eqp():
        user_id = user_id_entry.get()
        eqp_name = eqp_name_entry.get()
        # Connect to db
        con = db.connect("tuple.db")
        cur = con.cursor()
        try:
            # Check if the equipment exists in the eqp table
            cur.execute("SELECT eqp_name FROM eqp WHERE eqp_name = ?", (eqp_name,))
            if cur.fetchone() is None:
                messagebox.showinfo("Error", "Equipment not found")
            else:
                # Check if the equipment is already owned by the user
                cur.execute("SELECT * FROM eqp_owned WHERE user_id =? AND eqp_name = ?", (user_id, eqp_name))
                if cur.fetchone() is not None:
                    messagebox.showinfo("Error", "You already own this equipment.")
                else:
                    cur.execute("INSERT INTO eqp_owned(user_id, eqp_name) VALUES(?, ?)", (user_id, eqp_name))
                    con.commit()
                    messagebox.showinfo("Success", "Equipment added successfully")
        except db.IntegrityError:
            messagebox.showerror("Database Error", "Failed to add equipment. Make sure that the equipment name and user id are correct")
        except Exception as e:
            messagebox.showerror("Database Error", f"An unexpected error occurred: {e}")
        finally:
            con.close()
            add_user_eqp_window.destroy()  # Close the window after processing

    # Button to submit the new equipment ownership
    submit_btn = tk.Button(add_user_eqp_window, text="Add Equipment to User", command=submit_user_eqp)
    submit_btn.pack(pady=20)
#add equipment
def addEqp():
    # Create the add equipment window
    add_eqp_window = tk.Toplevel()
    add_eqp_window.title("Add Equipment")
    add_eqp_window.geometry("300x150")

    # Label and Entry for Equipment Name
    tk.Label(add_eqp_window, text="Enter the name of the Equipment:").pack(pady=(10, 0))
    eqp_name_entry = tk.Entry(add_eqp_window)
    eqp_name_entry.pack(pady=(0, 10))

    # Function to handle equipment addition
    def submit_eqp():
        eqp_name = eqp_name_entry.get()
        # Connect to db
        con = db.connect("tuple.db")
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO eqp(eqp_name) VALUES(?)", (eqp_name,))
            con.commit()
            messagebox.showinfo("Success", "Equipment successfully added")
        except db.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")
        finally:
            con.close()
            add_eqp_window.destroy()  # Close the window after adding

    # Button to submit the new equipment
    submit_btn = tk.Button(add_eqp_window, text="Add Equipment", command=submit_eqp)
    submit_btn.pack(pady=20)
#Update user goal 
def updateUserGoal():
    # Create the update goal window
    update_goal_window = tk.Toplevel()
    update_goal_window.title("Update User Goal Weight")
    update_goal_window.geometry("300x250")

    # Label and Entry for User ID
    tk.Label(update_goal_window, text="Enter the user ID:").pack(pady=(10, 0))
    user_id_entry = tk.Entry(update_goal_window)
    user_id_entry.pack(pady=(0, 10))

    # Label and Entry for New Goal Weight
    tk.Label(update_goal_window, text="Enter the new goal weight:").pack(pady=(10, 0))
    new_goal_entry = tk.Entry(update_goal_window)
    new_goal_entry.pack(pady=(0, 10))

    # Function to handle goal weight update
    def submit_goal_update():
        user_id = user_id_entry.get()
        new_goal = new_goal_entry.get()
        # Connect to db
        con = db.connect("tuple.db")
        cur = con.cursor()
        # Make the update statement
        cur.execute("UPDATE user SET g_weight = ? WHERE user_id = ?", (new_goal, user_id))

        if cur.rowcount == 0:
            messagebox.showinfo("Result", "No user found.")
        else:
            con.commit()
            messagebox.showinfo("Result", "User goal weight updated successfully")
        con.close()
        update_goal_window.destroy()  # Close the window after updating

    # Button to submit the update
    submit_btn = tk.Button(update_goal_window, text="Update Goal", command=submit_goal_update)
    submit_btn.pack(pady=20)

    # Button to cancel
    cancel_btn = tk.Button(update_goal_window, text="Cancel", command=update_goal_window.destroy)
    cancel_btn.pack(pady=10)
# Delete account method
def deleteAccount():
    # Create the delete account window
    delete_window = tk.Toplevel()
    delete_window.title("Delete Account")
    delete_window.geometry("300x200")

    # Label and Entry for User ID
    tk.Label(delete_window, text="Enter the user ID you want to delete:").pack(pady=10)
    user_id_entry = tk.Entry(delete_window)
    user_id_entry.pack()

    # Function to handle deletion
    def confirm_delete():
        user_id = user_id_entry.get()
        if messagebox.askyesno("Confirm", f"Are you sure you want to delete the account '{user_id}'? This action cannot be undone."):
            con = db.connect("tuple.db")
            cur = con.cursor()
            cur.execute("DELETE FROM user WHERE user_id = ?", (user_id,))
            if cur.rowcount == 0:
                messagebox.showinfo("Result", "No user found.")
            else:
                con.commit()
                messagebox.showinfo("Result", "Account deleted successfully")
            con.close()
            delete_window.destroy()  # Close the window after deletion

    # Buttons for confirming or canceling
    tk.Button(delete_window, text="Delete", command=confirm_delete).pack(side=tk.LEFT, padx=10, pady=20)
    tk.Button(delete_window, text="Cancel", command=delete_window.destroy).pack(side=tk.RIGHT, padx=10, pady=20)
#Update Weight Method
def updateUserWeight():
    # Create the update weight window
    update_window = tk.Toplevel()
    update_window.title("Update User Weight")
    update_window.geometry("300x200")

    # Label and Entry for User ID
    tk.Label(update_window, text="Enter the user ID:").pack(pady=(10, 0))
    user_id_entry = tk.Entry(update_window)
    user_id_entry.pack(pady=(0, 10))

    # Label and Entry for New Weight
    tk.Label(update_window, text="Enter the new weight:").pack(pady=(10, 0))
    new_weight_entry = tk.Entry(update_window)
    new_weight_entry.pack(pady=(0, 10))

    # Function to handle weight update
    def submit_update():
        user_id = user_id_entry.get()
        new_weight = new_weight_entry.get()
        # Connect to db
        con = db.connect("tuple.db")
        cur = con.cursor()
        # Make the update statement
        cur.execute("UPDATE user SET weight = ? WHERE user_id = ?", (new_weight, user_id))

        if cur.rowcount == 0:
            messagebox.showinfo("Result", "No user found.")
        else:
            con.commit()
            messagebox.showinfo("Result", "User weight updated successfully")
        con.close()
        update_window.destroy()  # Close the window after updating

    # Button to submit the update
    submit_btn = tk.Button(update_window, text="Update Weight", command=submit_update)
    submit_btn.pack(pady=20)


#Show admin screen
def show_admin_screen():
    global admin_screen
    app.withdraw()
    admin_screen = tk.Toplevel()
    admin_screen.title("Admin Screen")
    admin_screen.geometry('800x600')  # Set the size of the window to be much larger
    tk.Label(
        admin_screen, 
        text = "Admin Menu",
        bg = "white",
        fg = "black",
        font =("TkMenuFont", 14)
        ).pack()
    # Create 4 buttons with commands and pack them in the window
    button1 = tk.Button(admin_screen, text="ADD STUFF", command= show_admin_add_screen, bg = bg_color, fg = "white")
    button2 = tk.Button(admin_screen, text="DELETE STUFF", command=show_admin_delete_screen, bg = bg_color, fg = "white")
    button3 = tk.Button(admin_screen, text="VIEW STUFF", command=show_admin_view_screen, bg = bg_color, fg = "white")
    button4 = tk.Button(admin_screen, text="Log out", command= admin_logout, bg = bg_color, fg = "white")
    
    # Arrange buttons in a grid or pack them
    buttons = [button1, button2, button3, button4]
    for i, button in enumerate(buttons, start=1):
        button.pack(pady=10)

    admin_screen.protocol("WM_DELETE_WINDOW", on_closing_main_screen)
#Show admin add screen
def show_admin_add_screen():
    global admin_add_screen
    admin_screen.destroy()
    admin_add_screen = tk.Toplevel()
    admin_add_screen.title("Add Screen")
    admin_add_screen.geometry('800x600')  # Set the size of the window to be much larger
    tk.Label(
       admin_add_screen, 
        text = "Add Menu",
        bg = "white",
        fg = "black",
        font =("TkMenuFont", 14)
        ).pack()
    # Create 10 buttons with commands and pack them in the window
    button1 = tk.Button(admin_add_screen, text="Update User Weight", command=updateUserWeight, bg = bg_color, fg = "white")
    button2 = tk.Button(admin_add_screen, text="Update User Goal Weight", command=updateUserGoal, bg = bg_color, fg = "white")
    button3 = tk.Button(admin_add_screen, text="Add Equipment", command=addEqp, bg = bg_color, fg = "white")
    button4 = tk.Button(admin_add_screen, text="Add User Equipment", command=addUserEqp, bg = bg_color, fg = "white")
    button5 = tk.Button(admin_add_screen, text="Add Exercise", command=addExc, bg = bg_color, fg = "white")
    button6 = tk.Button(admin_add_screen, text="Add Muscle", command=addMuscle, bg = bg_color, fg = "white")
    button7 = tk.Button(admin_add_screen, text="Create Workout", command=createWorkout, bg = bg_color, fg = "white")
    button8 = tk.Button(admin_add_screen, text="Add an exercise to a workout", command=addExcToWorkout, bg = bg_color, fg = "white")
    button9 = tk.Button(admin_add_screen, text="Create Health Log", command=addHealthLog, bg = bg_color, fg = "white")
    button10 = tk.Button(admin_add_screen, text="Create Lift Log", command=addLiftingLog, bg = bg_color, fg = "white")
    button11 = tk.Button(admin_add_screen, text="Back", command=leave_admin_add, bg = bg_color, fg = "white")

    # Arrange buttons in a grid or pack them
    buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11]
    for i, button in enumerate(buttons, start=1):
        button.pack(pady=10)

    admin_add_screen.protocol("WM_DELETE_WINDOW", on_closing_main_screen)
#show admin delete screen
def show_admin_delete_screen():
    global admin_delete_screen
    admin_screen.destroy()
    admin_delete_screen = tk.Toplevel()
    admin_delete_screen.title("Delete Screen")
    admin_delete_screen.geometry('800x600')  # Set the size of the window to be much larger
    tk.Label(
        admin_delete_screen, 
        text = "Delete Menu",
        bg = "white",
        fg = "black",
        font =("TkMenuFont", 14)
        ).pack()
    #Create 7 buttons with commands and pack them in the window
    button1 = tk.Button(admin_delete_screen, text="Delete User Equipment", command=deleteUserEqp, bg = bg_color, fg = "white")
    button2 = tk.Button(admin_delete_screen, text="Delete Exercise", command=deleteExc, bg = bg_color, fg = "white")
    button3 = tk.Button(admin_delete_screen, text="Remove exercise from workout", command=removeExcFromWorkout, bg = bg_color, fg = "white")
    button4 = tk.Button(admin_delete_screen, text="Delete Health Log", command=deleteHealthLog, bg = bg_color, fg = "white")
    button5 = tk.Button(admin_delete_screen, text="Delete Lift Log", command=deleteliftLog, bg = bg_color, fg = "white")
    button6 = tk.Button(admin_delete_screen, text="Delete Account", command=deleteAccount, bg = bg_color, fg = "white")
    button7 = tk.Button(admin_delete_screen, text="Back", command=leave_admin_delete, bg = bg_color, fg = "white")

    # Arrange buttons in a grid or pack them
    buttons = [button1, button2, button3, button4, button5, button6, button7]
    for i, button in enumerate(buttons, start=1):
        button.pack(pady=10)

    admin_delete_screen.protocol("WM_DELETE_WINDOW", on_closing_main_screen)
#show admin view screen
def show_admin_view_screen():
    global admin_view_screen
    admin_screen.destroy()
    admin_view_screen = tk.Toplevel()
    admin_view_screen.title("View Screen")
    admin_view_screen.geometry('800x600')  # Set the size of the window to be much larger
    tk.Label(
       admin_view_screen, 
        text = "View Menu",
        bg = "white",
        fg = "black",
        font =("TkMenuFont", 14)
        ).pack()
    # Create 3 buttons with commands and pack them in the window
    button1 = tk.Button(admin_view_screen, text="Search by keyword", command=viewExcByType, bg = bg_color, fg = "white")
    button2 = tk.Button(admin_view_screen, text="Search for exercise Instructions", command=viewExcInstructions, bg = bg_color, fg = "white")
    button4 = tk.Button(admin_view_screen, text="Weight Progress", command=show_admin_progress_graph, bg = bg_color, fg = "white")
    button5 = tk.Button(admin_view_screen, text="View Max User Weight", command=display_max_weight, bg = bg_color, fg = "white")
    button6 = tk.Button(admin_view_screen, text="View Average User Weight", command=display_average_weight, bg = bg_color, fg = "white")
    button7 = tk.Button(admin_view_screen, text="View Min User Weight", command=display_min_weight, bg = bg_color, fg = "white")
    button8 = tk.Button(admin_view_screen, text="Back", command=leave_admin_view, bg = bg_color, fg = "white")

    # Arrange buttons in a grid or pack them
    buttons = [button1, button2, button4, button5, button6, button7, button8]
    for i, button in enumerate(buttons, start=1):
        button.pack(pady=10)

    admin_view_screen.protocol("WM_DELETE_WINDOW", on_closing_main_screen)

#The view Screen
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
    button1 = tk.Button(view_screen, text="Search by keyword", command=viewExcByType, bg = bg_color, fg = "white")
    button2 = tk.Button(view_screen, text="Search for exercise Instructions", command=viewExcInstructions, bg = bg_color, fg = "white")
    button4 = tk.Button(view_screen, text="Weight Progress", command=show_progress_graph, bg = bg_color, fg = "white")
    button5 = tk.Button(view_screen, text="View Max User Weight", command=display_max_weight, bg = bg_color, fg = "white")
    button6 = tk.Button(view_screen, text="View Average User Weight", command=display_average_weight, bg = bg_color, fg = "white")
    button7 = tk.Button(view_screen, text="View Min User Weight", command=display_min_weight, bg = bg_color, fg = "white")
    button8 = tk.Button(view_screen, text="Back", command=leave_view, bg = bg_color, fg = "white")

    # Arrange buttons in a grid or pack them
    buttons = [button1, button2, button4, button5, button6, button7, button8]
    for i, button in enumerate(buttons, start=1):
        button.pack(pady=10)

    view_screen.protocol("WM_DELETE_WINDOW", on_closing_main_screen)
#delete screen menu
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
    #Create 7 buttons with commands and pack them in the window
    button1 = tk.Button(delete_screen, text="Delete User Equipment", command=deleteUserEqp, bg = bg_color, fg = "white")
    button2 = tk.Button(delete_screen, text="Remove exercise from workout", command=removeExcFromWorkout, bg = bg_color, fg = "white")
    button3 = tk.Button(delete_screen, text="Delete Health Log", command=deleteHealthLog, bg = bg_color, fg = "white")
    button4 = tk.Button(delete_screen, text="Delete Lift Log", command=deleteliftLog, bg = bg_color, fg = "white")
    button5 = tk.Button(delete_screen, text="Back", command=leave_delete, bg = bg_color, fg = "white")

    # Arrange buttons in a grid or pack them
    buttons = [button1, button2, button3, button4, button5]
    for i, button in enumerate(buttons, start=1):
        button.pack(pady=10)

    delete_screen.protocol("WM_DELETE_WINDOW", on_closing_main_screen)
#add Screen menu
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
    button1 = tk.Button(add_screen, text="Update User Weight", command=updateUserWeight, bg = bg_color, fg = "white")
    button2 = tk.Button(add_screen, text="Update User Goal Weight", command=updateUserGoal, bg = bg_color, fg = "white")
    button3 = tk.Button(add_screen, text="Add User Equipment", command=addUserEqp, bg = bg_color, fg = "white")
    button4 = tk.Button(add_screen, text="Create Workout", command=createWorkout, bg = bg_color, fg = "white")
    button5 = tk.Button(add_screen, text="Add an exercise to a workout", command=addExcToWorkout, bg = bg_color, fg = "white")
    button6 = tk.Button(add_screen, text="Create Health Log", command=addHealthLog, bg = bg_color, fg = "white")
    button7 = tk.Button(add_screen, text="Create Lift Log", command=addLiftingLog, bg = bg_color, fg = "white")
    button8 = tk.Button(add_screen, text="Back", command=leave_add, bg = bg_color, fg = "white")

    # Arrange buttons in a grid or pack them
    buttons = [button1, button2, button3, button4, button5, button6, button7, button8]
    for i, button in enumerate(buttons, start=1):
        button.pack(pady=10)

    add_screen.protocol("WM_DELETE_WINDOW", on_closing_main_screen)
#Show main menu
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
#close all the windows
def on_closing_main_screen():
    app.destroy()
#Login submission 
def submit_login():
    con = db.connect("tuple.db")
    cur = con.cursor()
    try:
        user_id = entry_username.get()
        password = entry_password.get()
        cur.execute("SELECT password FROM user WHERE user_id = ?", (user_id,))
        stored_password = cur.fetchone()
        if stored_password is None:
            messagebox.showwarning("Login Failed", "User is not found.")
        elif password == "Admin123" and user_id == '911':
            messagebox.showinfo("Admin Login Successful", "Welcome Admin!")
            show_admin_screen()
        elif password == stored_password[0]:
            messagebox.showinfo("Login Successful", "Welcome!")
            show_main_screen()
        else:
            messagebox.showwarning("Login Failed", "Incorrect password.")
    except db.Error as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")
    finally:
        con.close()
#Account creation window
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
#account creation method
def create_account():
    # Extract values directly from entry widgets
    user_id = entry_user_id.get()
    password = entry_password.get()
    full_name = entry_full_name.get()
    weight = entry_weight.get()
    goal_weight = entry_goal_weight.get()
    goal_macros = entry_goal_macros.get()

    # Connect to the database and insert the new user
    con = db.connect("tuple.db")
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
#Login/Create new account window 
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
#GET MAX FUNCS
def get_max_weight(db_path='tuple.db'):
    conn = db.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(weight) FROM user")
    max_weight = cursor.fetchone()[0]
    conn.close()
    return max_weight

def get_min_weight(db_path='tuple.db'):
    conn = db.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT MIN(weight) FROM user")
    min_weight = cursor.fetchone()[0]
    conn.close()
    return min_weight

def get_average_weight(db_path='tuple.db'):
    conn = db.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(weight) FROM user")
    average_weight = cursor.fetchone()[0]
    conn.close()
    return average_weight if average_weight else 0
#DISPLAY MAX FUNCS
def display_max_weight():
    max_weight = get_max_weight()
    messagebox.showinfo("Maximum Weight", f"The maximum weight is {max_weight} lbs")

def display_min_weight():
    min_weight = get_min_weight()
    messagebox.showinfo("Minimum Weight", f"The minimum weight is {min_weight} lbs")

def display_average_weight():
    avg_weight = get_average_weight()
    messagebox.showinfo("Average Weight", f"The average weight is {avg_weight:.2f} lbs")

def show_progress_graph():
    # Create the graph window
    global progress_window
    view_screen.destroy()
    progress_window = tk.Toplevel()
    progress_window.title("Progress")
    progress_window.geometry("500x500")

    # the figure that will contain the plot 
    fig = Figure(figsize = (5, 5), dpi = 100) 
  
    # list of squares 
    y = [i**2 for i in range(101)] 
  
    # adding the subplot 
    plot1 = fig.add_subplot(111) 
  
    # plotting the graph 
    plot1.plot(y) 
  
    # creating the Tkinter canvas 
    # containing the Matplotlib figure 
    canvas = FigureCanvasTkAgg(fig, master = progress_window)   
    canvas.draw() 
  
    # placing the canvas on the Tkinter window 
    canvas.get_tk_widget().pack() 
  
    # creating the Matplotlib toolbar 
    toolbar = NavigationToolbar2Tk(canvas, progress_window) 
    toolbar.update() 
  
    # placing the toolbar on the Tkinter window 
    canvas.get_tk_widget().pack() 

    button = tk.Button(progress_window, text="Back", command=leave_graph, bg = bg_color, fg = "white")
    button.pack(pady=10)

def show_admin_progress_graph():
    # Create the graph window
    global admin_progress_window
    admin_view_screen.destroy()
    admin_progress_window = tk.Toplevel()
    admin_progress_window.title("Progress")
    admin_progress_window.geometry("500x500")

    # the figure that will contain the plot 
    fig = Figure(figsize = (5, 5), dpi = 100) 
  
    # list of squares 
    y = [i**2 for i in range(101)] 
  
    # adding the subplot 
    plot1 = fig.add_subplot(111) 
  
    # plotting the graph 
    plot1.plot(y) 
  
    # creating the Tkinter canvas 
    # containing the Matplotlib figure 
    canvas = FigureCanvasTkAgg(fig, master = admin_progress_window)   
    canvas.draw() 
  
    # placing the canvas on the Tkinter window 
    canvas.get_tk_widget().pack() 
  
    # creating the Matplotlib toolbar 
    toolbar = NavigationToolbar2Tk(canvas, admin_progress_window) 
    toolbar.update() 
  
    # placing the toolbar on the Tkinter window 
    canvas.get_tk_widget().pack() 

    button = tk.Button(admin_progress_window, text="Back", command=leave_admin_graph, bg = bg_color, fg = "white")
    button.pack(pady=10)




#Back buttons/Logout
def leave_graph():
    progress_window.destroy()
    show_view_screen()
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
#admin back buttons
def leave_admin_add():
    admin_add_screen.destroy()
    show_admin_screen()

def leave_admin_delete():
    admin_delete_screen.destroy()
    show_admin_screen()

def leave_admin_view():
    admin_view_screen.destroy()
    show_admin_screen()

def leave_admin_graph():
    progress_window.destroy()
    show_view_screen()

def admin_logout():
    admin_screen.destroy()
    setup_login_window()


setup_login_window()
app.mainloop()

#basically the program starts in a login/create user screen then the user is taken to a new window where the user can choose to add/delete/view data in the database the 
#the view page has things like view the instructions and the query to search exercises based on equipment and the add/delete would be like adding and deleting data from tables