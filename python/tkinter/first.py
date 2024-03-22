from tkinter import *

# Create the main window
windows = Tk()
windows.geometry("1300x700")
windows.title("learn code with noob")

# Set the window icon
# icon = PhotoImage(file="sharingan.png")
# windows.iconphoto(True, icon)

# Create a label widget and add it to the window
label = Label(windows, text="Welcome to Learn Code with Noob!")
label.pack()  # Packs the label into the window

# Start the Tkinter event loop
windows.mainloop()



# widgets = gui elements: buttons,textboxes,labels,images
# windows = serves as a container to hod or contain these widgets.
