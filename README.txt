# Agentic-AI-Lynq-Round-2-code

1. Create the Main Folder: Create a new folder on your computer named agentic-challenge.

2. Create Subfolders and Files: Inside agentic-challenge, create the following structure. You can create empty files for now; we'll add code to them later.

/agentic-challenge

├── level1/

│   ├── llm_call.py

│   └── pdf_reader.py

├── level2/

│   ├── weather_mcp.py

│   └── client_agent.py

├── requirements.txt

└── README.md

3. Set Up a Virtual Environment: It's a best practice to keep project dependencies isolated. 

We'll use uv, as suggested.

    Open your terminal or command prompt in the agentic-challenge folder.

    If you don't have uv, install it first (instructions are on their website).

    Create a virtual environment: uv venv

    Activate the environment:
        On macOS/Linux: source .venv/bin/activate
        On Windows: .venv\Scripts\activate

    Your terminal prompt should now show (.venv).

4. Get Your Gemini API Key:

    Go to Google AI Studio.

    Sign in with your Google account.

    Click on "Get API key" and then "Create API key in new project".

    Copy the key and save it somewhere secure. Never share this key publicly.

# Part 1: Level 1 - Exploration & Setup

This level is about making sure you can connect to an LLM and work with files.

## Task 1.1: Simple LLM Call (llm_call.py)

This script will make a basic call to the Gemini API to get an answer to a general question.

1. Install the Library: In your activated terminal, run: uv pip install google-generativeai python-dotenv

(We add python-dotenv to securely manage our API key).

2. Store Your API Key: Create a new file in the agentic-challenge folder called .env. Add your API key to it like this:

3. GOOGLE_API_KEY="YOUR_API_KEY_HERE"

4. Write the Code: Open level1/llm_call.py 

5. Run the Script: In your terminal (make sure you are in the agentic-challenge directory), run: python level1/llm_call.py

## Task 1.2: Reading a PDF (pdf_reader.py)

This script will use the pypdf library to extract text from a PDF file.

1. Install the Library: uv pip install pypdf

2. Get a Sample PDF: Find any PDF file and save it in your level1 folder. Let's call it sample.pdf.

3. Write the Code: Open level1/pdf_reader.py

4. Run the Script: python level1/pdf_reader.py

The output will be the text extracted from the first page of your sample.pdf.

## Bonus : UI chat interface using streamlit.

Step 1: Install Streamlit

In your terminal, with your virtual environment activated, run the following command to install Streamlit: uv pip install streamlit

Step 2: Create the Chat UI Script

Create a new file in your level1 folder named chat_ui.py. This will keep your bonus task separate from the core llm_call.py.

Step 3: Now, add the code to level1/chat_ui.py.

Step 4: Now, run the app from your terminal (make sure you're in the main agentic-challenge directory): streamlit run level1/chat_ui.py

A new tab will automatically open in your web browser, pointing to a local URL (like http://localhost:8501).

You will see your chat interface, ready to go!
