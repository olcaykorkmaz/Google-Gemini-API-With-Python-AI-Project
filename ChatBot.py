import google.generativeai as genai

import API_KEY

genai.configure(api_key=API_KEY.api_key)


model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content("türkiye'de kaç tane il var")
print(response.text)