# Offline Chatbot with Voice Output

A desktop-based AI chatbot application developed using Python, Tkinter, ChatterBot, and pyttsx3. The chatbot can communicate with users through a graphical interface and respond using both text and voice output.

## Features

* Offline chatbot functionality
* User-friendly graphical interface using Tkinter
* Voice output using Text-to-Speech (TTS)
* Real-time conversation support
* English language training corpus
* No internet connection required after setup
* Lightweight and easy to run

## Technologies Used

* Python
* Tkinter
* ChatterBot
* ChatterBot Corpus
* pyttsx3
* SQLite Database

## Project Structure

```text
Offline-Chatbot-with-Voice-Output/
│
├── chatbot.py
├── db/
│   └── db.sqlite3.zip
├── requirements.txt
└── README.md
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/KK-kavinkumar/Offline-Chatbot-with-Voice-Output.git
cd Offline-Chatbot-with-Voice-Output
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python chatbot.py
```

## How It Works

1. The user enters a message in the chat window.
2. ChatterBot processes the input and generates a response.
3. The response is displayed in the chatbot interface.
4. pyttsx3 converts the response into speech output.
5. The user can continue the conversation in real time.

## Database

The project uses SQLite for storing chatbot training data.

Database file:

```text
db/db.sqlite3.zip
```

Extract the database file before running the application if required.

## Future Enhancements

* Speech-to-Text input
* Multi-language support
* Modern web-based interface
* Azure OpenAI integration
* Enhanced conversational intelligence

## Author

**Kavin Kumar S**

B.Tech – Artificial Intelligence and Data Science

GitHub: https://github.com/KK-kavinkumar

## License

This project is created for educational and learning purposes.
