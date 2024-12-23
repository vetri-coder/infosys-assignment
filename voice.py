import os
import google.generativeai as genai
import pyttsx3
import speech_recognition as sr
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
engine = pyttsx3.init()
recognizer = sr.Recognizer()
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-8b",
    generation_config=generation_config,
)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"User: {text}")
            return text
        except Exception as e:
            print("Error: Could not understand audio")
            return None

def get_response(user_input):
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(user_input)
    return response.text
def run_assistant():
    print("Assistant: Hello, how can I assist you?")
    speak("Hello,?")
    
    while True:
        user_input = listen()
        
        if user_input:
            if "dot" in user_input.lower():
                print("Assistant: Goodbye!")
                speak("Goodbye!")
                break

            response = get_response(user_input)
            print(f"Assistant: {response}")
            speak(response)
if __name__ == "__main__":
    run_assistant()
