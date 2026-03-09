from google import genai

import google.generativeai as genai

# Replace with your API key
genai.configure(api_key="GEMINI_API_KEY")



# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")  # fast + free tier option

# Ask something
response = model.generate_content("Tell me a short story about a robot learning Python.")
print(response.text)
