from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

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
introduction = f"You: Hey! How are you, {character1} and {character2}? Let's talk about {topic}!"

# Appending the first message to the conversation
conversation.append(introduction)

print(*conversation, sep = "\n")

# Defining the function to generate one sentence per character
def dialogue(character, conversation): 

    # Shortening the conversation if necessary
    if len(conversation) > 10:
       prompt = conversation[-10:]

    else:
       prompt = conversation

    # Using the engine "gpt-3.5-turbo" to generate the reply
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": 'assistant',
                "content": f"Continue the dialogue: {prompt} as if you were {character} in one sentence"
            }
        ],
        max_tokens = 100,
        temperature = 0.7
    )
    
    # Appending the reply to the conversation
    conversation.append(response.choices[0].message.content)

    # Printing the last message
    print(f"{character}: {conversation[-1]}")
    return conversation

# Defining the function to obtain feedback from the user
def get_user_message(conversation):

    print(PURPLE + "--> Enter a message, leave it empty to continue, or 'quit' to end:" + RESET)
    user_message = input()

    # If user presses Enter, it continues the dialogue without changing the conversation variable
    # and without printing it
    if user_message != "":
        user_message = "User: " + user_message
        conversation.append(user_message)

    return user_message, conversation

# Defining the function to continue with the conversation after the user input
def continue_dialogue(user_message, character1, character2, conversation):
  
    # If the user decides to quit, conversation ends
    if user_message.lower() == "user: quit":
       print(PURPLE + "END OF CONVERSATION" + RESET)

       # Exiting the function if the user wants to quit
       return

    # Otherwise, the conversation continues
    dialogue(character1, conversation)
    dialogue(character2, conversation)

    # Get the next user message for the next iteration of the conversation
    user_message, conversation = get_user_message(conversation)

    # Continue the conversation recursively
    continue_dialogue(user_message, character1, character2, conversation)

# Executing the first dialogue functions
dialogue(character1, conversation)
dialogue(character2, conversation)

# Executing the function for getting feedback from the user and unmaking the tupple
user_message, conversation = get_user_message(conversation)

# Executing the function to continue the dialogue recursively
continue_dialogue(user_message, character1, character2, conversation)