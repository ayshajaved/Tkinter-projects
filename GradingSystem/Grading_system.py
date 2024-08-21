#Grading System, that prompts the user to enter his name, marks and then result will be displayed in a messagebox
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, showerror
#Preparing the window of the Grading System 
window = Tk()
window.config(bg="black")
window.title("Grading System")
window.geometry("600x600+300+30")           #Dimensions and place of the window
window.resizable(False, False)              #Fixing the size of the window
#adding boarder
border = Frame(window, bg="white", height= 2, width=2)
border.pack(fill="both", padx=0,pady=0)
#FUnction to add information in a dictionary
def details(d):
    details_str = ""
    for key, value in d.items():
        details_str += f"{key}: {value}\n"
    return details_str
#tkinter messagebox to display the result 
def show_result(d):
    askokcancel(title=f"Displaying Student {d["Student Name"]} Result!", message=details(d))

def student_info(): 
    #exception handling
    try:
        name = entry_name.get()
        bio = int(entry_bio.get())
        chem = int(entry_chem.get())
        phy = int(entry_phy.get())
        eng = int(entry_eng.get())
        urdu = int(entry_urdu.get())
        maths = int(entry_maths.get())
        all_marks = [bio, chem, phy, eng, urdu, maths]
        
        for i in all_marks:
            if i <0 or i >100:
                raise ValueError
        percentage = ((bio+chem+phy+eng+maths+urdu)/600)*100
        d = {
    "Student Name" : name,
    "Percentage"   : percentage
        }
        show_result(d)
    except ValueError:
        message = "Enter Marks in between 0-100!"
        showerror(title="Error", message=message)
    except Exception as er:
        #displaying the error messagebox incase if not the valid marks are entered!
        message = "Enter Valid Marks!"
        showerror(title="Error", message=message)

#Preparing the title of the school
lb_school = Label(window, text = "Welcome\nTo Python School", font = ("Eras Demi ITC",20), fg= "White", bg="black")
lb_school.pack() 
#Adding seperator in the form of frame
seperaotor = Frame(window,bg="white", height=5, width=250)
seperaotor.pack()
frame = Frame(window, bg="black")
frame.pack(anchor="w", padx=10, pady=10)
#Displaying System of Grading
lb_system = Label(frame, text = "•\"Grading System\"",font = ("Eras Demi ITC", 20), fg="yellow",bg= "black")
lb_system.pack(anchor="w")
#Displaying the Meaningful message
lb_user = Label(frame, text = "Enter Your marks(Out of 100)To get Result!", font=("Segoe UI Light",15 ), bg="black", fg="white")
lb_user.pack(anchor="n")
#User _entry of the marks
marks_frame = Frame(window, bg="black", height=400, width=500)
marks_frame.pack()
#Name
lb_name = Label(marks_frame, text="Enter name:", font=("Eras Demi ITC", 15), bg="black", fg="yellow")
lb_name.place(x = 10 , y = 15, anchor="w")
entry_name = Entry(marks_frame, font=("Eras Demi ITC", 15), bg="grey", fg="white", border=3)
entry_name.place(x = 170, y = 0)

#Biology marks
lb_bio = Label(marks_frame, text="Biology Marks:", font=("Eras Demi ITC", 15), bg="black", fg="yellow")
lb_bio.place(x = 10 , y =50 , anchor="w")
entry_bio = Entry(marks_frame, font=("Eras Demi ITC", 15), bg="grey", fg="white", border=3)
entry_bio.place(x = 170, y = 35)
#chemistry marks
lb_chem = Label(marks_frame, text="ChemistryMarks:", font=("Eras Demi ITC", 15), bg="black", fg="yellow")
lb_chem.place(x = 10 , y =90 , anchor="w")
entry_chem = Entry(marks_frame, font=("Eras Demi ITC", 15), bg="grey", fg="white", border=3)
entry_chem.place(x = 170, y = 70)
#physics marks
lb_phy = Label(marks_frame, text="Physics Marks:", font=("Eras Demi ITC", 15), bg="black", fg="yellow")
lb_phy.place(x = 10 , y =130 , anchor="w")
entry_phy = Entry(marks_frame, font=("Eras Demi ITC", 15), bg="grey", fg="white", border=3)
entry_phy.place(x = 170, y = 105)
#English marks
lb_eng = Label(marks_frame, text="English Marks:", font=("Eras Demi ITC", 15), bg="black", fg="yellow")
lb_eng.place(x = 10 , y =170 , anchor="w")
entry_eng = Entry(marks_frame, font=("Eras Demi ITC", 15), bg="grey", fg="white", border=3)
entry_eng.place(x = 170, y = 140)
#Urdu marks
lb_urdu = Label(marks_frame, text="Urdu Marks:", font=("Eras Demi ITC", 15), bg="black", fg="yellow")
lb_urdu.place(x = 10 , y =210 , anchor="w")
entry_urdu = Entry(marks_frame, font=("Eras Demi ITC", 15), bg="grey", fg="white", border=3)
entry_urdu.place(x = 170, y = 175)
#maths marks
lb_maths = Label(marks_frame, text="Maths Marks:", font=("Eras Demi ITC", 15), bg="black", fg="yellow")
lb_maths.place(x = 10 , y =250 , anchor="w")
entry_maths = Entry(marks_frame, font=("Eras Demi ITC", 15), bg="grey", fg="white", border=3)
entry_maths.place(x = 170, y = 210)

#Button to get result
result = Button(marks_frame, text= "COMPILE RESULT",font=("Eras Demi ITC",15 ), bg="black", fg="white",bd=5, relief="groove", command=student_info)
result.place(x = 220, y = 290, anchor="n")

#border of bottom
border_bottom = Frame(window, bg="white", height=2)
border_bottom.place(relwidth=2, rely=1, anchor='s')

window.mainloop()