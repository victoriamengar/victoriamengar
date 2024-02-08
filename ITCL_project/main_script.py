from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Defining the function to start generating the dialogue
def start_dialogue(character1, character2, topic): 

    # Using the engine "gpt-3.5-turbo" to generate message of character 1
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"Start a dialogue about {topic} between {character1} and {character2}, one sentence each"
            }
        ],
        max_tokens=100,
        temperature=0.5
    )
    
    return response
  
# Asking for the roles to the user
character1 = input("Enter name/role for first character: ")  
character2 = input("Enter name/role for second character: ")
topic = input("Enter topic the dialogue is about: ")

# Executing the function
finaltext = start_dialogue(character1, character2, topic)
message = finaltext.choices[0].message 
print(message.content)

# Continuing the dialogue with user inputs
def get_user_message():
  return input("Enter a message, leave it empty to continue, or 'quit' to end: ")

user_message = get_user_message()

def continue_dialogue(character1, character2, prompt, user_message):
  
    # If the user decides to quit, conversation ends
    if user_message.lower() == 'quit':
       response = "END OF CONVERSATION"
       print(response)

    # If user presses Enter, it continues the dialogue
    elif user_message == "":
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": f"Continue the {prompt} dialogue between {character1} and {character2}, one sentence each"
                }
            ],
            max_tokens=100,
            temperature=0.5
        )
        message = response.choices[0].message
        print(message.content)
        user_message = get_user_message()
        continue_dialogue(message.content, character1, character2, user_message)
    
    # If the user sends a message, it influences the conversation and it continues
    else:
       response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": f"Continue the {prompt} dialogue between {character1} and {character2} as if someone added {user_message} to the conversation, max one sentence each"
                }
            ],
            max_tokens=100,
            temperature=0.5
        )
       message = response.choices[0].message
       print(message.content)
       user_message = get_user_message()
       continue_dialogue(message.content, character1, character2, user_message)

continue_dialogue(message.content, character1, character2, user_message)