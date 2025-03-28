from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import Polybius.PolybiusScreen as PolybiusScreen
import Polybius.PolybiusEncryptMessageScreen as PolybiusEncryptMessageScreen

def encrypt_screen(root):

    def back():
        encrypt_frame.destroy()
        PolybiusScreen.EncryptDecrypt(root)

    def message_validation(message):
        if len(message) <= 0:
            messagebox.showerror("MESSAGE ERROR", "Plaintext must contain at least one letter!")
            return False
        elif not all(x.isalpha() for x in message):
            messagebox.showerror("MESSAGE ERROR", "Plaintext must contain alphabets only!")
            return False
        return True
    
 
    def encrypt_message():
        message = entry_message_widget.get("1.0", "end -1c").lower()
        if message_validation(message):
            encrypt_frame.destroy()
            PolybiusEncryptMessageScreen.encrypted_screen(root, message=message)

   
    encrypt_frame = Frame(root, bg="#c9c9c9")
    
    headline_label = Label(encrypt_frame, text="ENCRYPTION BOX - ENCRYPT", font=(None, 27), width=60, bg="#c9c9c9")
    headline_label.pack(pady=30, padx=5)
    
    space_lbl = Label(encrypt_frame, bg="#c9c9c9")
    space_lbl.pack(pady=1)
    
    entry_message_lbl = Label(encrypt_frame, text="Enter plaintext", font=(None, 20), bg="#c9c9c9")
    entry_message_lbl.pack(pady=5)
    
    entry_message_widget = scrolledtext.ScrolledText(encrypt_frame,
                                                     wrap=WORD,
                                                     width=45, height=5,
                                                     font=("David", 15),
                                                     borderwidth=5)
    entry_message_widget.pack()

    encrypt_button = Button(encrypt_frame, text="ENCRYPT",
                            command=encrypt_message,
                            font=(None, 20),
                            bg="#c9c9c9",
                            fg="#DC143C",
                            borderwidth=3)
    encrypt_button.pack(pady=5)
   
    back_button = Button(encrypt_frame, text="Back", command=back, font=(None, 15))
    back_button.pack(pady=15)
    
    encrypt_frame.pack()
