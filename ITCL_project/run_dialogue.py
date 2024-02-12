# This script executes all functions and conditions to create the dialogue
# functions.py is the file with function definitions
from functions import dialogue, get_user_message
import random
from questions import personal_characteristics

# Preparing ANSI code colours for the user
PURPLE = '\033[95m'
# ANSI escape code to reset text color
RESET = '\033[0m'

# Asking for the roles and topic to the user
print(PURPLE + "--> Enter name/role for first character:" + RESET)
character1 = input()
print(PURPLE + "--> Enter name/role for second character:" + RESET)
character2 = input()
print(PURPLE + "--> Enter topic the dialogue is about:" + RESET)
topic = input()

# Creating an empty list to store the conversation
conversation = []

# Storing the first sentence inside
user_message = f"You: Hey! How are you, {character1} and {character2}? Let's talk about {topic}!"

# Appending the first message to the conversation
conversation.append(user_message)

print(*conversation, sep = "\n")

# Selecting the random prompt to modify the conversation
personality1 = random.choice(personal_characteristics)
personality2 = random.choice(personal_characteristics) 

# Executing the first dialogue functions
conversation = dialogue(character1, conversation, personality1)
conversation = dialogue(character2, conversation, personality2)

# Loop to continue the dialogue until the user quits
while True:
    # Executing the function for getting feedback from the user and unmaking the tuple
    user_message, conversation = get_user_message(conversation)
    
    # If the user inputs "quit", end the conversation
    if user_message.lower() == "user: quit":
        print(PURPLE + "END OF CONVERSATION" + RESET)
        break
    
    # Continuing the conversation
    conversation = dialogue(character1, conversation, personality1)
    conversation = dialogue(character2, conversation, personality2)