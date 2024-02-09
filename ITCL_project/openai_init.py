# In PowerShell execute python -m venv openai-env (only the first time)
# Then activate it in CMD with ITCL_project\openai-env\Scripts\activate

from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))