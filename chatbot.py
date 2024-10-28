import nltk
import random
import re
responses = [
    {
        "patterns": ["hello", "hi", "hey", "good morning", "good afternoon", "greetings"],
        "responses": ["Hello there!", "Hi! How can I help you today?", "Hey! What's on your mind?"]
    },
    {
        "patterns": ["thank you", "thanks", "I appreciate it", "thanks a lot"],
        "responses": ["You're very welcome!", "No problem at all!", "Happy to help!"]
    },
    {
        "patterns": ["help", "I need assistance", "can you help me?", "support", "I have a question"],
        "responses": ["I'm here to help! What do you need assistance with?", "How can I assist you today?"]
    },
    {
        "patterns": ["goodbye", "bye", "see you later", "exit", "talk to you later"],
        "responses": ["Goodbye! Have a wonderful day!", "See you later! Take care!", "Goodbye! Feel free to come back if you need anything!"]
    },
    {
        "patterns": ["what is your name?", "who are you?", "what should I call you?"],
        "responses": ["I'm your friendly chatbot!", "I go by ChatBot, your virtual assistant.", "You can call me your assistant, here to help!"]
    },
    {
        "patterns": ["who created you?", "who made you?", "who is your creator?"],
        "responses": ["I was created by a developer (VICKY KHAN) to help answer your questions!"]
    },
    {
        "patterns": ["how are you?", "how's it going?", "what's up?"],
        "responses": ["I'm just a chatbot, but I'm here to help!", "I'm here and ready to assist you! How can I help today?", "I'm always here to chat with you!"]
    },
    {
        "patterns": ["what's the weather?", "is it going to rain?", "how hot is it outside?"],
        "responses": ["I'm unable to check live weather, but you can try a weather website or app!", "Check current weather on popular weather sites like Weather.com or AccuWeather.", "To check the weather, I recommend using a weather app!"]
    },
    {
        "patterns": ["tell me a joke", "make me laugh", "give me something funny"],
        "responses": ["Why did the scarecrow win an award? Because he was outstanding in his field!", "I'm reading a book on anti-gravity. It's impossible to put down!", "How do you organize a space party? You planet!"]
    },
]

def chatbot_response(user_input):
    user_input = user_input.lower()
    user_input_tokens = nltk.word_tokenize(user_input)

    for entry in responses:
        for pattern in entry["patterns"]:
            if re.search(pattern, user_input):
                return random.choice(entry["responses"])


    return "I'm sorry, I didn't  understand your question!"


while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "bye", "quit"]:
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)