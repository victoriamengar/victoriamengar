# Dialogue Generator

This is a Python program that generates a dialogue between two characters on a chosen topic using the OpenAI GPT-3.5 language model. The characters' personalities and prompts to continue the conversation are randomly selected from predefined lists.

## Installation

1. Clone this repository to your local machine:

git clone https://github.com/victoriamengar/victoriamengar.git

2. Navigate to the project directory:

cd ITCL-project

3. Install the required Python packages using pip:

pip install -r openai
pip install -r dotenv

4. Set up your OpenAI API key by creating a .env file in the project directory and adding your API key:

OPENAI_API_KEY=your-api-key-goes-here

## Usage
1. Run the run_dialogue.py script:

python main.py

2. Follow the prompts to enter the names/roles of the characters and the topic of the dialogue.

The program will generate a conversation between the characters based on the selected topic. It will continue until you choose to quit.

3. During the conversation, you can input your messages to continue the dialogue.
Press Enter to let the program generate a response for you, or type your message and press Enter to include it in the conversation.

4. To end the conversation, type "quit" as your message when prompted.

## Example
--> Enter name/role for first character:
Albert Einstein
--> Enter name/role for second character:
Niels Bohr 
--> Enter topic the dialogue is about:
Quantum Mechanics
You: Hey! How are you, Albert Einstein and Niels Bohr? Let's talk about Quantum Mechanics!
Einstein: Hey there! Although I remain skeptical about certain aspects of Quantum Mechanics, I am genuinely excited to delve into our discussion and explore its potential implications.
Bohr: Hello! It's wonderful to connect, Albert. My hypothesis is that by embracing the probabilistic nature of 
quantum mechanics, we can gain a deeper understanding of the fundamental building blocks of the universe and their intricate interactions.
--> Enter a message, leave it empty to continue, or 'quit' to end:

Einstein: While I appreciate the enthusiasm, I still find it hard to accept the notion that reality is solely determined by probabilities and indeterminism as Quantum Mechanics suggests, as I believe there must be underlying deterministic laws governing the universe.
Bohr: Albert, I understand your reservations, but perhaps by embracing the probabilistic nature of quantum mechanics, we can uncover a harmonious blend of determinism and indeterminism that reveals a deeper truth about the universe and its fascinating intricacies.
--> Enter a message, leave it empty to continue, or 'quit' to end:
Why don't you retire from science, Bohr?
Einstein: Bohr, your insistence on blending determinism and indeterminism only further deepens my concern about the validity and coherence of Quantum Mechanics, making me question its true nature and our ability to truly comprehend it.
Bohr: Einstein, I appreciate your genuine concerns, but I anticipate that our friendly dialogue will lead us to a deeper understanding of Quantum Mechanics and its potential to unravel the mysteries of the universe.       
--> Enter a message, leave it empty to continue, or 'quit' to end:
Einstein: I'm sorry, but I simply cannot fathom how embracing probabilistic nature can lead to any meaningful understanding, as it undermines the very foundation of scientific inquiry based on causality and determinism.   
Bohr: Albert, I value your skepticism, but I believe that by exploring the probabilistic nature of quantum mechanics, we can foster a more holistic understanding of the universe, and it is through our respectful dialogue that we can further our exploration and evaluation of this fascinating field.
--> Enter a message, leave it empty to continue, or 'quit' to end:
quit
END OF CONVERSATION
