#!/usr/bin/env python3

import customtkinter  as ctk 


window = ctk.CTk()

# Set the window geometry 
window.geometry("800x600")


def get_acrnonym():
    """ A function to get the only 4 letters of"""
    text = box.get()
    # Create a list of splited words 
    words = text.split()
    # result we'll need it later 
    result = ""

    for word in words:
     # get the the first 4 letters
        letter = word[0]
        letter = letter.title()
        result += letter
    
    # We use Label to print something to show up in the window 
    my_lable = ctk.CTkLabel(window,text = result[:4],
            font=('Arial',40,'bold'),
            fg_color="#00FF00",
            compound="bottom")
    my_lable.pack()



def clear():
    # We use delte and the argument 0 to end to delete everything in the box 
    box.delete(0,END)



# The box 
box = ctk.CTkEntry(window,
        font=("Arial",50),
        fg_color = "#00FF00",
        ) 

box.pack()


# The button to submit  
submit_button = ctk.CTkButton(window,text="submit",
     command = get_acrnonym,
     font=("Comic Sans",20))
        


submit_button.pack()

# The button to clear 
clear_button = ctk.CTkButton(window, text="clear", command=clear,
        font=("Comic Sans",20))
        
clear_button.pack()



window.mainloop()
