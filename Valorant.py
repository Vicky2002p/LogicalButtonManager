# Importing Module
from tkinter import *

# Making Buttons

# Creating an object
root = Tk()

# Adding title to the window box
root.title('Valorant')

# Adjusting the size of the box
root.geometry("250x250")

# Define Our Images
on = PhotoImage(file = "on.png")
off = PhotoImage(file = "off.png")

# Initializing variables to track button states
one_is_on = False
two_is_on = False
three_is_on = False

def switch1():
    global one_is_on, two_is_on, three_is_on

    # Toggle first button state and update image
    if one_is_on:
        first_button.config(image = off)
        one_is_on = False

        # If second button is also on, turn off third button
        if two_is_on:
            third_button.config(image = off)
            three_is_on = False
        # If third button is also on, turn off second button
        elif three_is_on:
            second_button.config(image = off)
            two_is_on = False
    else:
        first_button.config(image = on)
        one_is_on = True

        # If second and third buttons are on, turn off second button
        if two_is_on and three_is_on:
            second_button.config(image = off)
            two_is_on = False
def switch2():
    global one_is_on, two_is_on, three_is_on

    # Toggle third button state and update image
    if two_is_on:
        second_button.config(image = off)
        two_is_on = False

        # If first and second buttons are on, turn off third button
        if one_is_on and three_is_on:
            third_button.config(image = off)
            three_is_on = False
        # If only first button is on, turn off third button
        elif one_is_on:
            third_button.config(image = off)
            three_is_on = False
        # If only second button is on, turn off first button
        elif three_is_on:
            first_button.config(image = off)
            one_is_on = False
    else:
        second_button.config(image = on)
        two_is_on = True

        # If second and third buttons are on, turn off thrid button
        if one_is_on and two_is_on:
            third_button.config(image = off)
            three_is_on = False
def switch3():
    global one_is_on, two_is_on, three_is_on

    # Toggle third button state and update image
    if three_is_on:
        third_button.config(image = off)
        three_is_on = False

        # If first and second buttons are on, turn off second button
        if one_is_on and two_is_on:
            second_button.config(image = off)
            two_is_on = False
        # If only first button is on, turn off second button
        elif one_is_on:
            second_button.config(image = off)
            two_is_on = False
        # If only second button is on, turn off first button
        elif two_is_on:
            first_button.config(image = off)
            one_is_on = False
    else:
        third_button.config(image = on)
        three_is_on = True
        
        # If second and third buttons are on, turn off first button
        if two_is_on and three_is_on:
            first_button.config(image = off)
            one_is_on = False
        
        
# Create A Button
first_button = Button(root,bd=5,
                   text="I am Mentally stable",
                   compound='left',
                   pady=10,
                   command=switch1)
# Create A Button
second_button = Button(root,bd=5,
                   text="I play Valorant",
                   compound='left',
                   pady=10,
                   command=switch2)
# Create A Button
third_button = Button(root,bd=5,
                   text="I am not Racist",
                   compound='left',
                   pady=10,
                   command=switch3)

first_button.config(image=off)
first_button.pack()
second_button.config(image=off)
second_button.pack()
third_button.config(image=off)
third_button.pack()

# Execute it
root.mainloop()