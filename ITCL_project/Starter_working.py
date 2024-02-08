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
                "content": f"Start a dialogue about {topic} between {character1} and {character2}"
            }
        ],
        max_tokens=50,
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