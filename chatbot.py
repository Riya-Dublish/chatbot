import random

class SimpleChatBot:
    def __init__(self):
        self.responses = {
            "hi": ["Hello!", "Hi there!", "Hey!"],
            "how are you": ["I'm doing well, thank you!", "I'm good, thanks for asking.", "All good on this side!"],
            "bye": ["Goodbye!", "See you later!", "Bye!"],
            "weather": ["The weather is sunny today.", "It's raining outside.", "Expect some snowfall today."],
            "age": ["I'm just a chatbot, so I don't have an age.", "I'm timeless!", "I exist beyond the concept of time."],
            "name": ["I'm just a chatbot, but you can call me ChatBot.", "I go by the name ChatBot.", "I'm your friendly ChatBot!"],
            "default": ["I'm sorry, I didn't understand that.", "Could you please rephrase that?", "I'm not sure what you mean."]
        }

    def respond(self, query):
        query = query.lower()
        if query in self.responses:
            return random.choice(self.responses[query])
        elif "weather" in query:
            return random.choice(self.responses["weather"])
        elif "how old" in query or "age" in query:
            return random.choice(self.responses["age"])
        elif "what's your name" in query or "your name" in query:
            return random.choice(self.responses["name"])
        elif query.startswith("hi") or query.startswith("hello"):
            return random.choice(self.responses["hi"])
        elif query.startswith("bye"):
            return random.choice(self.responses["bye"])
        else:
            return random.choice(self.responses["default"])


chatbot = SimpleChatBot()


print("Welcome to the Simple ChatBot!")
print("You can type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("ChatBot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("ChatBot:", response)