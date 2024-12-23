import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Create the model
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
    system_instruction="You are my friendly AI assistant here to help with any questions or doubts I may have. Respond to my queries in a clear, simple, and friendly manner, just like a friend would. If I'm unsure about something, provide suggestions and guidance to help me understand the topic better. You can also suggest next steps or resources I can use to further explore a topic if you're not able to provide a complete answer. Keep the conversation friendly, open, and supportive.\n")
history=[]
print("bot:Hello?")
while True:
    user_input=input("You:")
    chat_session=model.start_chat(history=history)
    response=chat_session.send_message(user_input)
    model_response=response.text
    print(f'bot:{model_response}')
    print()
    history.append({"role":"user","parts":[user_input]})
    history.append({"role":"model","parts":[model_response]})