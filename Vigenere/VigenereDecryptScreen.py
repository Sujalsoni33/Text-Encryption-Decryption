from tkinter import *
from tkinter import messagebox, scrolledtext
import Vigenere.VigenereDecryptMessageScreen as VigenereDecryptMessageScreen
import Vigenere.VigenereScreen as VigenereScreen

def decipher_screen(root):
    def back_to_start():
        decipher_frame.destroy()
        VigenereScreen.EncryptDecrypt(root)

    def key_validation(key, message):
        if len(key) < 2:
            messagebox.showerror("KEY ERROR", "Key must contain at least 2 letters!")
            return False
        elif not all(x.isalpha() or x.isspace() for x in key):
            messagebox.showerror("KEY ERROR", "Key must contain letters only!")
            return False
        elif len(key) > len(message):
            messagebox.showerror("KEY ERROR", "Key can not be shorter then the ciphertext!")
            return False
        return True

    def message_validation(message):
        if len(message) < 2:
            messagebox.showerror("MESSAGE ERROR", "Ciphertext must contain at least two letter!")
            return False
        elif not all(x.isalpha() for x in message):
            messagebox.showerror("MESSAGE ERROR", "Ciphertext must contain letters only!")
            return False
        return True

    def decipher_message():
        if messagebox.askquestion("ATTENTION", "are you sure you entered the correct key?") == "yes":
            key = entry_key_widget.get().lower()
            message = entry_message_widget.get("1.0", "end -1c").lower()
            if key_validation(key, message) and message_validation(message):
                decipher_frame.destroy()
                VigenereDecryptMessageScreen.deciphered_screen(root, key=key, message=message)

    
    decipher_frame = Frame(root, bg="#c9c9c9")
   
    headline_label = Label(decipher_frame,
                           text="ENCRYPTION BOX - DECRYPT",
                           font=(None, 27),
                           width=60,
                           bg="#c9c9c9")
    headline_label.pack(pady=30, padx=5)
    
    key_instruction_lbl = Label(decipher_frame,
                                text="Enter key (at least 2 characters)",
                                font=(None, 20),
                                bg="#c9c9c9")
    key_instruction_lbl.pack(pady=5)
    
    entry_key_widget = Entry(decipher_frame, width=20, borderwidth=5, font=("David", 22))
    entry_key_widget.pack()
  
    space_lbl = Label(decipher_frame, bg="#c9c9c9")
    space_lbl.pack(pady=1)
   
    entry_message_lbl = Label(decipher_frame,
                              text="Enter ciphertext",
                              font=(None, 20),
                              bg="#c9c9c9")
    entry_message_lbl.pack(pady=5)
    
    entry_message_widget = scrolledtext.ScrolledText(decipher_frame,
                                                     wrap=WORD,
                                                     width=45, height=5,
                                                     font=("David", 15),
                                                     borderwidth=5)
    entry_message_widget.pack()
    
    decipher_button = Button(decipher_frame, text="DECIPHER",
                             font=(None, 20),
                             bg="#c9c9c9",
                             fg="#DC143C",
                             command=decipher_message,
                             borderwidth=3)
    decipher_button.pack(pady=5)
    
    back_button = Button(decipher_frame,
                         text="Back",
                         command=back_to_start,
                         font=(None, 15))
    back_button.pack(pady=15)
  
    decipher_frame.pack()
