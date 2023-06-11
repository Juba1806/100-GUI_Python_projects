#!/usr/bin/env python3 

import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("Simo window")

        # add widgets to app
        self.button = customtkinter.CTkButton(self, command=self.button_click)
        self.button.grid(row=0, column=0, padx=20, pady=10)

    # add methods to app
    def button_click(self):
        print("Who told to press the button ? ")


app = App()
app.mainloop()

