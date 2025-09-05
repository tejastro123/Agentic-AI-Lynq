import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API with your key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set GOOGLE_API_KEY in your .env file.")
genai.configure(api_key=api_key)

# Initialize the model
# We use 'gemini-1.5-flash' as it's fast and capable
model = genai.GenerativeModel('gemini-2.5-pro')

# Define the prompt
prompt = "What is the main purpose of an AI agent?"

print(f"🤖 Asking Gemini: {prompt}\n")

# Make the API call
response = model.generate_content(prompt)

# Print the response
print("✅ Gemini's Answer:")
print(response.text)