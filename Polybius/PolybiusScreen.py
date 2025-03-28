import tkinter
from tkinter import *
import StartScreen
import Polybius.PolybiusEncryptScreen as PolybiusEncryptScreen
import Polybius.PolybiusDecryptScreen as PolybiusDecryptScreen

def EncryptDecrypt(root):
  
    def back():
        start_frame.destroy()
        StartScreen.front_page(root)
    
    def encrypt_key():
        start_frame.destroy()
        PolybiusEncryptScreen.encrypt_screen(root)

    def decipher_key():
        start_frame.destroy()
        PolybiusDecryptScreen.decipher_screen(root)

    
    start_frame = Frame(root, bg="#c9c9c9")
    headline_label = Label(start_frame, text="ENCRYPTION BOX", font=(None, 35), width=60, bg="#c9c9c9")
    headline_label.pack(pady=12)

    description_label = Label(start_frame,
                              text="Encrypt or Decrypt text\n using Polybius Square.",
                              font=(None, 20),
                              bg="#c9c9c9")
    description_label.pack(pady=30)
    
    encrypt_frame = tkinter.Frame(start_frame, highlightbackground="black", highlightthickness=2, bd=0)
    encrypt_frame.pack(pady=10, padx=20)
    encrypt_button = Button(encrypt_frame,
                            text="Encrypt plaintext",
                            font=(None, 18), command=encrypt_key,
                            width=60,
                            height=3)
    encrypt_button.pack(pady=0, padx=0)

    decipher_frame = tkinter.Frame(start_frame, highlightbackground="black", highlightthickness=2, bd=0)
    decipher_frame.pack(pady=10, padx=20)
    decipher_button = Button(decipher_frame,
                             text="Decrypt Ciphertext",
                             font=(None, 18),
                             command=decipher_key,
                             width=60,
                             height=3)
    decipher_button.pack(pady=0, padx=0)
    
    back_button = Button(start_frame, text="Back", command=back, font=(None, 15))
    back_button.pack(pady=15)

    start_frame.pack()
