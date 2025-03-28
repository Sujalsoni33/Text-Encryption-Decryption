import tkinter
from tkinter import *
import Vigenere.VigenereScreen as VigenereScreen
import Polybius.PolybiusScreen as PolybiusScreen
import Hybrid.HybridScreen as HybridScreen

def front_page(root):

    def vigenere_cipher():
        start_frame.destroy()
        VigenereScreen.EncryptDecrypt(root)

    def polybius_sauare():
        start_frame.destroy()
        PolybiusScreen.EncryptDecrypt(root)

    def hybrid_cipher():
        start_frame.destroy()
        HybridScreen.EncryptDecrypt(root)

    
    start_frame = Frame(root, bg="#c9c9c9")
    
    headline_label = Label(start_frame, text="ENCRYPTION BOX", font=(None, 35), width=60, bg="#c9c9c9")
    headline_label.pack(pady=12)
    
    description_label = Label(start_frame,
                              text="Make Your Communication Secure\n Using Cryptographic Technique",
                              font=(None, 20),
                              bg="#c9c9c9")
    description_label.pack(pady=30)
    
    vigenere_cipher_frame = tkinter.Frame(start_frame, highlightbackground="black", highlightthickness=2, bd=0)
    vigenere_cipher_frame.pack(pady=10, padx=20)
    vigenere_button = Button(vigenere_cipher_frame,
                            text="Vigenere Cipher",
                            font=(None, 18), command=vigenere_cipher,
                            width=60,
                            height=2)
    vigenere_button.pack(pady=0, padx=0)
    
    polybius_sauare_frame = tkinter.Frame(start_frame, highlightbackground="black", highlightthickness=2, bd=0)
    polybius_sauare_frame.pack(pady=10, padx=20)
    polybius_sauare_button = Button(polybius_sauare_frame,
                             text="Polybius Square",
                             font=(None, 18),
                             command=polybius_sauare,
                             width=60,
                             height=2)
    polybius_sauare_button.pack(pady=0, padx=0)
    
    hybrid_cipher_frame = tkinter.Frame(start_frame, highlightbackground="black", highlightthickness=2, bd=0)
    hybrid_cipher_frame.pack(pady=10, padx=20)
    hybrid_cipher_button = Button(hybrid_cipher_frame,
                             text="Hybrid Cipher",
                             font=(None, 18),
                             command=hybrid_cipher,
                             width=60,
                             height=2)
    hybrid_cipher_button.pack(pady=0, padx=0)
    
    start_frame.pack()
