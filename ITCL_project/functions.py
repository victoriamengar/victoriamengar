# This script gets the key form the environment and defines the main functions of the program

# THE IDEA NOW IS TO MAKE A SEPARATE FILE WITH DIFFERENT PROMPT CONTENTS, RANDOM
# ALSO, I WANT A SEPARATE FILE TO SET PERSONALITIES

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

    # If user presses Enter, it continues the dialogue without its intervention
    if user_message == "":
        user_message = "User: continue your dialogue without me and saying something new while interacting with each other"
        conversation.append(user_message)

    # If the user says something, it will be part of the conversation    
    else:    
        user_message = "User: " + user_message
        conversation.append(user_message)  

    return user_message, conversation