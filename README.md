# JARVIS_v1

JARVIS_v1 is the first prototype of a personal assistant built in Python.
Right now, it can **listen, speak, and open basic apps** using simple loops and commands.

---

## ✨ Current Features

* 🎤 **Speech Recognition** – Understands voice commands.
* 🔊 **Text-to-Speech** – Talks back using Python’s TTS engine.
* 🖥️ **Basic App Control** – Open common applications (browser, notepad, etc.).
* 🔁 **Loop System** – Keeps running until user exits.

---

## 🛠️ Tech Stack

* **Language**: Python 3.10+
* **Libraries Used**:

speechrecognition – voice input
pyttsx3 – text-to-speech
webbrowser – open websites
pywhatkit – send WhatsApp messages / YouTube search
requests – API calls (weather, info, etc.)
---

## ⚡ Setup & Run

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run JARVIS:

   ```bash
   python main.py
   ```

---

## 🛣️ Roadmap

* [ ] Add more app integrations
* [ ] Improve speech accuracy
* [ ] Add personalized commands
* [ ] Store user preferences

---

## ⚠️ Note

This is just a **basic version (v1)**. It’s experimental and meant for learning.
