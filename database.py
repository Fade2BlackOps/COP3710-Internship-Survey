from tkinter import *
from tkinter import messagebox
import sqlite3

win_login = Tk()
win_login.title('Login')
win_login.iconbitmap('dinosaur_icon.ico')
win_login.geometry("200x200")


# Create Submit Function for Database
def newInternship_submit():
    # Create a database or connect to one
    conn = sqlite3.connect('survey_app.db')
    # Create cursor
    cursor = conn.cursor()

    # Generate new internship ID
    cursor.execute("SELECT * FROM internships")
    records = cursor.fetchall()

    # Count results
    count_internships = 0
    for internships in records:
        count_internships += 1

    generated_ID = count_internships + 1001

    # Insert Into Table
    cursor.execute("INSERT INTO internships VALUES (:ID, :date_start, :date_end, :company, :description)",
                   {
                       'ID': generated_ID,
                       'date_start': entry_newIntern_start.get(),
                       'date_end': entry_newIntern_end.get(),
                       'company': entry_newIntern_company.get(),
                       'description': entry_newIntern_role.get()
                   })

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    win_newInternship.destroy()


# function for adding new internship
def new_internship():
    # Create a database or connect to one
    conn = sqlite3.connect('survey_app.db')
    # Create cursor
    cursor = conn.cursor()

    global win_newInternship
    win_newInternship = Tk()
    win_newInternship.title('Add New Internship')
    win_newInternship.iconbitmap('dinosaur_icon.ico')
    win_newInternship.geometry("400x400")

    global entry_newIntern_company, entry_newIntern_start, entry_newIntern_end, entry_newIntern_role

    label_newIntern_company = Label(win_newInternship, text="What company did you intern at?")
    label_newIntern_company.pack()
    entry_newIntern_company = Entry(win_newInternship, width=30)
    entry_newIntern_company.pack(pady=(0, 20))

    label_newIntern_start = Label(win_newInternship, text="What date did you start? (FORMAT: YYYY-MM-DD)")
    label_newIntern_start.pack()
    entry_newIntern_start = Entry(win_newInternship, width=30)
    entry_newIntern_start.pack(pady=(0, 20))

    label_newIntern_end = Label(win_newInternship, text="What date did you finish? (FORMAT: YYYY-MM-DD)")
    label_newIntern_end.pack()
    entry_newIntern_end = Entry(win_newInternship, width=30)
    entry_newIntern_end.pack(pady=(0, 20))

    label_newIntern_role = Label(win_newInternship, text="What was your specific role called?")
    label_newIntern_role.pack()
    entry_newIntern_role = Entry(win_newInternship, width=30)
    entry_newIntern_role.pack(pady=(0, 20))

    # Tags for internship
    label_newTag = Label(win_newInternship, text="What tags would you like to associate with this internship?")
    label_newTag.pack()
    entry_newTag = Entry(win_newInternship, width=30)
    entry_newTag.pack(pady=(0, 20))

    # Submit button
    button_addIntern = Button(win_newInternship, text='Add Internship', command=newInternship_submit)
    button_addIntern.pack(pady=(30, 0))


def intern_update():
    # Create a database or connect to one
    conn = sqlite3.connect('survey_app.db')
    # Create cursor
    cursor = conn.cursor()

    cursor.execute("""UPDATE internships SET
        date_start = :start,
        date_end = :end,
        company = :company,
        description = :role

        WHERE ID = :intern_id""",
                   {
                       'start': entry_editIntern_start.get(),
                       'end': entry_editIntern_end.get(),
                       'company': entry_editIntern_company.get(),
                       'role': entry_editIntern_role.get(),
                       'intern_id': entry_home_internID.get()
                   })

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    win_intern_editor.destroy()


# function for editing internship
def edit_internship():
    global win_intern_editor
    win_intern_editor = Tk()
    win_intern_editor.title('Update an Internship')
    win_intern_editor.iconbitmap('dinosaur_icon.ico')
    win_intern_editor.geometry("400x400")

    # Create a database or connect to one
    conn = sqlite3.connect('survey_app.db')
    # Create cursor
    cursor = conn.cursor()

    record_id = entry_home_internID.get()
    # Query the database
    cursor.execute("SELECT * FROM internships WHERE ID = " + record_id)
    records = cursor.fetchall()

    # Create global variables for text box names
    global entry_editIntern_company, entry_editIntern_start, entry_editIntern_end, entry_editIntern_role

    label_editIntern_company = Label(win_intern_editor, text="What company did you intern at?")
    label_editIntern_company.pack()
    entry_editIntern_company = Entry(win_intern_editor, width=30)
    entry_editIntern_company.pack(pady=(0, 20))

    label_editIntern_start = Label(win_intern_editor, text="What date did you start? (FORMAT: YYYY-MM-DD)")
    label_editIntern_start.pack()
    entry_editIntern_start = Entry(win_intern_editor, width=30)
    entry_editIntern_start.pack(pady=(0, 20))

    label_editIntern_end = Label(win_intern_editor, text="What date did you finish? (FORMAT: YYYY-MM-DD)")
    label_editIntern_end.pack()
    entry_editIntern_end = Entry(win_intern_editor, width=30)
    entry_editIntern_end.pack(pady=(0, 20))

    label_editIntern_role = Label(win_intern_editor, text="What was your specific role called?")
    label_editIntern_role.pack()
    entry_editIntern_role = Entry(win_intern_editor, width=30)
    entry_editIntern_role.pack(pady=(0, 20))

    # Loop through results
    for internship in records:
        entry_editIntern_company.insert(0, internship[3])
        entry_editIntern_start.insert(0, internship[1])
        entry_editIntern_end.insert(0, internship[2])
        entry_editIntern_role.insert(0, internship[4])

    # Create a save button to save edited record
    update_btn = Button(win_intern_editor, text="Update Internship Record", command=intern_update)
    update_btn.pack(pady=10, padx=10, ipadx=145)


# function for showing all internship
def show_internships():
    win_show_internships = Tk()
    win_show_internships.title('Showing ALL Internships')
    win_show_internships.iconbitmap('dinosaur_icon.ico')
    win_show_internships.geometry('800x400')

    # Create a database or connect to one
    conn = sqlite3.connect('survey_app.db')
    # Create cursor
    cursor = conn.cursor()

    # list of submitted internships for a student
    # Query the database
    cursor.execute("SELECT * FROM internships")
    records = cursor.fetchall()

    print_internships = ''
    print_internships += "ID:\tStart Date:\tEnd Date:\tCompany:\tRole:\n"
    print_internships += "--------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
    for internship in records:
        print_internships += str(internship[0]) + "\t" + str(internship[1]) + "\t" + str(internship[2]) + "\t" + str(
            internship[3]) + "\t\t" + str(internship[4]) + "\n"

    query_label = Label(win_show_internships, text=print_internships, justify=LEFT)
    query_label.pack()


def survey_submit():
    # Create a database or connect to one
    conn = sqlite3.connect('survey_app.db')
    # Create cursor
    cursor = conn.cursor()

    # Generate new internship ID
    cursor.execute("SELECT * FROM surveys")
    records = cursor.fetchall()

    # Count results
    count_surveys = 0
    for survey in records:
        count_surveys += 1

    generated_ID = count_surveys + 1000000001

    # Insert Into Table
    cursor.execute("INSERT INTO surveys VALUES (:ID, :student_ID, :internship_ID, :company, :duty_description)",
                   {
                       'ID': generated_ID,
                       'student_ID': user_ID,
                       'internship_ID': entry_newSurvey_internID.get(),
                       'company': entry_newSurvey_company.get(),
                       'duty_description': entry_newSurvey_describe.get()
                   })

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    win_newSurvey.destroy()


def new_survey():
    global win_newSurvey
    win_newSurvey = Tk()
    win_newSurvey.title('New Survey')
    win_newSurvey.iconbitmap('dinosaur_icon.ico')
    win_newSurvey.geometry('400x400')

    global entry_newSurvey_internID, entry_newSurvey_company, entry_newSurvey_describe

    label_newSurvey_internID = Label(win_newSurvey, text="What internship did you complete? (Enter internship ID)")
    label_newSurvey_internID.pack()
    entry_newSurvey_internID = Entry(win_newSurvey, width=30)
    entry_newSurvey_internID.pack(pady=(0, 20))

    label_newSurvey_company = Label(win_newSurvey, text="What company was that internship with?")
    label_newSurvey_company.pack()
    entry_newSurvey_company = Entry(win_newSurvey, width=30)
    entry_newSurvey_company.pack(pady=(0, 20))

    label_newSurvey_describe = Label(win_newSurvey, text="Briefly describe your experience during the internship?")
    label_newSurvey_describe.pack()
    entry_newSurvey_describe = Entry(win_newSurvey, width=30)
    entry_newSurvey_describe.pack(pady=(0, 20))

    label_newSurvey_tags = Label(win_newSurvey, text="What tags would you like to associate with this survey?")
    label_newSurvey_tags.pack()
    entry_newSurvey_tags = Entry(win_newSurvey, width=30)
    entry_newSurvey_tags.pack(pady=(0, 20))

    # Submit button
    button_addIntern = Button(win_newSurvey, text='Submit Survey', command=survey_submit)
    button_addIntern.pack(pady=(30, 0))


def show_Surveys():
    # Create a database or connect to one
    conn = sqlite3.connect('survey_app.db')
    # Create cursor
    cursor = conn.cursor()

    win_showSurveys = Tk()
    win_showSurveys.title('Showing ALL Surveys')
    win_showSurveys.iconbitmap('dinosaur_icon.ico')
    win_showSurveys.geometry("800x400")

    # list of submitted surveys for a student
    cursor.execute("SELECT * FROM surveys")
    records = cursor.fetchall()

    print_surveys = ""
    print_surveys += "ID:\t\tStudent ID:\tInternship ID:\tCompany\tDuty Description:\n"
    print_surveys += "-------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
    for survey in records:
        print_surveys += str(survey[0]) + "\t" + str(survey[1]) + "\t\t" + str(survey[2]) + "\t\t" + str(
            survey[3]) + "\t\t" + str(survey[4]) + "\n"

    query_label = Label(win_showSurveys, text=print_surveys, justify=LEFT)
    query_label.pack()


def survey_update():
    # Create a database or connect to one
    conn = sqlite3.connect('survey_app.db')
    # Create cursor
    cursor = conn.cursor()

    cursor.execute("""UPDATE surveys SET
        internship_ID = :intern_id,
        company = :company,
        duty_description = :description

        WHERE ID = :survey_id""",
                   {
                       'intern_id': entry_editSurvey_internID.get(),
                       'company': entry_editSurvey_company.get(),
                       'description': entry_editSurvey_describe.get(),
                       'survey_id': entry_home_surveyID.get()
                   })

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    win_editSurvey.destroy()


def edit_Survey():
    global win_editSurvey
    win_editSurvey = Tk()
    win_editSurvey.title('Edit Survey')
    win_editSurvey.iconbitmap('dinosaur_icon.ico')
    win_editSurvey.geometry('400x400')

    # Create a database or connect to one
    conn = sqlite3.connect('survey_app.db')
    # Create cursor
    cursor = conn.cursor()

    # global variables
    record_id = entry_home_surveyID.get()
    # Query the database
    cursor.execute("SELECT * FROM surveys WHERE ID = " + record_id)
    records = cursor.fetchall()

    # Create global variables for text box names
    global entry_editSurvey_internID, entry_editSurvey_company, entry_editSurvey_describe

    label_editSurvey_internID = Label(win_editSurvey, text="What internship did you complete? (Enter internship ID)")
    label_editSurvey_internID.pack()
    entry_editSurvey_internID = Entry(win_editSurvey, width=30)
    entry_editSurvey_internID.pack(pady=(0, 20))

    label_editSurvey_company = Label(win_editSurvey, text="What company was that internship with?")
    label_editSurvey_company.pack()
    entry_editSurvey_company = Entry(win_editSurvey, width=30)
    entry_editSurvey_company.pack(pady=(0, 20))

    label_editSurvey_describe = Label(win_editSurvey, text="Briefly describe your experience during the internship?")
    label_editSurvey_describe.pack()
    entry_editSurvey_describe = Entry(win_editSurvey, width=30)
    entry_editSurvey_describe.pack(pady=(0, 20))

    label_editSurvey_role = Label(win_editSurvey, text="What tags would you like to associate with this survey?")
    label_editSurvey_role.pack()
    entry_editSurvey_role = Entry(win_editSurvey, width=30)
    entry_editSurvey_role.pack(pady=(0, 20))

    # Loop through results
    for survey in records:
        entry_editSurvey_internID.insert(0, survey[2])
        entry_editSurvey_company.insert(0, survey[3])
        entry_editSurvey_describe.insert(0, survey[4])

    # Create a save button to save edited record
    update_btn = Button(win_editSurvey, text="Update Survey Record", command=survey_update)
    update_btn.pack(pady=10, padx=10, ipadx=145)


# Set global ID and name to submitted info
def setUserInfo(name, ID):
    global user_ID
    global user_name
    user_ID = ID
    user_name = name
    home_page()


# after logging in...
def home_page():
    win_home = Tk()
    win_home.title('Home Page')
    win_home.iconbitmap('dinosaur_icon.ico')
    win_home.geometry('250x400')

    # Create a database or connect to one
    conn = sqlite3.connect('survey_app.db')
    # Create cursor
    cursor = conn.cursor()

    # options menu
    label_home_stuInfo = Label(win_home, text="Student Name:\t\t" + user_name + "\nStudent ID:\t\t" + str(user_ID),
                               justify=LEFT)
    label_home_stuInfo.grid(row=0, column=0, pady=(0, 15))

    # buttons for options
    button_new_internship = Button(win_home, text='Add New Internship', command=new_internship)
    button_new_internship.grid(row=1, column=0, columnspan=2, pady=(0, 15))

    global entry_home_internID
    entry_home_internID = Entry(win_home, width=30)
    entry_home_internID.grid(row=2, column=0, columnspan=2)

    button_edit_internship = Button(win_home, text='Edit Existing Internship', command=edit_internship)
    button_edit_internship.grid(row=3, column=0, columnspan=2, pady=(0, 15))

    button_show_internships = Button(win_home, text='View All Internships', command=show_internships)
    button_show_internships.grid(row=4, column=0, columnspan=2, pady=(0, 15))

    button_new_survey = Button(win_home, text='New Survey', command=new_survey)
    button_new_survey.grid(row=5, column=0, columnspan=2, pady=(0, 15))

    global entry_home_surveyID
    entry_home_surveyID = Entry(win_home, width=30)
    entry_home_surveyID.grid(row=6, column=0, columnspan=2)

    button_edit_survey = Button(win_home, text='Edit Existing Survey', command=edit_Survey)
    button_edit_survey.grid(row=7, column=0, columnspan=2, pady=(0, 15))

    button_show_surveys = Button(win_home, text='View All Surveys', command=show_Surveys)
    button_show_surveys.grid(row=8, column=0, columnspan=2, pady=(0, 15))

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()


# submit info and get new ID
def sign_up_submit():
    # Create a database or connect to one
    conn = sqlite3.connect('survey_app.db')
    # Create cursor
    cursor = conn.cursor()

    # check if entry is empty
    if len(entry_signUp_name.get()) == 0:
        response = messagebox.showerror("You don't have a name?", "Please ACTUALLY enter a name.")
        return

    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    # Count results
    count_students = 0
    for student in records:
        count_students += 1

    generated_ID = count_students + 100001
    # Add new student to database
    cursor.execute("""INSERT INTO students
                      VALUES (:new_ID, :new_name)""",
                   {
                       'new_ID': generated_ID,
                       'new_name': entry_signUp_name.get()
                   })

    response = messagebox.showinfo("Welcome to our cult!", "Welcome to our internship survey database!\n"
                                                           "Your Student ID is: " + str(generated_ID) + "\n"
                                                                                                        "We recommend that you write that down :)")

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    setUserInfo(entry_signUp_name.get(), generated_ID)
    win_login.destroy()
    win_signUp.destroy()


def sign_up():
    global win_signUp
    win_signUp = Tk()
    win_signUp.title('Sign Up')
    win_signUp.iconbitmap('dinosaur_icon.ico')
    win_signUp.geometry("400x400")

    # Create Text Box Label for sign up
    label_signUp_topText = Label(win_signUp, text="Sign Up!")
    label_signUp_topText.grid(row=0, column=0, pady=(10, 0))
    label_signUp_name = Label(win_signUp, text="Enter your first name:")
    label_signUp_name.grid(row=1, column=0, pady=(10, 0))

    # Create entry fields for student information
    global entry_signUp_name

    entry_signUp_name = Entry(win_signUp, width=30)
    entry_signUp_name.grid(row=4, column=0)

    # Create button for login/submitting student info to query
    button_login_submit = Button(win_signUp, text='Sign Up!', command=sign_up_submit)
    button_login_submit.grid(row=5, column=0, columnspan=2)


def login_popup():
    response = messagebox.showwarning("ERROR: ID not in Database",
                                      "The ID you entered is not in our database.  Please login with a valid ID, or click 'Sign Up' to "
                                      "register yourself in our database.")


def login_submit():
    # Create a database or connect to one
    conn = sqlite3.connect('survey_app.db')
    # Create cursor
    cursor = conn.cursor()

    cursor.execute("""SELECT id FROM students where id = :submitted_ID LIMIT 1""",
                   {
                       'submitted_ID': entry_login_ID.get()
                   })
    id_exists = cursor.fetchone()

    cursor.execute("""SELECT name, OID FROM students where id = :submitted_ID LIMIT 1""",
                   {
                       'submitted_ID': entry_login_ID.get()
                   })
    found_name = cursor.fetchone()

    if found_name != None:
        login_name = ''
        login_name += str(found_name[0])

    if id_exists == None:
        login_popup()
    else:
        setUserInfo(login_name, entry_login_ID.get())
        win_login.destroy()

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()


# Create function for logging in (runs first)
def login():
    # Create a database or connect to one
    conn = sqlite3.connect('survey_app.db')
    # Create cursor
    cursor = conn.cursor()

    # Create Text Box Label
    label_login_ID = Label(win_login, text="Student ID:")
    label_login_ID.grid(row=3, column=0, pady=(10, 0))

    # Create entry fields for student information
    global entry_login_name
    global entry_login_ID

    entry_login_ID = Entry(win_login, width=30)
    entry_login_ID.grid(row=4, column=0)

    # Create button for login/submitting student info to query
    button_login_submit = Button(win_login, text='Login', command=login_submit)
    button_login_submit.grid(row=5, column=0, columnspan=2)

    # Create button for sign up
    button_login_create = Button(win_login, text='Sign Up', command=sign_up)
    button_login_create.grid(row=6, column=0, columnspan=2)


login()
win_login.mainloop()
