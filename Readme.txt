Voice FAQ Bot


Project Overview


Voice FAQ Bot is an AI-powered assistant that allows users to ask frequently asked questions using either text or voice input.


The application converts voice questions into text, processes the question using an LLM, and provides an answer. The answer can then be converted into speech for a voice response.


 Features


- Text-based question input
- Voice-based question input
- Speech-to-text conversion
- AI-powered FAQ answering
- Text-to-speech response
- Simple and user-friendly interface
- FAQ knowledge base


How the System Work
User
  ↓
Text / Voice Input
  ↓
Speech-to-Text
  ↓
FAQ Knowledge Base
  ↓
LLM
  ↓
Answer
  ↓
Text-to-Speech
  ↓
Voice Output


Technologies Used
Python
Google Gemini API
Speech-to-Text
Text-to-Speech
Streamlit
Python-dotenv
Project Setup
1. Install Python


Make sure Python is installed on your computer.


2. Install Required Packages


Open the terminal in the project folder and run:


pip install -r requirements.txt


3. Configure API Keys


Create a .env file in the project folder.


Add the required API key:


GEMINI_API_KEY=your_api_key_here


If other services are used for speech-to-text or text-to-speech, add their API keys to the .env file as required.


Do not share API keys publicly.


Running the Application


If the project uses Streamlit, run:


streamlit run app.py


After running the command, open the local address shown in the terminal.


Example


The user can ask a question such as:


"What are the library timings?"


The system:


Receives the user's question.
Converts the voice input into text if voice input is used.
Processes the question using the FAQ knowledge base.
Uses the LLM to generate the answer.
Converts the answer into speech.
Provides the response to the user.
FAQ Knowledge Base


The chatbot uses a predefined FAQ knowledge base to answer common questions.


The system should provide answers based on the available FAQ information and avoid generating unsupported information.


Error Handling


The application handles common errors such as:


Missing API key
Invalid API key
Empty input
Microphone permission problems
Speech-to-text errors
LLM/API errors
Text-to-speech errors
Testing






The following features were tested:


Text input
Voice input
Speech-to-text conversion
FAQ question answering
LLM response generation
Text-to-speech output
Error handling
Assumptions
The application requires the necessary API keys.
Internet access is required for API-based services.
The user must provide microphone permission for voice input.
The chatbot answers questions using the available FAQ information.


Known Gaps
Speech recognition may be affected by background noise.
API response time depends on the external services.
The current FAQ knowledge base is limited.
A larger FAQ dataset could be improved using a RAG-based approach.
AI Assistance


AI coding assistance was used during development for code generation, debugging, and documentation. The generated code was reviewed and adapted for the project.














Security


API keys should be stored in the .env file and should not be uploaded to GitHub.


The .gitignore file should include:


.env
venv/
__pycache__/
*.pyc
Conclusion


The Voice FAQ Bot demonstrates how speech recognition, large language models, FAQ knowledge bases, and text-to-speech can be combined to create a simple voice-based AI assistant.




**Save this as:** `README.md`  
**Do not save it as:** `README.txt` or `README.docx`.