from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import Vigenere.VigenereScreen as VigenereScreen
import Vigenere.VigenereEncryptMessageScreen as VigenereEncryptMessageScreen

def encrypt_screen(root):

    def back():
        encrypt_frame.destroy()
        VigenereScreen.EncryptDecrypt(root)

    def key_validation(key, message):
        if len(key) < 2:
            messagebox.showerror("KEY ERROR", "Key must contain at least 2 letters!")
            return False
        elif not all(x.isalpha() for x in key):
            messagebox.showerror("KEY ERROR", "Key must contain letters only!")
            return False
        elif len(key) > len(message):
            messagebox.showerror("KEY ERROR", "Key can not be shorter then the plaintext!")
            return False
        return True

    def message_validation(message):
        if len(message) <= 0 or not all(x.isalpha() for x in message):
            messagebox.showerror("MESSAGE ERROR", "Plaintext must contain at least one letter and no other signs!")
            return False
        return True

    def encrypt_message():
        if messagebox.askquestion("ATTENTION", "Did you saved the key?") == "yes":
            key = entry_key_widget.get().lower()
            message = entry_message_widget.get("1.0", "end -1c").lower()
            if key_validation(key, message) and message_validation(message):
                encrypt_frame.destroy()
                VigenereEncryptMessageScreen.encrypted_screen(root, key=key, message=message)

   
    encrypt_frame = Frame(root, bg="#c9c9c9")
   
    headline_label = Label(encrypt_frame, text="ENCRYPTION BOX - ENCRYPT", font=(None, 27), width=60, bg="#c9c9c9")
    headline_label.pack(pady=30, padx=5)
    
    key_instruction_lbl = Label(encrypt_frame,
                                text="Enter key (at least 2 characters)",
                                font=(None, 20),
                                bg="#c9c9c9")
    key_instruction_lbl.pack(pady=5)
   
    warning_label = Label(encrypt_frame,
                          text="WARNING - Keep the key in a safe place!",
                          font=(None, 13, "bold"),
                          bg="#c9c9c9",
                          fg="Red")
    warning_label.pack()
    
    entry_key_widget = Entry(encrypt_frame, width=20, borderwidth=5, font=("David", 22))
    entry_key_widget.pack()
    
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
