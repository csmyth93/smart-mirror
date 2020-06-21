import tkinter as tk

# create the window
root = tk.Tk()

# add a title to the window
root.title('Hello world!') #this will need removing at a later date

# add a label to display in the window
label = tk.Label(root, text='Brad sucks eggs')
label.pack()

# create a set of options to display
options = ['Option 1', 'Option 2', 'Option 3']
select_option = tk.StringVar()
select_option.set(options[0])

root.mainloop()
