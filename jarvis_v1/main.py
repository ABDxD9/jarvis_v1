import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit as kit
import requests
# import vosk
# from newsapi import NewsApiClient

recognizer = sr.Recognizer()
# api = NewsApiClient(api_key='e2d3e07ec6ed4645931ed928a179eff1')


def speak(text):
    engine = pyttsx3.init('sapi5')  # re-init every time
    engine.say(text)
    engine.runAndWait()
    
def processcommand(c):
    c = c.lower().strip()  

    if "google" in c:
        webbrowser.open("https://google.com")
    elif "youtube" in c or "you tube" in c:
        webbrowser.open("https://youtube.com")
    elif "facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "instagram" in c:
        webbrowser.open("https://instagram.com")
    elif "twitter" in c or "x" in c:
        webbrowser.open("https://twitter.com")
    elif "linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif "reddit" in c:
        webbrowser.open("https://reddit.com")
    elif "whatsapp" in c:
        webbrowser.open("https://web.whatsapp.com")
    elif "snapchat" in c:
        webbrowser.open("https://www.snapchat.com")
    elif "pinterest" in c:
        webbrowser.open("https://www.pinterest.com")
    elif "chatgpt" in c or "Chat Gpt" in c:
        webbrowser.open("https://chat.openai.com")
        print("No matching command for:", c)
    elif "news" in c:
        r = requests.get()    


# Play music (general)
    elif ("play" in c and "music" in c) or ("play" in c and "youtube" in c):
        if source is not None:
            speak("What should I search on YouTube?")
            audio = recognizer.listen(source)
            try:
                query = recognizer.recognize_google(audio)
                speak(f"Playing {query} on YouTube")
                kit.playonyt(query)
            except sr.UnknownValueError:
                speak("Sorry, I did not catch that.")
            except sr.RequestError:
                speak("Network error while recognizing query.")

    # elif "news" in c:
    #         speak("Fetching latest news...")
    # try:
    #     # Use a keyword search instead of country/sources
    #     top_headlines = api.get_everything(
    #         q="India",
    #         language='en',
    #         sort_by='publishedAt',
    #         page_size=5
    #     )

    #     if not top_headlines['articles']:
    #         speak("Sorry, I couldn't find any news at the moment.")
    #     else:
    #         for article in top_headlines['articles']:
    #             speak(article['title'])
    # except Exception as e:
    #     speak("Sorry, I couldn't fetch the news at the moment.")
    #     print("NewsAPI Error:", e)


WAKE_WORD = "jarvis"   

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    command_mode = False  # Track if Jarvis is awake

    while True:
        try:
            with sr.Microphone() as source:
                if not command_mode:
                    print("Listening for wake word...")
                else:
                    print("Listening for command...")

                audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)
                text = recognizer.recognize_google(audio)
                print("Heard:", text)

                if not command_mode:  
                    if WAKE_WORD in text.lower():
                        speak("At your service sir")
                        command_mode = True  
                else:  
                    if "sleep" in text.lower():
                        speak("Going to sleep mode")
                        command_mode = False
                    else:
                        processcommand(text)
                        speak(f"You said: {text}")

        except Exception as e:
            print(f"Error: {e}")