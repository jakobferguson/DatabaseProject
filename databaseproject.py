import sqlite3 as db
from getpass import getpass


def genTable():
        con = db.connect("CS2300 PROJECT/tuple.db")
        cur = con.cursor()
        # Create user table
        command1 = """CREATE TABLE IF NOT EXISTS
        user(user_id INTEGER PRIMARY KEY, full_name TEXT, password TEXT, weight INTEGER, g_weight INTEGER, g_macros INT)"""
        cur.execute(command1)

        # Create the equipment (eqp) table
        command2 = """CREATE TABLE IF NOT EXISTS
        eqp(eqp_name TEXT PRIMARY KEY)"""
        cur.execute(command2)

        # Create the equipment owned (eqp_owned) table
        command3 = """CREATE TABLE IF NOT EXISTS
        eqp_owned(user_id INTEGER, eqp_name TEXT, 
                FOREIGN KEY(user_id) REFERENCES user(user_id), 
                FOREIGN KEY(eqp_name) REFERENCES eqp(eqp_name))"""
        cur.execute(command3)

        # Create the exercise table
        command4 = """CREATE TABLE IF NOT EXISTS
        exercise(exc_name TEXT PRIMARY KEY, instruction TEXT, type TEXT, eqp_name TEXT,
                FOREIGN KEY(eqp_name) REFERENCES eqp(eqp_name))"""
        cur.execute(command4)

        # Create the muscle used (m_used) table
        command5 = """CREATE TABLE IF NOT EXISTS
        m_used(exc_name TEXT, muscle TEXT,
        FOREIGN KEY(exc_name) REFERENCES exercise(exc_name),
        PRIMARY KEY(exc_name, muscle))"""
        cur.execute(command5)

        # Create the workout table
        command6 = """CREATE TABLE IF NOT EXISTS
        workout(wid INTEGER PRIMARY KEY, w_name TEXT, type TEXT, modifiable TEXT, user_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES user(user_id))"""
        cur.execute(command6)

        # Create the health log table
        command7 = """CREATE TABLE IF NOT EXISTS
        health_log(log_id INTEGER PRIMARY KEY, user_id INTEGER, weight INTEGER,
                FOREIGN KEY(user_id) REFERENCES user(user_id))"""
        cur.execute(command7)

        # Create the lifting log table
        command8 = """CREATE TABLE IF NOT EXISTS
        lift_log(log_id INTEGER PRIMARY KEY, user_id INTEGER, exc_name TEXT, weight INTEGER, sets INTEGER, reps INTEGER,
                FOREIGN KEY(user_id) REFERENCES user(user_id),
                FOREIGN KEY(exc_name) REFERENCES exercise(exc_name))"""
        cur.execute(command8)
        #create the exc_included table
        command9 = """CREATE TABLE IF NOT EXISTS 
                exc_included(wid INTEGER, exc_name TEXT, exc_sets INTEGER NOT NULL, exc_reps INTEGER NOT NULL,
                PRIMARY KEY (wid, exc_name),
                FOREIGN KEY (wid) REFERENCES workout(wid),
                FOREIGN KEY (exc_name) REFERENCES exercise(exc_name))
                """
        cur.execute(command9)

#create account function
def createAccount():
        # connect to database
        con = db.connect("CS2300 PROJECT/tuple.db")
        cur = con.cursor()
        #Prompt the user to enter the username and password to enter 
        user_id = input("Create your user id: ")
        password = getpass("Create your password: ")
        #promt the user for their attributes
        fullname = input("Give your Full Name: ")
        weight = input("Enter your current weight: ")
        g_weight = input("Enter your goal weight: ")
        g_macros = input("Enter your goal macros: ")
        #Generate user_id
        

        try:
                cur.execute("INSERT INTO user(user_id, full_name, password, weight, g_weight, g_macros) VALUES(?,?,?,?,?,?)",
                        (user_id, fullname, password, weight, g_weight, g_macros))
                con.commit()
                print("Account creation Successful")
        except db.IntegrityError as e:
                print("Error: Could not create account. Username might already exist.")
                print(e)
        except Exception as e:
                print("An error occurred:", e)
        finally:
                con.close()

#create the login function
def login():
    con = db.connect("CS2300 PROJECT/tuple.db")
    cur = con.cursor()

    try:
        # Prompt user for their login details
        user_id = input("Enter your user id: ")
        password = getpass("Enter your password: ")

        # Query to find the user
        cur.execute("SELECT password FROM user WHERE user_id = ?", (user_id,))
        stored_password = cur.fetchone()

        if stored_password is None:
            print("Login Failed: User is not found.")
            return login()  # Use return to avoid deep recursion stack issues
        else:
            if password == stored_password[0]:
                print("Login Successful!")
                return True
            else:
                print("Login Failed: Incorrect password.")
                return login()  # Use return to avoid deep recursion stack issues

    except db.Error as e:
        print(f"An error occurred: {e}")
    finally:
        con.close()
#delete an account 
def deleteAccount():
        user_id = input("Enter the user id of the account that you would like to delete: ")
        #ask the user to confirm the deletion
        confirm = input(f"Are you sure you want to delete the accoutn '{user_id}'? This action cannot be undone. Type 'yes' to confirm: ")
        if confirm.lower() == 'yes':
                con = db.connect("CS2300 PROJECT/tuple.db")
                cur = con.cursor()
                #execute the delete query 
                cur.execute("DELETE FROM user WHERE user_id = ?",(user_id,))
                if cur.rowcount == 0:
                        print("No user found")
                else:
                        con.commit()
                        print("Account deleted successfully")
                con.close()
#update the users weight
def updateUserWeight():
        #connect to db
        con = db.connect("CS2300 PROJECT/tuple.db")
        cur = con.cursor()
        #prompt the user to enter the new weight
        user_id = input("Enter the user id of the user who's weight we are updating: ")
        new_weight = input("Enter the new weight of the user: ")
        #Make the update statement
        cur.execute("UPDATE user SET weight = ? WHERE user_id = ?", (new_weight, user_id))

        if cur.rowcount == 0:
                print("There was no user found.")
        else:
                con.commit()
                print("User weight updated successfully")
        con.close()
#update the users weight goal
def updateUserGoal():
        #connect to db
        con = db.connect("CS2300 PROJECT/tuple.db")
        cur = con.cursor()
        #prompt the user to enter the new weight
        user_id = input("Enter the user id of the user who's goal we are updating: ")
        new_goal = input("Enter the new goal weight of the user: ")
        #Make the update statement
        cur.execute("UPDATE user SET g_weight = ? WHERE user_id = ?", (new_goal, user_id))

        if cur.rowcount == 0:
                print("There was no user found.")
        else:
                con.commit()
                print("User goal updated successfully")
        con.close()
#add equipment
def addEqp():
        #connect to db
        con = db.connect("CS2300 PROJECT/tuple.db")
        cur = con.cursor()
        # ask for the name of the equipment
        eqp_name = input("What is the name of the Equipment: ")
        cur.execute("INSERT INTO eqp(eqp_name) VALUES(?)",(eqp_name,))
        con.commit()
        print("Equipment successfully added")

#add user equipment
def addUserEqp():
        #connect to db
        con = db.connect("CS2300 PROJECT/tuple.db")
        cur = con.cursor()
        #Input equipment name
        user_id =  input("Enter the user id: ")
        eqp_name = input("Enter the name of the equipment: ")
        #check if the equipment exists in the eqp table
        cur.execute("SELECT eqp_name FROM eqp WHERE eqp_name = ? ", (eqp_name,))
        if cur.fetchone() is None:
                print("Equipment not found")
        else:
                #check if the equipment is already owned by the user
                cur.execute("SELECT * FROM eqp_owned WHERE user_id =? AND eqp_name = ?", (user_id, eqp_name))
                if cur.fetchone() is not None:
                        print("You already own this equipment.")
                else:
                        try:
                                cur.execute("INSERT INTO eqp_owned(user_id, eqp_name) VALUES(?, ?)", (user_id, eqp_name))
                                con.commit()
                                print("Equipment added successfully")
                        except db.IntegrityError:
                                print("Failed to add equipment. Make sure that the equipment name and user id are correct")
                        except Exception as e:
                                print(f"An unexpected error occured: {e}")
                con.close()
#delete user equipment
def deleteUserEqp():
        con = db.connect("CS2300 PROJECT/tuple.db")
        cur = con.cursor()
        #Input the name of the equipment 
        user_id = input("Enter your user id: ")
        eqp_name = input("Enter the name of the equipment: ")
        #query to see if the equipment exists
        cur.execute("SELECT * FROM eqp_owned WHERE user_id = ? AND eqp_name = ?", (user_id, eqp_name))
        if cur.fetchone() is None:
                print("No equipment found")
        else:
                try:
                        cur.execute("DELETE FROM eqp_owned WHERE user_id = ? AND eqp_name = ?", (user_id, eqp_name))
                        con.commit()
                        print("Equipment removed from your account successfully")
                except db.Error as e:
                        print(f"An error occurred: {e}")
        con.close()
#Add an exercise
def addExc():
        con = db.connect("CS2300 PROJECT/tuple.db")
        cur = con.cursor()
        #input exercise details
        exc_name = input("Enter the name of the exercise: ")
        desc = input("Enter the description of the exercise: ")
        xType = input("Enter the type of exercice it is (e.g., cardio, strength, flexibility): ")
        eqp_name = input("Enter the name of the equipment required(If none leave it blank): ")

        #check if the equipment exists if not empty

        if eqp_name:
                cur.execute("SELECT eqp_name FROM eqp WHERE eqp_name = ?", (eqp_name,))
                if cur.fetchone() is None:
                        print("Equipment not found. Please add the equipment first :)")
                        return
        #Insert the data into the db
        try:
                cur.execute("INSERT INTO exercise (exc_name, instruction, Type, eqp_name ) VALUES(?,?,?,?)",(exc_name, desc, xType, eqp_name or None))
                con.commit()
                print("The exercise has been added successfully")
        except db.IntegrityError:
                print("An exercise with this name already exists")
        except Exception as e:
                print(f"An error has occured: {e}")
        finally:
                con.close()
#Delete exercises
def deleteExc():
        con = db.connect("CS2300 PROJECT/tuple.db")
        cur = con.cursor()
        #input the exercise name to delete
        exc_name = input("Enter the name of the exercise you would like to delete: ")

        #verify the exercice exists
        cur.execute("SELECT exc_name FROM exercise WHERE exc_name = ?", (exc_name,))
        if cur.fetchone() is None:
                print("The exercice you have listed cannot be found")
        else: 
                try:
                        cur.execute("DELETE FROM exercise WHERE exc_name = ?", (exc_name,))
                        con.commit()
                        print("Deletion successful")
                except db.Error as e:
                        print(f"An Error has occurred: {e}")
def viewExcByType():
        con = db.connect("CS2300 PROJECT/tuple.db")
        cur = con.cursor()
        #input the keyword to search for 
        keyword = input("Enter the keyword you would like to search by (muscle, equipment, or type): ")
    
        # Prepare the search query to join exercise and m_used tables
        query = """
        SELECT e.exc_name, e.instruction, e.type, e.eqp_name, m.muscle
        FROM exercise e
        LEFT JOIN m_used m ON e.exc_name = m.exc_name
        WHERE e.type LIKE ? OR e.eqp_name LIKE ? OR m.muscle LIKE ?
        """
        # Execute the query
        cur.execute(query, ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))

        # Fetch all the results
        results = cur.fetchall()
        if results:
                print(f"Found {len(results)} exercises matching '{keyword}':")
                for exc in results:
                        print(f"Name: {exc[0]}, Instructions: {exc[1]}, Type: {exc[2]}, Equipment: {exc[3]}, Muscle: {exc[4]}")
        else:
                print("No exercises were found containing that keyword")
        
        con.close()
#add a muscle to muscle used
def addMuscle():
        con = db.connect("CS2300 PROJECT/tuple.db")
        cur = con.cursor()
        exc_name = input("Enter the name of the exercise: ")
        muscle = input("Enter the name of the muscle targeted: ")

        # First, check if the exercise exists in the 'exercise' table
        cur.execute("SELECT exc_name FROM exercise WHERE exc_name = ?", (exc_name,))
        if cur.fetchone() is None:
                print("The exercise you have listed cannot be found. Please add the exercise first.")
                con.close()
                return
        try:
                cur.execute("INSERT INTO m_used (exc_name, muscle) VALUES (?, ?)", (exc_name, muscle))
                con.commit()
                print("Muscle usage added successfully.")
        except db.IntegrityError:
                print("An error occurred while trying to add the muscle usage.")
        except Exception as e:
                print(f"An error has occurred: {e}")
        finally:
                con.close()
def viewExcInstructions(exercise):
        # Connect to the SQLite database
        con = db.connect("CS2300 PROJECT/tuple.db")
        cur = con.cursor()

        # Prepare the query to fetch the instruction for the specified exercise
        query = "SELECT instruction FROM exercise WHERE exc_name = ?"

        # Execute the query
        cur.execute(query, (exercise,))

        # Fetch the result
        result = cur.fetchone()
        if result:
                print(f"Instructions for {exercise}: {result[0]}")
        else:
                print(f"No instructions found for {exercise}")

        con.close()
#create a workout
def createWorkout():
        con = db.connect("CS2300 PROJECT/tuple.db")
        cur = con.cursor()
        #get input from the user
        w_name = input("Name the workout: ")
        wid = input("Give your workout a number: ")
        modifiable = 'no' # user created workouts aren't modifiable
        w_type = input("Enter the type of workout(Upper Body, Lower body, etc.: )")
        user_id = input("Enter your user id: ")
        #insert the data
        try:
                cur.execute("INSERT INTO workout (w_name, modifiable, wid, type, user_id) VALUES(?,?,?,?,?)", (w_name, w_type, wid, modifiable, user_id))
                con.commit()
                print("New Workout created successfully.")
        except db.IntegrityError as e:
                print("An error occured: A workout with this wid already exists")
        except Exception as e: 
                print(f"An unexpected error occurred: {e}")
        finally: 
                con.close()
#add a exercise to a workout
def addExcToWorkout():
        con = db.connect("CS2300 PROJECT/tuple.db")
        cur = con.cursor()
        #ask for the workout id and exercise name
        wid = input("Enter the workout number that you would like to add to: ")
        exc_name = input("Enter the name of the exercise you would like to add: ")
        reps = input("How many reps?: ")
        sets = input("How many sets?: ")

        #verify that the exercise and workout exists
        cur.execute("SELECT exc_name FROM exercise WHERE exc_name = ?", (exc_name,))
        if cur.fetchone() is None:
                print("The exercice you have listed cannot be found")
        cur.execute("SELECT wid FROM workout WHERE wid = ?", (wid,))
        if cur.fetchone() is None:
                print("The workout you have listed cannot be found")

        #insert the exercise into the workout
        try:
                cur.execute("INSERT INTO exc_included(wid, exc_name, exc_reps, exc_sets) VALUES (?,?,?,?)", (wid,exc_name, sets, reps))
                con.commit()
                print("Exercise added to the workout successfully.")
        except db.IntegrityError:
                print("This exercise is already included in the workout.")
        except Exception as e:
                print(f"An unexpected error occurred: {e}")
        finally:
                con.close()   
#remove an exercise from the workout   
def removeExcFromWorkout():
        con = db.connect("CS2300 PROJECT/tuple.db")
        cur = con.cursor()
        #ask the user which exercise they would like to remove 
        wid = input("Enter the number of the workout you would like to remove an exercise from: ")
        exc_name = input("Enter the name of the exercise that you would like to remove: ")

        # First, verify that the exercise exists within the specified workout
        cur.execute("SELECT * FROM exc_included WHERE wid = ? AND exc_name = ?", (wid, exc_name))
        if cur.fetchone() is None:
                print("No such exercise found in the specified workout.")
                con.close()
                return

        # Perform the deletion
        try:
                cur.execute("DELETE FROM exc_included WHERE wid = ? AND exc_name = ?", (wid, exc_name))
                con.commit()
                print("Exercise successfully removed from the workout.")
        except db.Error as e:
                print(f"An error occurred: {e}")
        finally:
                con.close()

#add health log
def addHealthLog():
        print("f")
        #connect to db
        con = db.connect("CS2300 PROJECT/tuple.db")
        cur = con.cursor()
        # get the time
        log_id = input("Enter the this logs number: ")
        # Get user ID and weight from the user
        user_id = input("Enter your user ID: ")
        weight = input("Enter your weight: ")

        # Insert the health log data into the database
        try:
                cur.execute("INSERT INTO health_log (log_id, user_id, weight) VALUES (?, ?, ?)", 
                        (log_id, user_id, weight))
                con.commit()
                print("Health log added successfully.")
        except db.IntegrityError:
                print("There was an issue adding the health log. Make sure the user ID exists.")
        except Exception as e:
                print(f"An error occurred: {e}")
        finally:
                con.close()
#delete a log
def deleteHealthLog():
        # Connect to the SQLite database
        con = db.connect("CS2300 PROJECT/tuple.db")
        cur = con.cursor()

        # Ask for the log ID to delete
        log_id = input("Enter the log number of the health log you want to delete: ")

        # First, verify that the log entry exists
        cur.execute("SELECT log_id FROM health_log WHERE log_id = ?", (log_id,))
        if cur.fetchone() is None:
                print("No such health log found.")
                con.close()
                return

        # Perform the deletion
        try:
                cur.execute("DELETE FROM health_log WHERE log_id = ?", (log_id,))
                con.commit()
                print("Health log deleted successfully.")
        except db.Error as e:
                print(f"An error occurred: {e}")
        finally:
                con.close()
#add a lifting log
def addLiftingLog():
        # Connect to the SQLite database
        con = db.connect("CS2300 PROJECT/tuple.db")
        cur = con.cursor()

        # Get user ID, weight lifted, number of reps, and sets from the user
        log_id = input("Enter the Log number: ")
        user_id = input("Enter your user ID: ")
        weight = input("Enter the weight lifted (in lbs or kg): ")
        reps = input("Enter the number of reps: ")
        sets = input("Enter the number of sets: ")

        

        # Insert the lifting log data into the database
        try:
                cur.execute("INSERT INTO lift_log (log_id, user_id, weight, reps, sets) VALUES (?, ?, ?, ?, ?)",
                        (log_id, user_id, weight, reps, sets))
                con.commit()
                print("Lifting log added successfully.")
        except db.IntegrityError:
                print("There was an issue adding the lifting log. Make sure the user ID exists and data is correct.")
        except Exception as e:
                print(f"An error occurred: {e}")
        finally:
                con.close()
#delete a lifting log
def deleteliftLog():
        # Connect to the SQLite database
        con = db.connect("CS2300 PROJECT/tuple.db")
        cur = con.cursor()

        # Ask for the log ID to delete
        log_id = input("Enter the log number of the lift log you want to delete: ")

        # First, verify that the log entry exists
        cur.execute("SELECT log_id FROM lift_log WHERE log_id = ?", (log_id,))
        if cur.fetchone() is None:
                print("No such health log found.")
                con.close()
                return

        # Perform the deletion
        try:
                cur.execute("DELETE FROM lift_log WHERE log_id = ?", (log_id,))
                con.commit()
                print("Lift log deleted successfully.")
        except db.Error as e:
                print(f"An error occurred: {e}")
        finally:
                con.close()



