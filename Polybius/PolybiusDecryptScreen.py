from tkinter import *
from tkinter import messagebox, scrolledtext
import Polybius.PolybiusDecryptMessageScreen as PolybiusDecryptMessageScreen
import Polybius.PolybiusScreen as PolybiusScreen

def decipher_screen(root):

    def back_to_start():
        decipher_frame.destroy()
        PolybiusScreen.EncryptDecrypt(root)

    def message_validation(message):
        if len(message) <= 0:
            messagebox.showerror("MESSAGE ERROR", "Ciphertext must contain at least one letter!")
            return False
        elif not all(x.isdigit() for x in message):
            messagebox.showerror("MESSAGE ERROR", "Ciphertext must contain numbers only!")
            return False
        return True

   
    def decipher_message():
        message = entry_message_widget.get("1.0", "end -1c").lower()
        if message_validation(message):
            decipher_frame.destroy()
            PolybiusDecryptMessageScreen.deciphered_screen(root, message=message)

    
    decipher_frame = Frame(root, bg="#c9c9c9")
    
    headline_label = Label(decipher_frame,
                           text="ENCRYPTION BOX - DECRYPT",
                           font=(None, 27),
                           width=60,
                           bg="#c9c9c9")
    headline_label.pack(pady=30, padx=5)
    
    
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
