import pyttsx3
import tkinter as tk
from tkinter import messagebox


engine = pyttsx3.init()
engine.setProperty("rate", 150)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id) 


def speak_text():
    text = entry.get().strip()
    if not text:
        messagebox.showwarning("Input Needed", "Please enter some text.")
        return
    engine.say(text)
    engine.runAndWait()
    entry.delete(0, tk.END)


window = tk.Tk()
window.title("Offline Text to Speech")
window.geometry("400x200")

label = tk.Label(window, text="Enter Text:", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 12), width=40)
entry.pack(pady=5)

button = tk.Button(window, text="Speak", command=speak_text, font=("Arial", 12), bg="lightblue")
button.pack(pady=10)

window.mainloop()
