import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK data (run once)
nltk.download('punkt')

# Define response pairs
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    [r"what is your name?", ["I'm a chatbot created with NLTK!"]],
    [r"how are you?", ["I'm just code, but I'm functioning well!"]],
    [r"your favorite (.*)", ["I'm a bot—I don't have favorites!"]],
    [r"quit", ["Bye! See you soon."]],
]

# Create Chatbot
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Chatbot: Hi! Hema ")
    chatbot.converse()

if __name__ == "__main__":
    start_chat()
