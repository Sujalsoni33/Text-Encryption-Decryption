from tkinter import *
from tkinter import scrolledtext
import Polybius.PolybiusScreen as PolybiusScreen

def encrypted_screen(root, message):
    def back_to_menu():
        encrypted_message_frame.destroy()
        PolybiusScreen.EncryptDecrypt(root)

    def encrypt(message):
        encrypted = ""
        for character in message:
            row = int((ord(character) - ord('a')) / 5) + 1
            col = (((ord(character)) - ord('a')) % 5) + 1
            if character == 'i':
                encrypted = encrypted + '24'
                continue
            if character == 'j':
                encrypted = encrypted + '00'
                continue
            if character == 'k':
                row = row - 1
                col = 5 - col + 1
            elif ord(character) >= ord('j'):
                if col == 1:
                    col = 6
                    row = row - 1
                col = col - 1
            r = str(row)
            c = str(col)
            encrypted = encrypted + r + c
        
        return encrypted


    encrypted_message_frame = Frame(root, bg="#c9c9c9")
    
    headline_label = Label(encrypted_message_frame,
                           text="ENCRYPTED MESSAGE",
                           font=(None, 30),
                           width=60,
                           bg="#c9c9c9")
    headline_label.pack(pady=30)
    
    description_label = Label(encrypted_message_frame,
                              text="The encrypted message is:",
                              font=(None, 25),
                              bg="#c9c9c9")
    description_label.pack(pady=30)
    
    entry_message_widget = scrolledtext.ScrolledText(encrypted_message_frame,
                                                     wrap=WORD,
                                                     width=45, height=5,
                                                     font=("David", 15),
                                                     borderwidth=5)
    entry_message_widget.insert(INSERT, encrypt(message))
    entry_message_widget.pack()
    
    instruction_label = Label(encrypted_message_frame, text="copy the cipher above",
                              font=(None, 20),
                              bg="#c9c9c9")
    instruction_label.pack()
    
    back_to_menu_button = Button(encrypted_message_frame,
                                 text="Back",
                                 command=back_to_menu,
                                 font=(None, 15))
    back_to_menu_button.pack(pady=25)
    
    encrypted_message_frame.pack()
