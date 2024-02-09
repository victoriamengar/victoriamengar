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
                "role": character,
                "content": f"Respond to {prompt} as if you were {character} in one sentence"
            }
        ],
        max_tokens=100,
        temperature=0.7
    )
    
    # Appending the reply to the conversation
    conversation = conversation.append(response.choices[0].message)

    #Printing the last message
    print(conversation[-1])
    return conversation

# Executing the function
dialogue(character1, conversation)
dialogue(character2, conversation)

# Continuing the dialogue with user inputs
def get_user_message():
  user_message = input("--> Enter a message, leave it empty to continue, or 'quit' to end: ")
  print("You: "+ user_message)


user_message = get_user_message()

def continue_dialogue(character1, character2, prompt, user_message):
  
    # If the user decides to quit, conversation ends
    if user_message.lower() == 'quit':
       response = "|\nEND OF CONVERSATION"
       print("|\n", response)

    # If user presses Enter, it continues the dialogue
    elif user_message == "":
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": f"Continue the {prompt} dialogue between {character1} and {character2}, one complete sentence each character"
                }
            ],
            max_tokens=100,
            temperature=0.7
        )
        message = response.choices[0].message
        print("|\n", message.content)
        user_message = get_user_message()
        continue_dialogue(message.content, character1, character2, user_message)
    
    # If the user sends a message, it influences the conversation and it continues
    else:
       response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": f"Continue the {prompt} dialogue between {character1} and {character2} as if someone added {user_message} to the conversation, one sentence from each character"
                }
            ],
            max_tokens=100,
            temperature=0.7
        )
       message = response.choices[0].message
       print("|\n", message.content)
       user_message = get_user_message()
       continue_dialogue(message.content, character1, character2, user_message)

continue_dialogue(message.content, character1, character2, user_message)