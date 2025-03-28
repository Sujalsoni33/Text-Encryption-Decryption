from tkinter import *
from tkinter import scrolledtext
import Hybrid.HybridScreen as HybridScreen

alphabet = "abcdefghijklmnopqrstuvwxyz"

def deciphered_screen(root, key, message):
    def back_to_menu():
        deciphered_message_frame.destroy()
        HybridScreen.EncryptDecrypt(root)

    def key_process():
        decrypted_text = decrypt()
        if len(key) == len(decrypted_text):
            return key
        padded_key = key
        x = 0
        for i in range(0, len(decrypted_text) - len(key)):
            padded_key = padded_key + str(key[x])
            x = (1 + x) % len(key)
        return padded_key

    def decipher_character(key_char, message_char):
        message_num = ord(message_char) - ord('a')
        key_num = ord(key_char) - ord('a')
        return alphabet[(message_num - key_num) % 26]
    
    def decipher():
        decrypted_text = decrypt()
        padded_key = key_process()
        deciphered_message = ""
        for i in range(0, len(decrypted_text)):
            deciphered_message = deciphered_message + str(decipher_character(padded_key[i], decrypted_text[i]))
        return deciphered_message

    def decrypt():
        encrypted = message
        s1 = list(encrypted)
        decrypted = ""
        for i in range(0, len(encrypted), 2):
            r = int(s1[i])
            c = int(s1[i+1])
            if r == 2 and c == 4:
                decrypted += 'i'
                continue
            if r == 0 and c == 0:
                decrypted += 'j'
                continue
            ch = chr(((r-1)*5+c+96))
            if (ord(ch)-96>=10):
                ch = chr(((r-1)*5+c+96+1))
            ch1 = str(ch)
            decrypted += ch1
        return decrypted
    
    deciphered_message_frame = Frame(root, bg="#c9c9c9")
    
    headline_label = Label(deciphered_message_frame,
                           text="DECIPHERED MESSAGE",
                           font=(None, 30),
                           width=60,
                           bg="#c9c9c9")
    headline_label.pack(pady=30)
   
    description_label = Label(deciphered_message_frame,
                              text="The DECIPHERED message is:",
                              font=(None, 25),
                              bg="#c9c9c9")
    description_label.pack(pady=30)
    
    entry_message_widget = scrolledtext.ScrolledText(deciphered_message_frame,
                                                     wrap=WORD,
                                                     width=45, height=5,
                                                     font=("David", 15),
                                                     borderwidth=5)
    entry_message_widget.insert(INSERT, decipher())
    entry_message_widget.pack()
   
    instruction_label = Label(deciphered_message_frame,
                              text="copy the deciphered message above",
                              font=(None, 20),
                              bg="#c9c9c9")
    instruction_label.pack()
    
    back_to_menu_button = Button(deciphered_message_frame,
                                 text="Back",
                                 command=back_to_menu,
                                 font=(None, 15))
    back_to_menu_button.pack(pady=25)
    
    deciphered_message_frame.pack()
