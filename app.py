import tkinter as tk
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import pyttsx3


bot = ChatBot("OfflineBot")
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")


engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
engine.setProperty('voice', engine.getProperty('voices')[1].id)  # 1 = female

def speak(text):
    engine.say(text)
    engine.runAndWait()


def get_response():
    user_text = entry.get()
    if user_text.strip() == "":
        return
    chat_log.insert(tk.END, f"You: {user_text}")
    response = str(bot.get_response(user_text))
    chat_log.insert(tk.END, f"Bot: {response}")
    speak(response)
    entry.delete(0, tk.END)


root = tk.Tk()
root.title("Offline Chatbot with Voice")
root.geometry("500x400")

chat_log = tk.Listbox(root, height=15, width=70, font=("Arial", 12))
chat_log.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), width=50)
entry.pack(pady=5)
entry.bind("<Return>", lambda event: get_response())

send_button = tk.Button(root, text="Speak", command=get_response, font=("Arial", 12), bg="lightblue")
send_button.pack(pady=5)

root.mainloop()
