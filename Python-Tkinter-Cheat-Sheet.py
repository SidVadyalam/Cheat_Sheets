# This is a Cheat Sheet for almost everything you can do in TKinter

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

"""
A few things to note about Tkinter:

1. Tkinter is an in built python module used to create GUI (Graphical User Interface) systems, basically systems
with user interactivity and are graphical representation of programs.

2. In Tkinter, everything that can be placed on a screen is called a widget. A widget is a piece of graphical media/interactivity
that the user can interact with, including buttons, checkboxes, labels etc.

3. The process of using Tkinter is composed of two parts. Part one is first defining a widget, and part two is then placing the
widget on the screen. This is a common process that you shall see in this notes sheet. You can also define and place the widget in one
go and we shall see that too, but the former is more popular.
"""


"""
The first and foremost step in all Tkinter projects is to define your main window, commonly referred to as your root window. This is
the primary window that will show up when the program runs and is itself the widget upon which other widgets get placed upon. We define
our root window by calling an instance of the Tk class. We can then use the .title(), .iconbitmap(), and .geometry() methods to customize
the properties of the main window.
"""
root = Tk()
root.title("Learning tkinter")
root.iconbitmap("Images/mars_planet_icon_263081.ico") # Only works on Windows Operating Systems apparently
# root.geometry("400x400") sets the size of the main window


"""
The most common type of wiget that you'll see is called the Label widget. This widget is common for displaying text on the root window. We
define the Label widget by calling an instance of the Label class and passing in a few arguments. The first argument that we pass in, whether
it be for the Label widget or any other widget is the widget/screen upon which we wish to place the current widget. In this case, and for most
of our cases as well, this background widget will be the root main screen widget, but it need not be. We can then pass a few keyword arguments
into the Label class, such as what text it contains, padding on the x and y direction, the width of the label etc. With that we have fully defined
the Label Widget. Also it is convinient to store the instance of the Label class in a variable, but it is not necessary.
"""
# Creating Label Widgets
myLabel1 = Label(root, text="Hello World", padx=10, pady=10)
myLabel2 = Label(root, text="This is a label", pady=10, padx=10)
myLabel3 = Label(root, text="                             ")



"""
Once we have fully defined the Label widget, we can then specify the location of the label widget by using the .grid method, which takes in the
row number and column number as key word arguments. An important thing to remember about the grid system is that is a row or column is empty,
then it will have zero width and height in the main window, meaning that in this case, since this Label is the first Label we make, if we specified
our row or column as greater than zero, the label will still be placed at the very top. Instead of the grid system, we can also use the .pack()
method which simple puts the widget at roughly the center of the top part of the screen. We can also use .place() method which takes in the x
and y coordinates that we desire to place as keyword arguments. Note that we can only follow one system at a time, mixing .pack() followed by a
.grid() and vice versa for widgets will throw an error
"""
# Placing the Label Widget onto the screen
# myLabel.pack() is one way to do it
# or you can use the grid system
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=0, column=1)
myLabel3.grid(row=0, column=2)


"""
The next common widget we shall see is the Button widget, which is used to create a button on screen. Similar to the Lable, we must define
a button as an instance of the button class, and then place it on screen. In order to add functionality to the button, we can specify
a function object within the keyword argument, command, and define the function before the declaring the button object. In such cases, a lambda
anonymous function is also useful.
"""
# Here I'm defining a simple fuction for a button
def myClick():
    myLabel4 = Label(root, text="Look, I clicked a button!")
    myLabel4.grid(row=1, column=0)

# Defining and Placing buttons
myButton= Button(root, text="Click me", padx=50, pady=50, command=myClick, fg="blue", bg="red")
myButton.grid(row=1, column=1)




"""
The next widget is an input widget for recieving user input/data. In Tkinter this is called the Entry widget, which displays a blank bar for the
user to enter information into. Like every other widget, we have to define and place it. In order to read the input within the Entry widget, we
can use the .get() method. Typically Entry widgets are paired with other widgets for increased functionality, as I have did below
"""
# Here we define and place an input field or an 'entry'
e = Entry(root, width=50, bg="red", fg="white", borderwidth=5)
e.grid(row=1, column=2)

# We can combine buttons, labels and entry widgets for increased functionality as shown below
name = Entry(root, width=50, bg='black', fg='white')
name.grid(row=2, column=0)

def btnclick():
    myLabel5 = Label(root, text=f'Hello {name.get()}')
    myLabel5.grid(row=2, column=2)
    


enter = Button(root, padx=20, text="Submit", command=btnclick)
enter.grid(row=2, column=1)

name.insert(100, "Enter Yer Name")





"""
The .quit() method on the root window, will immediately cause the program and Tkinter to quit. This is useful for making a custom exit button
"""
button_quit = Button(root, text="Quit The Program",  command=root.quit)
button_quit.grid(row=3, column=0)





"""
In order to add images in Tkinter, we can use the inbuilt methods, however those methods only support outdated image formats, so to enable the use
of png and jpeg formats, we must import the PIL module or the Python Imaging Library. This library lets us use latest image file formats within
Tkinter. To create an image, we must first create an object of class PhotoImage in the PIL library. We can then use this object within a Lable,
by specifying the image keyword argument as that object. We then place the Label onto the root/main window, allowing us to place an image
into Tkinter as a Label.
"""
my_img = ImageTk.PhotoImage(Image.open("Images/Image11.png"))
myLabel6 = Label(root, image=my_img)
myLabel6.grid(row=3, column=1)





"""
The next widget in Tkinter are called frames. Frames can be used to add bordering around other widgets or to seperate out widgets to give us a cleaner
and smoother look. We can also add widgets onto frames in order to save space in the root window or to organize widgets better. Like all widgets, we define
frames first by using the LabelFrame() class, before specifying the location of the frame. One specialty of frames is that if we want to add new widgets in
the frame, we simply specify the frame object as the first parameter when defining those new widgets as shown below.
"""
frame1 = LabelFrame(root, text="This is a frame...", padx=5, pady=5) # Padding on the inside
frame1.grid(row=3, column=2, padx=10, pady=10) # Padding on the outside

frame_button = Button(frame1, text="Button in a frame")
frame_button.pack()






"""
RadioButtons are widgets that are used to make the user chose from a set of predefined inputs, kinda like multiple choice tests. Defining a radio button
is same as any other widget (use the Radiobutton() class), with a few extra steps. First before we define any radio button widget, we must define a tkinter variable.
Tkinter variables are similar to python variables with a few differences. For instance, Tkinter variables have to be declared with their type before we can use them. This can
be done by equating the variable to an object of the available datatypes like IntVar(), StringVar() ... etc. We can then access the values in the variable
by using the .get() method and set the value of the vairable by using the .set() method. Once we have properly defined a tkinter variable, we must specify
the variable and the value the variable should hold if the radio button is selected when defining the radio button. This can be done by setting the keyword
argumnets variable and value. This way, whevenver the particular radiobutton is selected, the specified variable will attain the value denoted when defining
the radio button. After this we can continue to place the radio button normally using either grid or pack.
"""
frame2 = LabelFrame(root, padx=10, pady=10)
frame2.grid(row=4, column=0)

r = IntVar() # Defining a Tkinter variable
r.set(0)


Radiobutton(frame2, text="Option 1", variable=r, value=1, command=lambda:Label(frame2, text=f"The option selected is {r.get()}").pack()).pack()
Radiobutton(frame2, text="Option 2", variable=r, value=2, command=lambda:Label(frame2, text=f"The option selected is {r.get()}").pack()).pack()


myLabel7 = Label(frame2, text=f"The option selected is {r.get()}")
myLabel7.pack()





"""
In order to show the user a message box/popup whevener the user interacts with a widget we can utilize the message box class in Tkinter. Using this we can
define custom message boxes and is another way for us to get input from the user. To use message boxes, we only have to define them and they will be
automatically popup for the user when triggered. Defing message boxes includes using the messagebox. syntax and then specifying the type of messahebox
desired. There are different types of message boxes (all are shown below) and the response to each will be stored in the variable used to define it.
Different types of messageboxes will output different types of values for each resoonse, so be sure to test the output for the one you are using
"""
def popup():
    response = messagebox.askyesno("Pop Up Title", "Pop Up message")
    # Can also be showinfo, showwarning, showerror, askquestion, askokcancel, askyesno


    if response == 1: # User selected Yes
        Label(root, text="You clicked Yes").grid(row=4, column=2)
    elif response == 0: # User selected No
        Label(root, text="You clicked No").grid(row=4, column=2)
        

popup_button = Button(root, text="POPUP", command=popup)
popup_button.grid(row=4, column=1)





"""
Just like how the root window is a widget itself, we can define other windows as widgets. This is done by calling an instance of the Toplevel() class, which
creates a new window widget upon which we can place other widgets. We can then use the same methods as we did with root to modify the properties if the
window. The reason why we use the toplevel class and not another Tk() class instance, is that for every main window we create with the Tk() class, we have
to add a mainwindow loop at the end, and creating more than one main window will cause confusion as to which mainloop corresponds to which main window.
"""
top = Toplevel()
top.title("Learing Tkinter Part 2")
top.geometry("600x600")

myLabel8 = Label(top, text="I'm in a completely different screen!", padx=20, pady=20)
myLabel8.grid(row=0, column=0)

destroy_button = Button(top, text="Click me to close", command=top.destroy, padx=20, pady=20)
destroy_button.grid(row=0, column=1)




"""
Another form of input we can use in tkinter is asking the user to open particular files. This can be done with the filedialog class in Tkinter. Using the method
askopenfilename() allows us to  ask the user to open a file in a specified directory and of a specific file type. The askopenfilename() method however, only return
the path to the file, not the actual file itself. Since the file does not get open when the askopenfilename() method is run, we can bypass this by using various
other features of Tkinter and pass in the path to the file to have it be opened. In the below example, I have done exactly that by using the ImageTk class to open
image files
"""
"""
top.filename = filedialog.askopenfilename(initialdir="/Users/Siddharth Vadyalam/PFS-Internship/Images", title="Select a file", filetypes=(("png files", "*.png"),("all files", "*")))
# top.filename contains the path to the selected file
print(top.filename[41:])
myImage2 = ImageTk.PhotoImage(Image.open(top.filename[41:]))
myLabel9 = Label(top, image=myImage2)
myLabel9.grid(row=0, column=2)
"""





"""
The third last widget for Tkinter is called the scale widget, which is like a scale/slider/scroll bar. This works by displaying a vertical scroll bar to the user, which
can be used to select a value within a specified range (that is set by using the to and from keywords). As with any widget, this must be defined and placed on a screen
and scroll bars are defined as an object of the Scale() class
"""
frame3 = LabelFrame(top)
frame3.grid(row=0, column=2)

def slide(a):
    top.geometry(f"600x{vertical.get()}")

vertical = Scale(frame3, from_= 0, to=600, command=slide)
vertical.pack()

horizontal = Scale(frame3, from_= 0, to=600, orient=HORIZONTAL)
horizontal.pack()


scale_button = Button(frame3, text="Click Me", command=lambda: scale_button.config(text=horizontal.get()))
scale_button.pack()




"""
The penultimate widget is called the checkbox widget that displays a checkbox for the user to select. As with the radio button, a variable must be specified along with
a value that the variable attains once the checkbox is selected. This widget is defined as an object of the Checkbutton() class and must be placed like all other tkinter widgets
"""
var = StringVar()

checkbox = Checkbutton(top, text="I dare you to check this box", variable=var, onvalue='On', offvalue='Off')
checkbox.deselect()
checkbox.grid(row=1, column=0)

check_button = Button(top, text='Click me', command=lambda: check_button.config(text=var.get()))
check_button.grid(row=1, column=1)





"""
The final widget of them all is the dropdown menu widget, which can be defined with the OptionMenu() class. Like checkbuttons, a variable must also be specified to store
the value that the user selects. In this case, we do not need to set a value for the variable, since the variable will automatically be set to the value that was chosen in the
dropdown menu. 
"""
clicked = StringVar()
drop = OptionMenu(top, clicked, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday") # We can also use a list (remeber to use the *)
clicked.set("Monday")
drop.grid(row=1, column=2)


root.mainloop()



